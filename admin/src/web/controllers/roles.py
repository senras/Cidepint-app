from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from src.core.models.roles import *
from src.core.forms.rolForm import RolForm

roles_bp = Blueprint('roles', __name__, url_prefix='/roles')

# NO SE USA

"""
funcion para listar los roles
"""


@roles_bp.get('/')
def listar_roles():
    roles = list_roles()
    return render_template('roles/index.html', roles=roles)


"""
funcion para crear un rol
"""


@roles_bp.route('/crear', methods=['GET', 'POST'])
def crear_rol():
    form = RolForm(request.form)
    if request.method == 'POST' and form.validate():
        create_rol(nombre=form.nombre.data)
        return redirect(url_for('roles.listar_roles'))
    return render_template('roles/crear.html', form=form)


"""
funcion para editar un rol
"""


@roles_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_rol(id):
    rol = get_rol_by_id(id)
    form = RolForm(request.form, rol)
    if request.method == 'POST' and form.validate():
        edit_rol(id=id, data=form.nombre.data)
        return redirect(url_for('roles.listar_roles'))
    return render_template('roles/editar.html', id=id, form=form)


"""
funcion para eliminar un rol
"""


@roles_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
def eliminar_rol(id):
    delete_rol(id=id)
    return redirect(url_for('roles.listar_roles'))
