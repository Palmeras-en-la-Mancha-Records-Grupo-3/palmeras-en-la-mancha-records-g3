from pydantic import BaseModel
from typing import Optional


class GenreCreate(BaseModel):
    name: str


class GenreResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class GenreUpdate(BaseModel):
    name: Optional[str] = None