from wtforms import Form
from wtforms import TextAreaField


class cargarnotaForm(Form):
    comentario = TextAreaField(
        '', description="Ingrese sus comentarios sobre la solicitud para comunicarse con el cliente aquí..", )
