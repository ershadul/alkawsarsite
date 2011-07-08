
# fatawa models

from django.db import models
from alkawsarsite.issues.models import Issue

from alkawsarsite.languages import *

class Fatawa(models.Model):
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    issue = models.ForeignKey(Issue)
    serial = models.CharField(max_length=40, unique=True, db_index=True)
    questioner = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True, default='')
    question = models.TextField()
    answer = models.TextField()
    references = models.CharField(max_length=2024, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['language', '-serial']

    def __unicode__(self):
        return  self.serial
    
