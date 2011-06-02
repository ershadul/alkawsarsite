from django.conf.urls.defaults import *
from alkawsarsite.feeds.feed import RssIssueArticleFeed, AtomIssueArticleFeed

feeds = {
    'rss': RssIssueArticleFeed,
    'atom': AtomIssueArticleFeed,
}

urlpatterns = patterns('',
    (r'^rss/$', 'alkawsarsite.feeds.views.rss'),
    (r'^atom/$', 'alkawsarsite.feeds.views.atom'),
)