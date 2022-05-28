from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField, SelectField

from habr.models.database import CategoryChoices


class CreateArticleForm(FlaskForm):
    title = StringField('Название статьи', [validators.DataRequired()])
    text = TextAreaField('Текст', [validators.DataRequired()])
    category = SelectField('Категория', [validators.DataRequired()])
    description = TextAreaField('Описание', [validators.DataRequired()])
    submit = SubmitField('Добавить')


class AddCommentForm(FlaskForm):
    body = StringField('Ваш комментарий', [validators.InputRequired()])
    submit = SubmitField('Добавить')

class UpdateCommentForm(FlaskForm):
    body = StringField('Ваш комментарий', [validators.DataRequired()])
    submit = SubmitField('Обновить комментарий')