from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from src.core.models import users
from src.core.models.users.user import User
from src.core.database import db
from flask import flash


user_update_bp = Blueprint("user_update", __name__, url_prefix="/user_update")

# PERMISOS CHEQUEADOS


@user_update_bp.route('/<int:user_id>', methods=['GET', 'POST'])
# No necesita permisos
def user_update(user_id):
    """
    Función que permite actualizar la contraseña de un usuario en el sistema.
    Si la petición es POST, actualiza la contraseña del usuario en la base de datos
    y redirige a la página de inicio de sesión.
    Si la petición es GET, renderiza la página de actualización de contraseña.
    """
    if request.method == 'POST':
        existing_user = User.query.filter_by(
            user_name=request.form['user_name']).first()
        if existing_user:
            flash('¡El nombre de usuario ingresado ya está registrado!.', "error")
            return redirect(url_for("user_update.user_update", user_id=user_id))
        users.update_user_password(user_id, request.form['password'])
        users.update_user_name(user_id, request.form['user_name'])
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('user/user_update.html')
