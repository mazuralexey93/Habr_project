from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from habr.models.user import User


auth = Blueprint(
    name='auth',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@auth.route('/login', methods=['POST','GET'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))