from wtforms import Form
from wtforms import StringField
from wtforms import EmailField
from wtforms import PasswordField
from wtforms import validators


class EditUserForm(Form):
    email = EmailField('Email', [validators.Length(min=4, max=50, message="El email debe tener entre 4 y 50 caracteres."), validators.Email(
        message="El email debe ser válido."), validators.DataRequired(message="Debe ingresar un email.")])
    password = PasswordField('Contraseña', [
                             validators.Length(min=4, max=100, message="La contraseña debe tener entre 4 y 100 caracteres."), validators.DataRequired(message="Debe ingresar una contraseña.")])
    first_name = StringField('Nombre', [validators.Length(
        min=4, max=50, message="El nombre debe tener entre 4 y 50 caracteres."), validators.DataRequired()])
    last_name = StringField('Nombre', [validators.Length(
        min=4, max=50, message="El apellido debe tener entre 4 y 50 caracteres."), validators.DataRequired()])
