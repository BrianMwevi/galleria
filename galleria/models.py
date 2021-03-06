from django.db import models
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Image(models.Model):
    photo = CloudinaryField('photo')
    name = models.CharField(max_length=55, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=False)
    category = models.ForeignKey(
        'Category', related_name='image', on_delete=models.CASCADE)
    location = models.ForeignKey(
        'Location', related_name='image', on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_image(self):
        self.save()
        return self

    @classmethod
    def update_image(cls, obj):
        image = cls.get_image_by_id(obj.id)
        image.photo = obj.photo
        image.name = obj.name
        image.description = obj.description
        image.location = obj.location
        image.category = obj.category
        image.save_image()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(
            location__name=location).order_by('-created_at')
        return images

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def save_category(self):
        self.save()
        return self

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, obj):
        category = cls.objects.get(id=obj.id)
        category.name = obj.name
        category.save_category()

    @classmethod
    def get_category(cls, id):
        category = cls.objects.get(id=id)
        return category

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, obj):
        location = cls.objects.get(id=obj.id)
        location.name = obj.name
        location.save_location()

    @classmethod
    def get_location(cls, id):
        location = cls.objects.get(id=id)
        return location

    def __str__(self):
        return self.name
