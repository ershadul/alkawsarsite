from django.conf.urls.defaults import *
from django.conf import settings

handler404 = 'alkawsarsite.views.show404'
handler500 = 'alkawsarsite.views.show500'

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
    (r'^authors$', 'alkawsarsite.views.show_authors'),
    (r'^author/(?P<slug_name>[\w\-]+)$', 'alkawsarsite.views.show_author'),
    (r'^feedback$', 'alkawsarsite.feedbacks.views.feedback'),
    (r'^ask_question$', 'alkawsarsite.views.ask_question'),
    (r'^contact_us$', 'alkawsarsite.views.contact'),
    (r'^about_us$', 'alkawsarsite.views.about_us'),
    (r'^$', 'alkawsarsite.english_views.index'),
)