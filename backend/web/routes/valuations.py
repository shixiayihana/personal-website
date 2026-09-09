from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from pymysql.connections import Connection

from web.dependencies import get_connection
from web.schemas import Valuation

router = APIRouter()

VALUATION_SELECT = """
    SELECT v.index_code, i.index_name, v.`data`,
           v.pe_percentile, v.pb_percentile
    FROM index_valuation AS v
    INNER JOIN index_info AS i ON i.index_code = v.index_code
"""


def get_index_or_404(connection: Connection, index_code: str) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM index_info WHERE index_code = %s", (index_code,)
        )
        if cursor.fetchone() is None:
            raise HTTPException(status_code=404, detail="指数代码不存在")


def to_valuations(rows: list[dict]) -> list[Valuation]:
    return [Valuation.model_validate(row) for row in rows]


@router.get("/valuations/latest", response_model=list[Valuation])
def latest_valuations(
    connection: Connection = Depends(get_connection),
) -> list[Valuation]:
    with connection.cursor() as cursor:
        cursor.execute(
            VALUATION_SELECT
            + """
            WHERE (v.index_code, v.`data`) IN (
                SELECT index_code, MAX(`data`)
                FROM index_valuation
                GROUP BY index_code
            )
            ORDER BY i.id
            """
        )
        rows = cursor.fetchall()
    return to_valuations(rows)


@router.get("/valuations/date/{data}", response_model=list[Valuation])
def valuations_by_date(
    data: date,
    connection: Connection = Depends(get_connection),
) -> list[Valuation]:
    with connection.cursor() as cursor:
        cursor.execute(
            VALUATION_SELECT
            + "WHERE v.`data` = %s ORDER BY i.id",
            (data,),
        )
        rows = cursor.fetchall()
    return to_valuations(rows)


@router.get("/valuations/{index_code}/latest", response_model=Valuation)
def latest_valuation(
    index_code: str,
    connection: Connection = Depends(get_connection),
) -> Valuation:
    get_index_or_404(connection, index_code)
    with connection.cursor() as cursor:
        cursor.execute(
            VALUATION_SELECT
            + """
            WHERE v.index_code = %s
            ORDER BY v.`data` DESC
            LIMIT 1
            """,
            (index_code,),
        )
        row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="该指数暂无估值数据")
    return Valuation.model_validate(row)


@router.get("/valuations/{index_code}", response_model=list[Valuation])
def valuation_history(
    index_code: str,
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    limit: int = Query(default=365, ge=1, le=5000),
    connection: Connection = Depends(get_connection),
) -> list[Valuation]:
    get_index_or_404(connection, index_code)
    if start_date and end_date and start_date > end_date:
        raise HTTPException(status_code=422, detail="start_date 不能晚于 end_date")

    conditions = ["v.index_code = %s"]
    parameters: list[object] = [index_code]
    if start_date is not None:
        conditions.append("v.`data` >= %s")
        parameters.append(start_date)
    if end_date is not None:
        conditions.append("v.`data` <= %s")
        parameters.append(end_date)
    parameters.append(limit)

    with connection.cursor() as cursor:
        cursor.execute(
            VALUATION_SELECT
            + " WHERE "
            + " AND ".join(conditions)
            + " ORDER BY v.`data` DESC LIMIT %s",
            parameters,
        )
        rows = cursor.fetchall()
    return to_valuations(rows)