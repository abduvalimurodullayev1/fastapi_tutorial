from fastapi import FastAPI, APIRouter

import blog_router
import models
import user_router
from database import engine, SessionLocal
import login
app = FastAPI()
models.Base.metadata.create_all(engine)
router = APIRouter(
    tags=['auth']
)
app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(login.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
