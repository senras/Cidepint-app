from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from src.core.models.userRoles import *
from src.core.forms.userRolForm import UserRolForm
from src.core.forms.ownerCreateForm import OwnerCreateForm
from src.core.forms.ownerEditForm import OwnerEditForm
from src.core.forms.seleccionarInstitucionForm import SeleccionarInstitucionForm
from src.core.models.users import *
from src.core.models.roles import *
from src.core.models.instituciones import *
from src.core.auth import *
from src.core import auth
from flask import session
from src.core.models.configuracion import get_element_quantity
from src.web.helpers.auth import login_required
from src.web.helpers.auth import permission_require


usersRoles_bp = Blueprint('usersRoles', __name__, url_prefix='/usersRoles')

"""
funcion para listar los usersRoles
"""


@usersRoles_bp.get('/')
@login_required
@permission_require(['owner_index'])
def listar_usersRoles():
    # usersRoles = list_usersRoles()
    rol_owner = get_rol_by_name("owner")  # obtengo el rol owner
    page = request.args.get('page', 1, type=int)  # obtengo el numero de pagina
    usersRoles = UserRol.query.filter_by(rol_id=rol_owner.id).paginate(
        page=page, per_page=get_element_quantity())  # obtengo los userRoles que tengan el rol owner

    # renderizo la pagina de listar userRoles
    return render_template('usersRoles/index.html', usersRoles=usersRoles)


"""
funcion para que el usuario seleccione una institucion
dentro de las que tiene asignadas, y tambien para obtener el 
rol que tiene en esa institucion:
"""


@usersRoles_bp.route('/seleccionarInstitucion', methods=['GET', 'POST'])
@login_required
def seleccionarInstitucion():
    id = session["user"]
    instituciones = get_instituciones_by_user_id(id)
    seleccionarInstitucionForm = SeleccionarInstitucionForm(request.form)
    if request.method == 'POST' and seleccionarInstitucionForm.validate():
        session["institucion"] = seleccionarInstitucionForm.institucion_id.data
        session["rol"] = get_id_rol_by_user_institucion(
            id, session["institucion"])
        return redirect(url_for('home.home'))
    return render_template('usersRoles/seleccionarInstitucion.html', instituciones=instituciones)


"""
funcion para crear un userRol
"""


@usersRoles_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@permission_require(['owner_create'])
def crear_userRol():
    """
    cambie el formulario para que reciba solamente los id de institucion,
    y los id de usuarios, ya que el rol es owner
    """
    form = OwnerCreateForm(request.form)  # creo el formulario
    # obtengo todos los usuarios excepto el superadmin
    users = list_users_except_superadmin()
    instituciones = list_instituciones()  # obtengo todas las instituciones
    rol = get_rol_by_name("owner")  # obtengo el rol owner
    if request.method == 'POST' and form.validate():  # si se envio el formulario y es valido
        if verificar_userRol(user_id=form.user_id.data, rol_id=rol.id,
                             institucion_id=form.institucion_id.data):  # verifico si ya existe un userRol con ese usuario, ese rol y esa institucion
            # si ya existe, muestro un error
            return render_template('usersRoles/crear.html', form=form, users=users, instituciones=instituciones, error="Ya existe un usuario con ese rol en esa institucion")
        """cambie la funcion porque no me andaba con el otro create_userRol, lo tengo que cambiar:"""
        create_userRol2(rol_id=rol.id, user_id=form.user_id.data,
                        institucion_id=form.institucion_id.data)  # creo el usuario con rol de owner para una institucion
        # redirecciono a la lista de de dueños,que solo puede ver el superadmin
        return redirect(url_for('usersRoles.listar_usersRoles'))
    # si no se envio el formulario o no es valido, muestro el formulario para crear el rol de owner para un usuario en una institucion
    return render_template('usersRoles/crear.html', form=form, users=users, instituciones=instituciones, error="")


"""
funcion para editar un userRol
"""


@usersRoles_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
@permission_require(['owner_update'])
def editar_userRol(id):
    userRol = get_userRol_by_id(id)  # obtengo el userRol
    """
    cambie el formulario para que reciba solamente los id de institucion,
    ya que el id de usuario y el id de rol no se pueden modificar
    """
    form = OwnerEditForm(request.form)  # creo el formulario
    instituciones = list_instituciones()  # obtengo todas las instituciones
    rol = get_rol_by_name("owner")  # obtengo el rol owner
    if request.method == 'POST' and form.validate():  # si se envio el formulario y es valido
        if verificar_userRol(user_id=userRol.user_id, rol_id=rol.id,
                             institucion_id=form.institucion_id.data):  # verifico si ya existe un userRol con ese usuario, ese rol y esa institucion
            # si ya existe, muestro un error
            return render_template('usersRoles/editar.html', id=id, form=form, userRol=userRol, instituciones=instituciones, error="Ya existe un usuario con ese rol en esa institucion")
        data = {
            'user_id': userRol.user_id,
            'rol_id': rol.id,
            'institucion_id': form.institucion_id.data
        }  # creo un diccionario con los datos que voy a editar
        # edito el userRol, solo se puede editar la institucion
        edit_userRol(id=id, data=data)
        # redirecciono a la lista de de dueños,que solo puede ver el superadmin
        return redirect(url_for('usersRoles.listar_usersRoles'))
    # si no se envio el formulario o no es valido, muestro el formulario para editar el userRol
    return render_template('usersRoles/editar.html', id=id, form=form, userRol=userRol, instituciones=instituciones, error="")


"""
funcion para eliminar un userRol
"""


@usersRoles_bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
@login_required
@permission_require(['owner_destroy'])
def eliminar_userRol(id):
    delete_userRol(id=id)
    return redirect(url_for('usersRoles.listar_usersRoles'))
