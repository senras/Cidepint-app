from flask import render_template
from flask import Response


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La página a la que quieres acceder no existe.",
    }

    return render_template("error.html", **kwargs), 404

def not_permission_error(e):
    kwargs = {
        "error_name": "401 Not Permission Error",
        "error_description": "No tienes permisos para acceder a esta página.",
    }

    return render_template("error.html", **kwargs), 401

def bad_request_error(e):
    kwargs = {
        "error": "Parámetros inválidos"
    }

    return Response(kwargs, status=400)
