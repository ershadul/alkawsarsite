from haystack.indexes import *
from haystack import site

from alkawsarsite.articles.models import Article

class ArticleIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

site.register(Article, ArticleIndex)