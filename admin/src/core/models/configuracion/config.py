from datetime import datetime
from src.core.database import db


class Config(db.Model):
    __tablename__ = "config"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    element_quantity = db.Column(db.Integer, default=20)
    contact_email = db.Column(db.String(255), default="soporte@gmail.com")
    contact_phone = db.Column(db.String(255), default="221 200 4222")
    contact_address = db.Column(db.String(255), default="120 nº3080")
    in_manteinance = db.Column(db.Boolean, default=False)
    manteinance_message = db.Column(
        db.String(255), default="En mantenimiento.")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
