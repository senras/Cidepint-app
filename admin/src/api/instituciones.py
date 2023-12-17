from flask import request
from flask import Blueprint
from flask import jsonify
from src.core.models.configuracion import get_element_quantity
from src.core.models.instituciones import *


instituciones_api = Blueprint(
    "instituciones_api", __name__, url_prefix="/api/institutions")


""" ------------------ Instituciones - INFORMACIÓN DE LAS INSTITUCIONES  --------------------
    Obtiene todas las Instituciones dadas de alta en el sistema.

    Parametros:
        - page: página
        - per_page: resultados por página
"""


@instituciones_api.route('/', methods=['GET'])
# Checkeado, no requiere JWT
def info_instituciones():
    # Obtener parámetros de consulta
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=1, type=int)

    # Obtener instituciones
    instituciones = Institucion.query.paginate(page=page, per_page=per_page)

    # Crear lista de resultados
    resultados = []
    for institucion in instituciones.items:
        resultado = {
            'name': institucion.nombre,
            'information': institucion.infoInstitucion,
            'address': institucion.direccion,
            'lat': institucion.latitud,
            'lon': institucion.longitud,
            'web': institucion.web,
            'days_and_opening_hours': institucion.diasHorarios,
            'email': institucion.infoContacto,
            'enabled': institucion.habilitado
        }
        resultados.append(resultado)

    # Crear respuesta JSON
    response = {
        'data': resultados,
        'page': instituciones.page,
        'per_page': instituciones.per_page,
        'total': instituciones.total
    }

    return jsonify(response), 200
