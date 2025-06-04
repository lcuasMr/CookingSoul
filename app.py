from flask import Flask, render_template, request
from utils.forms import UserForm
import os
import sys
from flask_sqlalchemy import SQLAlchemy

from models.user import User

from mappers.UserMapper import UsuarioMapper

from Facade import Facade
from entities import Base
from sqlalchemy import create_engine

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



_DB_ENGINE = create_engine('sqlite:///cooking_soul.db')
Base.metadata.create_all(_DB_ENGINE)

_FACADE = Facade(engine=_DB_ENGINE)

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)

