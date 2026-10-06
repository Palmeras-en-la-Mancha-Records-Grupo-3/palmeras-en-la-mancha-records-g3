from sqlalchemy.orm import Session

from backend.model.model_albums import Album
from backend.model.model_record_labels import RecordLabel
from backend.schema.schema_record_labels import RecordLabelCreate, RecordLabelUpdate


def get_all_labels(db: Session):
    return db.query(RecordLabel).all()


def get_label(db: Session, label_id: int):
    return db.get(RecordLabel, label_id)


def create_label(db: Session, data: RecordLabelCreate):
    label = RecordLabel(**data.model_dump())
    db.add(label)
    db.commit()
    db.refresh(label)
    return label


def update_label(db: Session, label_id: int, data: RecordLabelUpdate):
    label = get_label(db, label_id)
    if label is None:
        return None
  
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(label, key, value)
    db.commit()
    db.refresh(label)
    return label


def delete_label(db: Session, label_id: int):
    label = get_label(db, label_id)
    if label is None:
        return False
    
    if db.query(Album).filter(Album.label_id == label_id).first():
        raise ValueError("No se puede borrar: la discográfica tiene álbumes")
    db.delete(label)
    db.commit()
    return True
