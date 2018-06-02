from django.http import Http404
from django.shortcuts import render
from home.models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'home/index.html', context={'articles': articles})

def detail(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        raise Http404
    # article = get_object_or_404(Article, pk=id)
    return render(request, 'home/article.html', context={'article': article})
