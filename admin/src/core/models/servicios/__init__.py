from src.core.database import db
from src.core.models.servicios.servicio import Servicio


def list_servicios():
    servicios = Servicio.query.all()
    return servicios


def create_servicio(**kwargs):
    servicio = Servicio(**kwargs)
    db.session.add(servicio)
    db.session.commit()
    return servicio


def edit_servicio(id, data):
    servicio = get_servicio_by_id(id)
    servicio.nombre = data['nombre']
    servicio.descripcion = data['descripcion']
    servicio.palabras_claves_busqueda = data['palabras_claves_busqueda']
    servicio.listado_centros_habilitados = data['listado_centros_habilitados']
    servicio.tipo_servicio = data['tipo_servicio']
    servicio.habilitado = data.get('habilitado')
    db.session.commit()
    return servicio


def delete_servicio(servicio):
    db.session.delete(servicio)
    db.session.commit()
    return servicio


def get_servicio_by_id(id):
    servicio = Servicio.query.get(id)
    return servicio


def get_tipos_de_servicios():
    tipos_de_servicios = db.session.query(
        Servicio.tipo_servicio).distinct().all()
    tipos_de_servicios = [tipo[0] for tipo in tipos_de_servicios]
    return tipos_de_servicios
