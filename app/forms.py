from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class BuscaTodos(FlaskForm):
    titulo = StringField('Escribe el titulo', validators=[DataRequired()])
    pagina = HiddenField('Pagina')
    submit = SubmitField('Aceptar')
