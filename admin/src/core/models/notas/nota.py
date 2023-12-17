from datetime import datetime
from src.core.database import db


class Nota(db.Model):
    _tablename_ = "notas"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    comentario = db.Column(db.String(255), default="")
    autor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    solicitud_id = db.Column(db.Integer, db.ForeignKey('solicitudes.id'))
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow())
