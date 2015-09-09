""" Detail view """

from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form

from ..models import Post, Comment


class DetailView(MethodView):
    """ Detail view definition """

    form = model_form(Comment, exclude=['created_at'])

    def get_context(self, slug):
        """ Create context for template """

        post = Post.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            'post': post,
            'form': form
        }

        return context

    def get(self, slug):  # pylint: disable=I0011,R0201
        """ Render detail template """

        context = self.get_context(slug)

        return render_template('posts/detail.html', **context)

    def post(self, slug):
        """ Handle comment form post """

        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            return redirect(url_for('posts.detail', slug=slug))

        return render_template('posts/detail.html', **context)
