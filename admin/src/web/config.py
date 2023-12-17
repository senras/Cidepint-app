from os import environ


class Config(object):
    """Base configuration."""

    SECRET_KEY = "secret"
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True
    TESTING = False
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    JWT_SECRET_KEY = "secret_key"
    JWT_TOKEN_LOCATION = ['headers']
    CORS_HEADERS = 'Content-Type'

    # Credenciales para servicio de correo
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = environ.get("MAIL_USER")
    MAIL_PASSWORD = environ.get("MAIL_PASS")


class ProductionConfig(Config):
    """Production configuration."""

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


class DevelopmentConfig(Config):
    """Development configuration."""

    DB_USER = "postgres"
    DB_PASS = "postgres"
    DB_NAME = "grupo06"
    DB_HOST = "localhost"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}
