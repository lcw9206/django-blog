# post/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


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


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('post/post_list.html')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {
        'form': form
    })
