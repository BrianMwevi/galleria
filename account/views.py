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


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("account:profile", pk=user.id)
    form = SignupForm()
    return render(request, 'accounts/login.html', {'form': form})


def profile(request, pk):
    images = Image.objects.filter(poster=request.user).order_by('-created_at')
    locations = Location.objects.all()
    context = {'images': images, 'locations': locations, 'pk': pk}
    return render(request, "accounts/profile.html", context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('gallery_list'))
