from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base

album_genres = Table(
    "album_genres",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("genres_id", Integer, ForeignKey("genres.id"), primary_key=True)
    )

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)

    album = relationship("Album", secondary=album_genres, back_populates="genres")