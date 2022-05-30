from django import forms
from galleria.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ("poster",)
