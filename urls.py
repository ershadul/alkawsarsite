from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'alkawsarsite.views.show404'
handler500 = 'alkawsarsite.views.show500'

urlpatterns = patterns('',
    # Example:
    # (r'^alkawsarsite/', include('alkawsarsite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
    
    #(r'^admin/', include(admin.site.urls)),

    (r'^feeds/', include('alkawsarsite.feeds.urls')),
    (r'^issues/archives', 'alkawsarsite.views.back_issues'),
    (r'^issue/(?P<year>\d+)/(?P<month>\d+)/section/question-answer', 'alkawsarsite.views.issue_fatawas'),
    (r'^issue/(?P<year>\d+)/(?P<month>\d+)/section/student-advicing', 'alkawsarsite.views.issue_advices'),
    (r'^issue/(?P<year>\d+)/(?P<month>\d+)/section/(?P<slug_title>[\w\-]+)', 'alkawsarsite.views.issue_section'),
    (r'^issue/(?P<year>\d+)/(?P<month>\d+)/', 'alkawsarsite.views.show_issue'),
    
    (r'^sections', 'alkawsarsite.views.all_sections'),
    (r'^section/question-answer', 'alkawsarsite.views.all_fatawas'),
    (r'^section/student-advicing', 'alkawsarsite.views.all_advices'),
    (r'^section/(?P<slug_title>[\w\-]+)', 'alkawsarsite.views.show_section'),
    
    (r'^authors$', 'alkawsarsite.views.show_authors'),
    (r'^author/(?P<slug_name>[\w\-]+)$', 'alkawsarsite.views.show_author'),

    (r'^topic/(?P<topic_id>\d+)', 'alkawsarsite.views.show_topic'),
    
    (r'^article/(?P<article_id>\d+)$', 'alkawsarsite.views.article'),
    (r'^article/(?P<article_id>\w+)/print$', 'alkawsarsite.views.article_print'),
    (r'^article/(?P<guid>\w+)$', 'alkawsarsite.views.show_article'),
    (r'^article/(?P<guid>\w+)/print$', 'alkawsarsite.views.show_article_print'),
    
    (r'^tag/(?P<slug_name>[\w\-]+)$', 'alkawsarsite.views.show_tag'),

    (r'^subscribe-agent$', 'alkawsarsite.views.subscribe_agent'),
    
    #(r'^member/register$', 'alkawsarsite.members.views.register'),
    #(r'^member/signin$', 'alkawsarsite.members.views.sign_in'),
    #(r'^member/signout$', 'alkawsarsite.members.views.sign_out'),
    #(r'^member/ask$', 'alkawsarsite.members.views.ask_question'),
    #(r'^member/profile/change-password$', 'alkawsarsite.members.views.change_password'),
    #(r'^member/profile$', 'alkawsarsite.members.views.show_profile'),
    #(r'^member/forgot-password$', 'alkawsarsite.members.views.retrieve_password'),
    
    (r'^feedback$', 'alkawsarsite.feedbacks.views.feedback'),
    (r'^ask_question$', 'alkawsarsite.views.ask_question'),
    
    (r'^language/change$', 'alkawsarsite.views.change_language'),
    (r'^contact_us$', 'alkawsarsite.views.contact'),
    (r'^about_us$', 'alkawsarsite.views.about_us'),
    (r'^help/font$', 'alkawsarsite.views.help_font'),
    
    (r'^english_version', 'django.views.generic.simple.direct_to_template', {'template': 'english_version.html'}),
    
	(r'^$', 'alkawsarsite.views.index'),
    
    #(r'', include('django.contrib.flatpages.urls')),
)
