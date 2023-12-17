from flask import render_template
from flask import Blueprint
from flask import session
from src.web.helpers.auth import is_authenticated
from src.web.helpers.auth import in_manteinance
from src.core.models.configuracion import get_manteinance_message
from src.core.models.configuracion import get_manteinance_status


home_bp = Blueprint("home", __name__, url_prefix="/")

# PERMISOS CHEQUEADOS


@home_bp.before_request
def before_request():
    if not is_authenticated(session) and get_manteinance_status():
        return render_template('configuracion/manteinance.html', message=get_manteinance_message())
    return in_manteinance()


@home_bp.get("/")
# No necesita permisos
def home():
    """Renderiza la página principal de la aplicación."""
    return render_template("home.html")