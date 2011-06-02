from django.db import models

# Content Model

class ContentCategory(models.Model):
    name = models.SlugField(max_length=50, db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.name
