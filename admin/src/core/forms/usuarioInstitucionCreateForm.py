from wtforms import Form
from wtforms import IntegerField
from wtforms import validators

class UsuarioInstitucionCreateForm(Form):
    user_id = IntegerField('Selecciona usuario', [validators.InputRequired(message="El campo usuario es requerido")])  
    rol_id = IntegerField('Selecciona rol', [validators.InputRequired(message="El campo rol es requerido")])