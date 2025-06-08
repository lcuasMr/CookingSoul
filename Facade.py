import sys

from entities import UserEntity

from daos.UserDAO import UserDAO
from daos.IngredientDAO import IngredientDAO
from daos.RecipieDAO import RecipieDAO
from daos.PostDAO import PostDAO

from sqlalchemy import Engine, MetaData, Table, Column, Integer, String, ForeignKey, ARRAY

from models.user import User
from models.ingredient import Ingredient
from models.recipie import Recipie
from models.post import Post

from entities.UserEntity import UserEntity
from entities.IngredientEntity import IngredientEntity
from entities.RecipieEntity import RecipieEntity
from entities.association_tables import RecipieIngredientAssociation
from utils import ingredients as ingredient_list
from utils.recipiesexample import example_recipies, example_posts

import os

import json

from entities import Base

class Facade:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        print(f"Facade initialized with engine: {self._engine}", file=sys.stdout)
        # Check if the database file exists, if not, create it
        if not os.path.exists('cooking_soul.db'):
            self.create_database()
        

    def create_database(self):
        
        Base.metadata.create_all(self._engine)

        userdao = UserDAO(self._engine)
        ingredientdao = IngredientDAO(self._engine)
        
        print(userdao.persist_model(User(username='admin', email='admin@gmail.com', password='$2b$12$H9PsJZRejbI.Vx5y.BeXfuMdwoi5Oe0wZSEm1bbaeaveF2vc/oEWe')), file=sys.stdout)
        print(userdao.persist_model(User(username='user', email='user@gmail.com', password='$2b$12$ph8V9FlJWYEGgGqabOwqF..WqE506jn.0zLaz279D3gV.S525GoVq')), file=sys.stdout)
        for ingredient in ingredient_list.ingredients_json:
          ingredientdao.persist_model(Ingredient(**ingredient))

        for recipe in example_recipies:
            dao = RecipieDAO(self._engine)
            dao.persist_model_example(Recipie(**recipe))
            #print(f"Adding example recipe: {recipe}", file=sys.stdout)
        for post in example_posts:
            post_dao = PostDAO(self._engine)
            print(f"EXAMPLE POST DICT: {post}", file=sys.stdout)
            post_dao.persist_model(Post(**post))
            print(f"Adding example post: {post}", file=sys.stdout)
            
    def get_user(self, user_id) -> User:
        user_dao: UserDAO = UserDAO(self._engine)
        return user_dao.get_user_by_id(user_id)
    
    def get_user_by_name(self, username) -> User:
        user_dao: UserDAO = UserDAO(self._engine)
        return user_dao.get_user_by_name(username)

    def add_user(self, username: str, email: str, password: str) -> UserEntity:
        user_dao: UserDAO = UserDAO(self._engine)
        user = User(username=username, email=email, password=password)
        user_dao.persist_model(user)
        return user
    
    def delete_user(self, user_id: int) -> bool:
        user_dao: UserDAO = UserDAO(self._engine)
        return user_dao.delete_user(user_id)
    
    def list_users(self) -> list[UserEntity]:
        user_dao: UserDAO = UserDAO(self._engine)
        print(f"Listing all users: {user_dao.get_all_users()}", file=sys.stdout)
        return user_dao.get_all_users()

    def list_ingredients(self) -> list:
        ingredient_dao = IngredientDAO(self._engine)
        ingredients = ingredient_dao.get_all_ingredients()
        return ingredients
    
    def get_ingredient_by_id(self, ingredient_id: int) -> Ingredient:
        ingredient_dao = IngredientDAO(self._engine)
        ingredient = ingredient_dao.get_ingredient_by_id(ingredient_id)
        print(f"Retrieved ingredient by ID {ingredient_id}: {ingredient}", file=sys.stdout)
        if ingredient:
            return ingredient
        else:
            raise ValueError(f"Ingredient with ID {ingredient_id} not found.")
        
    def add_recipie(self, title, description, ingredient_cuantity, instructions):
        recipie_dao = RecipieDAO(self._engine)
        print(ingredient_cuantity, file=sys.stdout)
        recipie = Recipie(title=title, description=description, ingredients=ingredient_cuantity, instructions=instructions)
        print(f"Adding new recipie: {recipie}", file=sys.stdout)
        return recipie_dao.persist_model(recipie)
    
    def post_recipie(self, user_id, title, description, ingredient_cuantity, instructions):
        recipie_dao = RecipieDAO(self._engine)
        print(ingredient_cuantity, file=sys.stdout)
        recipie = Recipie(title=title, description=description, ingredients=ingredient_cuantity, instructions=instructions)
        print(f"Adding new recipie: {recipie}", file=sys.stdout)
        new_recipie = recipie_dao.persist_model(recipie)
    
        post_dao = PostDAO(self._engine)
        return post_dao.persist_model(Post(user_id=user_id, content_type='recipie', description=new_recipie.description, recipie_id=new_recipie.id))


    def get_recipie_by_id(self, recipie_id: int) -> Recipie:
        recipie_dao = RecipieDAO(self._engine)
        recipie = recipie_dao.get_recipie_by_id(recipie_id)
        print(f"Retrieved recipie by ID {recipie_id}: {recipie}", file=sys.stdout)
        if recipie:
            return recipie
        else:
            raise ValueError(f"Recipie with ID {recipie_id} not found.")
        
    def get_all_recipies(self) -> list[Recipie]:
        recipie_dao = RecipieDAO(self._engine)
        recipies = recipie_dao.get_all_recipies()
        print(f"Retrieved all recipies: {recipies}", file=sys.stdout)
        return recipies

    def get_posts_by_user_id(self, user_id: int) -> list[Post]:
        post_dao = PostDAO(self._engine)
        posts = post_dao.get_posts_by_user_id(user_id)
        print(f"Retrieved posts by user ID {user_id}: {posts}", file=sys.stdout)
        return posts
    
