from wtforms import Form
from wtforms import IntegerField
from wtforms import validators

class RolPermisoForm(Form):
    permiso_id = IntegerField('Selecciona permiso', [validators.InputRequired()])
    rol_id = IntegerField('Selecciona rol', [validators.InputRequired()])