from fastapi import APIRouter, Depends
from pymysql.connections import Connection

from web.dependencies import get_connection
from web.schemas import IndexInfo

router = APIRouter()


@router.get("/indices", response_model=list[IndexInfo])
def list_indices(
    connection: Connection = Depends(get_connection),
) -> list[IndexInfo]:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT index_code, index_name
            FROM index_info
            ORDER BY id
            """
        )
        rows = cursor.fetchall()
    return [IndexInfo.model_validate(row) for row in rows]