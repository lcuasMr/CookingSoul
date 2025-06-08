from flask import Flask, render_template, request, redirect, url_for
import os
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

from models.user import User

from mappers.UserMapper import UserMapper
from mappers.IngredientMapper import IngredientMapper
from mappers.RecipieMapper import RecipieMapper

from entities import UserEntity

from utils.forms import RegisterForm, LoginForm

from Facade import Facade
from entities import Base
from sqlalchemy import create_engine

import json

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bcrypt = Bcrypt(app)


_DB_ENGINE = create_engine('sqlite:///cooking_soul.db')

_FACADE = Facade(engine=_DB_ENGINE)

def get_facade():
    return _FACADE

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return _FACADE.get_user(user_id)

@app.route('/')
@login_required
def index():
    recipies = _FACADE.get_all_recipies()
    ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
    recipies_map = [RecipieMapper.reverse_map(recipie) for recipie in recipies]

    return render_template('index.html', recetas= recipies_map)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        _FACADE.add_user(form.username.data, form.email.data, hashed_password)
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = _FACADE.get_user_by_name(form.username.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
    else:
        return render_template('login.html', form=form, name='Login')

@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/my_profile')
@login_required
def my_profile():
    user = _FACADE.get_user(current_user.id)
    posts = _FACADE.get_posts_by_user_id(current_user.id)
    print(f"YO: {user}")
    return render_template('user.html', user=current_user, posts=posts)

@app.route('/user/<username>')
@login_required
def user(username):
    return render_template('user.html', username=username)

@app.route('/add_user', methods=['POST', 'GET'])
@login_required
def add_user():
    form = RegisterForm()
    if request.method == 'POST':
        _FACADE.add_user(username=form.username.data, email=form.email.data, password=form.password.data) 
        return render_template('add_user.html', form=form, name='Add User', success=True)    
    else:
        return render_template('add_user.html', form=form, name='Add User')
        

@app.route('/user/<int:user_id>')
@login_required
def get_user(user_id):
    user = _FACADE.get_user(user_id)
    posts = _FACADE.get_posts_by_user_id(user_id)
    print(f"Posts de el usuario {user.username}: {posts}")
    if user:
        return render_template('user.html', user=user, posts=posts)
    else:
        return "User not found", 404
    
@app.route('/usuarios', methods=['GET'])
@login_required
def usuarios():
    users = _FACADE.list_users()
    print(users, file=sys.stdout)
    return render_template('usuarios.html', usuarios=users)

@app.route('/ingredientes', methods=['GET'])
@login_required
def ingredientes():
    ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
    print(ingredients, file=sys.stdout)
    return render_template('ingredientes.html', ingredients=ingredients)

@app.route('/ingredientes/<int:ingredient_id>', methods=['GET'])
@login_required
def ingrediente(ingredient_id):
    ingredient = _FACADE.get_ingredient_by_id(ingredient_id)
    print(ingredient, file=sys.stdout)
    if ingredient:
        return render_template('ingredient.html', ingredient=IngredientMapper.reverse_map(ingredient))
    else:
        return "Ingredient not found", 404
    
@app.route('/add_receta', methods=['POST', 'GET'])
@login_required
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

@app.route('/post_receta', methods=['POST', 'GET'])
@login_required
def post_receta():
    if request.method == 'POST':
        # Here you would handle the form submission for adding a recipe
        # For now, we just return a success message
        ingredient_cuantity: list[tuple] = []
        ingredients_json = request.form['ingredients']
        ingredients_list = json.loads(ingredients_json)
        for ingredient in ingredients_list:
            #print(ingredient, file=sys.stdout)
            ingredient_cuantity.append((ingredient.get("id"), ingredient.get("cuantity", 0)))

        new_post = _FACADE.post_recipie(
            user_id=current_user.id,
            title=request.form['title'],
            description=request.form['description'],
            ingredient_cuantity=ingredient_cuantity,
            instructions=request.form['instructions']
        )

        print(f"NUEVO POST: {new_post}", file=sys.stdout)

        ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
        return render_template('post_receta.html', ingredients=ingredients, success=True)
    else:
        ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
        return render_template('post_receta.html', ingredients=ingredients, success=True)
    
@app.route('/recetas', methods=['GET'])
@login_required
def recetas():
    recipies = _FACADE.get_all_recipies()
    ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
    recipies_map = [RecipieMapper.reverse_map(recipie) for recipie in recipies]
    print(f"Map: {recipies_map}", file=sys.stdout)
    return render_template('recetas.html', recetas=recipies_map, ingredients=ingredients)

@app.route('/recetas/<int:recipie_id>', methods=['GET'])
@login_required
def receta(recipie_id):
    print("VIENDO UNA RECETA", file=sys.stdout)
    receta = _FACADE.get_recipie_by_id(recipie_id)
    if receta: 
        ingredients = [IngredientMapper.reverse_map(ingredient) for ingredient in _FACADE.list_ingredients()]
        receta_map = RecipieMapper.reverse_map(receta)
        print(f"Map: {receta_map}", file=sys.stdout)
        return render_template('receta.html', receta=receta, ingredients=ingredients)
    else:
        return "Recipie not found", 404

if __name__ == '__main__':
    app.run(debug=True)

