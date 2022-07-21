from flask import Flask, render_template, request


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
    from web import index

    app.register_blueprint(index.routes)


def register_extensions(app):
    from web.extensions import (
        admin,
        db,
        migrate
    )

    admin.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_shell_context(app):
    from .extensions import db

    def shell_context():
        return {'db': db}

    app.shell_context_processor(shell_context)


def register_error_handlers(app):
    def handler(error):
        return render_template('error.html', error=error), error.code

    for code in [401, 404, 500]:
        app.register_error_handler(code, handler)


def configure_logging(app):
    from logging import getLogger, DEBUG, WARNING
    from web.logging import stream_handler

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


