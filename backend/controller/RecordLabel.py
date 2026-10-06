from sqlalchemy.orm import Session

from model.Album import Album
from model.RecordLabel import RecordLabel
from schema.RecordLabel import RecordLabelCreate, RecordLabelUpdate

#Trae todos los label
def get_all_labels(db: Session):
    return db.query(RecordLabel).all()

#Trae el label por su id
def get_label(db: Session, label_id: int):
    return db.get(RecordLabel, label_id)

#Crea el label
def create_label(db: Session, data: RecordLabelCreate):
    label = RecordLabel(**data.model_dump())
    db.add(label)
    db.commit()
    db.refresh(label)
    return label

#Actualiza el label
def update_label(db: Session, label_id: int, data: RecordLabelUpdate):
    label = get_label(db, label_id)
    if label is None:
        return None
  
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(label, key, value)
    db.commit()
    db.refresh(label)
    return label

#Borra el label
def delete_label(db: Session, label_id: int):
    label = get_label(db, label_id)
    if label is None:
        return False
    
    if db.query(Album).filter(Album.label_id == label_id).first():
        raise ValueError("No se puede borrar: la discográfica tiene álbumes")
    db.delete(label)
    db.commit()
    return True