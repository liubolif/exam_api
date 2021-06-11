import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        app.config.from_object(Config)

        db.init_app(app)

        from . import views
        from .api_restful import api_restful_bp

        app.register_blueprint(api_restful_bp, url_prefix='/api')

    return app
