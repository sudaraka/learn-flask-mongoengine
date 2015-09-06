""" Comment model """

import datetime

from ..app import db


class Comment(db.EmbeddedDocument):
    """ Comment document definition """

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name='Comment', required=True)
    author = db.StringField(verbose_name='Name', max_length=255, required=True)
