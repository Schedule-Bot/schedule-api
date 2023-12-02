from fastapi import FastAPI, HTTPException

from api.exceptions import http_exception_handler
from api.routers import university


def make_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(university.router)
    _app.add_exception_handler(
        exc_class_or_status_code=HTTPException, handler=http_exception_handler
    )
    return _app


app = make_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)
