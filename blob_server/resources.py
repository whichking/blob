from flask import current_app as app
from flask_restful import Resource
from sqlalchemy import desc

from blob_server.models import BlogPost


class PostResource(Resource):
    def get(self):
        query = app.session.query(BlogPost).order_by(desc(BlogPost.created))
        posts = [post.serializable for post in query]
        return posts
