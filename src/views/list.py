""" List view """

from flask import render_template
from flask.views import MethodView

from ..models import Post


class ListView(MethodView):
    """ List view definition """

    def get(self):
        """ Render list template """

        posts = Post.objects.all()

        return render_template('posts/list.html', posts=posts)
