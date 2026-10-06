import cloudinary.uploader

from fastapi import UploadFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.model.model_albums import Album
from backend.model.model_album_formats import AlbumFormat
from backend.model.model_artists import Artist
from backend.model.model_formats import Format
from backend.model.model_genres import Genre
from backend.model.model_record_labels import RecordLabel
from backend.schema.schema_albums import AlbumCreate, AlbumUpdate


def _check_label(db: Session, label_id: int | None) -> None:
    if label_id is None:
        return

    if db.get(RecordLabel, label_id) is None:
        raise ValueError(f"La discográfica {label_id} no existe")


def _get_artists(db: Session, artist_ids: list[int]) -> list[Artist]:
    if not artist_ids:
        return []

    unique_ids = set(artist_ids)

    if len(unique_ids) != len(artist_ids):
        raise ValueError("La lista de artistas contiene IDs duplicados")

    artists = (
        db.query(Artist)
        .filter(Artist.id.in_(unique_ids))
        .all()
    )

    found_ids = {artist.id for artist in artists}
    missing_ids = unique_ids - found_ids

    if missing_ids:
        raise ValueError(
            f"Los siguientes artistas no existen: {sorted(missing_ids)}"
        )

    return artists


def _get_genres(db: Session, genre_ids: list[int]) -> list[Genre]:
    if not genre_ids:
        return []

    unique_ids = set(genre_ids)

    if len(unique_ids) != len(genre_ids):
        raise ValueError("La lista de géneros contiene IDs duplicados")

    genres = (
        db.query(Genre)
        .filter(Genre.id.in_(unique_ids))
        .all()
    )

    found_ids = {genre.id for genre in genres}
    missing_ids = unique_ids - found_ids

    if missing_ids:
        raise ValueError(
            f"Los siguientes géneros no existen: {sorted(missing_ids)}"
        )

    return genres


def _build_album_formats(db: Session, formats) -> list[AlbumFormat]:
    result = []
    format_ids = [item.format_id for item in formats]

    if len(set(format_ids)) != len(format_ids):
        raise ValueError(
            "La lista de formatos contiene IDs duplicados"
        )

    for item in formats:
        format_ = db.get(Format, item.format_id)

        if format_ is None:
            raise ValueError(
                f"El formato {item.format_id} no existe"
            )

        if item.price < 0:
            raise ValueError(
                "El precio no puede ser negativo"
            )

        if item.stock < 0:
            raise ValueError(
                "El stock no puede ser negativo"
            )

        result.append(
            AlbumFormat(
                format=format_,
                price=item.price,
                stock=item.stock,
            )
        )

    return result


def get_all_albums(db: Session):
    return db.query(Album).all()


def get_albums(
    db: Session,
    title: str | None = None,
    artist_id: int | None = None,
    artist_name: str | None = None,
    label_id: int | None = None,
    label_name: str | None = None,
    format_id: int | None = None,
    format_name: str | None = None,
    genre_id: int | None = None,
    genre_name: str | None = None,
):
    query = db.query(Album)

    if title:
        query = query.filter(
            Album.title.ilike(f"%{title}%")
        )

    if artist_id is not None or artist_name:
        query = query.join(Album.artists)

        if artist_id is not None:
            query = query.filter(
                Artist.id == artist_id
            )

        if artist_name:
            query = query.filter(
                Artist.name.ilike(f"%{artist_name}%")
            )

    if genre_id is not None or genre_name:
        query = query.join(Album.genres)

        if genre_id is not None:
            query = query.filter(
                Genre.id == genre_id
            )

        if genre_name:
            query = query.filter(
                Genre.name.ilike(f"%{genre_name}%")
            )

    if label_id is not None:
        query = query.filter(
            Album.label_id == label_id
        )

    if label_name:
        query = (
            query.join(Album.label)
            .filter(
                RecordLabel.name.ilike(f"%{label_name}%")
            )
        )

    if format_id is not None or format_name:
        query = query.join(Album.album_formats)

        if format_id is not None:
            query = query.filter(
                AlbumFormat.format_id == format_id
            )

        if format_name:
            query = (
                query.join(AlbumFormat.format)
                .filter(
                    Format.name.ilike(f"%{format_name}%")
                )
            )

    return query.distinct().all()


def get_album(db: Session, album_id: int):
    return db.get(Album, album_id)


def create_album(db: Session, data: AlbumCreate):
    _check_label(db, data.label_id)

    artists = _get_artists(db, data.artist_ids)
    genres = _get_genres(db, data.genre_ids)
    album_formats = _build_album_formats(db, data.formats)

    album = Album(
        title=data.title,
        release_year=data.release_year,
        cover_image_url=data.cover_image_url,
        label_id=data.label_id,
        artists=artists,
        genres=genres,
        album_formats=album_formats,
    )

    try:
        db.add(album)
        db.commit()
        db.refresh(album)

    except IntegrityError:
        db.rollback()
        raise ValueError(
            "No se pudo guardar el álbum: "
            "datos duplicados o inválidos"
        )

    return album


def update_album(
    db: Session,
    album_id: int,
    data: AlbumUpdate,
):
    album = get_album(db, album_id)

    if album is None:
        return None

    fields = data.model_dump(
        exclude_unset=True,
        exclude={
            "artist_ids",
            "genre_ids",
            "formats",
        },
    )

    if "label_id" in fields:
        _check_label(db, fields["label_id"])

    for key, value in fields.items():
        setattr(album, key, value)

    if data.artist_ids is not None:
        album.artists = _get_artists(db, data.artist_ids)

    if data.genre_ids is not None:
        album.genres = _get_genres(db, data.genre_ids)

    if data.formats is not None:
        album.album_formats = _build_album_formats(
            db,
            data.formats,
        )

    try:
        db.commit()
        db.refresh(album)

    except IntegrityError:
        db.rollback()
        raise ValueError(
            "No se pudo actualizar el álbum: "
            "datos duplicados o inválidos"
        )

    return album


def delete_album(db: Session, album_id: int) -> bool:
    album = get_album(db, album_id)

    if album is None:
        return False

    db.delete(album)
    db.commit()

    return True


def upload_cover(
    db: Session,
    album_id: int,
    file: UploadFile,
):
    album = get_album(db, album_id)

    if album is None:
        return None

    if (
        not file.content_type
        or not file.content_type.startswith("image/")
    ):
        raise ValueError("El archivo debe ser una imagen")

    result = cloudinary.uploader.upload(
        file.file,
        folder="palmeras/covers",
    )

    album.cover_image_url = result["secure_url"]

    db.commit()
    db.refresh(album)

    return album