
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

import models
import schemas
from auth2 import get_current_user
from database import SessionLocal
from hashing import Hash
from repository import blog


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, db, request)


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')