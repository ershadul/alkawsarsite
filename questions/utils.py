import datetime
from alkawsarsite.questions.models import Question

from django.conf import settings
from django.core.mail import send_mail

def email_questions():
    questions = Question.objects.filter(is_answered=False).order_by('id').all()
    for question in questions:
        print question.id, question.get_email()
        try:
            send_mail(question.get_questioner(),
                      question.question,
                      question.get_email(),
                      [settings.QUESTION_EMAIL]
            )
        except Exception, e:
            print e


def export_questions():
    questions = Question.objects.filter(is_answered=False).all()
    string = u''
    for q in questions:
        string += 'ID: %s, Name: %s, Email: %s, Submitted at: %s\nQuestion: %s\n\n' % (q.id, q.name, q.email, str(q.created_at), q.question)

    today = datetime.date.today()
    file_obj = open('questions/%s.txt' % str(today), 'w')
    file_obj.write(string.encode('UTF-8'))
    file_obj.close()
        