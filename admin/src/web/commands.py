from src.core import database
from src.core import seeds


def register_commands(app):
    """ para reiniciar a la base de datos usar flask resetdb """
    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    """ para cargar los datos de prueba usar flask seedsdb """
    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()
