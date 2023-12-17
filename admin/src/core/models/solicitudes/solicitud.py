from datetime import datetime
from src.core.database import db


class Solicitud(db.Model):
    __tablename__ = "solicitudes"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.String(50), nullable=False)
    observaciones = db.Column(db.String(255), default="")
    status_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='solicitudes')
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'))
    servicio = db.relationship('Servicio', back_populates='solicitudes')
    notas = db.relationship('Nota', backref='solicitud', lazy=True)
