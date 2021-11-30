from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template import loader
from blogging.models import Post
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


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
