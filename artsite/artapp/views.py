from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query).prefetch_related('photos').order_by('-date_posted') | Post.objects.filter(content__icontains=search_query).prefetch_related('photos').order_by('-date_posted')
    else:
        posts = Post.objects.prefetch_related('photos').order_by('-date_posted')
    #posts = Post.objects.prefetch_related('photos').order_by('-date_posted')

    template = loader.get_template('artsite/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))