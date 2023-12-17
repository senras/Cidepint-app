from datetime import datetime 



from src.core.database import db

class UserRol(db.Model):
    
        __tablename__ = "userRol"
    
        id = db.Column(db.Integer, primary_key=True, unique=True)
        rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
        rol = db.relationship('Rol', back_populates='usersRoles')
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        institucion_id = db.Column(db.Integer, db.ForeignKey('instituciones.id'))
        update_at = db.Column(
    
            db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    
        )
    
        inserted_at = db.Column(db.DateTime, default=datetime.utcnow)