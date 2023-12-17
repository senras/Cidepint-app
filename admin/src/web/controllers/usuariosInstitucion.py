from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from src.core.models.userRoles import *
from src.core.models.users import *
from src.core.models.roles import *
from src.core.models.userRoles import *
from src.core.models.instituciones import *
from src.core.forms.userRolForm import UserRolForm
from src.core.forms.usuarioInstitucionCreateForm import UsuarioInstitucionCreateForm
from src.core.forms.usuarioInstitucionEditForm import UsuarioInstitucionEditForm
from src.core.models.configuracion import get_element_quantity
from src.web.helpers.auth import login_required, permission_require

usuariosInstitucion_bp = Blueprint(
    'usuariosInstitucion', __name__, url_prefix='/usuariosInstitucion')


@usuariosInstitucion_bp.get('/')
@login_required
@permission_require(["user_institucion_index"])
def listar_usuariosInstitucion():
    institucion = get_institucion(session.get("institucion"))
    page = request.args.get('page', 1, type=int)
    usuariosInstitucion = UserRol.query.filter_by(institucion_id=session.get("institucion")).paginate(
        page=page, per_page=get_element_quantity())
    # usuariosInstitucion = list_usuariosInstitucion()
    return render_template('usuariosInstitucion/index.html', usuariosInstitucion=usuariosInstitucion, institucion=institucion)


@usuariosInstitucion_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@permission_require(["user_institucion_create"])
def crear_rol_institucion():
    # form = UserRolForm(request.form)
    form = UsuarioInstitucionCreateForm(request.form)  # creo el formulario
    # obtengo todos los usuarios excepto el owner y el superadmin
    users = list_users_except_owner_and_superadmin(session.get("user"))
    # obtengo todos los roles excepto el owner y el superadmin
    roles = list_roles_except_owner_and_superadmin_and_pendiente()
    # obtengo la institucion del usuario logueado
    institucion = get_institucion(session.get("institucion"))
    if request.method == 'POST' and form.validate():  # si el metodo es post y el formulario es valido
        """ con esto verifico que no exista un userRol con el mismo user_id, rol_id e institucion_id"""
        if verificar_userRol(user_id=form.user_id.data,
                             institucion_id=institucion.id):  # si existe un userRol con el mismo user_id, rol_id e institucion_id
            # renderizo el formulario con el error
            return render_template('usuariosInstitucion/crear.html', form=form, users=users, institucion=institucion, roles=roles, error="El usuario ya tiene un rol en la institución.")
        """cambie la funcion porque no me andaba con el otro create_userRol, lo tengo que cambiar:"""
        create_userRol2(rol_id=form.rol_id.data, user_id=form.user_id.data,
                        institucion_id=institucion.id)  # creo el rol para un determinado usuario en esa institucion
        # redirecciono a la lista de usuariosInstitucion
        return redirect(url_for('usuariosInstitucion.listar_usuariosInstitucion'))
    # renderizo el formulario
    return render_template('usuariosInstitucion/crear.html', form=form, users=users, roles=roles, institucion=institucion, error="")


@usuariosInstitucion_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_require(["user_institucion_update"])
def editar_rol_institucion(id):
    userRol = get_userRol_by_id(id)  # obtengo el userRol por id
    # form = UserRolForm(request.form, obj=userRol)
    form = UsuarioInstitucionEditForm(request.form)  # creo el formulario
    user = userRol.user  # obtengo el usuario del userRol
    # obtengo todos los roles excepto el owner y el superadmin
    roles = list_roles_except_owner_and_superadmin_and_pendiente()
    # obtengo la institucion del usuario logueado
    institucion = get_institucion(session.get("institucion"))
    if request.method == 'POST' and form.validate():  # si el metodo es post y el formulario es valido
        """ con esto verifico que no exista un userRol con el mismo user_id, rol_id e institucion_id"""
        if verificar_userRol(user_id=user.id, rol_id=form.rol_id.data,
                             institucion_id=institucion.id):  # si existe un userRol con el mismo user_id, rol_id e institucion_id
            # renderizo el formulario con el error
            return render_template('usuariosInstitucion/editar.html', id=id, form=form, user=user, institucion=institucion, roles=roles, error="Ya existe un usuario con ese rol en esa institución, por favor elija otro rol.")
        data = {
            "rol_id": form.rol_id.data,
            "user_id": user.id,
            "institucion_id": institucion.id
        }  # creo el diccionario con los datos
        # edito el rol de un determinado usuario de esa institucion
        edit_userRol(id=id, data=data)
        # redirecciono a la lista de usuariosInstitucion
        return redirect(url_for('usuariosInstitucion.listar_usuariosInstitucion'))
    # renderizo el formulario
    return render_template('usuariosInstitucion/editar.html', id=id, form=form, user=user, roles=roles, institucion=institucion, error="")


@usuariosInstitucion_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_require(["user_institucion_destroy"])
def eliminar_rol_institucion(id):
    delete_userRol(id=id)
    return redirect(url_for('usuariosInstitucion.listar_usuariosInstitucion'))
