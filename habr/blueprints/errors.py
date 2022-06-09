from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound, Forbidden, InternalServerError

errors = Blueprint(
    name='errors',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@errors.app_errorhandler(Forbidden)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(NotFound)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(InternalServerError)
def error_500(error):
    return render_template('errors/500.html'), 500
