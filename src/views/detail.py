""" Detail view """

from flask import render_template
from flask.views import MethodView

from ..models import Post


class DetailView(MethodView):
    """ Detail view definition """

    def get(self, slug):
        """ Render detail template """

        post = Post.objects.get_or_404(slug=slug)

        return render_template('posts/detail.html', post=post)
