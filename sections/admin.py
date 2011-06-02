from django.contrib import admin
from alkawsarsite.sections.models import Section

class SectionAdmin(admin.ModelAdmin):
    search_fields = ['title', 'tag_line', 'description']
    list_filter = ('language', 'contentcategory', 'is_published', 'is_regular',)
    ordering = ['order']
    
    list_display = ('id', 'language', 'title', 'slug_title', 'contentcategory', 'order', 'is_regular', 'is_published', )

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(Section, SectionAdmin)
