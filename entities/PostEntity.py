from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy.types import PickleType
from sqlalchemy.ext.declarative import declarative_base
from models.post import Post

import sys

from entities import Base

class PostEntity(Base):
    __tablename__ = 'posts'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    content_type = mapped_column(String(10), nullable=False)
    description = mapped_column(String(255), nullable=True)
    recipie_id = mapped_column(ForeignKey('recipies.id'))
    likes = mapped_column(Integer, default=0)

    recipie: Mapped["RecipieEntity"] = relationship(back_populates="post")

    user: Mapped["UserEntity"] = relationship("UserEntity", back_populates="posts")

    #implementar comments en un futuro

    def __init__(self, post_model):
        super().__init__()
        print(f"Creating PostEntity with model: {post_model}", file=sys.stdout)
        self.id = post_model.id
        self.user_id = post_model.user_id
        self.content_type = post_model.content_type
        self.description = post_model.description
        self.recipie_id = post_model.recipie_id
        self.likes = post_model.likes if post_model.likes is not None else 0

    def __repr__(self):
        return f"<PostEntity(id={self.id}, user_id={self.user_id}, content_type='{self.content_type}', description='{self.description}', recipie_id={self.recipie_id}, likes={self.likes})>"

    def to_model(self) -> Post:
        return Post(
            id=self.id,
            user_id=self.user_id,
            content_type=self.content_type,
            description=self.description,
            recipie_id=self.recipie_id,
            likes=self.likes
        )
