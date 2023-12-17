from flask import Blueprint
from flask import request
from src.core.models.solicitudes import *
from src.core.models.notas import *
from src.core.models.users import *
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask_cors import cross_origin


solicitudes_api_bp = Blueprint(
    'solicitudes_api', __name__, url_prefix='/api/me/requests')


'''Obtener todas las solicitudes realizadas por el usuario autenticado'''


@solicitudes_api_bp.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
# @jwt_required()
def get_my_solicitudes():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    sort = request.args.get('sort')
    order = request.args.get('order')
    estado = request.args.get('estado')
    fecha = request.args.get('fecha')
    user_id = request.args.get('user_id')
    solicitudes = Solicitud.query
    solicitudes = solicitudes.filter(Solicitud.user_id == user_id)
    if fecha:
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
        solicitudes = solicitudes.filter(
            Solicitud.inserted_at >= fecha,
            Solicitud.inserted_at <= fecha + timedelta(days=1)
        )
    if estado:
        if estado != "Todas":
            solicitudes = solicitudes.filter(Solicitud.status == estado)
    if sort and order:
        if sort == "fecha":
            if order == "ascendente":
                solicitudes = solicitudes.order_by(Solicitud.inserted_at.asc())
            elif order == "descendente":
                solicitudes = solicitudes.order_by(
                    Solicitud.inserted_at.desc())
        elif sort == "estado":
            if order == "ascendente":
                solicitudes = solicitudes.order_by(Solicitud.status.asc())
            elif order == "descendente":
                solicitudes = solicitudes.order_by(Solicitud.status.desc())
    solicitudes = solicitudes.paginate(page=page, per_page=per_page)
    resultados = list(map(lambda solicitud: {
        "id": solicitud.id,
        "title": "Pedido de " + solicitud.servicio.nombre + " por " + solicitud.user.first_name,
        "creation_date": solicitud.inserted_at,
        "close_date": solicitud.status_at if solicitud.status == "Finalizada" else "",
        "status": solicitud.status,
        "notas": list(map(lambda nota: {
            "id": nota.id,
            "comment": nota.comentario,
            "author": nota.autor_id,
            "date": nota.inserted_at,
        }, get_notas(solicitud_id=solicitud.id))) or "",
    }, solicitudes.items))

    response = {
        "data": resultados,
        "page": page,
        "per_page": per_page,
        "total": solicitudes.total,
    }
    return jsonify(response), 200


'''Obtener la solicitud realizada por el usuario autenticado'''


@solicitudes_api_bp.get('/<int:id>')
# @jwt_required()
def get_my_solicitud(id):
    solicitud = get_solicitud_by_id(id)
    notas = get_notas(solicitud_id=solicitud.id)
    solicitante = get_user_by_id(solicitud.user_id)
    resultados = []
    for nota in notas:
        if nota.autor_id == solicitante.id:
            autor = solicitante.first_name + " " + solicitante.last_name
        autor = get_user_by_id(nota.autor_id).first_name + " " + \
            get_user_by_id(nota.autor_id).last_name + "(Staff)"
        resultado = {
            "id": nota.id,
            "comment": nota.comentario,
            "author": autor,
            "date": nota.inserted_at,
        }
        resultados.append(resultado)

    solicitud = {
        "id": solicitud.id,
        "title": "Pedido de " + solicitud.servicio.nombre +
        " por " + solicitud.user.first_name + " " + solicitud.user.last_name,
        "creation_date": solicitud.inserted_at,
        "close_date": solicitud.status_at if solicitud.status == "Finalizada" else "",
        "status": solicitud.status,
        "notas": resultados,
    }
    response = {
        "data": solicitud,
    }
    return jsonify(response), 200


'''Crear una solicitud de servicio'''


@solicitudes_api_bp.route('/', methods=['POST'])
# @jwt_required()
def crear_solicitud():
    data = request.get_json()
    user_id = data['user_id']
    servicio_id = data['servicio_id']
    solicitud = create_solicitud(user_id=user_id, servicio_id=servicio_id)
    notas = get_notas(solicitud_id=solicitud.id)
    resultados = []
    for nota in notas:
        resultado = {
            "id": nota.id,
            "comment": nota.comentario,
            "author": nota.autor_id,
            "date": nota.inserted_at,
        }
        resultados.append(resultado)
    solicitud = {
        "id": solicitud.id,
        "title": "Pedido de " + solicitud.servicio.nombre + " por " + solicitud.user.first_name,
        "creation_date": solicitud.inserted_at,
        "close_date": solicitud.status_at if solicitud.status == "Finalizada" else "",
        "status": solicitud.status,
        "notas": resultados if len(resultados) > 0 else "",
    }
    response = {
        "data": solicitud,
    }
    return jsonify(response), 201


'''Carga una nota en la solicitud de servicio por un usuario autenticado.'''


@solicitudes_api_bp.post('/<int:id>/notes')
# @jwt_required()
def cargar_nota(id):
    data = request.get_json()
    comentario = data['comentario']
    # El autor_id debería tomarlo de JWT, mientras tanto lo mando por json
    autor_id = data['autor_id']
    solicitud = cargar_nota_a_solictud(comentario=comentario, autor_id=autor_id,
                                       id_solicitud=id)

    resultados = list(map(lambda nota: {
        "id": nota.id,
        "comment": nota.comentario,
        "author": nota.autor_id,
        "date": nota.inserted_at,
    }, get_notas(solicitud_id=solicitud.id)))

    solicitud = {
        "id": solicitud.id,
        "title": f"Pedido de {solicitud.servicio.nombre} por {solicitud.user.first_name}",
        "creation_date": solicitud.inserted_at,
        "close_date": solicitud.status_at if solicitud.status == "Finalizada" else "",
        "status": solicitud.status,
        "notas": resultados if len(resultados) > 0 else "",
    }
    response = {
        "data": solicitud,
    }
    return jsonify(response), 201
