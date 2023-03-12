from django.forms import ModelForm
from . import models


class CreateArticle(ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'image']
