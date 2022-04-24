from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField


class CreateArticleForm(FlaskForm):
    title = StringField('Название статьи', [validators.DataRequired()])
    text = TextAreaField('Текст', [validators.DataRequired()])
    description = TextAreaField('Описание', [validators.DataRequired()])
    submit = SubmitField('Добавить')