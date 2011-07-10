from django.db import models

from alkawsarsite.languages import *
from alkawsarsite import util

class Author(models.Model):
    name = models.CharField(max_length=255)
    slug_name = models.SlugField(max_length=255)
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    description = models.TextField(null=True, blank=True)
    short_introduction = models.CharField(max_length=1024, blank=True, default='')
    email = models.EmailField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True, default=1)

    class Meta:
        ordering = ['language', 'order']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/author/' + self.slug_name

    def save(self, force_insert=False, force_update=False):
        if Author.objects.filter(slug_name=self.slug_name, language=self.language).exclude(pk=self.id).count() != 0:
            raise Exception('Duplicate slug title !!!')
        return super(Author, self).save(force_insert=force_insert, force_update=force_update)