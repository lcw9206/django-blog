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


@login_required
def my_post_list(request):
    list_query = Post.objects.filter(user_id=request.user)
    search = request.GET.get('search', '')

    if search:
        list_query = list_query.filter(title__icontains=search)

    return render(request, 'post/post_list.html', {
        'post_list': list_query,
        'search': search,
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm()
    category = Post.objects.filter(category_id=post.category_id).order_by('-created_at')[0:5]

    return render(request, 'post/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
        'category_list': category,
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
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.user:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == "POST":
        post.delete()
        messages.success(request, '글 삭제를 완료했습니다.')

    return redirect('post:post_list')


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.user:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '글 수정에 성공했습니다.')
            return redirect('post:post_detail', post_id)
        else:
            messages.error(request, '글 수정에 실패했습니다.')
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_form.html', {
        'form': form
    })


@login_required
def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "댓글이 등록되었습니다.")
            return redirect('post:post_detail', post_id)
        else:
            messages.error(request, "댓글 등록에 실패했습니다.")

    return redirect('post:post_detail', post_id)


@login_required
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == "POST":
        comment.delete()
        messages.success(request, '댓글 삭제가 완료되었습니다.')
        return redirect('post:post_detail', post_id)

    return redirect('post:post_detail', post_id)
