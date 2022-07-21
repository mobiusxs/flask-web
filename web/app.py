from flask import Flask


def create_app(config='web.settings'):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    register_extensions(app)
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
