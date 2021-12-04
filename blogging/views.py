from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template import loader
from blogging.models import Post, Category
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join("\t%s" % a for a in args)
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(
            ["\t%s: %s" % i for i in kwargs.items()]
        )  # returning 2 values
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = Post
    template_name = "blogging/list.html"

    # def get(self, request, *args, **kwargs):
    #     published = Post.objects.exclude(published_date__exact=None)
    #     return published


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    # def get(self, request, *args, **kwargs):
    #     published = Post.objects.exclude(published_date__exact=None)

    #     try:
    #         post = published.get(pk=post_id)
    #     except Post.DoesNotExist:
    #         raise Http404
    #     context = {'object': post}
    #     return render(request, 'blogging/detail.html', context)
