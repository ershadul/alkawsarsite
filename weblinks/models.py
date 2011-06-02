from django.db import models

from alkawsarsite.languages import *

class WebLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    is_published = models.BooleanField(default=True)
    
    
    class Meta:
        ordering = ['language']
    
    def __unicode__(self):
        return self.title
