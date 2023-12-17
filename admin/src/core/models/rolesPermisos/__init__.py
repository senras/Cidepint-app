from src.core.database import db

from src.core.models.rolesPermisos.rolPermiso import RolPermiso

"""
funcion para obtener un rolPermiso por id
"""


def get_rolPermiso_by_id(id):
    return RolPermiso.query.filter_by(id=id).first()


"""
funcion para listar los rolesPermisos
"""


def list_rolesPermisos():
    return RolPermiso.query.all()


"""
funcion para crear un rolPermiso
"""


def create_rolPermiso(**kwargs):
    rolPermiso = RolPermiso(**kwargs)
    db.session.add(rolPermiso)
    db.session.commit()
    return rolPermiso


"""
funcion para editar un rolPermiso
"""


def edit_rolPermiso(id, data):
    rolPermiso = get_rolPermiso_by_id(id)
    rolPermiso.rol_id = data['rol_id']
    rolPermiso.permiso_id = data['permiso_id']
    db.session.commit()
    return rolPermiso


"""
funcion para eliminar un rolPermiso
"""


def delete_rolPermiso(id):
    rolPermiso = get_rolPermiso_by_id(id)
    db.session.delete(rolPermiso)
    db.session.commit()
    return rolPermiso


def add_permisos_to_rol(rol, permisos):
    rol_id = rol.id
    for permiso in permisos:
        rolPermiso = RolPermiso(rol_id=rol_id, permiso_id=permiso.id)
        db.session.add(rolPermiso)
    db.session.commit()
    return rolPermiso
