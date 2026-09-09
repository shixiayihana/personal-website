from fastapi import APIRouter, Depends
from pymysql.connections import Connection

from web.dependencies import get_connection

router = APIRouter()


@router.get("/health")
def health(connection: Connection = Depends(get_connection)) -> dict[str, str]:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return {"status": "ok", "database": "ok"}