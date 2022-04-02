from flask import Blueprint

posts = Blueprint('posts',__name__, template_folder='templates', static_folder='static')

@posts.route('/')
def index():
    return "posts"