from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schema.schema_genres import (
    GenreCreate,
    GenreResponse,
    GenreUpdate
)
from backend.controller.controller_genres import (
    create_genre,
    get_all_genres,
    get_genre,
    update_genre,
    delete_genre
)

router = APIRouter(
    prefix="/api/genre",
    tags=["Géneros"]
)

@router.post(
    "",
    response_model=GenreResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea un género"
)
def create_genre_routes(
    genre_data: GenreCreate,
    db: Session = Depends(get_db)
):
    return create_genre(
        db,
        genre_data
    )

@router.get(
    "",
    response_model=list[GenreResponse],
    summary="Consulta la lista de géneros"
)
def get_genres_routes(
    db: Session = Depends(get_db),
):
    return get_all_genres(
        db=db,
    )

@router.get(
    "/{genre_id}",
    response_model=GenreResponse,
    summary="Consulta un género"
)
def get_genre_routes(
    genre_id: int,
    db: Session = Depends(get_db)
):
    return get_genre(
        db,
        genre_id
    )

@router.put(
    "/{genre_id}",
    response_model=GenreResponse,
    summary="Modifica un género"
)
def update_genre_routes(
    genre_id: int,
    genre_data: GenreUpdate,
    db: Session = Depends(get_db)
):
    return update_genre(
        db,
        genre_id,
        genre_data        
    )

@router.delete(
    "/{genre_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina un género"
)
def delete_genre_routes(
    genre_id: int,
    db: Session = Depends(get_db)
):
    delete_genre(
    	db,
    	genre_id
    )
    return None