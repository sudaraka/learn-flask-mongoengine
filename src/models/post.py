""" Post model """

import datetime

from flask import url_for
from ..app import db
from .comment import Comment


class Post(db.Document):
    """ Post document definition """

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def url(self):
        """ Return post url """
        return url_for('post', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title
