from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('User.id'))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="creator")
