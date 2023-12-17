from flask_cors import cross_origin
from flask import jsonify
from flask import Blueprint
from src.core.models.solicitudes import *
from src.core.models.servicios import *
from src.core.models.instituciones import *
charts_api_bp = Blueprint("charts_api", __name__, url_prefix="/api/charts")


# 1. Gráfico de tortas/barras con la cantidad de las solicitudes realizadas agrupadas por estado.
@charts_api_bp.get('/solicitudes_por_estado')
@cross_origin(supports_credentials=True)
def solicitudes_por_estado():
    solicitudes = get_solicitudes()
    solicitudes_por_estado = {
        'Aceptada': len([s for s in solicitudes if s.status == 'Aceptada']),
        'Rechazada': len([s for s in solicitudes if s.status == 'Rechazada']),
        'En_proceso': len([s for s in solicitudes if s.status == 'En proceso']),
        'Finalizada': len([s for s in solicitudes if s.status == 'Finalizada']),
        'Cancelada': len([s for s in solicitudes if s.status == 'Cancelada'])
    }
    response = {
        'data': solicitudes_por_estado
    }
    return jsonify(response), 200

# 2. Ranking de los servicios más solicitados


@charts_api_bp.get('/servicios_mas_solicitados')
@cross_origin(supports_credentials=True)
def servicios_mas_solicitados():
    servicios = list_servicios()
    # Get the 10 most requested services, sorted by the number of requests
    servicios_mas_solicitados = sorted(
        servicios, key=lambda s: len(s.solicitudes), reverse=True)[:10]
    serialized_servicios = {
        'data': [
            {
                'nombre': s.nombre,
                'cantidad_solicitudes': len(s.solicitudes)
            } for s in servicios_mas_solicitados
        ]
    }
    return jsonify(serialized_servicios), 200

# 3. Top 10 de las Instituciones con mejor tiempo de resolución[1]


@charts_api_bp.get('/instituciones_mejor_tiempo_resolucion')
@cross_origin(supports_credentials=True)
def instituciones_mejor_tiempo_resolucion():
    instituciones = list_instituciones()
    # Get the 10 institutions with the best resolution time using get_resolucion_promedio
    instituciones_mejor_tiempo_resolucion = sorted(
        [i for i in instituciones if get_resolucion_promedio(i.id) > 0], key=lambda i: get_resolucion_promedio(i.id))[:10]
    response = {
        'data': [
            {
                'id': i.id,
                'nombre': i.nombre,
                'promedio': round(get_resolucion_promedio(i.id), 2)
            } for i in instituciones_mejor_tiempo_resolucion
        ]
    }
    return jsonify(response), 200
