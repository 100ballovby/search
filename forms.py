from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):  # мои формы строятся по шаблону FlaskForm
    p_lang = StringField('Programmig language',  # подпись к полю
                         validators=[DataRequired()])  # сделать поле обязательным
    sort = StringField('Sort')
    submit = SubmitField('Search')
