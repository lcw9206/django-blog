# post/views.py

from django.shortcuts import render
from .models import Post


def post_list(request):
    list_query = Post.objects.all()

    return render(request, 'post/post_list.html', {
        'post_list': list_query,
    })


def post_detail(request,id):
    post = Post.objects.get(id=id)

    return render(request, 'post/post_detail.html', {
        'post': post,
    })
