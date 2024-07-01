from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post


def index(request):
    posts = []
    posts = Post.objects.all()
    template = loader.get_template('artsite/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))