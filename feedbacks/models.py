from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail

class Feedback(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, default='')
    email = models.EmailField(null=True, blank=True, default='')
    feedback = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    
    
    def get_sender(self):
        if self.user:
            return self.user.username
        else:
            return self.name
    
    def __unicode__(self):
        return self.get_sender() +' says: "' + self.feedback[0:50] + '"'

# Signal Handlers
def send_feedback_email(sender, **kwargs):
    # Try to send email
    if kwargs['created'] == True:
        try:
            feedback = kwargs['instance']
            send_mail(feedback.name, feedback.feedback, feedback.email,
                      [settings.FEEDBACK_EMAIL])
        except Exception, e:
            pass
    
post_save.connect(send_feedback_email, sender=Feedback)