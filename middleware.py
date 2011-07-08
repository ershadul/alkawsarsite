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

class ServerErrorMiddleware(object):
    """ This middleware will catch exceptions and creates a ticket in an existing
error model

To install, be sure to place this middleware near the beginning
of the MIDDLEWARE_CLASSES setting in your settings file.
This will make sure that it doesn't accidentally catch errors
you were meaning to catch with other middleware.
"""
    IGNORE_EXCEPTIONS = (Http404,)

    def process_exception(self, request, exception):
        # If this is an error we don't want to hear about, just return.
        if isinstance(exception, self.IGNORE_EXCEPTIONS) or \
                exception in self.IGNORE_EXCEPTIONS:
            return
        
        try:
            error_data = {}
            error_data['type'] = exception.__class__.__name__
            error_data['message'] = str(exception)
            try:
                request_repr = repr(request)
            except:
                request_repr = "Request repr() unavailable"
            
            description = "{{{\n%s\n}}}\n\n{{{\n%s\n}}}" % (self._get_traceback(sys.exc_info()), request_repr)
            
            error_data['description'] = description
            
            setattr(request, 'error_data', error_data)
        except Exception, e:
            pass
        
        return

    def _get_traceback(self, exc_info=None):
        "Helper function to return the traceback as a string"
        import traceback
        return '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))