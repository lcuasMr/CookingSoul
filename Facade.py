import sys

from entities import UserEntity

from daos.UserDAO import UserDAO
from daos.IngredientDAO import IngredientDAO

from sqlalchemy import Engine, MetaData, Table, Column, Integer, String

from models.user import User
import os

class Facade:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        self._metadata: MetaData = MetaData()
        print(f"Facade initialized with engine: {self._engine}", file=sys.stdout)
        # Check if the database file exists, if not, create it
        if not os.path.exists('cooking_soul.db'):
            self.create_database()
        

    def create_database(self):
        users = Table(
            'users',
            self._metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('username', String(50), nullable=False, unique=True),
            Column('email', String(100), nullable=False, unique=True),
            Column('password', String(255), nullable=False)
        )

        ingredients = Table(
            'ingredients',
            self._metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(100), nullable=False),
            Column('region', String(100), nullable=True),
            Column('variety', String(100), nullable=True),
            Column('flavor', String(100), nullable=True),
            Column('medition', String(50), nullable=True)
        )
        
        self._metadata.create_all(self._engine)

        userdao = UserDAO(self._engine)
        
        print(userdao.persist_model(User(id=1, username='admin', email='cosa@gmail.com', password='admin')), file=sys.stdout)

    def add_user(self, username: str, email: str, password: str) -> UserEntity:
        user_dao: UserDAO = UserDAO(self._engine)
        user = User(username=username, email=email, password=password)
        user_dao.persist_model(user)
        return user
    
    def list_users(self) -> list[UserEntity]:
        user_dao: UserDAO = UserDAO(self._engine)
        return user_dao.get_all_users()

    def list_ingredients(self) -> list:
        ingredient_dao = IngredientDAO(self._engine)
        ingredients = ingredient_dao.get_all_ingredients()
        return []
