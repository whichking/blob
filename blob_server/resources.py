from flask import current_app as app
from flask_restful import Resource
from werkzeug.exceptions import NotFound
from sqlalchemy import desc

from blob_server.models import BlogPost


class PostsResource(Resource):
    def get(self):
        query = app.session.query(BlogPost).order_by(desc(BlogPost.created))
        posts = [post.serializable for post in query]
        return posts


class PostResource(Resource):
    def get(self, post_id):
        post = app.session.query(BlogPost).filter_by(id=post_id).first()
        if post is None:
            raise NotFound('No such post: "{}"'.format(post_id))
        return post.serializable
