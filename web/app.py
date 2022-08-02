from logging import getLogger
from logging import DEBUG
from logging import WARNING

from flask import Flask
from flask import render_template
from flask import request

from web import index
from web.extensions import admin
from web.extensions import db
from web.extensions import migrate
from web.logging import stream_handler


def create_app(config='web.settings'):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_logging(app)
    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_error_handlers(app)
    return app


def register_blueprints(app):

    app.register_blueprint(index.routes)


def register_extensions(app):

    admin.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_shell_context(app):

    def shell_context():
        return {'db': db}

    app.shell_context_processor(shell_context)


def register_error_handlers(app):
    def handler(error):
        app.logger.error(f'{request.remote_addr} {request.method} {request.full_path} {error.code}')
        return render_template('error.html', error=error), error.code

    for code in [401, 404, 500]:
        app.register_error_handler(code, handler)


def configure_logging(app):

    app.logger.setLevel(DEBUG)              # default level is DEBUG
    app.logger.handlers = []                # remove default handler
    app.logger.addHandler(stream_handler)   # add your own handlers

    @app.before_first_request
    def set_werkzeug_level():
        werkzeug = getLogger('werkzeug')
        werkzeug.setLevel(WARNING)

    @app.after_request
    def log_request(response):
        app.logger.info(f'{request.remote_addr} {request.method} {request.full_path} {response.status_code}')
        return response
