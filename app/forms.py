from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField


class BuscaTodos(FlaskForm):
    titulo = StringField('Escribe el titulo', validators=[DataRequired()])
    submit = SubmitField('Aceptar')
