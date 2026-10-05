from pydantic import BaseModel
from typing import Optional


class AlbumCreate(BaseModel):
    title: str
    artist: str
    release_year: int
    genre: str
    cover_image_url: Optional[str] = None
    label_id: Optional[int] = None


class AlbumResponse(BaseModel):
    id: int
    title: str
    artist: str
    release_year: int
    genre: str
    cover_image_url: Optional[str] = None
    label_id: Optional[int] = None

    class Config:
        from_attributes = True


class AlbumUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    release_year: Optional[int] = None
    genre: Optional[str] = None
    cover_image_url: Optional[str] = None
    label_id: Optional[int] = None