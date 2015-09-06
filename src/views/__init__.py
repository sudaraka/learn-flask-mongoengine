""" Views module """

from flask import Blueprint

from .list import ListView
from .detail import DetailView

posts = Blueprint('posts', __name__, template_folder='templates')

posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>', view_func=DetailView.as_view('detail'))
