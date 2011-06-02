
# studend advicing models

from django.db import models

from alkawsarsite.issues.models import Issue
from alkawsarsite.languages import *
from alkawsarsite import util

class StudentAdvice(models.Model):
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    issue = models.ForeignKey(Issue)
    questioner = models.CharField(max_length=128)
    address = models.CharField(max_length=128, null=True, blank=True)
    serial = models.CharField(max_length=12, null=True, blank=True)
    question = models.TextField()
    answer = models.TextField()
    references = models.CharField(max_length=2024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    guid = models.CharField(max_length=40, unique=True, db_index=True, default=util.get_uuid)
    
    class Meta:
        ordering = ['language', 'issue', 'serial']

    def __unicode__(self):
        return  self.question[0:100]
    