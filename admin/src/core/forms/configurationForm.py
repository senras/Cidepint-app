from wtforms import Form
from wtforms import IntegerField
from wtforms import StringField
from wtforms import BooleanField
from wtforms import EmailField
from wtforms import TelField
from wtforms import validators


class ConfigForm(Form):
    element_quantity = IntegerField('Cantidad de elementos por página (Paginación):', [
                                    validators.NumberRange(min=1, max=100, message="El valor debe estar entre 1 y 100")])
    contact_email = EmailField('Email:', [validators.Length(
        min=4, max=50, message="El email debe tener entre 4 y 50 caracteres"), validators.Email(message="El email no es válido")])
    contact_phone = TelField('Teléfono:', [validators.Length(
        min=4, max=50, message="El teléfono debe tener entre 4 y 50 caracteres")])
    contact_address = StringField(
        'Dirección:', [validators.Length(min=4, max=50, message="La dirección debe tener entre 4 y 50 caracteres")])
    in_manteinance = BooleanField("En mantenimiento:")
    manteinance_message = StringField(
        'Mensaje de mantenimiento:', [validators.Length(min=4, max=50, message="El mensaje debe tener entre 4 y 50 caracteres")], default="En mantenimiento")
