from django.contrib import admin
from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin
from .models import Article, Person


class ArticleAdmin(dj_admin.ModelAdmin):
    list_display = ("title", "body", "slug", "date", "image", "author")


neo_admin.register(Article, ArticleAdmin)


class PersonAdmin(dj_admin.ModelAdmin):
    list_display = ("uuid","name")


neo_admin.register(Person, PersonAdmin)
