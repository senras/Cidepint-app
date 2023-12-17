from src.core.database import db
from sqlalchemy import not_
from src.core.models.userRoles.userRol import UserRol


"""
funcion para obtener un userRol por id
"""


def get_userRol_by_id(id):
    return UserRol.query.get(id)


"""
obtiene los userRoles de un usuario
"""


def get_instituciones_by_user_id(id):
    userRoles = UserRol.query.filter_by(user_id=id).all()
    instituciones = [
        userRol.instituciones for userRol in userRoles if userRol.instituciones is not None]

    return instituciones


def get_userRol_by_user_id(id):
    return UserRol.query.filter_by(user_id=id).all()


"""
funcion para listar los usersRoles
"""


def list_usersRoles():
    return UserRol.query.all()


"""
funcion para crear un userRol
"""


def create_userRol(rol, user, institucion=None):
    if institucion:
        institucion_id = institucion.id
    else:
        institucion_id = None
    userRol = UserRol(rol=rol, user=user, institucion_id=institucion_id)
    db.session.add(userRol)
    db.session.commit()
    return userRol


"""
funcion que verifica si un usuario ya tiene un rol determinado en una institucion
"""


def verificar_userRol(user_id, institucion_id, rol_id=None):
    if rol_id == None:
        return UserRol.query.filter_by(user_id=user_id, institucion_id=institucion_id).first() is not None
    return UserRol.query.filter_by(user_id=user_id, institucion_id=institucion_id, rol_id=rol_id).first() is not None


"""
esta funcion fue creada para crear un userRol por los id de usuario, rol e institucion
"""


def create_userRol2(**kwargs):
    userRol = UserRol(**kwargs)
    db.session.add(userRol)
    db.session.commit()
    return userRol


"""
funcion para obtener el id del rol a partir del id de usuario y de institucion
"""


def get_id_rol_by_user_institucion(user_id, institucion_id):
    return UserRol.query.filter_by(user_id=user_id, institucion_id=institucion_id).first().rol_id


"""
funcion para editar un userRol
"""


def edit_userRol(id, data):
    userRol = get_userRol_by_id(id)
    userRol.user_id = data['user_id']
    userRol.rol_id = data['rol_id']
    userRol.institucion_id = data['institucion_id']
    db.session.commit()
    return userRol


"""
funcion para eliminar un userRol
"""


def delete_userRol(id):
    userRol = get_userRol_by_id(id)
    db.session.delete(userRol)
    db.session.commit()
    return userRol


def get_id_userRol_by_userid_rolid(user_id, rol_id):
    """
    Busca el userRol por id de usuraio y id de rol
    """
    user_rol = UserRol.query.filter_by(user_id=user_id, rol_id=rol_id).first()
    if user_rol is not None:
        return user_rol.id
    else:
        return None
