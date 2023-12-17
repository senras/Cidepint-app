from flask import render_template
from src.core.models.configuracion.config import Config
from src.core.database import db


'''Módulo de configuración general de la app (usando singleton)'''


def create_Config():
    config = Config()
    db.session.add(config)
    db.session.commit()
    return config


def get_Config():
    if Config.query.first() is None:
        return create_Config()
    return Config.query.first()


def edit_Config(data, checked):
    config = get_Config()
    config.element_quantity = data['element_quantity']
    config.contact_email = data['contact_email']
    config.contact_phone = data['contact_phone']
    config.contact_address = data['contact_address']
    config.manteinance_message = data['manteinance_message']
    config.in_manteinance = checked
    db.session.commit()
    return config


def get_element_quantity():
    config = get_Config()
    return config.element_quantity


def get_manteinance_message():
    config = get_Config()
    return config.manteinance_message


def get_manteinance_status():
    config = get_Config()
    return config.in_manteinance


def get_contact_email():
    config = get_Config()
    return config.contact_email


def get_contact_phone():
    config = get_Config()
    return config.contact_phone


# Chequearlo
def dec_manteinance(f):
    def decorated_function(*args, **kwargs):
        if get_Config().in_manteinance:
            return render_template('manteinance.html', config=get_Config())
        return f(*args, **kwargs)
    return decorated_function
