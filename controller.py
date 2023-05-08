from app import app
from models import user_model
from flask import request

user = user_model()

@app.route('/')
def index():
    return "Hello !!!"

@app.route('/user/all')
def get_all_user():
    return user.all_user_model()

@app.route('/user/<id>')
def get_user(id):
    return user.get_user_model(id)

@app.route('/user/create', methods=["POST"])
def create_user():
    return user.add_user_model(request.form)

@app.route('/user/update', methods=["PUT"])
def update_user():
    return user.update_user_model(request.form)

@app.route('/user/delete/<id>', methods=["DELETE"])
def delete_user(id):
    return user.delete_user_model(id)