from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from src.core.models.instituciones import *
from src.core.forms.institucionForm import InstitucionForm
from src.core.models.configuracion import get_element_quantity
from src.web.helpers.auth import login_required
from src.web.helpers.auth import permission_require
from src.web.helpers.auth import in_manteinance


instituciones_bp = Blueprint(
    'instituciones', __name__, url_prefix='/instituciones')


@instituciones_bp.before_request
def before_request():
    in_manteinance()


@instituciones_bp.get('/')
@login_required
@permission_require(["institucion_index"])
def listar_instituciones():
    page = request.args.get('page', 1, type=int)
    instituciones = Institucion.query.paginate(
        page=page, per_page=get_element_quantity())
    return render_template('instituciones/index.html', instituciones=instituciones)


@instituciones_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@permission_require(["institucion_create"])
def crear_institucion():
    form = InstitucionForm(request.form)
    if request.method == 'POST' and form.validate():
        create_institucion(nombre=form.nombre.data, infoInstitucion=form.infoInstitucion.data, direccion=form.direccion.data, latitud=form.latitud.data,
                           longitud=form.longitud.data, web=form.web.data, palabrasClaves=form.palabrasClaves.data, diasHorarios=form.diasHorarios.data, infoContacto=form.infoContacto.data)
        return redirect(url_for('instituciones.listar_instituciones'))
    return render_template('instituciones/crear.html', form=form)


@instituciones_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
@login_required
@permission_require(["institucion_destroy"])
def eliminar_institucion(id):
    delete_institucion(id=id)
    return redirect(url_for('instituciones.listar_instituciones'))


@instituciones_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
@permission_require(["institucion_update"])
def editar_institucion(id):
    institucion = get_institucion(id)
    form = InstitucionForm(request.form, institucion)
    if request.method == 'POST' and form.validate():
        nombre_institucion = request.form['nombre']
        existe_institucion = Institucion.query.filter_by(
            nombre=nombre_institucion).first()
        if existe_institucion:
            if existe_institucion.id != id:
                flash('Ya existe una institucion con ese nombre', 'danger')
                return render_template('instituciones/editar.html', id=id, form=form)
        # Se hace esto porque el formulario no acepta floats
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        form.latitud.data = float(latitud)
        form.longitud.data = float(longitud)
        edit_institucion(id=id, data=form.data)
        if session.get("institucion"):
            return redirect(url_for('usuariosInstitucion.listar_usuariosInstitucion', id=id))
        return redirect(url_for('instituciones.listar_instituciones'))
    return render_template('instituciones/editar.html', id=id, form=form)


# Completar
@instituciones_bp.route('/<int:id>/ver', methods=['GET', 'POST'])
@login_required
@permission_require(["institucion_show"])
def ver_institucion(id):
    institucion = get_institucion(id)
    return render_template('instituciones/detalle.html', institucion=institucion)
    # Crear template


@instituciones_bp.route('/<int:id>/habilitar', methods=['GET', 'POST'])
@login_required
@permission_require(["institucion_activate"])
def habilitar_institucion(id):
    unban_institucion(id=id)
    return redirect(url_for('instituciones.listar_instituciones'))


@instituciones_bp.route('/<int:id>/deshabilitar', methods=['GET', 'POST'])
@login_required
@permission_require(["institucion_deactivate"])
def deshabilitar_institucion(id):
    ban_institucion(id=id)
    return redirect(url_for('instituciones.listar_instituciones'))
