from sqlalchemy import Column, Integer, String
from backend.database.database import Base

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)