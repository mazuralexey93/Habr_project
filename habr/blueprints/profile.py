from flask import Blueprint, render_template
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound, Forbidden
from habr.models.post import Post
from habr.models.user import User, Profile

status_dic = {
    'not_published': 'Черновики',
    'published': 'Опубликованы',
    'modering': 'На модерации',
    'need_refactor': 'Требуется редактирование',
    'archieved': 'В архиве',
}

profile = Blueprint(
    name='profile',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static',
    url_prefix='/profile')


@profile.route("/")
def user_profile_page():
    if current_user.is_anonymous:
        raise Forbidden()
    user_profile = User.query.get(current_user.id)
    title = f'Личный кабинет {current_user.username}'
    return render_template('profile_index_page.html', title=title, user=user_profile)


@profile.route("/about/")
def user_profile_info():
    if current_user.is_anonymous:
        raise Forbidden()
    user_profile = User.query.get(current_user.id)
    profile_info = Profile.query.filter_by(user_id=current_user.id).first()
    title = f'Личные данные {current_user.username}'
    return render_template('profile_info.html', title=title, user=user_profile, profile=profile_info)


@profile.route("/posts/")
def user_posts_page():
    if current_user.is_anonymous:
        raise Forbidden()
    user_profile = User.query.filter_by(id=current_user.id).first_or_404()
    title = f'Статьи {current_user.username}'
    return render_template('profile_posts_index.html', title=title, user=user_profile)


@profile.route("/posts/<status_name>/")
def status_filter(status_name: str):
    if status_name not in status_dic.keys():
        raise NotFound()
    postlist = Post.query \
        .filter(Post.status == status_name.upper()) \
        .filter_by(user_id=current_user.id) \
        .order_by(
        Post.created_at.desc()).all()
    return render_template('index.html', menu=status_name,
                           pageheader=status_dic[status_name],
                           title=status_dic[status_name], postlist=postlist)


@profile.route("/posts/all/")
def show_user_posts():
    if current_user.is_anonymous:
        raise Forbidden()
    user_profile = User.query.filter_by(id=current_user.id).first_or_404()
    postlist = Post.query.filter_by(user_id=current_user.id).order_by(
        Post.created_at.desc()).all()

    title = f'Все статьи {current_user.username}'
    return render_template('index.html', title=title, postlist=postlist, user=user_profile)


@profile.route("/admin/<status>/")
def moder_user_posts(status: str):
    status = 'modering'
    if current_user.is_admin or current_user.is_staff:
        postlist = Post.query.filter(Post.status == status.upper()).order_by(Post.created_at.desc()).all()
    else:
        raise Forbidden()

    title = f'Статьи пользователя {current_user.username} на модерации'
    return render_template('index.html', title=title, postlist=postlist)
