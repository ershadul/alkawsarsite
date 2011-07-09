import sys
import traceback

from django import http
from server_errors import utils


class ServerErrorMiddleware(object):
    """
    This middleware will catch exceptions and creates a entry in an existing
    error model.

    To install, be sure to place this middleware in the
    MIDDLEWARE_CLASSES setting in your settings file.
    """
    IGNORE_EXCEPTIONS = (http.Http404,)

    def process_exception(self, request, exception):
        # If this is an error we don't want to hear about, just return.
        if isinstance(exception, self.IGNORE_EXCEPTIONS) or \
                exception in self.IGNORE_EXCEPTIONS:
            return None
        
        try:
            error_type = exception.__class__.__name__
            title = str(exception)
            try:
                request_repr = repr(request)
            except:
                request_repr = "Request repr() unavailable"

            description = "{{{\n%s\n}}}\n\n{{{\n%s\n}}}" % \
                          (self._get_traceback(sys.exc_info()), request_repr)
            error = utils.create_server_error(title=title, \
                        description=description, error_type=error_type)
        except Exception, e:
            pass
        
        return   

    def _get_traceback(self, exc_info=None):
        """
        Helper function to return the traceback as a string.
        """
        return '\n'.join(traceback.format_exception(*(exc_info or \
                                                      sys.exc_info())))
