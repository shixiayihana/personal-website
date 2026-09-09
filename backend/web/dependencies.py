from collections.abc import Generator

from pymysql.connections import Connection

from common.db_config import get_db_connection


def get_connection() -> Generator[Connection, None, None]:
    connection = get_db_connection()
    try:
        yield connection
    finally:
        connection.close()