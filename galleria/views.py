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


@login_required
def create_gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = request.user
            image.save_image()
        return redirect("account:profile", pk=request.user.id)
    form = ImageForm()
    locations = Location.objects.all()
    categories = Category.objects.all()
    context = {'form': form, "categories": categories, "locations": locations}
    return render(request, 'create_gallery.html', context)


def search_gallery(request):
    category = request.GET.get('q')
    print(category)
    if category:
        images = Image.search_image(category)
    else:
        images = Image.objects.all()
    context = {'images': images, 'category': category}
    return render(request, 'index.html', context)
