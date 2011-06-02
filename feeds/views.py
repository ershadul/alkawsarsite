# -*- coding: utf-8 -*-

from django.http import *
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.feedgenerator import Atom1Feed

from alkawsarsite.issues.models import Issue

def rss(request, issue=None):
    issue = Issue.objects.get(is_default=True, is_published=True, 
                language=request.language)
    articles = issue.article_set.filter(is_published=True).all()
    
    feed = Rss201rev2Feed(title=request.locals['magazine_name'] + u' - ' + issue.title + u' ' + request.locals['number'], 
            link=u'http://' + request.get_host() + request.get_full_path(), description=request.locals['magazine_slogan'])
    for article in articles:
        feed.add_item(title=article.headline, 
            link=u'http://' + request.get_host() + article.get_absolute_url(),
            description=article.intro_text,
            pubdate=article.created_at,
            unique_id=article.guid)
    return HttpResponse(feed.writeString('UTF-8'), mimetype='application/rss+xml')

def atom(request, issue=None):
    issue = Issue.objects.get(is_default=True, is_published=True, 
                language=request.language)
    articles = issue.article_set.filter(is_published=True).all()
    
    feed = Atom1Feed(title=request.locals['magazine_name'] + u' - ' + issue.title + u' ' + request.locals['number'], 
            link=u'http://' + request.get_host() + request.get_full_path(), 
            description=request.locals['magazine_slogan'],
            subtitle=request.locals['magazine_slogan'])
    for article in articles:
        feed.add_item(title=article.headline, 
            link=u'http://' + request.get_host() + article.get_absolute_url(),
            description=article.intro_text,
            pubdate=article.created_at,
            unique_id=article.guid)
    return HttpResponse(feed.writeString('UTF-8'), mimetype='application/atom+xml')

    