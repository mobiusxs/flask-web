from logging import getLogger
from logging import DEBUG
from logging import WARNING
from os import environ

from flask import Flask
from flask import render_template
from flask import request

from web import private
from web import public
from web.admin import admin
from web.commands import web
from web.extensions import db
from web.extensions import migrate
from web.logging import stream_handler


def create_app(config='web.settings'):
    """Application Factory"""

    app = Flask(__name__)
    app.config.from_object(config)
    configure_logging(app)
    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_error_handlers(app)
    register_commands(app)
    return app


def configure_logging(app):
    """Configure app logging handlers after removing default handlers.
    Disable Werkzeug logging of requests and replace with own logging."""

    app.logger.setLevel(DEBUG)
    app.logger.handlers = []  # remove default handler
    app.logger.addHandler(stream_handler)
    getLogger('werkzeug').setLevel(WARNING)
    host = environ.get('FLASK_RUN_HOST', '127.0.0.1')
    port = environ.get('FLASK_RUN_PORT', 5000)
    app.logger.info(f'Running on http://{host}:{port} (Press CTRL+C to quit)')

    @app.after_request
    def log_request(response):
        """Log all requests as Werkzeug no longer does so"""

        path = request.path
        if request.args:
            path = request.full_path

        app.logger.info(f'{request.remote_addr} {response.status_code} {request.method} {request.scheme} {path}')
        return response


def register_blueprints(app):
    """Register Blueprints on the app."""

    app.register_blueprint(private.routes)
    app.register_blueprint(public.routes)


def register_extensions(app):
    """Initialize all extensions on the app."""

    admin.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_shell_context(app):
    """Add objects to shell context to improve development experience."""

    def shell_context():
        """Add key/value pairs to make objects available in shell.
        Function must return a dict.
        """

        return {'db': db}

    app.shell_context_processor(shell_context)


def register_error_handlers(app):
    """Server error.html with specific context for 401, 404, and 500 errors"""

    def handler(error):
        """Log error and server error.html"""

        app.logger.error(f'{request.remote_addr} {request.method} {request.full_path} {error.code}')
        return render_template('error.html', error=error), error.code

    for code in [401, 404, 500]:
        app.register_error_handler(code, handler)


def register_commands(app):
    """Add application specific commands"""

    app.cli.add_command(web)
