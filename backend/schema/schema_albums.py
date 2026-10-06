from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal


class AlbumCreate(BaseModel):
    title: str
    release_year: int
    cover_image_url: Optional[str] = None
    label_id: Optional[int] = None

    artist_ids: list[int] = Field(default_factory=list)
    genre_ids: list[int] = Field(default_factory=list)
    formats: list[AlbumFormatInput] = Field(default_factory=list)


class AlbumResponse(BaseModel):
    id: int
    title: str
    release_year: int
    cover_image_url: Optional[str] = None
    label_id: Optional[int] = None

    class Config:
        from_attributes = True


class AlbumUpdate(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    cover_image_url: Optional[str] = None
    label_id: Optional[int] = None

    artist_ids: Optional[list[int]] = None
    genre_ids: Optional[list[int]] = None
    formats: Optional[list[AlbumFormatInput]] = None


class AlbumFormatInput(BaseModel):
    format_id: int
    price: Decimal
    stock: int