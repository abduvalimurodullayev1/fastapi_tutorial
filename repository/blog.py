from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from models import Blog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id{id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'blog is delete'


def update(id: int, db: Session, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    # Update the attributes of the blog object
    blog.title = request.title
    blog.body = request.body

    db.commit()
    return 'Updated'


def show(id: int, db: Session, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")
    return blog
