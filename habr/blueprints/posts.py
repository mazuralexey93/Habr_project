from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from habr.models.post import Post

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
def theme_filter(theme_name: str):
    chosen_category = ''
    postlist = Post.query.order_by(Post.created_at.desc()).filter(Post.category == theme_name.upper()).all()

    for cat in postlist:
        if theme_name == cat.category:
            chosen_category = cat.category

        return render_template('index.html', cat=chosen_category, postlist=postlist)
    else:
        raise NotFound("Нет такой категории!")
