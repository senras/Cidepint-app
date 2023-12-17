from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from src.core.models import users
from src.core.models.users import User
from src.core.database import db
from src.web import mail
from flask import flash

registration_bp = Blueprint(
    "registration", __name__, url_prefix="/registration")

# PERMISOS CHEQUEADOS


@registration_bp.route("/", methods=["GET", "POST"])
# No necesita permisos
def registration():
    """
    Función que gestiona la creación de un nuevo usuario en el sistema.
    Si la petición es POST, crea el usuario, lo añade a la base de datos,
    envía un correo electrónico de confirmación y redirige a la página de inicio de sesión.
    Si la petición es GET, renderiza la página de registro.
    """
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        user_name = None
        password = None
        status = "Habilitado"

        # Comprobar si el correo electrónico ya está registrado

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('¡El correo electrónico ingresado ya está registrado!.', "error")
            return redirect(url_for("registration.registration"))

        new_user = users.create_user(first_name=first_name,
                                     last_name=last_name,
                                     email=email,
                                     user_name=user_name,
                                     password=password,
                                     status=status,
                                     )

        # link = "http://127.0.0.1:5000/user_update/"+str(new_user.id)

        link = "https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/user_update/" + \
            str(new_user.id)

        mail.send_mail(subject="Confirmación de Registro",
                       recipients=email, body=link)

        return redirect(url_for('auth.login'))

    return render_template("user/registration.html")
