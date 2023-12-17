from wtforms import Form
from wtforms import IntegerField
from wtforms import validators

class OwnerCreateForm(Form):
    user_id = IntegerField('Selecciona usuario', [validators.InputRequired(message="El campo usuario es requerido")])
    institucion_id = IntegerField('Selecciona institucion', [validators.InputRequired(message="El campo institucion es requerido")])
