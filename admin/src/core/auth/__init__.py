from src.core.models.users import User
from src.core.bcrypt import bcrypt
from src.core.models.userRoles import UserRol
from src.core.models.rolesPermisos import RolPermiso


def find_user_by_email(email):
    """
    Busca y devuelve al usuario cuyo Email recibe por parametro.
    """
    return User.query.filter_by(email=email).first()


def check_user(email, password):
    """
    Verifica si el usuario con el email proporcionado existe y si la contraseña es correcta.

    Args:
        email (str): El correo electrónico del usuario.
        password (str): La contraseña proporcionada por el usuario.

    Returns:
        user: Devuelve el objeto de usuario si las credenciales son correctas, de lo contrario None.
    """
    user = find_user_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None


"""
    este metodo es para buscar un usuario por su mail
"""
def find_user_by_mail(mail):
    return User.query.filter_by(email=mail).first()


"""
    este metodo es para buscar un rol por el id del usuario y el id de la institucion
"""
def find_role_by_user_id_and_institution_id(user_id, institution_id):
    return UserRol.query.filter_by(user_id=user_id, institution_id=institution_id).first().role


"""
    este metodo es para listar los permisos por el id del rol
"""
def list_permissions_by_role_id(role_id):
    Permisos_roles = RolPermiso.query.filter_by(rol_id=role_id).all()

    permisos_nombres = []
    for permisoPorRol in Permisos_roles:
        permisos_nombres.append(permisoPorRol.permiso.nombre)
    return permisos_nombres
