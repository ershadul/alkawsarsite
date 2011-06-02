from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail

class Question(models.Model):
    user =  models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=128)
    url = models.CharField(max_length=128, blank=True, default='')
    email = models.EmailField(max_length=128, blank=True, null=True)
    question = models.TextField()
    serial = models.CharField(default='', blank=True, max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    is_answered = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.get_questioner()
    
    def get_questioner(self):
        if self.user:
            return self.user.username
        else:
            return self.name
    
    def get_email(self):
        if self.user:
            return self.user.email
        else:
            return self.email
        
# Signal Handlers
def send_question_email(sender, **kwargs):
    # Try to send email
    if kwargs['created'] == True:
        try:
            question = kwargs['instance']
            send_mail(question.get_questioner(),
                      question.question,
                      question.get_email(),
                      [settings.QUESTION_EMAIL]
            )
        except Exception, e:
            pass
    
post_save.connect(send_question_email, sender=Question)