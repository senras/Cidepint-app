from datetime import datetime 



from src.core.database import db



class Permiso(db.Model):

	__tablename__ = "permiso"

	id = db.Column(db.Integer, primary_key=True, unique=True)
	nombre = db.Column(db.String(255))
	rolesPermisos = db.relationship('RolPermiso', backref='permiso')
	update_at = db.Column(

		db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow

	)

	inserted_at = db.Column(db.DateTime, default=datetime.utcnow)