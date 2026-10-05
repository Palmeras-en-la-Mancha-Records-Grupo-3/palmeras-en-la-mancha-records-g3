from pydantic import BaseModel
from typing import Optional


class FormatCreate(BaseModel):
    name: str
    description: Optional[str] = None


class FormatResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class FormatUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None