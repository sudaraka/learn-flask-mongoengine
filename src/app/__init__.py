""" Application module """

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {'DB': 'flask_mongoengine'}
app.config['SECRET_KEY'] = 'SEFO36867TPL9Yl77c5iYTC3IVjGTWtp'

db = MongoEngine(app)
