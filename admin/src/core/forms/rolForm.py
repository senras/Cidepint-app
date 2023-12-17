from wtforms import Form
from wtforms import StringField
from wtforms import validators


class RolForm(Form):
    nombre = StringField('Nombre', [validators.Length(min=4, max=25)])