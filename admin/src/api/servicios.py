from flask import request
from flask import Blueprint
from flask import jsonify
from src.core.models.configuracion import get_element_quantity
from src.core.models.servicios import *
from src.core.models.instituciones import *
from flask_cors import cross_origin
# from flask_jwt_extended import jwt_required


servicio_api = Blueprint("servicio_api", __name__, url_prefix="/api/services")


""" ------------------ BUSCADOR DE SERVICIOS  --------------------
  Endpoint para listar y filtrar servicios

  Parámetros:
    - q: término de búsqueda
    - type: tipo de servicio
    - page: página
    - per_page: resultados por página
"""


@servicio_api.route('/search', methods=['GET'])
# Checkeado, no requiere JWT
def buscar_servicios():
    # Obtener parámetros de consulta
    q = request.args.get('q', default='', type=str)
    service_type = request.args.get('type', default='', type=str)
    description = request.args.get('description', default='', type=str)
    laboratory = request.args.get('laboratory', default='', type=str)
    keywords = request.args.get('keywords', default='', type=str)
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get(
        'per_page', default=get_element_quantity(), type=int)

    # Obtener servicios que coinciden con los parámetros de búsqueda
    servicios = Servicio.query.join(Institucion).filter(
        Servicio.nombre.ilike(f'%{q}%'),
        Servicio.tipo_servicio.ilike(f'%{service_type}%'),
        Servicio.descripcion.ilike(f'%{description}%'),
        Institucion.nombre.ilike(f'%{laboratory}%'),
        Servicio.palabras_claves_busqueda.ilike(f'%{keywords}%'),
        Servicio.habilitado.is_(True)
    ).paginate(page=page, per_page=per_page)

    # Crear lista de resultados
    resultados = []
    for servicio in servicios.items:
        resultado = {
            'name': servicio.nombre,
            'description': servicio.descripcion,
            'laboratory': servicio.institucion.nombre,
            'keywords': servicio.palabras_claves_busqueda,
            'id': servicio.id,
            'enabled': servicio.habilitado
        }
        resultados.append(resultado)

    # Crear respuesta JSON
    response = {
        'data': resultados,
        'page': servicios.page,
        'per_page': servicios.per_page,
        'total': servicios.total
    }

    return jsonify(response)


""" ------------------ Endpoint SERVICIOS - Obtener servicio  (Obtiene el detalle del servicio.)  --------------------
    Endpoint para obtener un servicio por ID
    
    Parámetros: 
        - id: ID del servicio
"""


@servicio_api.route('/<int:id>', methods=['GET'])
# Checkeado, no requiere JWT
def obtener_servicio(id):
    servicio = get_servicio_by_id(id)
    response = {
        'name': servicio.nombre,
        'description': servicio.descripcion,
        'laboratores': servicio.listado_centros_habilitados,
        'keywords': servicio.palabras_claves_busqueda,
        'enabled': servicio.habilitado,
        'latitud':  servicio.institucion.latitud,
        'longitud': servicio.institucion.longitud,
        'infoInstitucion': servicio.institucion.infoInstitucion,
        'nameInstitucion': servicio.institucion.nombre,
        'days_and_opening_hours': servicio.institucion.diasHorarios,
        'address': servicio.institucion.direccion
    }
    return jsonify(response), 200


""" ------------------ Endpoint TIPOS DE SERVICIOS - Listado de tipos de servicios ------------------
    Obtiene el listado de tipos de servicios
"""


@servicio_api.route('/types', methods=['GET'])
# @jwt_required()
@cross_origin(supports_credentials=True)
def obtener_tipos_de_servicios():
    tipos_de_servicios = ['Análisis', 'Consultoría', 'Desarrollo']
    # Crea la respuesta JSON
    response = {
        "data": tipos_de_servicios
    }

    return jsonify(response), 200
