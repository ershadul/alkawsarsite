from django.db import models
from django.utils.translation import ugettext_lazy as _

class ServerError(models.Model):
    """
    ServerError model will store all exception that occurs in a
    django project.
    """
    PRIORITY_LEVELS = (
        (1, _('High')),
        (2, _('Medium')),
        (3, _('Low')),
    )
    
    STATUS_TYPES = (
        (1, _('New')),
        (2, _('In progress')),
        (3, _('For review')),
        (4, _('Rework')),
        (5, _('Completed')),
        (6, _('Hold')),
    )
    
    title = models.CharField(max_length=255)
    error_type = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_LEVELS, default=1, db_index=True)
    status = models.IntegerField(choices=STATUS_TYPES, default=1, db_index=True)
    comment = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
