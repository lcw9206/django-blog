# post/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def post_list(request):
    list_query = Post.objects.all()

    return render(request, 'post/post_list.html', {
        'post_list': list_query,
    })


def post_detail(request, id):
    post = get_object_or_404(Post,id=id)

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
            messages.success(request, '새 글이 등록되었습니다.')
            return redirect('post:post_list')
        else:
            messages.error(request, '글 등록에 실패하였습니다.')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {
        'form': form
    })


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        messages.success(request, '글 삭제를 완료했습니다.')
    return redirect('post:post_list')


@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '글 수정에 성공했습니다.')
            return redirect('post:post_list')
        else:
            messages.error(request, '글 수정에 실패했습니다.')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {
        'form': form
    })
