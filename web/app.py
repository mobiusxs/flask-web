from flask import Flask, render_template


def create_app(config='web.settings'):
    app = Flask(__name__)
    app.config.from_object(config)
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
