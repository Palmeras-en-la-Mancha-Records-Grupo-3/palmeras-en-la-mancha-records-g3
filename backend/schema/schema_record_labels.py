from pydantic import BaseModel
from typing import Optional


class RecordLabelCreate(BaseModel):
    name: str
    country: str
    website: Optional[str] = None


class RecordLabelResponse(BaseModel):
    id: int
    name: str
    country: str
    website: Optional[str] = None

    class Config:
        from_attributes = True


class RecordLabelUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    website: Optional[str] = None