from django.contrib import admin
from alkawsarsite.topics.models import Topic

class TopicAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_filter = ['language']
    ordering = ['name']
    
    list_display = ('id', 'language', 'name',)

    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
              '/media/js/tiny_mce/tiny_mce.js',
              '/media/js/textareas.js',)

admin.site.register(Topic, TopicAdmin)
