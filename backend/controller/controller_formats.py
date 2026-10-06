from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

from model.AlbumFormat import AlbumFormat
from model.Format import Format
from schema.Format import FormatCreate, FormatUpdate


def get_all_formats(db: Session):
    return db.query(Format).all()


def get_format(db: Session, format_id: int):
    return db.get(Format, format_id)


def create_format(db: Session, data: FormatCreate):
    format_ = Format(**data.model_dump())
    db.add(format_)
    db.commit()
    db.refresh(format_)
    return format_


def update_format(db: Session, format_id: int, data: FormatUpdate):
    format_ = get_format(db, format_id)
    if format_ is None:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(format_, key, value)
    db.commit()
    db.refresh(format_)
    return format_


def delete_format(db: Session, format_id: int):
    format_ = get_format(db, format_id)
    if format_ is None:
        return False
    
    if db.query(AlbumFormat).filter(AlbumFormat.format_id == format_id).first():
        raise ValueError("No se puede borrar: hay Ã¡lbumes con este formato")
    db.delete(format_)
    db.commit()
    return True
