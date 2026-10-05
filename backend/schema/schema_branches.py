from pydantic import BaseModel
from typing import Optional


class BranchCreate(BaseModel):
    name: str
    address: str
    phone: str


class BranchResponse(BaseModel):
    id: int
    name: str
    address: str
    phone: str

    class Config:
        from_attributes = True


class BranchUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None