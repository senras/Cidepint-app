from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from src.core.models.rolesPermisos import *
from src.core.forms.rolPermisoForm import RolPermisoForm
from src.core.models.permisos import *
from src.core.models.roles import *


rolesPermisos_bp = Blueprint(
    'rolesPermisos', __name__, url_prefix='/rolesPermisos')

"""
funcion para listar los rolesPermisos
"""


@rolesPermisos_bp.get('/')
def listar_rolesPermisos():
    rolesPermisos = list_rolesPermisos()
    return render_template('rolesPermisos/index.html', rolesPermisos=rolesPermisos)


"""
funcion para crear un rolPermiso
"""


@rolesPermisos_bp.route('/crear', methods=['GET', 'POST'])
def crear_rolPermiso():
    form = RolPermisoForm(request.form)
    permisos = list_permisos()
    roles = list_roles()
    if request.method == 'POST' and form.validate():
        create_rolPermiso(rol_id=form.rol_id.data,
                          permiso_id=form.permiso_id.data)
        return redirect(url_for('rolesPermisos.listar_rolesPermisos'))
    return render_template('rolesPermisos/crear.html', form=form, permisos=permisos, roles=roles)


"""
funcion para editar un rolPermiso
"""


@rolesPermisos_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_rolPermiso(id):
    rolPermiso = get_rolPermiso_by_id(id)
    form = RolPermisoForm(request.form, rolPermiso)
    permisos = list_permisos()
    roles = list_roles()
    if request.method == 'POST' and form.validate():
        edit_rolPermiso(id=id, data=form.data)
        return redirect(url_for('rolesPermisos.listar_rolesPermisos'))
    return render_template('rolesPermisos/editar.html', id=id, form=form, permisos=permisos, roles=roles)


"""
funcion para eliminar un rolPermiso
"""


@rolesPermisos_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
def eliminar_rolPermiso(id):
    delete_rolPermiso(id=id)
    return redirect(url_for('rolesPermisos.listar_rolesPermisos'))
