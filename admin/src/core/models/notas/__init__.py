from src.core.models.notas.nota import Nota
from src.core.database import db


def get_notas(solicitud_id):
    return Nota.query.filter_by(solicitud_id=solicitud_id).all()


def cargar_nota(id_solicitud, comentario, autor_id):
    nota = Nota(comentario=comentario, autor_id=autor_id,
                solicitud_id=id_solicitud)
    db.session.add(nota)
    db.session.commit()
    return nota
