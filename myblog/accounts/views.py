# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form,
    })


@login_required()
def profile(request):
    return render(request,'accounts/profile.html')


@login_required()
def profile_change(request):
    profile = get_object_or_404(Profile, pk=request.user.profile.id)
    print(request.user.profile.id)
    print('=====================')
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'accounts/profile_change.html', {
        'form': form
    })