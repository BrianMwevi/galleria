from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=55, required=True)
    password = forms.CharField(max_length=55, required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)
