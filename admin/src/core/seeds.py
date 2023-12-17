from src.core.models import users
from src.core.models import roles
from src.core.models import instituciones
# from src.core.seeds import permisos
from src.core.models.permisos import create_permiso
from src.core.models.rolesPermisos import add_permisos_to_rol
from src.core.models.userRoles import create_userRol
from src.core.models.servicios import create_servicio
from src.core.models.solicitudes import create_solicitud
from src.core.models.notas import cargar_nota


def run():
    print("Precargando base de datos...")
    user1 = users.create_user(
        email="mailuser1@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Homero",
        last_name="Gutierrez",
    )
    user2 = users.create_user(
        email="mailuser2@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Carlos",
        last_name="Perez",
    )
    user3 = users.create_user(
        email="mailuser3@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Juan",
        last_name="Perez",
    )
    user4 = users.create_user(
        email="mailuser4@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Pedro",
        last_name="Perez",
    )
    user5 = users.create_user(
        email="mailuser5@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Maria",
        last_name="Perez",
    )
    user6 = users.create_user(
        email="mailuser6@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Jose",
        last_name="Perez",
    )
    user7 = users.create_user(
        email="mailuser7@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Martín",
        last_name="Perez",
    )
    user8 = users.create_user(
        email="mailuser8@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Nicolás",
        last_name="Santos",
    )
    user9 = users.create_user(
        email="mailuser9@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Silvio",
        last_name="Rodriguez",
    )
    user10 = users.create_user(
        email="mailuser10@gmail.com",
        password="1234",
        status="Habilitado",
        first_name="Francisco",
        last_name="Fernandez",
    )
    super_admin = users.create_user(
        email="superadmin@gmail.com", password="superadmin1234", status="Habilitado", first_name="admin", last_name="admin"
    )

    """INSTITUCIONES"""
    institucion1 = instituciones.create_institucion(nombre="UNLP Informática", infoInstitucion="Universidad Nacional de La Plata", direccion="Calle 50 &, Av. 120, La Plata, Provincia de Buenos Aires", latitud=-34.90328670324879, longitud=-57.937685330086516,
                                                    web="https://www.info.unlp.edu.ar/", palabrasClaves="Universidad Nacional Pública Informática LP", diasHorarios="8.30 a 12 hs.- 14 a 17 hs.", infoContacto="difusion@info.unlp.edu.ar")
    institucion2 = instituciones.create_institucion(nombre="UNLP Exactas", infoInstitucion="Universidad Nacional de La Plata", direccion="Calle 50 &, Av. 120, La Plata, Provincia de Buenos Aires", latitud=-34.90328670324879, longitud=-57.937685330086516,
                                                    web="https://www.info.unlp.edu.ar/", palabrasClaves="Universidad Nacional Pública Informática LP", diasHorarios="8.30 a 12 hs.- 14 a 17 hs.", infoContacto="difusion@info.unlp.edu.ar")
    """ROLES DE USUARIO"""

    rol_super_administrador = roles.create_rol("super_administrador")
    rol_owner = roles.create_rol("owner")
    rol_administrador = roles.create_rol("administrador")
    rol_operador = roles.create_rol("operador")
    rol_pendiente = roles.create_rol("pendiente")

    """PERMISOS + ASIGNACION DE PERMISOS A ROLES"""

    """Permisos CRUD DE USUARIOS (super administrador)"""
    user_index = create_permiso("user_index")  # Checked
    user_create = create_permiso("user_create")  # Checked
    user_destroy = create_permiso("user_destroy")  # Checked
    user_update = create_permiso("user_update")  # Checked
    user_show = create_permiso("user_show")  # Checked
    add_permisos_to_rol(rol_super_administrador, [
                        user_index, user_create, user_destroy, user_update, user_show])

    """Permisos CRUD DE INSTITUCIONES (super administrador)"""
    institucion_index = create_permiso("institucion_index")  # Checked
    institucion_create = create_permiso("institucion_create")  # Checked
    institucion_destroy = create_permiso("institucion_destroy")  # Checked
    institucion_update = create_permiso(
        "institucion_update")  # Checked
    institucion_show = create_permiso(
        "institucion_show")  # Checked - "mejorable"
    institucion_activate = create_permiso("institucion_activate")  # Checked
    institucion_deactivate = create_permiso(
        "institucion_deactivate")  # Checked
    add_permisos_to_rol(rol_owner, [institucion_update])
    add_permisos_to_rol(rol_super_administrador, [institucion_index, institucion_create, institucion_destroy,
                        institucion_update,   institucion_show, institucion_activate, institucion_deactivate])
    """ Permisos MODULO DE CRUD PARA OWNERS (super administrador)"""

    owner_index = create_permiso("owner_index")
    owner_create = create_permiso("owner_create")
    owner_update = create_permiso("owner_update")
    owner_destroy = create_permiso("owner_destroy")

    add_permisos_to_rol(rol_super_administrador, [
                        owner_index, owner_create, owner_update, owner_destroy])

    """Permisos MODULO DE CONFIGURACIÓN (super administrador)"""
    configuracion_show = create_permiso("configuracion_show")  # Checked
    configuracion_update = create_permiso(
        "configuracion_update")  # Checked
    add_permisos_to_rol(rol_super_administrador,
                        [configuracion_show, configuracion_update])

    """Permisos DUEÑO DE INSTITUCIONES (dueño)"""
    user_institucion_index = create_permiso("user_institucion_index")  # diego
    user_institucion_create = create_permiso(
        "user_institucion_create")  # diego
    user_institucion_destroy = create_permiso(
        "user_institucion_destroy")  # diego
    user_institucion_update = create_permiso(
        "user_institucion_update")  # diego
    add_permisos_to_rol(rol_owner, [user_institucion_index, user_institucion_create,
                        user_institucion_destroy, user_institucion_update])
    # Agregar a institucion un usuario

    """Permisos SERVICIOS DE INSTITUCIÓN (administrador/dueño/operador))"""
    servicio_index = create_permiso("servicio_index")
    servicio_create = create_permiso("servicio_create")
    servicio_destroy = create_permiso("servicio_destroy")
    servicio_update = create_permiso("servicio_update")
    servicio_show = create_permiso("servicio_show")
    add_permisos_to_rol(rol_administrador, [servicio_index, servicio_create,
                        servicio_destroy, servicio_update, servicio_show])
    add_permisos_to_rol(rol_owner, [servicio_index, servicio_create,
                        servicio_destroy, servicio_update, servicio_show])
    add_permisos_to_rol(rol_operador, [servicio_index, servicio_create,
                        servicio_update, servicio_show])

    """Permisos GESTIÓN DE SOLICITUDES DE SERVICIOS (administrador/dueño/operador)"""
    solicitud_servicio_index = create_permiso("solicitud_servicio_index")
    solicitud_servicio_destroy = create_permiso("solicitud_servicio_destroy")
    solicitud_servicio_update = create_permiso("solicitud_servicio_update")
    solicitud_servicio_show = create_permiso("solicitud_servicio_show")
    add_permisos_to_rol(rol_administrador, [solicitud_servicio_index,
                        solicitud_servicio_destroy, solicitud_servicio_update, solicitud_servicio_show])
    add_permisos_to_rol(rol_owner, [solicitud_servicio_index,
                        solicitud_servicio_destroy, solicitud_servicio_update, solicitud_servicio_show])
    add_permisos_to_rol(rol_operador, [
                        solicitud_servicio_index, solicitud_servicio_update, solicitud_servicio_show])

    """ASIGNACION DE ROLES A USUARIOS"""

    """Se le asigna a un usuario el rol de super administrador"""
    create_userRol(rol=rol_super_administrador, user=super_admin)
    create_userRol(rol=rol_owner, user=user1, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user1, institucion=institucion2)
    create_userRol(rol=rol_operador, user=user2, institucion=institucion1)
    create_userRol(rol=rol_administrador, user=user3, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user3, institucion=institucion2)
    create_userRol(rol=rol_operador, user=user4, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user5, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user6, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user7, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user8, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user9, institucion=institucion1)
    create_userRol(rol=rol_operador, user=user10, institucion=institucion1)

    """SERVICIOS"""
    servicio_1 = create_servicio(nombre="Servicio 1", descripcion="Descripcion 1", palabras_claves_busqueda="palabra1, palabra2, palabra3",
                                 listado_centros_habilitados="Centro 1, Centro 2, Centro 3", tipo_servicio="Análisis", institucion=institucion1)
    servicio_2 = create_servicio(nombre="Servicio 2", descripcion="Descripcion 2", palabras_claves_busqueda="palabra1, palabra2, palabra3",
                                 listado_centros_habilitados="Centro 1, Centro 2, Centro 3", tipo_servicio="Consultoría", institucion=institucion2)
    servicio_3 = create_servicio(nombre="Servicio 3", descripcion="Descripcion 3", palabras_claves_busqueda="palabra1, palabra2, palabra3",
                                 listado_centros_habilitados="Centro 1, Centro 2, Centro 3", tipo_servicio="Desarrollo", institucion=institucion2)

    """SOLICITUDES"""
    solicitud_1 = create_solicitud(
        user=user1, servicio=servicio_1)
    solicitud_2 = create_solicitud(
        user=user2, servicio=servicio_2)

    """NOTAS"""
    nota_1 = cargar_nota(
        id_solicitud=solicitud_1.id, comentario="Una porquería", autor_id=1)
    nota_2 = cargar_nota(
        id_solicitud=solicitud_2.id, comentario="Muy bueno", autor_id=1)

    print("Base de datos precargada!")
