from wtforms import Form
from wtforms import StringField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):

    first_name = StringField('Nombre', [validators.Length(
        min=4, max=100, message="El nombre debe tener entre 4 y 100 caracteres.")])
    last_name = StringField('Apellido', [validators.Length(
        min=4, max=100, message="El apellido debe tener entre 4 y 100 caracteres.")])
    user_name = StringField('Nombre de usuario', [validators.Length(
        min=4, max=100, message="El nombre de usuario debe tener entre 4 y 100 caracteres.")])
    email = EmailField('Email', [validators.Length(
        min=4, max=100, message="El email debe tener entre 4 y 100 caracteres."), validators.Email()])
