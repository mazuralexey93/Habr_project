from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from habr.models.post import Post

themes_dic = {
    'design': 'Дизайн',
    'web': 'Веб-разработка',
    'mobile': 'Мобильная разработка',
    'marketing': 'Маркетинг',
}

posts = Blueprint(
    name='posts',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@posts.route('/')
def post_list():
    postlist = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', menu=None, title="Главная страница",
                           postlist=postlist)


@posts.route("/theme/<theme_name>/")
def theme_filter(theme_name: str):
    postlist = Post.query.filter(Post.category == theme_name.upper()).order_by(
        Post.created_at.desc())
    return render_template('index.html', menu=theme_name,
                           title=themes_dic[theme_name], postlist=postlist)
