from fastapi import APIRouter, HTTPException

from api.schemas.university import UniversityScheme

router = APIRouter(tags=[""])

ALL_UNIVERSITIES = [  # TODO(issue-1): Доставать университеты из базы, а не из кода!
    UniversityScheme(
        id=1,
        name="ВлГУ",
        description="Владимировский государственный институт имени Александра и Николая Григорьевича Столетовых",
    )
]


@router.get("/api/v1/universities")
async def get_universities() -> list[UniversityScheme]:
    return ALL_UNIVERSITIES


@router.get("/api/v1/universities/{university_id}")
async def get_university(university_id: int) -> UniversityScheme:
    for university in ALL_UNIVERSITIES:
        if university.id == university_id:
            return university
    raise HTTPException(
        status_code=404,
        detail=f"The university with the ID={university_id} was not found",
    )
