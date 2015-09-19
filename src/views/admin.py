""" Admin view """

from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form

from ..models import Post, BlogPost, Video, Image, Quote
from ..app.auth import requires_auth


class List(MethodView):
    """ Admin list view definition """

    decorators = [requires_auth]
    cls = Post

    def get(self):
        posts = self.cls.objects.all()

        return render_template('admin/list.html', posts=posts)


class Detail(MethodView):
    """ Admin detail view definition """

    decorators = [requires_auth]
    class_map = {
        'post': BlogPost,
        'video': Video,
        'image': Image,
        'quote': Quote
    }

    def get_context(self, slug=None):
        """ Create context for template """

        if slug:
            post = Post.objects.get_or_404(slug=slug)
            cls = post.__class__ if post.__class__ != Post else BlogPost
            form_cls = model_form(Post, exclude=('created_at', 'comments'))

            if 'POST' == request.method:
                form = form_cls(request.form, initial=post._data)
            else:
                form = form_cls(obj=post)
        else:
            cls = self.class_map.get(request.args.get('type', 'post'))
            post = cls()
            form_cls = model_form(Post, exclude=('created_at', 'comments'))
            form = form_cls(request.form)

        context = {
            'post': post,
            'form': form,
            'create': slug is None
        }

        return context

    def get(self, slug):  # pylint: disable=I0011,R0201
        """ Render detail template """

        context = self.get_context(slug)

        return render_template('admin/detail.html', **context)

    def post(self, slug):
        """ Handle comment form post """

        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index'))

        return render_template('admin/detail.html', **context)
