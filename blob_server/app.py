from blob_server.database import get_session_registry, get_engine
from blob_server.app_config import Config
from flask import Flask


def create_app(config=Config):
    app = Flask(__name__)
    app.engine = get_engine()
    app.session = get_session_registry(app.engine)
    app.config.from_object(config)
    return app
