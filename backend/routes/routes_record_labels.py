from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schema.schema_record_labels import (
    RecordLabelCreate,
    RecordLabelResponse,
    RecordLabelUpdate
)
from backend.controller.controller_record_labels import (
    create_label,
    get_all_labels,
    get_label,
    update_label,
    delete_label
)

router = APIRouter(
    prefix="/api/record_label",
    tags=["Compañías discográficas"]
)

@router.post(
    "",
    response_model=RecordLabelResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea una compañía discográfica"
)
def create_label_routes(
    record_label_data: RecordLabelCreate,
    db: Session = Depends(get_db)
):
    return create_label(
        db,
        record_label_data
    )

@router.get(
    "",
    response_model=list[RecordLabelResponse],
    summary="Consulta la lista de compañías discográficas"
)
def get_all_labels_routes(
    db: Session = Depends(get_db),
):
    return get_all_labels(
        db=db,
    )

@router.get(
    "/{record_label_id}",
    response_model=RecordLabelResponse,
    summary="Consulta una compañía discográfica"
)
def get_label_routes(
    record_label_id: int,
    db: Session = Depends(get_db)
):
    return get_label(
        db,
        record_label_id
    )

@router.put(
    "/{record_label_id}",
    response_model=RecordLabelResponse,
    summary="Modifica una compañía discográfica"
)
def update_label_routes(
    record_label_id: int,
    record_label_data: RecordLabelUpdate,
    db: Session = Depends(get_db)
):
    return update_label(
        db,
        record_label_id,
        record_label_data        
    )

@router.delete(
    "/{record_label_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina una compañía discográfica"
)
def delete_label_routes(
    record_label_id: int,
    db: Session = Depends(get_db)
):
    delete_label(
        db,
        record_label_id
    )
    return None