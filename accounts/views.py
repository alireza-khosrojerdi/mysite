from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token
from .forms import LoginForm, RegisterForm, PasswordResetForm , SetPasswordForm
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


@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(email=user_email).first()
            if associated_user:
                subject = 'Password reset request'
                message = render_to_string('accounts/template_reset_password.html', {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    'protocol': 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[
                                     associated_user.email])
                if email.send():
                    messages.success(request,
                                     """
                                     password reset sent !!!
                                     """
                                     )
                else:
                    messages.error(
                        request, 'problem sending reset password email, <b><SERVER PROBLEM/b>')
            return redirect('/')


    form = PasswordResetForm()
    context = {'form': form}
    return render(request, 'accounts/password_reset.html', context)










def PasswordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user , request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "your password has been set")
                return redirect('/')
            else:
            
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'accounts/password_reset_confirm.html',{'form':form})
    else:
        messages.error(request, 'link is expired')



    messages.error(request, 'somthing is wrong . we back to home page')
    return redirect('/')
