from django.db import models
from django_neomodel import DjangoNode
from neomodel import *


class Person(DjangoNode):
    uuid = UniqueIdProperty(primary_key=True)
    name = StringProperty()

    class Meta:
        app_label = 'articles'


class Article(DjangoNode):
    uuid = UniqueIdProperty(primary_key=True)
    title = StringProperty(max_length=100)
    body = StringProperty()
    date = DateTimeFormatProperty(format="%Y-%m-%d %H:%M:%S", default_now=True)
    slug = StringProperty(unique_index=True, required=True)
    image = StringProperty(default='default.png', required=False)

    author = RelationshipTo(Person, 'AUTHOR')

    class Meta:
        app_label = 'articles'

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
