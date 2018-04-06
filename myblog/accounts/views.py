# accounts/views.py

from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'accounts/signup_form.html',{
        'form' : form,
    })


@login_required()
def profile(request):
    return render(request,'accounts/profile.html')