from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    func,
    Integer,
    String,
    Table,
    Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()


PostTagLinks = Table(
    'post_tag_links',
    Base.metadata,
    Column('post_id', Integer, ForeignKey(blog_posts.id)),
    Column('tag_id', Integer, ForeignKey(tags.id))
)


class BlogPost(Base):
    """An entry containing the created date and the content of text"""
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    content = Column(Text)
    tags = relationship(
        'Tag',
        back_populates='blog_posts',
        secondary='post_tag_links'
    )


class Tag(Base):
    """A tag indicating the subject of a blog post"""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    posts = relationship(
        'Post',
        back_populates='tags',
        secondary='post_tag_links'
    )
