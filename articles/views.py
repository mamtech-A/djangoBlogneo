from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from . import forms


def articles_list(request):
    articles = Article.nodes.all()
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.nodes.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid:
            form.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form': form})
