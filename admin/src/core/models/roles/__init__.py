from src.core.database import db

from src.core.models.roles.rol import Rol
from src.core.models.rolesPermisos.rolPermiso import RolPermiso
from src.core.models.userRoles.userRol import UserRol


"""
funcion para listar los roles
"""
def list_roles():
    return Rol.query.all()

"""
funcion para obtener un rol por id
"""
def get_rol_by_id(id):
    return Rol.query.get(id)

"""
funcion para obtener un rol por nombre
"""
def get_rol_by_name(name):
    return Rol.query.filter_by(nombre=name).first()

def list_roles_except_owner_and_superadmin_and_pendiente():
    """
    Devuelve un queryset con todos los usuarios excepto el dueño, 11 seria el superadmin.
    """
    roles = Rol.query.filter((Rol.nombre != 'owner') & (Rol.nombre != 'super_administrador') & (Rol.nombre != 'pendiente')).all()

    return roles

"""
funcion para crear un rol
"""
def create_rol(nombre):
    rol = Rol(nombre=nombre)
    db.session.add(rol)
    db.session.commit()
    return rol  

"""
funcion para editar un rol
"""
def edit_rol(id, data):
    rol = get_rol_by_id(id)
    rol.nombre = data
    db.session.commit()
    return rol

"""
funcion para eliminar un rol, elimina los userRoles y los rolPermisos asociados al rol
"""
def delete_rol(id):
    rol = get_rol_by_id(id)
    user_roles = UserRol.query.filter_by(rol_id=id).all()
    list(map(db.session.delete, user_roles))
    rol_permisos = RolPermiso.query.filter_by(rol_id=id).all()
    list(map(db.session.delete, rol_permisos))
    db.session.delete(rol)
    db.session.commit()
    return rol

