from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_app(app):
    """
    Inicialiación de la aplicación.
    """
    db.init_app(app)
    config_db(app)

def config_db(app):
    """
    Configuración de la aplicación.
    """
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()

def reset_db():
    """
    Reseteo de la base de datos. Crea las tablas necesarias de acuerdo a los modelos establecidos.
    """
    print("Borrando base de datos...")
    db.drop_all()
    print("Creando base de datos...")
    db.create_all() 
    print("Listo!")