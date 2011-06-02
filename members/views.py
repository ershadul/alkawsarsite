# -*- coding: utf-8 -*-

from django.http import *
from django.shortcuts import *

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from alkawsarsite.members.forms import UserCreationForm, LoginForm, PasswordRetrievalForm
from alkawsarsite.members.models import UserProfile
from alkawsarsite.tags.models import Tag

def register(request):
    """
    Registers a new User
    """
    
    data = {}
    errors = None
    if request.method == 'POST':
        data = request.POST.copy()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception, e:
                pass
        else:
            errors = form.errors
            #print str(errors)
            
    return render_to_response('register.html', {'data': data, 'errors': errors})
    

def sign_in(request):
    
    data = {}
    errors = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = LoginForm(request.POST)
        if form.is_valid():
            user  = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                errors['username'] = 'You\'ve entered invalid username or password'
        else:
            errors = form.errors
    return render_to_response('sign-in.html', {'data': data, 'errors': errors})

@login_required
def sign_out(request):
    
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required  
def show_profile(request):
    return render_to_response('profile.html', {
        'user': request.user,
        'language': request.language,
        'locals': request.locals
    })

def change_password(request):
    data = {}
    errors = {}
    return render_to_response('change-password.html',
                              {'data': data,
                               'errors': errors
                               })

def retrieve_password(request):
    data = {}
    errors = {}
    if request.method == 'POST':
        data = request.POST.copy()
        form = PasswordRetrievalForm(data)
        if form.is_valid():
            user = User.objects.get(email=form.cleaned_data['email'])
            try:
                profile = user.userprofile
            except:
                profile = UserProfile(user=user)
            profile.set_resetpassword_key()
            profile.save()
            data['successful_msg'] = 'Your password reset link is on its way! Check your inbox for an email from us.'
        else:
            errors = form.errors
    return render_to_response('forgot-password.html',
        {
         'data': data,
         'errors': errors,
         'user': request.user,
         'locals': request.locals
         }
    )