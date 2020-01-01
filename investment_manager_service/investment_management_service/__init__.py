from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    cors = CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}'
    app.config['CORS_HEADERS'] = 'Content-Type'
    with app.app_context():
        from . import routes
        db.create_all()
        return app

