from wtforms import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import validators


class editarsolicitudForm(Form):
    status = SelectField("Estado", choices=[
                         'Aceptada', 'Rechazada', 'En proceso', 'Finalizada', 'Cancelada'])
    observaciones = TextAreaField(
        'Observaciones', description="Escribir cualquier observación relevante aquí..")
