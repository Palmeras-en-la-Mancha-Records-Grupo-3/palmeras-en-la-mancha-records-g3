from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schema.schema_formats import (
    FormatCreate,
    FormatResponse,
    FormatUpdate
)
from backend.controller.controller_formats import (
    create_format,
    get_all_formats,
    get_format,
    update_format,
    delete_format
)

router = APIRouter(
    prefix="/api/format",
    tags=["Formatos"]
)

@router.post(
    "",
    response_model=FormatResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea un formato"
)
def create_album_routes(
    format_data: FormatCreate,
    db: Session = Depends(get_db)
):
    return create_format(
        db,
        format_data
    )

@router.get(
    "",
    response_model=list[FormatResponse],
    summary="Consulta la lista de formatos"
)
def get_formats_routes(
    db: Session = Depends(get_db),
):
    return get_all_formats(
        db=db,
    )

@router.get(
    "/{format_id}",
    response_model=FormatResponse,
    summary="Consulta un formato"
)
def get_album_routes(
    format_id: int,
    db: Session = Depends(get_db)
):
    return get_format(
        db,
        format_id
    )

@router.put(
    "/{format_id}",
    response_model=FormatResponse,
    summary="Modifica un formato"
)
def update_album_routes(
    format_id: int,
    format_data: FormatUpdate,
    db: Session = Depends(get_db)
):
    return update_format(
        db,
        format_id,
        format_data        
    )

@router.delete(
    "/{format_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina un formato"
)
def delete_album_routes(
    format_id: int,
    db: Session = Depends(get_db)
):
    delete_format(
        db,
        format_id
    )
    return None