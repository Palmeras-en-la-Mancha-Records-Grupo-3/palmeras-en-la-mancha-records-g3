from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database.database import Base

class RecordLabel(Base):
    __tablename__ = "record_labels"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)
    country = Column(String, index=True, nullable=False)
    website = Column(String, index=True, nullable=True)

    albums = relationship("Album", back_populates="label")