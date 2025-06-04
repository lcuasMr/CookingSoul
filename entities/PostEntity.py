from sqlalchemy import Column, Integer
from sqlalchemy.types import PickleType
from sqlalchemy.ext.declarative import declarative_base
from models.post import Post

Base = declarative_base()

class PostEntity(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(PickleType, nullable=False)  # Puede ser cualquier objeto

    def __init__(self, post_model):
        super().__init__()
        self.id = post_model.id
        self.content = post_model.content

    def __repr__(self):
        return f"<PostEntity(id={self.id}, content={repr(self.content)})>"

    def to_model(self) -> Post:
        return Post(
            id=self.id,
            content=self.content
        )