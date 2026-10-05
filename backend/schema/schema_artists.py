from pydantic import BaseModel
from typing import Optional


class ArtistCreate(BaseModel):
    name: str
    description: str


class ArtistResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True


class ArtistUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None