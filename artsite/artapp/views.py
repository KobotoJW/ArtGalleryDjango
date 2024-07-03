from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

def index(request):
    # Prefetch the photos for each post to minimize database queries
    posts = Post.objects.prefetch_related('photos').order_by('-date_posted')
    template = loader.get_template('artsite/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))