from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator

from .models import Post, Photo

def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query).prefetch_related('photos').order_by('-date_posted') | Post.objects.filter(content__icontains=search_query).prefetch_related('photos').order_by('-date_posted')
        photos = Photo.objects.all().order_by('-post__date_posted')
    else:
        posts = Post.objects.prefetch_related('photos').order_by('-date_posted')
        photos = Photo.objects.all().order_by('-post__date_posted')

    paginator = Paginator(photos, 6)
    page_obj = paginator.get_page(request.GET.get('page'))

    if is_ajax(request):
        html = render_to_string('artsite/partials/photo_list.html', {'page_obj': page_obj})
        return JsonResponse({'html': html})

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'artsite/index.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'