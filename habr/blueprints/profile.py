from flask import Blueprint, render_template
from flask_login import login_required, current_user

from habr.models.post import Post
from habr.models.user import User, Profile

profile = Blueprint(
    name='profile',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static',
    url_prefix='/profile')


@login_required
@profile.route("/")
def user_profile_page():

    user_profile = User.query.get(int(1))  # после логина тут будет вставляться id пользователя
    title = f'Личный кабинет {current_user.username}'
    return render_template('profile_index_page.html', title=title, user=user_profile)


@login_required
@profile.route("/about/")
def user_profile_info():

    user_profile = User.query.get(current_user.id)  # после логина тут будет вставляться id пользователя
    profile_info = Profile.query.filter_by(user_id=current_user.id).one_or_none()  # и тут
    title = f'Личные данные {current_user.username}'
    return render_template('profile_info.html', title=title, user=user_profile, profile=profile_info)


@login_required
@profile.route("/posts/")
def user_posts_page():
    user_profile = User.query.filter_by(id=current_user.id).first_or_404()  # и тут
    title = f'Статьи {current_user.username}'
    return render_template('profile_posts_index.html', title=title, user=user_profile)


@login_required
@profile.route("/posts/all/")
def show_user_posts():
    user_profile = User.query.filter_by(id=current_user.id).first_or_404()  # и тут
    postlist = Post.query.filter_by(user_id=current_user.id).order_by(   # и тут
                Post.created_at.desc()).all()

    title = f'Все статьи {current_user.username}'
    return render_template('index.html', title=title, postlist=postlist, user=user_profile)
