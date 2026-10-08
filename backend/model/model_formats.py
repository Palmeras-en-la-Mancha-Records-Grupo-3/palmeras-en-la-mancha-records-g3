from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database.database import Base

class Format(Base):
    __tablename__ = "formats"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)
    description = Column(String, index=True, nullable=True)
    
    album_formats = relationship("AlbumFormat", back_populates="format")