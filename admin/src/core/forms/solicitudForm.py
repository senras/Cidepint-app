from wtforms import Form
from wtforms import TextAreaField
from wtforms import SelectField
from wtforms import validators


# Es un formulario para crear una solicitud de testeo // Se crea desde la app pública
class SolicitudForm(Form):
    user = SelectField("Usuario", choices=[])
    servicio = SelectField("Servicio", choices=[])
    observaciones = TextAreaField('Observaciones', validators=[
        validators.Length(min=4, max=255)]
    )
