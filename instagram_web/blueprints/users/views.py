from flask import Blueprint, render_template, request, redirect, url_for, flash, Flask, app
from models import user
from werkzeug.security import generate_password_hash, check_password_hash
import re

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


# sign up page
@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/sign_up.html')


# sign up action
@users_blueprint.route('/new/create', methods=['POST'])
def create():
    hashed_password = generate_password_hash(request.form['password'])
    s = user.User(username=request.form['username'],
                  email=request.form['email'], password=hashed_password)

    if s.save():
        flash("Successfully Sign Up")
        return redirect(url_for('users.new'))

    else:
        return render_template('users/sign_up.html', username=request.form['username'], email=request.form['email'], password=request.form['password'], errors=s.errors)


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
