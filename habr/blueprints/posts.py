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
    postlist = Post.query.all()
    return render_template('index.html', postlist=postlist)


@posts.route("/theme/<theme_name>/")
def theme_filter(theme_name):
    for theme in Post.query.all():
        if theme_name == 'web':
            concrete_theme = theme
        elif theme_name == 'design':
            concrete_theme = theme
        elif theme_name == 'mobile':
            concrete_theme = theme
        elif theme_name == 'marketing':
            concrete_theme = theme
        else:
            raise NotFound("Нет такой категории!")
    return render_template('index.html', theme=concrete_theme)
