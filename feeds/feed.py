# -*- coding: utf-8 -*-

from alkawsarsite.issues.models import Issue
from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from alkawsarsite.languages import *

class RssIssueArticleFeed(Feed):
    title = u'মাসিক আলকাউসার - চলতি সংখ্যা'
    link = "http://www.alkawsar.com"
    description = "গবেষণামূলক উচ্চতর শিক্ষাপ্রতিষ্ঠান মারকাযুদ্ দাওয়াহ আলইসলামিয়া ঢাকা-এর মুখপত্র"

    def items(self):
        return Issue.objects.get(is_default=True, is_published=True, 
                language=default_language).article_set.filter(is_published=True).all()

class AtomIssueArticleFeed(RssIssueArticleFeed):
    feed_type = Atom1Feed
    subtitle = RssIssueArticleFeed.description