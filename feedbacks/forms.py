from django import forms

from alkawsarsite.feedbacks.models import Feedback

class FeedbackForm(forms.Form):
    name = forms.CharField(required=False, max_length=30)
    email = forms.EmailField(required=False)
    feedback = forms.CharField(required=True, max_length=512,
        error_messages={'required': 'Please enter your feedback'})
    user_id = forms.IntegerField(required=False)
    
    def clean_name(self):
        if self.user.id:
            return self.cleaned_data['name']
        else:
            if self.cleaned_data['name']:
                return self.cleaned_data['name']
            else:
                raise forms.ValidationError('Please enter your name')
    
    def clean_email(self):
        if self.user.id:
            return None
        if not self.cleaned_data.has_key('email'):
            raise forms.ValidationError('Please enter your email')
        elif self.cleaned_data['email'] == '':
            raise forms.ValidationError('Please enter your email')
        else:
            return self.cleaned_data['email']

