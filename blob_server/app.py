from blob_server.database import get_session_registry, get_engine
from blob_server.app_config import Config
from blob_server.resources import PostResource
from flask import Flask
from flask_restful import Api


def add_resources(app):
    api = Api(app)
    api.add_resource(PostResource, '/posts')


def create_app(config=Config):
    app = Flask(__name__)
    add_resources(app)
    app.engine = get_engine()
    app.session = get_session_registry(app.engine)
    app.config.from_object(config)
    return app


