from flask import Blueprint

from . import views

routes = Blueprint('public', __name__, url_prefix='/', template_folder='templates')

routes.add_url_rule('/', endpoint='index', view_func=views.index, methods=['GET', 'POST'])
