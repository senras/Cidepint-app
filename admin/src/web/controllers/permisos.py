from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from src.core.models.permisos import *
from src.core.forms.permisoForm import PermisoForm

permisos_bp = Blueprint('permisos', __name__, url_prefix='/permisos')

# NO SE USA

# @permisos_bp.route('/permisos')
"""
funcion para listar los permisos
"""


@permisos_bp.get('/')
def listar_permisos():
    permisos = list_permisos()
    return render_template('permisos/index.html', permisos=permisos)


"""
funcion para crear un permiso
"""


@permisos_bp.route('/crear', methods=['GET', 'POST'])
def crear_permiso():
    form = PermisoForm(request.form)
    if request.method == 'POST' and form.validate():
        create_permiso(nombre=form.nombre.data)
        return redirect(url_for('permisos.listar_permisos'))
    return render_template('permisos/crear.html', form=form)


"""
funcion para editar un permiso
"""


@permisos_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_permiso(id):
    permiso = get_permiso_by_id(id)
    form = PermisoForm(request.form, permiso)
    if request.method == 'POST' and form.validate():
        edit_permiso(id=id, data=form.nombre.data)
        return redirect(url_for('permisos.listar_permisos'))
    return render_template('permisos/editar.html', id=id, form=form)


"""
funcion para eliminar un permiso
"""


@permisos_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
def eliminar_permiso(id):
    delete_permiso(id=id)
    return redirect(url_for('permisos.listar_permisos'))
