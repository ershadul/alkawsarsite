from django.db import models

from alkawsarsite.languages import *

class Topic(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['language', 'name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/topic/%s" % str(self.id)
