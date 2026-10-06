from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base
from backend.model.model_artists import album_artists
from backend.model.model_genres import album_genres

class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, nullable=False, unique=True)
    artist = Column(String, index=True, nullable=False)
    release_year = Column(Integer, index=True, nullable=False)
    genre = Column(String, index=True, nullable=False)
    cover_image_url = Column(String, index=True, nullable=True, unique=True)
    label_id = Column(Integer, ForeignKey("record_labels.id"), nullable=True)

    label = relationship("RecordLabel", back_populates="albums")

    album_format = relationship("AlbumFormat", back_populates="album")    

    artists = relationship("Artist", secondary=album_artists, back_populates="album")

    genres = relationship("Genre", secondary=album_genres, back_populates="album")