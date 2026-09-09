from __future__ import annotations

import pymysql
from pymysql.connections import Connection

from common.settings import load_settings


def get_db_connection() -> Connection:
    settings = load_settings()
    if not settings.db_user:
        raise RuntimeError("DB_USER 未配置")

    return pymysql.connect(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
        charset="utf8mb4",
        autocommit=True,
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
    )