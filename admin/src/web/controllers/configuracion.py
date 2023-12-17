from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from src.core.forms.configurationForm import ConfigForm
from src.core.models.configuracion import *
from src.web.helpers.auth import login_required
from src.web.helpers.auth import permission_require


config_bp = Blueprint(
    "config", __name__, url_prefix="/config")

# PERMISOS CHEQUEADOS


@config_bp.route("/", methods=["GET", "POST"])
@login_required
@permission_require(["configuracion_show", "configuracion_update"])
def index():
    configuracion = get_Config()
    form = ConfigForm(request.form, configuracion)
    # IMPORTANTE = Usar esto cuando se tiene un field boolean para que tome el valor del modelo
    form.in_manteinance.checked = configuracion.in_manteinance
    if request.method == 'POST' and form.validate():
        if form.validate():
            checked = request.form.get('flexSwitchCheckDefault')
            if checked is None:
                checked = False
            else:
                checked = True
            edit_Config(data=form.data, checked=checked)
        return redirect(url_for('home.home'))
    return render_template('configuracion/config.html', form=form)
