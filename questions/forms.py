from django import forms

class QuestionForm(forms.Form):
    name = forms.CharField(max_length=128)
    url = forms.URLField(required=False, max_length=128, verify_exists=False)
    email = forms.EmailField(max_length=128)
    question = forms.CharField()
    