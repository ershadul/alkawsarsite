from django.http import *
from django.conf import settings
from django.http import *
from django.shortcuts import render_to_response

from alkawsarsite.articles.models import Article


def index(request):
    articles = Article.objects.filter(language=request.language, is_published=True).all()[0:10]
    #print len(articles)
    return render_to_response('english_layout.html',
       {
            'articles': articles,
            'language': request.language,
            'weblinks': request.weblinks,
            'tags': request.tags,
            'locals': request.locals,
            'user': request.user
       }
    )