from typing import List
from fastapi import status
from fastapi import APIRouter, Depends, HTTPException, Response
from passlib.context import CryptContext
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal
from hashing import Hash
from models import Blog
from repository import user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    tags=['Users'],
    prefix='/user'
)

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post('/', response_model=schemas.ShowUser, )
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.post('/{id}', response_model=schemas.ShowUser, )
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Email yoki parol xato")
    return user
