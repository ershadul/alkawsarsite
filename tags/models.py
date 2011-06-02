from django.db import models

from alkawsarsite.languages import *

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug_name = models.SlugField(max_length=50, default='', blank=True)
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    is_published = models.BooleanField(default=True)
    total_ref = models.IntegerField(default=0, blank=True)
    font_size = models.FloatField(default=0, blank=True)
    
    
    class Meta:
        ordering = ['language', 'name']
        
    def __unicode__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False):
        if Tag.objects.filter(slug_name=self.slug_name, language=self.language).exclude(pk=self.id).count() != 0:
            raise Exception('Duplicate slug title !!!')
        return super(Tag, self).save(force_insert=force_insert, force_update=force_update)
