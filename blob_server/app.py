from blob_server.app_config import Config
from flask import Flask


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app
