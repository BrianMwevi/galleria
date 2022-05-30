from django.db import models
from django.contrib.auth.models import User
from galleria.models import Image
# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    images = models.ManyToManyField(
        Image, related_name='user', blank=True)

    def save_poster(self):
        self.save()
        return self

    def __str__(self):
        return self.user.username
