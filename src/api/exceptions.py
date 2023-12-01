from fastapi import HTTPException, Request
from starlette.responses import JSONResponse


async def http_exception_handler(
    request: Request, exc: HTTPException  # pylint: disable=unused-argument
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "data": None,
            "status_code": exc.status_code,
            "error": True,
            "detail": exc.detail,
        },
    )
