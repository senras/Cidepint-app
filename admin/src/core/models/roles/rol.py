from datetime import datetime 



from src.core.database import db



class Rol(db.Model):

	__tablename__ = "rol"

	id = db.Column(db.Integer, primary_key=True, unique=True)
	nombre = db.Column(db.String(255))
	
	update_at = db.Column(

		db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow

	)

	inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
	rolesPermisos = db.relationship('RolPermiso', back_populates='rol')
	usersRoles = db.relationship('UserRol', back_populates='rol')