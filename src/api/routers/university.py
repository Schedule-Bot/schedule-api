from fastapi import APIRouter, HTTPException

from api.schemas.university import UniversityScheme
from api.utils import Response, ResponseList, write_response

router = APIRouter(tags=[""])

ALL_UNIVERSITIES = [  # TODO(issue-1): Доставать университеты из базы, а не из кода!
    UniversityScheme(
        id=1,
        name="ВлГУ",
        description="Владимировский государственный институт имени Александра и Николая Григорьевича Столетовых",
    )
]


@router.get("/api/v1/universities")
async def get_universities() -> ResponseList[UniversityScheme]:
    return write_response(ALL_UNIVERSITIES)


@router.get("/api/v1/universities/{university_id}")
async def get_university(university_id: int) -> Response[UniversityScheme]:
    for university in ALL_UNIVERSITIES:
        if university.id == university_id:
            return write_response(university)
    raise HTTPException(
        status_code=404,
        detail=f"Университет с ID={university_id} не найден",
    )
