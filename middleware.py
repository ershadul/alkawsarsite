import sys
import os

from django.http import *
from django.conf import settings
from django.core import exceptions
from django.utils.encoding import smart_str

from alkawsarsite.languages import *
from alkawsarsite.sections.models import Section
from alkawsarsite.issues.models import Issue
from alkawsarsite import localization

class DomainMiddleware:
    """ Set subdomain attribute to request object. """
    
    def process_request(self, request):
        """Parse out the subdomain from the request"""
        subdomain = ''
        domain = ''
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        if len(host_s) > 2:
            subdomain = ''.join(host_s[:-2])
            domain = '.'.join(host_s[1:])
        else:
            domain = host
        
        if subdomain == 'mail':
            return HttpResponsePermanentRedirect('http://www.google.com/a/alkawsar.com')
        if subdomain == 'admin':
            setattr(request, 'urlconf', 'alkawsarsite.admin_urls')
        
        setattr(request, 'domain', domain)
        setattr(request, 'subdomain', subdomain)
        
        return None

class LanguageMiddleware(object):
    def process_request(self, request):
        if request.subdomain:
            if request.subdomain in ['mail', 'admin', 'en']:
                if request.subdomain == 'en':
                    request.language = 'english'
                    setattr(request, 'urlconf', 'alkawsarsite.en_urls')
                else:
                    request.language = default_language
            else:
                raise Http404
        else:
            request.language = default_language
        request.locals = getattr(localization, request.language)

class IssueMiddleware(object):
    def process_request(self, request):
        back_issues = []
        current_issue = None
        current_issue = Issue.objects.filter(
                                    is_published=True,
                                    is_default=True,
                                    language=request.language
                                ).all()[0:1].get()
        back_issues = Issue.objects.filter(
                                        is_published=True,
                                        is_default=False, 
                                        language=request.language
                                    ).all()
        request.current_issue = current_issue
        request.back_issues = back_issues
        return None