from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base

class AlbumFormat(Base):
    __tablename__ = "album_formats"

    album_id = Column(Integer, ForeignKey("albums.id"), primary_key=True)
    format_id = Column(Integer, ForeignKey("formats.id"), primary_key=True)
    
    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

    album = relationship("Album", back_populates="album_format")
    format = relationship("Format", back_populates="album_format")