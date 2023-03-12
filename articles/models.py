from django.db import models
from django_neomodel import DjangoNode
from neomodel import *


class Article(DjangoNode):
    title = StringProperty(max_length=100)
    body = StringProperty()
    date = DateTimeFormatProperty(format="%Y-%m-%d %H:%M:%S", default_now=True)
    slug = StringProperty(unique_index=True, required=True)
    image = StringProperty(default='default.jpg', required=False)

    class Meta:
        app_label = 'article'

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
