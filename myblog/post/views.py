# post/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def post_list(request):
    list_query = Post.objects.all()
    search = request.GET.get('search', '')

    if search:
        list_query = list_query.filter(title__icontains=search)

    return render(request, 'post/post_list.html', {
        'post_list': list_query,
        'search': search,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_form = CommentForm()

    return render(request, 'post/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
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

    if request.user != post.user:
        messages.warning(request,'잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == "POST":
        post.delete()
        messages.success(request, '글 삭제를 완료했습니다.')

    return redirect('post:post_list')


@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.user:
        messages.warning(request,'잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '글 수정에 성공했습니다.')
            return redirect('post:post_detail')
        else:
            messages.error(request, '글 수정에 실패했습니다.')
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_form.html', {
        'form': form
    })


@login_required
def comment_new(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "댓글이 등록되었습니다.")
            return redirect('post:post_detail', id)
        else:
            messages.error(request, "댓글 등록에 실패했습니다.")

    return redirect('post:post_detail')
