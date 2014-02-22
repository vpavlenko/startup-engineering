from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


def show_article(request, title):
    article = Article.objects.get(title=title)
    return render(request, 'article.html', {'article': article, 'edit': False})


def edit_article(request, title):
    try: 
        article = Article.objects.get(title=title)
    except Article.DoesNotExist:
        article = Article(title=title)
        article.save()

    return render(request, 'article.html', {'article': article, 'edit': True})


def save_article(request):
    title = request.GET['title']
    content = request.GET['content']
    article = Article.objects.get(title=title)
    article.content = content
    article.save()
    return redirect('show', title)


def create_article(request):
    return redirect('edit', request.GET['title'])

