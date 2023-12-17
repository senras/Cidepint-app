import urllib.request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import Blueprint
from flask import request
from flask import session
from src.core.models.roles import UserRol
from src.core.models.users.user import User
from src.core.models.users import *
from src.core.forms.searchUserForm import searchUserForm
from src.core.forms.edituserForm import EditUserForm
from src.core.forms.userCreateByAdminForm import UserCreateByAdminForm
from src.core.models.configuracion import get_element_quantity
from src.web.helpers.auth import login_required
from src.web.helpers.auth import permission_require
from src.web.helpers.auth import is_super_admin_by_id


users_bp = Blueprint(
    "users", __name__, url_prefix="/users")


"""
Index con filtrado de usuarios
"""


@users_bp.route('/', methods=['GET', 'POST'])
@login_required
@permission_require(["user_index"])
def index():
    form = searchUserForm(request.form)
    page = request.args.get('page', 1, type=int)
    # Lista de usuarios excluyendo al superadmin
    users = User.query.filter(User.userRoles.any(
        UserRol.rol.has(nombre="super_administrador")) == False)
    users_paginated = users.paginate(
        page=page, per_page=get_element_quantity())
    if request.method == 'POST' and form.validate():
        email = request.form.get('email')
        status = request.form.get('status')
        users = User.query.filter(User.userRoles.any(
            UserRol.rol.has(nombre="super_administrador")) == False)
        if status != "Todos":
            users = users.filter_by(status=status)
        if email:
            # get users where email like %email% or user_name like %email% or first_name like %email% or last_name like %email%
            users = users.filter(User.email.ilike(
                "%"+email+"%") | User.user_name.ilike("%"+email+"%") | User.first_name.ilike("%"+email+"%") | User.last_name.ilike("%"+email+"%"))
        users = users.paginate(
            page=page, per_page=get_element_quantity())
        return render_template('users/index.html', users=users, form=form)
    return render_template('users/index.html', users=users_paginated, form=form)


# COMPLETAR
@users_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@permission_require(["user_create"])
def crear_usuario():
    form = UserCreateByAdminForm(request.form)
    if request.method == 'POST' and form.validate():
        # Chequear si el email ya existe, si existe mostrar error
        if User.query.filter_by(email=form.email.data).first():
            flash("Email ya está en uso", "error")
            return render_template('users/createAdmin.html', form=form, error="El email ya existe")
        create_user(user_name=form.user_name.data, email=form.email.data, password=form.password.data,
                    first_name=form.first_name.data, last_name=form.last_name.data, status=form.status.data)
        return redirect(url_for('users.index'))
    # CREAR TEMPLATE
    return render_template('users/createAdmin.html', form=form)


@users_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
@login_required
@permission_require(["user_destroy"])
def borrar_usuario(id):
    delete_user(id=id)
    return redirect(url_for('users.index'))


@users_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
@permission_require(["user_update"])
def editar_usuario(id):
    user = get_user_by_id(id)
    form = EditUserForm(request.form, user)
    if request.method == 'POST' and form.validate():
        # Chequear si el email ya existe, si existe y no es el mismo usuario, mostrar error
        if User.query.filter_by(email=form.email.data).first():
            if User.query.filter_by(email=form.email.data).first().id != id:
                flash("Email ya está en uso", "error")
                return render_template('users/edit.html', id=id, form=form, error="El email ya existe")
        edit_user(id=id, data=form.data)
        return redirect(url_for('users.index'))

    return render_template('users/edit.html', id=id, form=form)


@users_bp.route('/<int:id>/ban', methods=['GET', 'POST'])
@login_required
@permission_require(["user_update"])
def bloquear_usuario(id):
    if is_super_admin_by_id(id):
        flash("No puede bloquear a un super administrador", "error")
        return redirect(url_for('users.index'))
    ban_user(id=id)
    return redirect(url_for('users.index'))


@users_bp.route('/<int:id>/unban', methods=['GET', 'POST'])
@login_required
@permission_require(["user_update"])
def desbloquear_usuario(id):
    unban_user(id=id)
    return redirect(url_for('users.index'))


# COMPLETAR
# Agregar en el template un botón que redirija a esta ruta
@users_bp.route('/<int:id>/perfil', methods=['GET', 'POST'])
@login_required
@permission_require(["user_show"])
def ver_usuario(id):
    user = get_user_by_id(id)
    date = user.created_at.strftime("%d/%m/%Y")
    return render_template('users/profile.html', user=user, date=date)

# Ejemplo de búsqueda de servicios
# GET https://admin-grupoXX.proyecto2023.unlp.edu.ar/api/services/search?q=&type=&page=2&per_page=10


"""
funcion para ver mi perfil
"""


@users_bp.get('/mi_perfil')
@login_required
def ver_perfil():
    id = session.get('user')
    user = get_user_by_id(id)
    date = user.created_at.strftime("%d/%m/%Y")
    return render_template('users/profile.html', user=user, date=date)
