from src.core.models.users.user import User
from src.core.models.userRoles import create_userRol
from src.core.database import db
from src.core.bcrypt import bcrypt
from src.core.models.userRoles.userRol import UserRol

"""
funcion para listar los users
"""


def list_users():
    """
    Devuelve un queryset con todos los usuarios.
    """
    users = User.query.all()

    return users


def list_users_except_owner_and_superadmin(owner_id):
    """
    Devuelve un queryset con todos los usuarios excepto el dueño y el superadmin.
    """
    id_superadmin = UserRol.query.filter_by(institucion_id = None).first().user_id#obtengo el id de usuario del superadmin
    users = User.query.filter((User.id != owner_id) & (User.id != id_superadmin)).all()#filtro los usuarios que no sean el dueño ni el superadmin

    return users

def list_users_except_superadmin():
    """
    Devuelve un queryset con todos los usuarios excepto el superadmin.
    """
    id_superadmin = UserRol.query.filter_by(institucion_id = None).first().user_id#obtengo el id de usuario del superadmin
    users = User.query.filter(User.id != id_superadmin).all()#filtro los usuarios que no sean el superadmin

    return users


def get_user_by_id(user_id):
    """
    Devuelve el usuario con el id que recibe como parámetro.
    """
    user = User.query.get(user_id)

    return user


def edit_user(id, data):
    """
    Edita el usuario con el id que recibe como parámetro.
    """
    user = get_user_by_id(id)
    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    db.session.commit()
    return user


def ban_user(id):
    """
    Bloquea el usuario con el id que recibe como parámetro.
    """
    user = get_user_by_id(id)
    user.status = "Bloqueado"
    db.session.commit()
    return user


def unban_user(id):
    """
    Desbloquea el usuario con el id que recibe como parámetro.
    """
    user = get_user_by_id(id)
    user.status = "Habilitado"
    db.session.commit()
    return user


def create_user(**kwargs):
    """
    Crea un usuario con los datos que recibe como.
    """
    password = kwargs["password"]
    if password is not None:
        hash = bcrypt.generate_password_hash(
            kwargs["password"].encode("utf-8"))
        kwargs.update(password=hash.decode("utf-8"))
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user


def delete_user(id):
    """
    Elimina el usuario con el id que recibe como parámetro.
    """
    user = get_user_by_id(id)
    user_roles = UserRol.query.filter_by(user_id=id).all()
    list(map(db.session.delete, user_roles))
    db.session.delete(user)
    db.session.commit()

    return True


def update_user_password(user_id, password):
    """
    Actualiza el password del usuario.
    """
    user = User.query.get(user_id)
    if user is None:
        return None  # Agregar manejador de error en caso e no encontrar el User

    hash = bcrypt.generate_password_hash(password.encode("utf-8"))
    user.password = hash.decode("utf-8")
    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_id(id):
    """
    Devuelve un usuario por su ID.
    """
    user = User.query.get(id)

    return user


def update_user_name(user_id, user_name):
    """
    Actualiza el nombre del usuario.
    """
    user = User.query.get(user_id)
    if user is None:
        return None  # Agregar manejador de error en caso e no encontrar el User
    user.user_name = user_name
    db.session.add(user)
    db.session.commit()
    return user


def add_role(user, role):
    """
    Agrega un rol a un usuario.
    """
    if user is None:
        return None  # Agregar manejador de error en caso e no encontrar el User
    userRol = create_userRol(user_id=user.id, rol_id=role.id)
    user.userRoles.append(userRol)
    db.session.add(user)
    db.session.commit()

    return user
