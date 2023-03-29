from django.forms import ModelForm
from . import models
from django import forms


class CreateArticle(ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'image']

    image = forms.ImageField(required=False)
    body = forms.Textarea()
