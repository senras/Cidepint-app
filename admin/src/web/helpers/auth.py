from functools import wraps
from flask import session
from flask import abort
from flask import render_template
from flask import redirect
from src.core import auth
from src.core.models.users import get_user_by_id
from src.core.models.configuracion import get_Config
from src.core.models.roles import get_rol_by_id
from src.core.models.instituciones import get_institucion
from src.core.models.configuracion import get_manteinance_status
from src.core.models.configuracion import get_manteinance_message
from src.core.models.solicitudes import get_solicitudes_by_institucion_id


def is_authenticated(session):
    """
    Verifica si el usuario actual está autenticado.

    Args:
        session (dict): El objeto de sesión de la aplicación Flask.

    Returns:
        bool: Devuelve True si el usuario está autenticado, de lo contrario False.
    """
    return session.get("user") is not None


"""
funcion para validar si el usuario esta logueado
"""


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function


"""
funcion para validar si el usuario es super administrador (para usar dentro del layout)
"""


def is_super_admin_by_id(user_id):
    user = get_user_by_id(user_id)
    if user.userRoles:
        if user.userRoles[0].rol.nombre == "super_administrador":
            return True
        else:
            return False
    else:
        return False


def is_super_admin(session):
    user = get_user_by_id(session.get("user"))
    if user:
        if user.userRoles:
            if user.userRoles[0].rol.nombre == "super_administrador":
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def is_super_admin_session(session):
    role = get_rol_by_id(session.get("rol"))
    if role:
        if role.nombre == "super_administrador":
            return True
        else:
            return False
    else:
        return None


"""
funcion para validar si el usuario es dueño(para usar dentro del layout)
"""


def is_owner(session):
    role = get_rol_by_id(session.get("rol"))
    if role:
        if role.nombre == "owner":
            return True
        else:
            return False
    else:
        return None


def is_operador(session):
    role = get_rol_by_id(session.get("rol"))
    if role:
        if role.nombre == "operador":
            return True
        else:
            return False
    else:
        return None


"""
decorador de permisos
"""


def permission_require(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not has_permission(permission):
                return abort(401)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


"""
funcion para obtener las instituciones del usuario autenticado que no es el super administrador
"""


def get_instituciones_by_user_id(session):
    user = get_user_by_id(session.get("user"))
    instituciones = []
    if user:
        for userRol in user.userRoles:
            instituciones.append(userRol.instituciones)
        return instituciones
    return None


def get_instituciones_by_user_id_without_blocked(session):
    user = get_user_by_id(session.get("user"))
    instituciones = []
    if user:
        for userRol in user.userRoles:
            if userRol.instituciones.habilitado:
                instituciones.append(userRol.instituciones)
        return instituciones
    return None


"""
funcion para validar si el usuario tiene permisos para acceder a la pagina
"""


def has_permission(required_permissions_list):
    has_permission = True
    """
    se consigue una lista de permisos del usuario por el rol que tiene:
    """
    user_permissions_list = auth.list_permissions_by_role_id(
        session.get("rol"))
    for permission in required_permissions_list:
        if not (permission in user_permissions_list):
            print("has_permission === no esta el permiso %s " % permission)
            has_permission = False
            break
    return has_permission


# Funcion para mostrar info del modulo de configuracion
def get_config():
    config = get_Config()
    return config


"""
esta funcion obtiene el nombre de la institucion actual del usuario
"""


def get_institucion_actual(session):
    institucion = get_institucion(session.get("institucion"))
    return institucion.nombre


def get_institucion_actual(session):
    institucion = get_institucion(session.get("institucion"))
    if institucion:
        return institucion.nombre
    else:
        return None


def rol_pendiente(session):
    role = get_rol_by_id(session.get("rol"))
    if role:
        if role.nombre == "pendiente":
            return True
        else:
            return False
    else:
        return None


def in_manteinance():
    if get_manteinance_status() and (not is_super_admin(session)):
        print("Estado de mantenimiento:", get_manteinance_status())
        print("Es admin:", not is_super_admin(session))
        return render_template('configuracion/manteinance.html', message=get_manteinance_message())


def parse_date(date):
    parsed_date = date.strftime("%d/%m/%Y")
    return parsed_date


def parse_date_with_hour(date):
    parsed_date = date.strftime("%H:%M - %d/%m/%Y")
    return parsed_date


def get_cant_solicitudes(session):
    solicitudes = get_solicitudes_by_institucion_id(session.get("institucion"))
    return len(solicitudes)
