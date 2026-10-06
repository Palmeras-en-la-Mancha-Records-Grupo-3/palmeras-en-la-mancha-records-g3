from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base

album_artists = Table(
    "album_artists",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("artist_id", Integer, ForeignKey("artists.id"), primary_key=True)
    )

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)
    description = Column(String, nullable=False)

    album = relationship("Album", secondary=album_artists, back_populates="artists")