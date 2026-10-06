from sqlalchemy.orm import Session

from backend.model.model_branches import Branch
from backend.schema.schema_branches import BranchCreate, BranchUpdate


def get_all_branches(db: Session):
    return db.query(Branch).all()


def get_branch(db: Session, branch_id: int):
    return db.get(Branch, branch_id)


def create_branch(db: Session, data: BranchCreate):
    branch = Branch(**data.model_dump())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch


def update_branch(db: Session, branch_id: int, data: BranchUpdate):
    branch = get_branch(db, branch_id)
    if branch is None:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(branch, key, value)
    db.commit()
    db.refresh(branch)
    return branch


def delete_branch(db: Session, branch_id: int):
    branch = get_branch(db, branch_id)
    if branch is None:
        return False
    db.delete(branch)
    db.commit()
    return True
