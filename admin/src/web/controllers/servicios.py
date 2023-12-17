from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import abort
import urllib.request
from src.core.models.servicios import *
from core.forms.serviceForm import ServiceForm
from src.core.models.configuracion import get_element_quantity
from src.web.helpers.auth import login_required
from src.web.helpers.auth import permission_require
from src.web.helpers.auth import in_manteinance

servicio_bp = Blueprint("servicios", __name__, url_prefix="/servicios")


@servicio_bp.before_request
def before_request():
    return in_manteinance()


@servicio_bp.get("/")
@login_required
@permission_require(["servicio_index"])
def index():
    page = request.args.get('page', 1, type=int)
    institucion_id = session['institucion']
    servicios = Servicio.query.filter_by(institucion_id=institucion_id)
    servicios = servicios.paginate(
        page=page, per_page=get_element_quantity())
    return render_template("servicios/index.html", servicios=servicios)


@servicio_bp.route('/create_service', methods=['GET', 'POST'])
@login_required
@permission_require(["servicio_create"])
def create_service():
    form = ServiceForm(request.form)
    if request.method == 'POST' and form.validate():
        create_servicio(nombre=form.nombre.data, descripcion=form.descripcion.data, palabras_claves_busqueda=form.palabras_claves_busqueda.data,
                        listado_centros_habilitados=form.listado_centros_habilitados.data, tipo_servicio=form.tipo_servicio.data, institucion_id=session['institucion'])
        return redirect(url_for('servicios.index'))
    return render_template('servicios/create.html', form=form)


@servicio_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
@permission_require(["servicio_update"])
def editar_servicio(id):
    servicio = get_servicio_by_id(id)
    form = ServiceForm(request.form, servicio)
    form.habilitado.checked = servicio.habilitado
    if request.method == 'POST' and form.validate():
        edit_servicio(id=id, data=form.data)
        return redirect(url_for('servicios.index'))
    return render_template('servicios/edit.html', id=id, form=form)


@servicio_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
@login_required
@permission_require(["servicio_destroy"])
def eliminar_servicio(id):
    servicio = get_servicio_by_id(id)
    delete_servicio(servicio)
    return redirect(url_for('servicios.index'))
