from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(db)
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    with app.app_context():
        from . import routes
        db.create_all()
        return app
