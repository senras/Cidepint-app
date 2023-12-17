from src.core.database import db
from src.core.models.instituciones.institucion import Institucion
from src.core.models.userRoles.userRol import UserRol

"""
funcion para listar los instituciones
"""


def list_instituciones():
    instituciones = Institucion.query.all()

    return instituciones


"""
funcion para crear un institucion
"""


def create_institucion(**kwargs):
    institucion = Institucion(**kwargs)
    db.session.add(institucion)
    db.session.commit()

    return institucion


"""
funcion para obtener una institucion
"""


def get_institucion(id):
    institucion = Institucion.query.get(id)

    return institucion


"""
funcion para editar una institucion
"""


def edit_institucion(id, data):
    institucion = get_institucion(id)
    institucion.nombre = data['nombre']
    institucion.infoInstitucion = data['infoInstitucion']
    institucion.direccion = data['direccion']
    institucion.latitud = data['latitud']
    institucion.longitud = data['longitud']
    institucion.web = data['web']
    institucion.palabrasClaves = data['palabrasClaves']
    institucion.diasHorarios = data['diasHorarios']
    institucion.infoContacto = data['infoContacto']
    db.session.commit()

    return institucion


"""
funcion para eliminar una institucion, en la cual antes de eliminarla se eliminan 
los userRoles asociados a la institucion
"""


def delete_institucion(id):
    institucion = get_institucion(id)
    user_roles = UserRol.query.filter_by(institucion_id=id).all()
    list(map(db.session.delete, user_roles))
    db.session.delete(institucion)
    db.session.commit()

    return True


def ban_institucion(id):
    institucion = get_institucion(id)
    institucion.habilitado = False
    db.session.commit()

    return True


def unban_institucion(id):
    institucion = get_institucion(id)
    institucion.habilitado = True
    db.session.commit()

    return True


def get_resolucion_promedio(id):
    # get resolution average for an institution in hours
    # The resolution time is the difference between the insertion date and the status at date of the request
    # if the request has a status of 'Finalizada'
    institucion = get_institucion(id)
    promedio = 0
    for servicio in institucion.servicios:
        for solicitud in servicio.solicitudes:
            if solicitud.status == 'Finalizada':
                promedio += (solicitud.status_at -
                             solicitud.inserted_at).seconds / 3600
    return promedio / len(institucion.servicios)
