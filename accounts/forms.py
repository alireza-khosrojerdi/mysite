from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        help_text='A valid email address, please', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Username or Email'}),
        label='Username or Email')

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'Password'})

    )
