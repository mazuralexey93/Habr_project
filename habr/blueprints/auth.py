from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from habr.models.user import User
from habr.forms.auth import UserLoginForm


auth = Blueprint(
    name='auth',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserLoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if (user is None) or (not check_password_hash(user.password, form.password.data)):
            return render_template("login.html", form=form, error="invalid username or password")

        login_user(user)
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))