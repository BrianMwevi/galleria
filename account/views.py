import re
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from galleria.models import Image, Location
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from account.forms import SignupForm, LoginForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account:login'))
    form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
