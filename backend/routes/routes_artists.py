from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schema.schema_artists import (
    ArtistCreate,
    ArtistResponse,
    ArtistUpdate
)
from backend.controller.controller_artists import (
    create_artist,
    get_all_artists,
    get_artist,
    update_artist,
    delete_artist
)

router = APIRouter(
    prefix="/api/artist",
    tags=["artist"]
)

@router.post(
    "",
    response_model=ArtistResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea un artista"
)
def create_artist_routes(
    artist_data: ArtistCreate,
    db: Session = Depends(get_db)
):
    return create_artist(
        db,
        artist_data
    )

@router.get(
    "",
    response_model=list[ArtistResponse],
    summary="Consulta la lista de artistas"
)
def get_artists_routes(
    db: Session = Depends(get_db),
):
    return get_all_artists(
        db=db,
    )

@router.get(
    "/{artist_id}",
    response_model=ArtistResponse,
    summary="Consulta un artista"
)
def get_artist_routes(
    artist_id: int,
    db: Session = Depends(get_db)
):
    return get_artist(
        db,
        artist_id
    )

@router.put(
    "/{artist_id}",
    response_model=ArtistResponse,
    summary="Modifica un artista"
)
def update_artist_routes(
    artist_id: int,
    artist_data: ArtistUpdate,
    db: Session = Depends(get_db)
):
    return update_artist(
        db,
        artist_id,
        artist_data        
    )

@router.delete(
    "/{artist_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina un artista"
)
def delete_artist_routes(
    artist_id: int,
    db: Session = Depends(get_db)
):
    delete_artist(
    	db,
    	artist_id
    )
    return None