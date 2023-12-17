from flask import request
from flask import Blueprint
from flask import jsonify
from src.web.controllers import auth
from src.core.auth import *
from src.core.models.users import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_refresh_token
from flask_cors import cross_origin
from src.web.oauth_vue import o_auth
from flask import url_for
from src.core import auth
from src.core.models import users


autenticacion_api = Blueprint(
    "autenticacion_api", __name__, url_prefix="/api/auth")


"""
------------------  Autenticación - LOGIN --------------------
    Permite obtener el un JSON Web Token válido para el usuario y password.
    
    Parámetros:
        - email: email del usuario
        - password: clave del usuario
"""



@autenticacion_api.route('/login', methods=['POST'])
def login_jwt():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = check_user(email, password)
    if user:
        access_token = create_access_token(identity=user.id)
        response = jsonify(message="autenticado")
        return {'access_token': access_token}, 200
    else:
        return jsonify(message="Unauthorized"), 401


"""
------------------  Autenticación - LOGOUT --------------------
    invalida el JSON Web Token del usuario (almacenado en el header).
        
    Parámetros:
        - Ninguno
"""


@autenticacion_api.route('/logout_jwt', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def logout_jwt():
    response = jsonify()
    response.headers['Authorization'] = ''
    return response, 200


""" 
------------------  Autenticación - USER --------------------
    Devuelve el usuario logueado.
        
    Parámetros:
        - Ninguno
"""


@autenticacion_api.get('/user_jwt')
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = get_user_by_id(current_user)
    response = jsonify(user)
    return response, 200


""" PRUEBA DE RUTA PROTEGIDA """""


@autenticacion_api.get('/ruta_protegida')
@jwt_required()
def ruta_protegida():
    current_user = get_jwt_identity()
    return {'message': f'Acceso permitido para {current_user}'}, 200


""" API DE GOOGLE VUE """


@autenticacion_api.get("/google/vue/login")
def googleVueLogin():
    redirect_uri = url_for(
        "autenticacion_api.googleVueCallback", _external=True)
    return o_auth.google.authorize_redirect(redirect_uri)


@autenticacion_api.post("/google/vue/login/callback")
def googleVueCallback():
    try:
        print('hola gato')
        token = o_auth.google.authorize_access_token()
        print(token)
        user_info = token['userinfo']
        email = user_info.get('email')
        user = auth.find_user_by_email(email)
        if user:
            response = {
                "id": user.id,
                "name": user.first_name,
                "message": "El usuario ya esta registrado!",
            }

            return response, 200  # envia response el usuario existe
        else:
            email = user_info.get('email')
            given_name = user_info.get('given_name')
            family_name = user_info.get('family_name')

            users.create_user(first_name=given_name,
                              last_name=family_name,
                              email=email,
                              user_name=None,
                              password=None,
                              status=None,
                              )
            response = {
                "id": user.id,
                "name": user.first_name,
                "message": "El usuario ya esta registrado!",
            }

            return response, 200  # envia response el usuario existe

    except Exception as e:
        response = {
            "message": "Error en logueo con google!",
        }
        print('error')
        print('hola gato'+str(e))
        print(e)
        return response, 400
