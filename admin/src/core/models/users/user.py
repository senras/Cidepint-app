from datetime import datetime
from src.core.database import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    status = db.Column(db.String(50))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    userRoles = db.relationship('UserRol', backref='user')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    solicitudes = db.relationship('Solicitud', back_populates='user')
    notas = db.relationship('Nota', backref='autor', lazy=True)
