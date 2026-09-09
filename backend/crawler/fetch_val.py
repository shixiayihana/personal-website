from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from common.db_config import get_db_connection

API_URL = "https://danjuanfunds.com/djapi/index_eva/dj"
DEFAULT_REFERER = "https://danjuanfunds.com/rn/value-center?channel=1300100141"
SHANGHAI_TZ = ZoneInfo("Asia/Shanghai")
TARGET_INDICES = {
    "SH000300": "沪深300",
    "SH000905": "中证500",
    "SZ399006": "创业板",
}


@dataclass(frozen=True)
class ValuationRecord:
    index_code: str
    index_name: str
    data: date
    pe_percentile: float
    pb_percentile: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="抓取指数估值百分位并写入 MySQL/MariaDB。")
    parser.add_argument("--dry-run", action="store_true", help="只请求和校验接口，不写入数据库。")
    parser.add_argument("--retries", type=int, default=3, help="请求失败时的最大尝试次数，默认3次。")
    return parser.parse_args()


def fetch_api_json(retries: int) -> dict[str, Any]:
    if retries < 1:
        raise ValueError("--retries 必须大于或等于1")
    request = Request(
        API_URL,
        headers={
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": DEFAULT_REFERER,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0",
        },
        method="GET",
    )
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urlopen(request, timeout=20) as response:
                result = json.loads(response.read().decode("utf-8"))
            if not isinstance(result, dict):
                raise RuntimeError("接口返回结果不是 JSON 对象")
            return result
        except HTTPError as exc:
            last_error = RuntimeError(f"HTTP {exc.code} {exc.reason}")
            if exc.code < 500 and exc.code != 429:
                break
        except (URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
            last_error = exc
        if attempt < retries:
            time.sleep(2 ** (attempt - 1))
    raise RuntimeError(f"请求接口失败（尝试{retries}次）：{last_error}") from last_error


def parse_percentile(value: Any, field_name: str, index_code: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"{index_code} 的 {field_name} 不是有效数值：{value!r}") from exc
    if not math.isfinite(number) or not 0 <= number <= 1:
        raise RuntimeError(f"{index_code} 的 {field_name} 超出范围[0, 1]：{number!r}")
    return number


def timestamp_to_date(value: Any, index_code: str) -> date:
    try:
        return datetime.fromtimestamp(int(value) / 1000, tz=timezone.utc).astimezone(SHANGHAI_TZ).date()
    except (TypeError, ValueError, OverflowError, OSError) as exc:
        raise RuntimeError(f"{index_code} 的 ts 不是有效毫秒时间戳：{value!r}") from exc


def parse_records(payload: dict[str, Any]) -> list[ValuationRecord]:
    if payload.get("result_code") != 0:
        raise RuntimeError(f"接口返回失败，result_code={payload.get('result_code')!r}")
    data = payload.get("data")
    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list):
        raise RuntimeError("接口返回结构异常：data.items 不是列表")
    items_by_code = {
        str(item.get("index_code", "")).strip(): item
        for item in items
        if isinstance(item, dict)
    }
    records: list[ValuationRecord] = []
    for index_code, index_name in TARGET_INDICES.items():
        item = items_by_code.get(index_code)
        if item is None:
            raise RuntimeError(f"接口缺少目标指数：{index_code}（{index_name}）")
        records.append(ValuationRecord(
            index_code=index_code,
            index_name=index_name,
            data=timestamp_to_date(item.get("ts"), index_code),
            pe_percentile=parse_percentile(item.get("pe_percentile"), "pe_percentile", index_code),
            pb_percentile=parse_percentile(item.get("pb_percentile"), "pb_percentile", index_code),
        ))
    if len({record.data for record in records}) != 1:
        raise RuntimeError("三个目标指数的 ts 对应日期不一致")
    return records


def save_records(records: list[ValuationRecord]) -> None:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.executemany(
                """INSERT INTO index_info (index_code, index_name) VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE index_name = VALUES(index_name)""",
                [(record.index_code, record.index_name) for record in records],
            )
            cursor.executemany(
                """INSERT INTO index_valuation (index_code, `data`, pe_percentile, pb_percentile)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE pe_percentile = VALUES(pe_percentile), pb_percentile = VALUES(pb_percentile)""",
                [(record.index_code, record.data, record.pe_percentile, record.pb_percentile) for record in records],
            )
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def main() -> None:
    args = parse_args()
    records = parse_records(fetch_api_json(args.retries))
    if not args.dry_run:
        save_records(records)
    action = "校验完成，未写入数据库" if args.dry_run else "已写入数据库"
    print(f"{action}：data={records[0].data}")
    for record in records:
        print(f"{record.index_code} {record.index_name}: PE={record.pe_percentile:.2%}, PB={record.pb_percentile:.2%}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise SystemExit(f"任务失败：{exc}") from exc