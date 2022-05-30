from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Image, Location, Category
from galleria.forms import ImageForm


def galleries(request):
    location = request.GET.get('location')
    if location:
        images = Image.filter_by_location(location.title())
    else:
        images = Image.objects.order_by('-created_at')
    locations = Location.objects.all()
    context = {'images': images, "locations": locations}
    return render(request, 'index.html', context)
