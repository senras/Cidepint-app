from src.core.database import db
from src.core.models.rolesPermisos.rolPermiso import RolPermiso
from src.core.models.permisos.permiso import Permiso

"""
funcion para listar los permisos
"""
def list_permisos():
    return Permiso.query.all()

"""
funcion para obtener un permiso por id
"""
def get_permiso_by_id(id):
    return Permiso.query.get(id)    


"""
funcion para obtener un permiso por nombre
"""
def get_permiso_by_name(name):
    return Permiso.query.filter_by(nombre=name).first()

"""
funcion para crear un permiso
"""
def create_permiso(nombre):
    permiso = Permiso(nombre=nombre)
    db.session.add(permiso)
    db.session.commit()
    return permiso

"""
funcion para editar un permiso
"""
def edit_permiso(id, data):
    permiso = get_permiso_by_id(id)
    permiso.nombre = data
    db.session.commit()
    return permiso

"""
funcion para eliminar un permiso, elimina los rolPermisos asociados al permiso
"""
def delete_permiso(id):
    permiso = get_permiso_by_id(id)
    rol_permisos = RolPermiso.query.filter_by(permiso_id=id).all()
    list(map(db.session.delete, rol_permisos))
    db.session.delete(permiso)
    db.session.commit()
    return permiso

