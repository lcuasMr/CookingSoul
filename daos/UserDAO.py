from typing import List, Optional
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from models.user import User  # Assuming you have a User model defined in models/User.py
from entities.UserEntity import UserEntity  # Assuming you have a UserEntity defined in entities/UserEntity.py
class UserDAO:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        self._session_maker: sessionmaker[Session] = sessionmaker(bind=self._engine)

    def persist_model(self, usuario: User) -> None:
        session = self._session_maker()
        try:
            new_user = UserEntity(usuario)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        
            return new_user.to_model()
        except Exception as e:
            session.rollback()
            print("Error persisting usuario entity:", e)
            raise

        finally:
            session.close()
        

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        with self._session_maker() as session:
            return session.query(User).filter(User.id == user_id).first()

    def get_all_users(self) -> List[User]:
        with self._session_maker() as session:
            return session.query(UserEntity).all()

    def create_user(self, user: User) -> User:
        with self._session_maker() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def update_user(self, user_id: int, updated_data: dict) -> Optional[User]:
        with self._session_maker() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in updated_data.items():
                    setattr(user, key, value)
                session.commit()
                session.refresh(user)
            return user

    def delete_user(self, user_id: int) -> bool:
        with self._session_maker() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False