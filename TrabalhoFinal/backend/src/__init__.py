from flask import Flask
from flask_cors import CORS
from config import Config
from src.extensions import pymongo


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    # inicializando as extensões do Flask
    pymongo.init_app(app)

    # registrando os blueprints
    from src.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app
