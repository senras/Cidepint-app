from datetime import datetime 



from src.core.database import db

class RolPermiso(db.Model):
    
        __tablename__ = "rolPermiso"
    
        id = db.Column(db.Integer, primary_key=True, unique=True)
        rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
        rol = db.relationship('Rol', back_populates='rolesPermisos')
        permiso_id = db.Column(db.Integer, db.ForeignKey('permiso.id'))
        
        update_at = db.Column(
    
            db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    
        )
    
        inserted_at = db.Column(db.DateTime, default=datetime.utcnow)