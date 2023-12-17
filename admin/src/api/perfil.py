from flask import request
from flask import Blueprint
from flask import jsonify
from src.core.models.users import *
from flask_jwt_extended import jwt_required
from flask import session


perfil_api = Blueprint("perfil_api", __name__, url_prefix="/api/me/profile")

"""
 ------------------ Endpoint PERFIL - informacion del perfil  --------------------
    Endpoint para obtener la información del perfil del usuario autenticado
    Parametros:
        - id: id del usuario
"""


@perfil_api.route('/', methods=['GET'])
@jwt_required()
def get_profile():
    if session.get('user'):
        id = session.get('user')
        user = get_user_by_id(id)
        perfil = {
            "Usuario": user.user_name,
            "Email": user.email,
            "status": user.status,
            "Nombre/s": user.first_name,
            "Apellidos/": user.last_name,
            "Fecha de creación": user.created_at,
            "Fecha actualización": user.updated_at,
        }
        return jsonify(perfil)
    else:
        return jsonify({'message': 'Parámetros inválidos!'}), 400


@perfil_api.route('/<int:id>', methods=['GET'])
# Para probar en Postman sin JWT
def get_profile_by_id(id):
    if (id):
        user = get_user_by_id(id)
        perfil = {
            "Usuario": user.user_name,
            "Email": user.email,
            "status": user.status,
            "Nombre/s": user.first_name,
            "Apellidos/": user.last_name,
            "Fecha de creación": user.created_at,
            "Fecha actualización": user.updated_at,
        }
        return jsonify(perfil), 200
    else:
        return jsonify({'message': 'Parámetros inválidos!'}), 400
