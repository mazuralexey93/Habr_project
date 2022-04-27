from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField


class UserLoginForm(FlaskForm):
    email = StringField('Login', [
        validators.DataRequired(),
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    submit = SubmitField('Log in')
