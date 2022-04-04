from flask import Blueprint, render_template
from habr.models.database import db

users = Blueprint('users',__name__, template_folder='templates', static_folder='static')

@users.route('/')
def user_list():
    users  = db.session.query.all()
    return render_template('user.html', list=users)