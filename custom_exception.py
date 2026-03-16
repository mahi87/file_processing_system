from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


class DBException(HTTPException):
    def __init__(self, detail: str = "Failed to save to db"):
        super().__init__(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )
