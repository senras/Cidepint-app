from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from src.core import auth
from src.web.helpers.auth import is_super_admin
from src.web.oauth import o_auth
from src.core.models import users
from src.core.models.users import User
from src.core.models.userRoles import get_userRol_by_user_id, create_userRol
from src.core.models.roles import get_rol_by_id
from src.web.helpers.auth import login_required


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

# PERMISOS CHEQUEADOS


@auth_blueprint.get("/")
# No necesita permisos
def login():
    """Renderiza la página de inicio de sesión."""
    return render_template("user/login.html")


@auth_blueprint.post("/authenticate")
# No necesita permisos
def authenticate():
    """
    Autentica al usuario y inicia una sesión si las credenciales son correctas.
    Redirige a la página de inicio de sesión si las credenciales son incorrectas.
    """
    params = request.form
    user = auth.check_user(params["email"], params["password"])
    if not user:
        flash("Email o clave incorrectos!", "error")
        return redirect(url_for("auth.login"))
    if user.status == "Bloqueado":
        flash("Usuario bloqueado!", "error")
        return redirect(url_for("auth.login"))
    session["user"] = user.id
    # flash("La sesión se inició correctamente!", "success")
    """
    Si el usuario es el super administrador, se redirige a la página de inicio.
    """
    if is_super_admin(session):
        session["institucion"] = None
        session["rol"] = 1
        return redirect(url_for("home.home"))
    """
    si el usuario no es super administrador, se redirige a la página de seleccionar institucion.
    """
    return redirect(url_for("usersRoles.seleccionarInstitucion"))


@auth_blueprint.get("/logout")
@login_required
def logout():
    """
    Cierra la sesión del usuario actual, si hay una sesión iniciada.
    Redirige a la página de inicio de sesión.
    """
    if session.get("user"):
        del session["user"]
        if "institucion" in session:
            del session["institucion"]
        if "rol" in session:
            del session["rol"]
        session.clear()
        # flash("La sesión se cerró correctamente!", "info")
    else:
        flash("No hay sesión iniciada!", "info")
    return redirect(url_for("auth.login"))


@auth_blueprint.get("/google/login")
def googleLogin():
    redirect_uri = url_for("auth.googleCallback", _external=True)
    return o_auth.google.authorize_redirect(redirect_uri)


@auth_blueprint.get("/google/login/callback")
def googleCallback():
    try:
        token = o_auth.google.authorize_access_token()
        user_info = token['userinfo']

        email = user_info.get('email')
        session['email'] = email

        user = auth.find_user_by_email(email)
        if user:
            session['user'] = user.id
            if get_userRol_by_user_id(user.id):
                # print(get_userRol_by_user_id(user.id).first())
                if user.userRoles[0].rol.nombre == "pendiente":
                    session["rol"] = 5
                    session["institucion"] = None
                    flash("La sesión se inició correctamente!", "success")
                    return redirect(url_for("home.home"))
                flash("La sesión se inició correctamente!", "success")
                return redirect(url_for("usersRoles.seleccionarInstitucion"))
            else:
                # usuario con rol sin asignar
                create_userRol(get_rol_by_id(5), user)
                session["rol"] = 5
                session["institucion"] = None
                return redirect(url_for("home.home"))
        else:
            email = user_info.get('email')
            given_name = user_info.get('given_name')
            family_name = user_info.get('family_name')

            print(email)
            print(given_name)
            print(family_name)

            new_user = users.create_user(first_name=given_name,
                                         last_name=family_name,
                                         email=email,
                                         user_name=None,
                                         password=None,
                                         status=None,
                                         )
            create_userRol(get_rol_by_id(5), new_user)
            session['user'] = new_user.id
            session["rol"] = 5
            session["institucion"] = None
            flash("La sesión se inició correctamente!", "success")
            return redirect(url_for("home.home"))
    except Exception as e:
        return "Error en el proceso de autenticación!"
