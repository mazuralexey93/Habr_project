from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from habr.models.post import Post
from habr.models.user import User

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
    return render_template('index.html', menu='main', title="Главная страница",
                           pageheader="Главная страница", postlist=postlist)


@posts.route("/theme/<theme_name>/")
def theme_filter(theme_name: str):
    if theme_name not in themes_dic.keys():
        raise NotFound('Нет такой категории!')
    postlist = Post.query.filter(Post.category == theme_name.upper()).order_by(
        Post.created_at.desc()).all()
    return render_template('index.html', menu=theme_name,
                           pageheader=themes_dic[theme_name],
                           title=themes_dic[theme_name], postlist=postlist)


@posts.route("/author/<int:pk>/")
def author_filter(pk: int):
    author = User.query.filter_by(id=pk).first_or_404()
    postlist = Post.query.filter_by(user_id=pk).order_by(
        Post.created_at.desc()).all()
    title = f'Все статьи автора {author.username}'
    return render_template('index.html', title=title, postlist=postlist)


@posts.route('/post/<int:pk>')
def concrete_post(pk: int):
    selected_post = Post.query.filter_by(id=pk).first_or_404()
    title = selected_post.user.username + ' «' + selected_post.header + '»'
    return render_template('article.html', post=selected_post, title=title)
