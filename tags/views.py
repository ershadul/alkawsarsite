# Create your views here.
from django.http import *
from django.shortcuts import *

from alkawsarsite.tags.models import *

def show(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
        articles = tag.article_set.all()
    except:
        return HttpResponseNotFound()
    
    return render_to_response('tag_page.html', 
        {
            'tag': tag,
            'articles': articles
        }
    )
