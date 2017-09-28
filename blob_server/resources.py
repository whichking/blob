from flask import current_app as app
from flask_restful import Resource
from werkzeug.exceptions import NotFound
from sqlalchemy import desc

from blob_server.models import BlogPost, Tag


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


class TagsResource(Resource):
    def get(self):
        query = app.session.query(Tag).order_by(desc(Tag.name))
        tags = [tag.serializable for tag in query]
        return tags


class TagResource(Resource):
    def get(self, tag_id):
        tag= app.session.query(Tag).filter_by(id=tag_id).first()
        if tag is None:
            raise NotFound('No such tag: "{}'.format(tag_id))
        return tag.serializable
