from sqlalchemy.orm import Session

from backend.model.model_albums import Album
from backend.model.model_genres import Genre
from backend.schema.schema_genres import GenreCreate, GenreUpdate


def get_all_genres(db: Session):
    return db.query(Genre).all()


def get_genre(db: Session, genre_id: int):
    return db.get(Genre, genre_id)


def create_genre(db: Session, data: GenreCreate):
    genre = Genre(**data.model_dump())
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre


def update_genre(db: Session, genre_id: int, data: GenreUpdate):
    genre = get_genre(db, genre_id)
    if genre is None:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(genre, key, value)
    db.commit()
    db.refresh(genre)
    return genre


def delete_genre(db: Session, genre_id: int):
    genre = get_genre(db, genre_id)
    if genre is None:
        return False
   
    if db.query(Album).filter(Album.genre_id == genre_id).first():
        raise ValueError("No se puede borrar: hay álbumes de este género")
    db.delete(genre)
    db.commit()
    return True
