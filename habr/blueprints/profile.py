from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from habr.models.post import Post
from habr.models.user import User, Profile

profile = Blueprint(
    name='profile',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static',
    url_prefix='/profile')


@profile.route("/<int:pk>/")
def user_profile_info(pk: int):
    user_profile = User.query.filter_by(id=pk).first_or_404()
    profile_info = Profile.query.filter_by(user_id=pk).one_or_none()
    title = f'Личный кабинет {user_profile.username}'
    if not user_profile:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template('profile.html', title=title, user=user_profile, profile=profile_info)


@profile.route("/posts/<int:pk>/")
def show_user_posts(pk: int):
    user_profile = User.query.filter_by(id=pk).first_or_404()
    postlist = Post.query.filter_by(user_id=pk).order_by(
                Post.created_at.desc()).all()

    title = f'Все статьи {user_profile.username}'
    return render_template('index.html', title=title, postlist=postlist, user=user_profile)
