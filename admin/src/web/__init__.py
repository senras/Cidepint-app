from flask import Flask
from src.core import database
from src.web.config import config
from flask_session import Session
from src.web.routes import register_routes
from src.web.commands import register_commands
from src.web import mail
from src.web import oauth
from src.web import oauth_vue
from src.web.helpers.auth import is_authenticated
from src.web.helpers.auth import is_super_admin
from src.web.helpers.auth import is_owner
from src.web.helpers.auth import is_operador
from src.web.helpers.auth import rol_pendiente
from src.web.helpers.auth import get_Config
from src.web.helpers.auth import get_instituciones_by_user_id
from src.web.helpers.auth import get_institucion_actual
from src.web.helpers.auth import parse_date
from src.web.helpers.auth import parse_date_with_hour
from src.web.helpers.auth import get_cant_solicitudes
from src.web.helpers.auth import get_instituciones_by_user_id_without_blocked
from src.web.helpers.auth import *
from src.web import mail
from flask_cors import CORS
from flask_jwt_extended import JWTManager


session = Session()


def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)
    
    # Configure JWT
    jwt = JWTManager(app)

    app.config.from_object(config[env])

    # Configure CORS
    CORS(app, methods=["GET","POST","HEAD"], resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    
    # Import config
    app.config.from_object(config[env])

    # Add to jinja
    app.jinja_env.globals.update(is_authenticated=is_authenticated, is_super_admin=is_super_admin_session, is_owner=is_owner,
                                 get_instituciones_by_user_id=get_instituciones_by_user_id, get_institucion_actual=get_institucion_actual, get_config=get_Config, parse_date=parse_date, parse_date_with_hour=parse_date_with_hour, get_cant_solicitudes=get_cant_solicitudes, rol_pendiente=rol_pendiente, is_operador=is_operador, get_instituciones_by_user_id_without_blocked=get_instituciones_by_user_id_without_blocked)

    # Server Side session
    session.init_app(app)

    # Configure mail
    mail.init_app(app)

    # Configure db
    database.init_app(app)

    register_routes(app)
    register_commands(app)

    oauth.init_oauth(app)
    oauth_vue.init_oauth(app)

    return app
