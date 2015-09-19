""" Post model """

import datetime

from flask import url_for
from ..app import db
from .comment import Comment


class Post(db.DynamicDocument):
    """ Post document definition """

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    @property
    def post_type(self):
        """ post_type property """
        return self.__class__.__name__

    def url(self):
        """ Return post url """
        return url_for('post', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title


class BlogPost(Post):
    """ Blog post """
    body = db.StringField(required=True)


class Video(Post):
    """ Video """
    embed_code = db.StringField(required=True)


class Image(Post):
    """ Image """
    image_url = db.StringField(required=True, max_length=255)


class Quote(Post):
    """ Quote """
    body = db.StringField(required=True)
    author = db.StringField(verbose_name='Author Name', required=True,
                            max_length=255)
