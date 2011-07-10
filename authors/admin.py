from django.contrib import admin
from alkawsarsite.authors.models import Author

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_filter = ('language',)
    list_display = ('id', 'language', 'name', 'email', 'order',)
    list_editable = ('order',)

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(Author, AuthorAdmin)
