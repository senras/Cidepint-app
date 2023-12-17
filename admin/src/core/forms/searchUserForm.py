from wtforms import Form
from wtforms import SelectField
from wtforms import StringField


class searchUserForm(Form):
    choices = [('Bloqueado', 'Bloqueado'),
               ('Habilitado', 'Habilitado'), ('Todos', 'Todos')]
    email = StringField('', description="mail@buscado.com")
    status = SelectField('', choices=choices, default="Todos")
