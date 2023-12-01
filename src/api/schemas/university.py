from pydantic import BaseModel


class UniversityScheme(BaseModel):
    id: int
    name: str
    description: str
