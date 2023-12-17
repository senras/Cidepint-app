from wtforms import Form
from wtforms import IntegerField
from wtforms import validators


class SeleccionarInstitucionForm(Form):
    institucion_id = IntegerField('Selecciona institucion', [validators.InputRequired()])

