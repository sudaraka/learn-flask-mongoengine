""" Views module """

from flask import Blueprint

from .list import ListView
from .detail import DetailView
from .admin import List, Detail

posts = Blueprint('posts', __name__, template_folder='templates')

posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>', view_func=DetailView.as_view('detail'))


admin = Blueprint('admin', __name__, template_folder='templates')

admin.add_url_rule('/admin/', view_func=List.as_view('index'))
admin.add_url_rule('/admin/create/', defaults={'slug': None},
                   view_func=Detail.as_view('create'))
admin.add_url_rule('/admin/<slug>/', view_func=Detail.as_view('edit'))
