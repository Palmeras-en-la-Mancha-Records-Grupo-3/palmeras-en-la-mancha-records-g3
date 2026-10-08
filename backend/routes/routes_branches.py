from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.schema.schema_branches import (
    BranchCreate,
    BranchResponse,
    BranchUpdate
)
from backend.controller.controller_branches import (
    create_branch,
    get_all_branches,
    get_branch,
    update_branch,
    delete_branch
)

router = APIRouter(
    prefix="/api/branch",
    tags=["Filiales"]
)

@router.post(
    "",
    response_model=BranchResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea una filial"
)
def create_branch_routes(
    branch_data: BranchCreate,
    db: Session = Depends(get_db)
):
    return create_branch(
        db,
        branch_data
    )

@router.get(
    "",
    response_model=list[BranchResponse],
    summary="Consulta la lista de filiales"
)
def get_branches_routes(
    db: Session = Depends(get_db),
):
    return get_all_branches(
        db=db,
    )

@router.get(
    "/{branch_id}",
    response_model=BranchResponse,
    summary="Consulta una filial"
)
def get_branch_routes(
    branch_id: int,
    db: Session = Depends(get_db)
):
    return get_branch(
        db,
        branch_id
    )

@router.put(
    "/{branch_id}",
    response_model=BranchResponse,
    summary="Modifica una filial"
)
def update_branch_routes(
    branch_id: int,
    branch_data: BranchUpdate,
    db: Session = Depends(get_db)
):
    return update_branch(
        db,
        branch_id,
        branch_data        
    )

@router.delete(
    "/{branch_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina una filial"
)
def delete_branch_routes(
    branch_id: int,
    db: Session = Depends(get_db)
):
    delete_branch(
    	db,
    	branch_id
    )
    return None