from wtforms import Form
from wtforms import SelectField
from wtforms import StringField
from wtforms import DateField
from wtforms import validators
from wtforms.validators import ValidationError
from datetime import timedelta
from datetime import datetime
from flask import flash


class searchSolicitudForm(Form):
    # Filtrar solicitud por tipo de servicio, rango de fechas, estado de solucitud y solicitante.
    status_choices = ['Aceptada', 'Rechazada',
                      'En proceso', 'Finalizada', 'Cancelada', 'Todas']
    tipo_servicio_choices = ["Análisis", "Consultoría", "Desarrollo", "Todos"]
    tipo_servicio = SelectField(
        'Tipo de servicio', choices=tipo_servicio_choices, default="Todos", validators=[validators.DataRequired(message="Debe seleccionar un tipo de servicio.")])
    fecha_inicio = DateField(
        'Fecha inicial', format='%Y-%m-%d', default=(datetime.today() - timedelta(days=30)))
    fecha_fin = DateField('Fecha final', format='%Y-%m-%d',
                          default=datetime.today)
    status = SelectField('Estado de solicitud',
                         choices=status_choices, default="Todas")
    cliente = StringField('Cliente', description="cliente, usuario, etc.")

    def validate_fecha_fin(form, field):
        if field.data < form.fecha_inicio.data:
            return flash("Fecha final debe ser mayor a fecha inicial", "error")

    # datetime.strptime("2023-01-01", '%Y-%m-%d')
