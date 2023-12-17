from src.core.database import db
from src.core.models.solicitudes.solicitud import Solicitud
from src.core.models.servicios.servicio import Servicio
from src.core.models.notas import cargar_nota
from src.core.models import notas
from datetime import datetime


def get_solicitudes():
    return Solicitud.query.all()


def get_solicitudes_by_institucion_id(id):
    solicitudes = Solicitud.query.filter(Solicitud.servicio.has(
        Servicio.institucion_id == id)).all()
    return solicitudes


def get_solicitudes_by_user_id(id):
    return Solicitud.query.filter_by(user=id).all()


def get_solicitud_by_id(id):
    return Solicitud.query.filter_by(id=id).first()


def edit_solicitud(id, data):
    solicitud = get_solicitud_by_id(id)
    print(data['status'], solicitud.status)
    if data['status'] != solicitud.status:
        solicitud.status_at = datetime.utcnow()
        solicitud.status = data['status']
        solicitud.observaciones = data['observaciones']
    db.session.commit()
    return solicitud


def delete_solicitud(id):
    solicitud = get_solicitud_by_id(id)
    db.session.delete(solicitud)
    db.session.commit()
    return solicitud


def create_solicitud(**kwargs):
    solicitud = Solicitud(**kwargs)
    solicitud.status = "En proceso"
    db.session.add(solicitud)
    db.session.commit()
    return solicitud


def cargar_nota_a_solictud(id_solicitud, comentario, autor_id):
    cargar_nota(id_solicitud, comentario, autor_id)
    solicitud = get_solicitud_by_id(id_solicitud)
    return solicitud
