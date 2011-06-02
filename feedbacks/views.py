from django.shortcuts import render_to_response
from alkawsarsite.feedbacks.forms import FeedbackForm
from alkawsarsite.feedbacks.models import Feedback


def feedback(request):
    data = {}
    errors = {}
    
    message = ''
    successful = False
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = FeedbackForm(data)
        form.user = request.user
        if form.is_valid():
            feedback = Feedback()
            feedback.name = form.cleaned_data['name']
            feedback.email = form.cleaned_data['email']
            feedback.feedback = form.cleaned_data['feedback']
            if request.user.id:
                feedback.user = request.user
            feedback.save()
            successful = True
            message = 'ALHAMDULILLAH !, we\'ll look at your valuable suggestion or comment.'
        else:
            errors = form.errors
            
    return render_to_response('feedback.html', {
        'language': request.language,
        'user': request.user,
        'data': data,
        'errors': errors,
        'message': message,
        'successful': successful
    })

