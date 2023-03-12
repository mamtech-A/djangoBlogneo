from django.contrib import admin
from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin
from .models import Article


class ArticleAdmin(dj_admin.ModelAdmin):
    list_display = ("title", "body", "slug", "date", "image")


neo_admin.register(Article, ArticleAdmin)
