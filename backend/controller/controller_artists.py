from sqlalchemy.orm import Session

from model.model_album import Album
from model.model_artist import Artist
from schema.schema_artist import ArtistCreate, ArtistUpdate


def get_all_artists(db: Session):
    return db.query(Artist).all()


def get_artist(db: Session, artist_id: int):
    return db.get(Artist, artist_id)


def create_artist(db: Session, data: ArtistCreate):
    artist = Artist(**data.model_dump())
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist


def update_artist(db: Session, artist_id: int, data: ArtistUpdate):
    artist = get_artist(db, artist_id)
    if artist is None:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(artist, key, value)
    db.commit()
    db.refresh(artist)
    return artist


def delete_artist(db: Session, artist_id: int):
    artist = get_artist(db, artist_id)
    if artist is None:
        return False
    if db.query(Album).filter(Album.artist_id == artist_id).first():
        raise ValueError("No se puede borrar: el artista tiene álbumes")
    db.delete(artist)
    db.commit()
    return True