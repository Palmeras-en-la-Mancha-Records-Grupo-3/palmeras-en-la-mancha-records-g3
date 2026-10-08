from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schema.schema_albums import (
    AlbumCreate,
    AlbumResponse,
    AlbumUpdate
)
from backend.controller.controller_albums import (
    create_album,
    get_all_albums,
    get_albums,
    get_album,
    update_album,
    delete_album
)

router = APIRouter(
    prefix="/api/album",
    tags=["Álbumes"]
)

@router.post(
    "",
    response_model=AlbumResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea un álbum"
)
def create_album_routes(
    album_data: AlbumCreate,
    db: Session = Depends(get_db)
):
    return create_album(
        db,
        album_data
    )

@router.get(
    "",
    response_model=list[AlbumResponse],
    summary="Consulta la lista de álbumes"
)
def get_albums_routes(
    db: Session = Depends(get_db),
):
    return get_all_albums(
        db=db,
    )

@router.get(
    "/search",
    response_model=list[AlbumResponse],
    summary="Consulta álbumes por título, artista, sello, formato o género"
)
def list_albums(
    title: str | None = None,
    artist_id: int | None=None,
    artist_name: str | None = None,
    label_id: int | None = None,
    label_name: str | None = None,
    format_id: int | None = None,
    format_name: str | None = None,
    genre_id: int | None=None,
    genre_name: str | None=None,
    db: Session = Depends(get_db),
):
    return get_albums(
        db,
        title=title,
        artist_id=artist_id,
        artist_name=artist_name,
        label_id=label_id,
        label_name=label_name,
        format_id=format_id,
        format_name=format_name,
        genre_id=genre_id,
        genre_name=genre_name
    )

@router.get(
    "/{album_id}",
    response_model=AlbumResponse,
    summary="Consulta un álbum"
)
def get_album_routes(
    album_id: int,
    db: Session = Depends(get_db)
):
    return get_album(
        db,
        album_id
    )

@router.put(
    "/{album_id}",
    response_model=AlbumResponse,
    summary="Modifica un álbum"
)
def update_album_routes(
    album_id: int,
    album_data: AlbumUpdate,
    db: Session = Depends(get_db)
):
    return update_album(
        db,
        album_id,
        album_data        
    )

@router.delete(
    "/{album_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina un álbum"
)
def delete_album_routes(
    album_id: int,
    db: Session = Depends(get_db)
):
    delete_album(
        db,
        album_id
    )
    return None