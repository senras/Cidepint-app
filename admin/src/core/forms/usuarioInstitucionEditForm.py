from wtforms import Form
from wtforms import IntegerField
from wtforms import validators

class UsuarioInstitucionEditForm(Form): 
    rol_id = IntegerField('Selecciona rol', [validators.InputRequired(message="El campo rol es requerido")])