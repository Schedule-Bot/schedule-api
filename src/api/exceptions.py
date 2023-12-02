from fastapi import HTTPException, Request
from starlette.responses import JSONResponse

from api.utils import Response


async def http_exception_handler(
    request: Request, exc: HTTPException  # pylint: disable=unused-argument
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=Response(
            data=None, status_code=exc.status_code, error=True, detail=exc.detail
        ).model_dump(),
    )
