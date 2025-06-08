from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.ext.declarative import declarative_base
from models.user import User  # Assuming you have a User model defined in models/User.py

from entities import Base

class UserEntity(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(50), nullable=False, unique=True)
    email = mapped_column(String(100), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)

    posts: Mapped[list["PostEntity"]] = relationship("PostEntity", back_populates="user")


    def __init__(self, user_model):
        super().__init__()
        self.id = user_model.id
        self.username = user_model.username
        self.email = user_model.email
        self.password = user_model.password
        self.posts = []

    def __repr__(self):
        return f"<UserEntity(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    def to_model(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            posts=[post.to_model for post in self.posts]
        )
    
from entities.PostEntity import PostEntity
# Ensure that PostEntity is imported to avoid circular import issues