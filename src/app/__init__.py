""" Application module """

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {'DB': 'flask_mongoengine'}
app.config['SECRET_KEY'] = 'SEFO36867TPL9Yl77c5iYTC3IVjGTWtp'

db = MongoEngine(app)


def register_blueprints(target_app):
    """ Register blueprints in the application """

    from ..views import posts
    from ..views import admin

    target_app.register_blueprint(posts)
    target_app.register_blueprint(admin)


register_blueprints(app)
