from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session
from datetime import timedelta
from datetime import datetime
from src.core.models.configuracion import get_element_quantity
from src.core.models.solicitudes import *
from src.core.models.solicitudes import Solicitud
from src.core.models.servicios import Servicio
from src.core.models.users import User
from src.core.forms.cargarnotaForm import cargarnotaForm
from src.core.forms.editarsolicitudForm import editarsolicitudForm
from src.core.forms.solicitudForm import SolicitudForm
from src.core.forms.searchSolicitudForm import searchSolicitudForm
from src.core.models.users import list_users
from src.core.models.servicios import list_servicios
from src.web.helpers.auth import login_required
from src.web.helpers.auth import permission_require
from src.web.helpers.auth import in_manteinance


# import requests

solicitudes_bp = Blueprint('solicitudes', __name__, url_prefix='/solicitudes')

# GET https://admin-grupoXX.proyecto2023.unlp.edu.ar/api/me/requests?page=2&per_page=10


@solicitudes_bp.before_request
def check_manteinance():
    return in_manteinance()


@solicitudes_bp.route('/', methods=['POST', 'GET'])
@login_required
@permission_require(["solicitud_servicio_index"])
def index():
    # base_url = request.host_url
    # print('Url base:' + base_url)
    # url = '/api/me/requests?page=' + str(page) + '&per_page' + str(per_page)
    # print("Url completa:" + url)
    # solicitudes = requests.get(url).content
    form = searchSolicitudForm(request.form)
    page = request.args.get('page', 1, type=int)
    institucion_id = session['institucion']
    solicitudes = Solicitud.query.filter(
        Solicitud.servicio.has(Servicio.institucion_id == institucion_id))
    solicitudes_paginadas = solicitudes.paginate(
        page=page, per_page=get_element_quantity())
    if request.method == 'POST' and form.validate():
        tipo_servicio = request.form.get('tipo_servicio')
        if tipo_servicio != "Todos":
            solicitudes = solicitudes.filter(
                Solicitud.servicio.has(Servicio.tipo_servicio == tipo_servicio))
        status = request.form.get('status')
        if status != "Todas":
            solicitudes = solicitudes.filter_by(status=status)
        cliente = request.form.get('cliente')
        if cliente:
            solicitudes = solicitudes.filter(
                Solicitud.user.has(User.first_name.ilike("%"+cliente+"%")) | Solicitud.user.has(User.last_name.ilike("%"+cliente+"%")) | Solicitud.user.has(User.email.ilike("%"+cliente+"%")))
        fecha_inicio = datetime.strptime(
            request.form.get('fecha_inicio'), '%Y-%m-%d')
        fecha_fin = datetime.strptime(request.form.get(
            'fecha_fin'), '%Y-%m-%d') + timedelta(days=1)
        if fecha_inicio and fecha_fin:
            solicitudes = solicitudes.filter(Solicitud.inserted_at >= fecha_inicio).filter(
                Solicitud.inserted_at <= fecha_fin)
        solicitudes_paginadas = solicitudes.paginate(
            page=page, per_page=get_element_quantity())
    return render_template('solicitudes/index.html', form=form, solicitudes=solicitudes_paginadas)


@solicitudes_bp.route('/<int:id>/notes', methods=['POST', 'GET'])
@login_required
@permission_require(["solicitud_servicio_update"])
def cargar_nota(id):
    form = cargarnotaForm(request.form)
    if request.method == 'POST' and form.validate():
        cargar_nota_a_solictud(
            id_solicitud=id, comentario=form.comentario.data, autor_id=session['user'])
        return redirect(url_for('solicitudes.index'))
    return render_template('solicitudes/nota.html', id=id, form=form)


@solicitudes_bp.route('/<int:id>/edit', methods=['POST', 'GET'])
@login_required
@permission_require(["solicitud_servicio_update"])
def editar_solicitud(id):
    solicitud = get_solicitud_by_id(id)
    form = editarsolicitudForm(request.form, solicitud)
    if request.method == 'POST' and form.validate():
        edit_solicitud(id=id, data=form.data)
        return redirect(url_for('solicitudes.index'))
    return render_template('solicitudes/edit.html', id=id, form=form)


@solicitudes_bp.route('/<int:id>/eliminar', methods=['POST', 'GET'])
@login_required
@permission_require(["solicitud_servicio_destroy"])
def eliminar_solicitud(id):
    delete_solicitud(id)
    return redirect(url_for('solicitudes.index'))


@solicitudes_bp.route('/crear', methods=['POST', 'GET'])
# Este controlador no va, se usa solo para probar las solicitudes
@login_required
def crear_solicitud():
    form = SolicitudForm(request.form)
    users = list_users()
    servicios = list_servicios()
    form.user.choices = [
        (user.id, (str(user.first_name) + " " + str(user.last_name))) for user in users]
    form.servicio.choices = [(servicio.id, servicio.nombre)
                             for servicio in servicios]
    if request.method == 'POST' and form.validate():
        create_solicitud(user_id=form.user.data, servicio_id=form.servicio.data,
                         observaciones=form.observaciones.data)
        return redirect(url_for('solicitudes.index'))
    return render_template('solicitudes/crear.html', form=form)


@solicitudes_bp.route('/<int:id>/show', methods=['POST', 'GET'])
@login_required
def mostrar_solicitud(id):
    solicitud = get_solicitud_by_id(id)
    return render_template('solicitudes/detalle.html', solicitud=solicitud)
