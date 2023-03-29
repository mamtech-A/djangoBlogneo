from django.shortcuts import render, HttpResponse, redirect
from .models import Article, Person
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.core.paginator import Paginator


def articles_list(request):
    articles = Article.nodes.order_by('-date').all()
    article_list = []
    for article in articles:
        author = article.author.single()
        article_data = {
            'title': article.title,
            'body': article.body,
            'slug': article.slug,
            'date': article.date,
            'author': author.name,
            'snippet': article.snippet()
        }
        article_list.append(article_data)
    args = {'articles': article_list}
    return render(request, 'articles/articleslist.html', args)


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.nodes.get(slug=slug)
    author = article.author.single()
    return render(request, 'articles/article_detail.html', {'article': article, 'author': author})


@login_required(login_url='/accounts/login')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save()
            account = Person.nodes.get(name=request.user.username)
            instance.author.connect(account)
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form': form})
