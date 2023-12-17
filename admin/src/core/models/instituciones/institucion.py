from datetime import datetime
from src.core.database import db


class Institucion(db.Model):
    __tablename__ = "instituciones"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(100))
    infoInstitucion = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    web = db.Column(db.String(100))
    palabrasClaves = db.Column(db.String(255))
    diasHorarios = db.Column(db.String(255))
    infoContacto = db.Column(db.String(255))
    habilitado = db.Column(db.Boolean(), default=True)
    update_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    usersRoles = db.relationship('UserRol', backref='instituciones')
    servicios = db.relationship('Servicio', back_populates='institucion')
