# post/views.py

from django.shortcuts import render
from .models import Post


def post_list(request):
    list_query = Post.objects.all()
    for i in list_query:
        print(i.title)
    return render(request, 'post/post_list.html', {
        'post_list': list_query,
    })

