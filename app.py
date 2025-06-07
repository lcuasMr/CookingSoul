from flask import Flask, render_template, request
from utils.forms import UserForm
import os
import sys
from flask_sqlalchemy import SQLAlchemy

from models.user import User

from mappers.UserMapper import UsuarioMapper
from mappers.IngredientMapper import IngredientMapper
from mappers.RecipieMapper import RecipieMapper


from Facade import Facade
from entities import Base
from sqlalchemy import create_engine

import json

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



_DB_ENGINE = create_engine('sqlite:///cooking_soul.db')

_FACADE = Facade(engine=_DB_ENGINE)

@app.route('/')
def index():
    recipies = _FACADE.get_all_recipies()
    ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
    recipies_map = [RecipieMapper.reverse_map(recipie) for recipie in recipies]

    return render_template('index.html', recetas= recipies_map)

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        _FACADE.add_user(username=form.username.data, email=form.email.data, password=form.password.data) 
        return render_template('add_user.html', form=form, name='Add User', success=True)    
    else:
        return render_template('add_user.html', form=form, name='Add User')
        

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template('user.html', user=user)
    else:
        return "User not found", 404
    
@app.route('/usuarios', methods=['GET'])
def usuarios():
    users = [UsuarioMapper.reverse_map(user) for user in _FACADE.list_users()]
    print(users, file=sys.stdout)
    return render_template('usuarios.html', usuarios=users)

@app.route('/ingredientes', methods=['GET'])
def ingredientes():
    ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
    print(ingredients, file=sys.stdout)
    return render_template('ingredientes.html', ingredients=ingredients)

@app.route('/ingredientes/<int:ingredient_id>', methods=['GET'])
def ingrediente(ingredient_id):
    ingredient = _FACADE.get_ingredient_by_id(ingredient_id)
    print(ingredient, file=sys.stdout)
    if ingredient:
        return render_template('ingredient.html', ingredient=IngredientMapper.reverse_map(ingredient))
    else:
        return "Ingredient not found", 404
    
@app.route('/add_receta', methods=['POST', 'GET'])
def add_receta():
    if request.method == 'POST':
        # Here you would handle the form submission for adding a recipe
        # For now, we just return a success message
        ingredient_cuantity: list[tuple] = []
        ingredients_json = request.form['ingredients']
        ingredients_list = json.loads(ingredients_json)
        for ingredient in ingredients_list:
            print(ingredient, file=sys.stdout)
            ingredient_cuantity.append((ingredient.get("id"), ingredient.get("cuantity", 0)))
        _FACADE.add_recipie(
            title=request.form['title'],
            description=request.form['description'],
            ingredient_cuantity=ingredient_cuantity,
            instructions=request.form['instructions']
        )
        ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
        return render_template('add_receta.html', ingredients=ingredients, success=True)
    else:
        ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
        return render_template('add_receta.html', ingredients=ingredients, success=True)

@app.route('/recetas', methods=['GET'])
def recetas():
    recipies = _FACADE.get_all_recipies()
    ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
    recipies_map = [RecipieMapper.reverse_map(recipie) for recipie in recipies]
    print(f"Map: {recipies_map}", file=sys.stdout)
    return render_template('recetas.html', recetas=recipies_map, ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)

