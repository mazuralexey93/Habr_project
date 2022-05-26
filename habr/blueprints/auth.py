from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from habr.models.user import User
from habr.forms.auth import UserLoginForm, UserRegisterForm
from habr.models.database import db

auth = Blueprint(
    name='auth',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.user_profile_info', pk=current_user.id))

    form = UserLoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        print(check_password_hash(user.password, form.password.data))
        if (user is None) or (not check_password_hash(user.password, form.password.data)):
            return render_template("login.html", form=form, error="invalid username or password")
        login_user(user)
        return redirect(url_for('profile.user_profile_info', pk=current_user.id))

    return render_template("login.html", form=form)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile.user_profile_info', pk=current_user.id))

    form = UserRegisterForm(request.form)

    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('/register.html', form=form)

        _user = User(
            email=form.email.data,
            username=form.username.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)
        return render_template('/profile_index_page.html')

    return render_template('/register.html', form=form, errors=errors, title="Регистрация")

