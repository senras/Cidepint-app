from src.web.controllers.home import home_bp
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.registration import registration_bp
from src.web.controllers.user_update import user_update_bp
from src.web.controllers.instituciones import instituciones_bp
# from src.web.controllers.roles import roles_bp
# from src.web.controllers.permisos import permisos_bp
from src.web.controllers.users import users_bp
from src.web.controllers.usersRoles import usersRoles_bp
from src.web.controllers.rolesPermisos import rolesPermisos_bp
from src.web.controllers.configuracion import config_bp
from src.web.controllers.servicios import servicio_bp
from src.web.controllers.solicitudes import solicitudes_bp
from src.web.controllers.usuariosInstitucion import usuariosInstitucion_bp
from src.api.servicios import servicio_api
from src.api.instituciones import instituciones_api
from src.api.perfil import perfil_api
from src.api.autenticacion import autenticacion_api
from src.api.solicitudes import solicitudes_api_bp
from src.api.charts import charts_api_bp
from src.web import error


def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(registration_bp)
    app.register_blueprint(user_update_bp)
    app.register_blueprint(instituciones_bp)
    # app.register_blueprint(roles_bp)
    # app.register_blueprint(permisos_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(usersRoles_bp)
    # app.register_blueprint(rolesPermisos_bp)
    app.register_blueprint(usuariosInstitucion_bp)
    app.register_blueprint(solicitudes_api_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(solicitudes_bp)
    app.register_blueprint(servicio_bp)
    app.register_blueprint(servicio_api)
    app.register_blueprint(instituciones_api)
    app.register_blueprint(perfil_api)
    app.register_blueprint(autenticacion_api)
    app.register_blueprint(charts_api_bp)
    app.register_error_handler(404, error.not_found_error)
    app.register_error_handler(400, error.bad_request_error)
    app.register_error_handler(401, error.not_permission_error)
