from fastapi import APIRouter
from sqlalchemy.orm import Session

import schemas
EXACT_TOKEN_TYPES = ["access", "refresh"]
router = APIRouter()


@router.post('/login')
def login(request: schemas.Login, db: Session):
    return login(request, db)
