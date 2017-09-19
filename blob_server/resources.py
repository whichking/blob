from flask import current_app as app
from flask_restful import Resource


class PostResource(Resource):
    def get(self):
        return {'hello': 'world'}
