from wtforms import Form
from wtforms import BooleanField
from wtforms import StringField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import validators


class ServiceForm(Form):
    tipo_servicio_choices = [
        ('Análisis'),
        ('Consultoría'),
        ('Desarrollo'),
    ]
    nombre = StringField('Nombre', [validators.Length(
        min=4, max=255, message="El nombre debe tener entre 4 y 255 caracteres.")])
    descripcion = TextAreaField(
        'Descripción', [validators.DataRequired(message="Debe ingresar una descripción.")])
    palabras_claves_busqueda = StringField('Palabras claves de búsqueda', [
                                           validators.DataRequired(message="Debe ingresar al menos una palabra clave de búsqueda.")])
    listado_centros_habilitados = StringField('Centros habilitados', [
                                              validators.DataRequired(message="Debe ingresar al menos un centro habilitado.")])
    tipo_servicio = SelectField(
        'Tipo de servicio', choices=tipo_servicio_choices, validators=[validators.DataRequired(message="Debe seleccionar un tipo de servicio.")])
    habilitado = BooleanField('Habilitado', default=True)
