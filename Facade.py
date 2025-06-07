import sys

from entities import UserEntity

from daos.UserDAO import UserDAO
from daos.IngredientDAO import IngredientDAO
from daos.RecipieDAO import RecipieDAO

from sqlalchemy import Engine, MetaData, Table, Column, Integer, String, ForeignKey, ARRAY

from models.user import User
from models.ingredient import Ingredient
from models.recipie import Recipie

from entities.UserEntity import UserEntity
from entities.IngredientEntity import IngredientEntity
from entities.RecipieEntity import RecipieEntity
from entities.association_tables import RecipieIngredientAssociation
from utils import ingredients as ingredient_list
from utils.recipiesexample import example_recipies

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
        
        print(userdao.persist_model(User(id=1, username='admin', email='cosa@gmail.com', password='admin')), file=sys.stdout)
        print(ingredientdao.persist_model(Ingredient(id=0, name='tomate', region='España', variety='cherry', flavor= 'dulce', medition= 'Kg', image_url = None)), file=sys.stdout)
        for ingredient in ingredient_list.ingredients_json:
          ingredientdao.persist_model(Ingredient(**ingredient))

        for recipe in example_recipies:
            dao = RecipieDAO(self._engine)
            dao.persist_model_example(Recipie(**recipe))
            #print(f"Adding example recipe: {recipe}", file=sys.stdout)
            


    def add_user(self, username: str, email: str, password: str) -> UserEntity:
        user_dao: UserDAO = UserDAO(self._engine)
        user = User(username=username, email=email, password=password)
        user_dao.persist_model(user)
        return user
    
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
        ingredient_dao = IngredientDAO(self._engine)
        recipie = Recipie(title=title, description=description, ingredients=ingredient_cuantity, instructions=instructions)
        print(f"Adding new recipie: {recipie}", file=sys.stdout)
        return recipie_dao.persist_model(recipie)
