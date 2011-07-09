from alkawsarsite.feedbacks.models import Feedback

from django.conf import settings
from django.core.mail import send_mail

def email_feedbacks():
    feedbacks = Feedback.objects.all()
    for feedback in feedbacks:
        print feedback.id, feedback.get_sender()
        try:
            send_mail(feedback.name, feedback.feedback, feedback.email,
                      [settings.FEEDBACK_EMAIL])
        except Exception, e:
            #print e
            pass