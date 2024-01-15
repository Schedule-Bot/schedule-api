# from typing import Generic, TypeVar

from pydantic import BaseModel, Field

# PydanticModel = TypeVar("PydanticModel", bound=BaseModel)


class Response[PydanticModel:BaseModel](BaseModel):
    data: PydanticModel | None = None
    status_code: int = Field(default=200, description="HTTP статус код")
    error: bool = Field(
        default=False,
        description="Наличие ошибки (`true`, если присутствует ошибка и `false` в противном случае)",
    )
    detail: str | None = Field(
        default=None,
        description='Детальное описание ошибки. `null`, если отсутствует ошибка (`"error": false`)',
    )


class ResponseList[PydanticModel:BaseModel](Response):
    data: list[PydanticModel]


def write_response(
    content: PydanticModel | list[PydanticModel],
    status_code: int = 200,
    error: bool = False,
    detail: str | None = None,
) -> Response[PydanticModel] | ResponseList[PydanticModel]:
    response_json = {
        "data": content,
        "status_code": status_code,
        "error": error,
        "detail": detail,
    }
    if isinstance(content, list):
        return ResponseList[PydanticModel].model_validate(response_json)
    return Response[PydanticModel].model_validate(response_json)
