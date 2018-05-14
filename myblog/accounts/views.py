# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')
        else:
            messages.error(request, '회원가입에 실패하였습니다.')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_change(request):
    profile = get_object_or_404(Profile, pk=request.user.profile.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필 변경이 완료되었습니다.')
            return redirect('profile')
        else:
            messages.error(request, '프로필 변경에 실패하였습니다.')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_change.html', {
        'form': form
    })


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호 변경이 완료되었습니다.')
            return render(request, 'accounts/profile.html', {
                'form': form
            })
        else:
            messages.error(request, '비밀번호 변경에 실패했습니다.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })
