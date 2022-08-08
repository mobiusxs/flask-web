from flask import Blueprint

from . import views

routes = Blueprint('private', __name__, url_prefix='/private', template_folder='templates',
                   static_folder='static', static_url_path='/private/static')

routes.add_url_rule('/', endpoint='index', view_func=views.index, methods=['GET'])
