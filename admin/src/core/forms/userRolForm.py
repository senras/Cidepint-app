from wtforms import Form
from wtforms import IntegerField
from wtforms import validators

class UserRolForm(Form):
    user_id = IntegerField('Selecciona usuario', [validators.InputRequired()])
    institucion_id = IntegerField('Selecciona institucion', [validators.InputRequired()])
    rol_id = IntegerField('Selecciona rol', [validators.InputRequired()])