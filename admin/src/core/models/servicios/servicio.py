from datetime import datetime
from src.core.database import db


class Servicio(db.Model):
    __tablename__ = "servicios"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    palabras_claves_busqueda = db.Column(db.String(100))
    listado_centros_habilitados = db.Column(db.String(100))
    tipo_servicio = db.Column(db.String(50))
    habilitado = db.Column(db.Boolean(), default=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    institucion_id = db.Column(db.Integer, db.ForeignKey("instituciones.id"))
    institucion = db.relationship("Institucion", back_populates="servicios")
    solicitudes = db.relationship("Solicitud", back_populates="servicio")
