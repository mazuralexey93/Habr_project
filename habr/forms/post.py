from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, validators, SubmitField, SelectField


class CreateArticleForm(FlaskForm):
    title = StringField('Название статьи', [validators.DataRequired()])
    text = CKEditorField('Текст', [validators.DataRequired()])
    category = SelectField('Категория', [validators.DataRequired()])
    description = CKEditorField('Описание', [validators.DataRequired()])
    submit = SubmitField('Сохранить')
    status = SelectField('Cтатус')


class AddCommentForm(FlaskForm):
    body = StringField('Ваш комментарий', [validators.InputRequired()])
    submit = SubmitField('Добавить')


class UpdateCommentForm(FlaskForm):
    body = StringField('Ваш комментарий', [validators.DataRequired()])
    submit = SubmitField('Обновить комментарий')
