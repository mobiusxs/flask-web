from flask import Flask


def create_app(config='web.settings'):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from web import index

    app.register_blueprint(index.routes)
