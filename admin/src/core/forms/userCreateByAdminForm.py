from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import EmailField
from wtforms import validators


class UserCreateByAdminForm(Form):

    user_name = StringField('Nombre de usuario', [
                            validators.DataRequired(message="Debe ingresar un nombre de usuario."), validators.Length(min=3, max=50, message="El nombre de usuario debe tener entre 3 y 50 caracteres.")])
    first_name = StringField('Nombre', [validators.DataRequired(
        message="Debe ingresar un nombre."), validators.Length(min=3, max=100, message="El nombre debe tener entre 3 y 100 caracteres.")])
    last_name = StringField('Apellido', [validators.Length(
        min=3, max=100), validators.DataRequired(message="Debe ingresar un apellido.")])
    email = EmailField('Email', [validators.DataRequired(message="Debe ingresar un email."), validators.Length(
        min=6, max=100), validators.Email(message="Debe ingresar un email válido.")])
    password = PasswordField('Contraseña', [validators.DataRequired(message="Debe ingresar una contraseña."), validators.Length(
        min=4, max=100)])
    status = StringField('Estado', [validators.Length(
        min=2, max=15)], default='Habilitado')
