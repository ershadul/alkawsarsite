from django.contrib import admin
from alkawsarsite.tags.models import Tag

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug_name']
    list_filter = ('language', 'is_published',)
    ordering = ['name']
    
    list_display = ('id', 'language', 'name', 'slug_name', 'total_ref', 'font_size',)

    class Media:
        js = ('/media/js/jquery-1.4.2.min.js',
              '/media/js/tiny_mce/tiny_mce.js',
              '/media/js/textareas.js',)

admin.site.register(Tag, TagAdmin)
