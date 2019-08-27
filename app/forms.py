from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BuscaTodos(FlaskForm):
    titulo = StringField('Escribe el titulo', validators=[DataRequired()])
    submit = SubmitField('Aceptar')
