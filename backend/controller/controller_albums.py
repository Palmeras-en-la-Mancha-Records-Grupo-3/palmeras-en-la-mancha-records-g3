import cloudinary.uploader
from fastapi import UploadFile
from sqlalchemy.orm import Session

from model.Album import Album
from model.AlbumFormat import AlbumFormat
from model.Format import Format
from model.RecordLabel import RecordLabel
from schema.Album import AlbumCreate, AlbumUpdate
from sqlalchemy.exc import IntegrityError

def _check_label(db: Session, label_id: int):
    if db.get(RecordLabel, label_id) is None:
        raise ValueError(f"La discográfica {label_id} no existe")


def _build_formats(db: Session, formats: list[dict]):
   
    editions = []
    for f in formats:
        if db.get(Format, f["format_id"]) is None:
            raise ValueError(f"El formato {f['format_id']} no existe")
        editions.append(
            AlbumFormat(format_id=f["format_id"], price=f["price"], stock=f["stock"])
        )
    return editions


def get_albums(
    db: Session,
    title: str | None = None,
    artist: str | None = None,
    label_id: int | None = None,
    label_name: str | None = None,
    format_id: int | None = None,
    format_name: str | None = None,
):
    
    query = db.query(Album)

    if title:
        query = query.filter(Album.title.ilike(f"%{title}%"))
    if artist:
        query = query.filter(Album.artist.ilike(f"%{artist}%"))

    
    if label_id:
        query = query.filter(Album.label_id == label_id)
    if label_name:
        query = query.join(Album.label).filter(RecordLabel.name.ilike(f"%{label_name}%"))

    
    if format_id or format_name:
        query = query.join(Album.formats)
        if format_id:
            query = query.filter(AlbumFormat.format_id == format_id)
        if format_name:
            query = query.join(AlbumFormat.format).filter(
                Format.name.ilike(f"%{format_name}%")
            )

    return query.distinct().all()


def get_album(db: Session, album_id: int):
    return db.get(Album, album_id)



def create_album(db: Session, data: AlbumCreate):
    fields = data.model_dump()
    formats = fields.pop("formats", [])

    _check_label(db, fields["label_id"])
    album = Album(**fields)
    album.formats = _build_formats(db, formats)
    try:
        db.add(album)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("No se pudo guardar el álbum: datos duplicados o inválidos")

    
    db.refresh(album)
    return album



def update_album(db: Session, album_id: int, data: AlbumUpdate):
    album = get_album(db, album_id)
    if album is None:
        return None

    fields = data.model_dump(exclude_unset=True)
    formats = fields.pop("formats", None)

    if "label_id" in fields:
        _check_label(db, fields["label_id"])
    for key, value in fields.items():
        setattr(album, key, value)

    
    if formats is not None:
        album.formats = _build_formats(db, formats)

    db.commit()
    db.refresh(album)
    return album



def delete_album(db: Session, album_id: int):
    album = get_album(db, album_id)
    if album is None:
        return False
    db.delete(album)  
    db.commit()
    return True



def upload_cover(db: Session, album_id: int, file: UploadFile):
    album = get_album(db, album_id)
    if album is None:
        return None
    if not file.content_type or not file.content_type.startswith("image/"):
        raise ValueError("El archivo debe ser una imagen")

    result = cloudinary.uploader.upload(file.file, folder="palmeras/covers")
    album.cover_image_url = result["secure_url"]

    db.commit()
    db.refresh(album)
    return album
