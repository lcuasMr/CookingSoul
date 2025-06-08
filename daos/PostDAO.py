from typing import List, Optional
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from entities.PostEntity import PostEntity
from models.post import Post
import sys

class PostDAO:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        self._session_maker: sessionmaker[Session] = sessionmaker(bind=self._engine)

    def persist_model(self, post: Post) -> Optional[Post]:
        session = self._session_maker()
        try:
            new_post = PostEntity(post)
            print(f"Persisting post: {new_post}", file=sys.stdout)
            session.add(new_post)
            session.commit()
            session.refresh(new_post)
            return new_post.to_model()
        except Exception as e:
            session.rollback()
            print("Error persisting post entity:", e)
            raise
        finally:
            session.close()

    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        with self._session_maker() as session:
            entity = session.query(PostEntity).filter(PostEntity.id == post_id).first()
            return entity.to_model() if entity else None
        
    def get_posts_by_user_id(self, user_id: int) -> List[Post]:
        with self._session_maker() as session:
            entities = session.query(PostEntity).filter(PostEntity.user_id == user_id).all()
            return [entity.to_model() for entity in entities]

    def get_all_posts(self) -> List[Post]:
        with self._session_maker() as session:
            entities = session.query(PostEntity).all()
            return [entity.to_model() for entity in entities]

    def update_post(self, post_id: int, updated_data: dict) -> Optional[Post]:
        with self._session_maker() as session:
            entity = session.query(PostEntity).filter(PostEntity.id == post_id).first()
            if entity:
                for key, value in updated_data.items():
                    if hasattr(entity, key):
                        setattr(entity, key, value)
                session.commit()
                session.refresh(entity)
                return entity.to_model()
            return None

    def delete_post(self, post_id: int) -> bool:
        with self._session_maker() as session:
            entity = session.query(PostEntity).filter(PostEntity.id == post_id).first()
            if entity:
                session.delete(entity)
                session.commit()
                return True
            return False