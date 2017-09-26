from uuid import uuid4
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restful import Api
from blob_server.database import get_session_registry, get_engine
from blob_server.app_config import Config
from blob_server.models import BlogPost, Tag
from blob_server.resources import PostResource


def add_resources(app):
    """adds /posts endpoint"""
    api = Api(app)
    api.add_resource(PostResource, '/posts')


def add_admin_interface(app):
    admin = Admin(app, name='madison', template_mode='bootstrap3')
    admin.add_view(ModelView(BlogPost, app.session))
    admin.add_view(ModelView(Tag, app.session))


def create_app(config=Config):
    """creates the app"""
    app = Flask(__name__)
    add_resources(app)
    app.secret_key = str(uuid4()).encode()
    app.engine = get_engine()
    app.session = get_session_registry(app.engine)
    add_admin_interface(app)
    app.config.from_object(config)
    return app



