from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, validators, SubmitField, SelectField


class CreateArticleForm(FlaskForm):
    title = StringField('Название статьи', [validators.DataRequired()])
    text = CKEditorField('Текст', [validators.DataRequired()])
    category = SelectField('Категория', [validators.DataRequired()])
    description = CKEditorField('Описание', [validators.DataRequired()])
    submit = SubmitField('Добавить')