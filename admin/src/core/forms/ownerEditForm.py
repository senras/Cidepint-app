from wtforms import Form
from wtforms import IntegerField
from wtforms import validators


class OwnerEditForm(Form):
    institucion_id = IntegerField('Selecciona institucion', [
                                  validators.InputRequired(message="Debe seleccionar una institución.")])
