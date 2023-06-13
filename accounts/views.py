from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm
from .decorators import user_not_authenticated
# Create your views here.


@user_not_authenticated
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')

        form = LoginForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@user_not_authenticated
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
