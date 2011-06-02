# section model

from django.db import models
from alkawsarsite.languages import *
from alkawsarsite import util
from alkawsarsite.contentcategories.models import ContentCategory

class PublishedSectionManager(models.Manager):
    def get_query_set(self):
        return super(PublishedSectionManager, self).get_query_set().filter(is_published=True)

class UnpublishedSectionManager(models.Manager):
    def get_query_set(self):
        return super(PublishedSectionManager, self).get_query_set().filter(is_published=False)

class Section(models.Model):
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    parent = models.ForeignKey('self', null=True, blank=True)
    contentcategory = models.ForeignKey(ContentCategory)
    
    title = models.CharField(max_length=128)
    slug_title = models.SlugField(max_length=128, blank=True, default='')
    tag_line = models.SlugField(max_length=256, blank=True, default='')
    
    description = models.CharField(max_length=2024, blank=True, default='')
    image = models.CharField(max_length=256, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_regular = models.BooleanField(default=False)
    
    order = models.IntegerField(default=1)
    n_clicks = models.IntegerField(default=0)
    n_comments = models.IntegerField(default=0)
    url = models.CharField(max_length=256, blank=True, default='')
    guid = models.CharField(max_length=40, blank=True, unique=True, db_index=True, default=util.get_uuid)
    
    objects = models.Manager()
    published_sections = PublishedSectionManager()
    unpublished_sections = UnpublishedSectionManager()

    class Meta:
        ordering = ['language', 'order']
    
    def __unicode__(self):
        return  self.title
    
    def get_absolute_url(self):
        return '/section/' + self.slug_title
    
    def save(self, force_insert=False, force_update=False):
        if Section.objects.filter(slug_title=self.slug_title, language=self.language).exclude(pk=self.id).count() == 0:
            return super(Section, self).save(force_insert=force_insert, force_update=force_update)
        else:
            raise Exception('Duplicate slug title !!!')