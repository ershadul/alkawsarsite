# -*- coding: utf-8 -*-

# article model
from django.db import models

from alkawsarsite.languages import *
from alkawsarsite.authors.models import Author
from alkawsarsite.sections.models import Section
from alkawsarsite.issues.models import Issue
from alkawsarsite import util
from alkawsarsite.topics.models import Topic


class DeferredBodyTextManager(models.Manager):
    def get_query_set(self):
        return super(DeferredBodyTextManager, self).get_query_set().defer('body_text')
    
class Article(models.Model):
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    issue = models.ForeignKey(Issue)
    section = models.ForeignKey(Section, null=True, blank=True)
    topics = models.ManyToManyField(Topic, null=True, blank=True)
    
    authors = models.ManyToManyField(Author, blank=True, related_name='article_set')
    author_name = models.CharField(max_length=256, blank=True, default='')
    author_description = models.CharField(max_length=256, default='', blank=True)
    
    headline = models.CharField(max_length=256)
    slug_headline = models.SlugField(max_length=256, blank=True, default='')
    
    intro_text = models.CharField(max_length=2024, default='', blank=True)
    highlighted_text = models.CharField(max_length=1024, null=True, blank=True)
    body_text = models.TextField()
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    
    url = models.CharField(max_length=256, blank=True, default='')
    guid = models.CharField(max_length=40, blank=True, unique=True, db_index=True, default=util.get_uuid)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    is_published = models.BooleanField(default=False)
    n_clicks = models.IntegerField(default=0)
    n_comments = models.IntegerField(default=0)
    
    objects = DeferredBodyTextManager()

    class Meta:
        ordering = ['language', 'issue']
        
    def get_authors_link(self):
        link = ''
        if self.authors.count() > 1:
            for author in self.authors.all():
                link = link + '<span><a href="' + author.get_absolute_url() + '">' + author.name + '</a></span>'
        else:
            for author in self.authors.all():
                link = link + '<span><a href="' + author.get_absolute_url() + '">' + author.name + '</a></span>'  
        if not link:
            link = self.author_name
        if link:
            if self.language == 'english':
                return '<p class="byline">' + link + '</p>'
            else:
                return u'<p class="byline">' + unicode(link) + u'</p>'
        else:
            return link

    def get_authors(self):
        link = ''
        if self.authors.count() > 1:
            for author in self.authors.all():
                link = link + '<span><a href="' + author.get_absolute_url() + '">' + author.name + '</a></span>'
        else:
            for author in self.authors.all():
                link = link + '<span><a href="' + author.get_absolute_url() + '">' + author.name + '</a></span>'
        if not link:
            link = u'<span>%s</span>' % self.author_name
        return link

    def get_absolute_url(self):
        return "/article/" + str(self.id)
    
    def get_issue_section_url(self):
        if self.section:
            return '/issue/' + str(self.issue.year) + '/' + str(self.issue.month) + self.section.get_absolute_url()

    def __unicode__(self):
        return self.headline
	

	
