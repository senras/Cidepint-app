from wtforms import Form
from wtforms import BooleanField
from wtforms import StringField
from wtforms import FloatField
from wtforms import validators


class InstitucionForm(Form):
    nombre = StringField('Nombre', [validators.DataRequired(
        message="Debe ingresar un nombre para la institución."), validators.Length(min=3, max=255, message="El nombre debe ser mayor a 3 caracteres.")])
    infoInstitucion = StringField('Información de la institución', [
                                  validators.Length(min=4, max=255, message="La información de la institución debe ser mayor a 4 caracteres.")])
    direccion = StringField('Dirección', [validators.Length(
        min=4, max=100, message="La dirección debe estar entre 4 y 100 caracteres.")])
    web = StringField('Web', [validators.Length(
        min=4, max=100, message="La dirección web debe estar entre 4 y 100 caracteres.")])
    palabrasClaves = StringField('Palabras claves de búsqueda', [
                                 validators.Length(min=4, max=255, message="Las palabras claves de búsqueda deben ser mayor a 4 caracteres.")])
    diasHorarios = StringField('Días y horarios de atención', [
                               validators.Length(min=4, max=255, message="Los días y horarios de atención deben ser mayor a 4 caracteres.")])
    infoContacto = StringField('Información de contacto', [
                               validators.Length(min=4, max=255, message="La información de contacto debe ser mayor a 4 caracteres.")])
    habilitado = BooleanField('Habilitado', default=True)
    latitud = FloatField('Latitud', [validators.DataRequired(
        message="Debe ingresar una latitud.")])
    longitud = FloatField('Longitud', [validators.DataRequired(
        message="Debe ingresar una longitud.")])
