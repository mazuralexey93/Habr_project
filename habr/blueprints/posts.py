from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from habr.models.database import db
from habr.models.post import Post
from habr.models.user import User

posts = Blueprint(
    name='posts',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@posts.route('/')
def post_list():
    postlist = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', postlist=postlist)


@posts.route("/theme/<theme_name>/")
def theme_filter(theme_name):
    postlist = Post.query.order_by(Post.created_at.desc()).all()

    for cat in postlist:
        theme_name = cat.category

    #         raise NotFound("Нет такой категории!")
    return render_template('index.html', theme_name=theme_name, postlist=postlist)
