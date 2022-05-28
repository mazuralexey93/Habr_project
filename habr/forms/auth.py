from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField


class UserLoginForm(FlaskForm):
    email = StringField('Почтовый адрес', [
        validators.DataRequired(),
    ])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
    ])
    submit = SubmitField('Log in')


class UserRegisterForm(FlaskForm):
    email = StringField('Почтовый адрес', [
        validators.DataRequired(),
        validators.Email(),
    ])
    username = StringField('Имя')
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.Length(min=8),
    ])
    confirm = PasswordField('Повторите пароль', [
        validators.DataRequired(),
        validators.EqualTo('password', message="Пароли не совпадают"),
    ])
    submit = SubmitField('Зарегистрировать')
