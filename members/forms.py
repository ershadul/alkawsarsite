from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """
    username = forms.RegexField(max_length=30, regex=r'^\w+$', min_length=6,
        error_messages={
                       'invalid': 'Username must contain only letters, numbers and underscores',
                       'required': 'Please enter your username'
    })
    password1 = forms.CharField(
        min_length=6,
        max_length=30,
        error_messages={'required': 'Enter your password',
                        'invalid': 'Enter minimum 6 characters'
    })
    password2 = forms.CharField(
        min_length=6,
        max_length=30,
        error_messages={'required': 'Re-enter your password'
    })
    email = forms.EmailField(required=True,
        error_messages={'required': 'Please enter your email address',
                        'invalid': 'Please enter a valid email address'
    })

    class Meta:
        model = User
        fields = ("username", "email", )

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists")
    
    def clean_email(self):
        email_address = self.cleaned_data["email"]
        try:
            User.objects.get(email=email_address)
        except User.DoesNotExist:
            return email_address
        raise forms.ValidationError("A user with that email alread exists")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    
    username = forms.RegexField(max_length=30, regex=r'^\w+$', min_length=6,
        error_messages={
                       'invalid': 'Username must contain only letters, numbers and underscores',
                       'required': 'Please enter your username'
    })
    password = forms.CharField(
        min_length=6,
        max_length=30,
        error_messages={'required': 'Enter your password',
                        'invalid': 'Enter minimum 6 characters'
    })
    
    
class PasswordRetrievalForm(forms.Form):
    email = forms.EmailField(required=True,
        error_messages={
            'required': 'Please enter your email address',
            'invalid': 'Please enter a valid email address'
    })
        
    def clean_email(self):
        email_address = self.cleaned_data["email"]
        try:
            User.objects.get(email=email_address)
            return email_address
        except User.DoesNotExist:
            raise forms.ValidationError("Sorry! we've not any user with this email.")