from sqlalchemy.orm import Session

from model.Branch import Branch
from schema.Branch import BranchCreate, BranchUpdate

#Traer todas las branch
def get_all_branches(db: Session):
    return db.query(Branch).all()

#Traer una branch por id
def get_branch(db: Session, branch_id: int):
    return db.get(Branch, branch_id)

#Crear una branch
def create_branch(db: Session, data: BranchCreate):
    branch = Branch(**data.model_dump())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch

#Subir una branch
def update_branch(db: Session, branch_id: int, data: BranchUpdate):
    branch = get_branch(db, branch_id)
    if branch is None:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(branch, key, value)
    db.commit()
    db.refresh(branch)
    return branch

#Borrar una branch
def delete_branch(db: Session, branch_id: int):
    branch = get_branch(db, branch_id)
    if branch is None:
        return False
    db.delete(branch)
    db.commit()
    return True