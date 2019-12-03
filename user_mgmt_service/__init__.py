from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    with app.app_context():
        from . import routes
        return app
