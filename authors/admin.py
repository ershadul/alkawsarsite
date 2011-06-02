from django.contrib import admin
from alkawsarsite.authors.models import Author

class AuthorAdmin(admin.ModelAdmin):
        search_fields = ['name', 'email', 'guid']
	list_filter = ('language',)
	list_display = ('id', 'language', 'name', 'email', 'guid',)

        class Media:
                js = ('/static/js/jquery-1.4.2.min.js',
                      '/static/js/tiny_mce/tiny_mce.js',
                      '/static/js/textareas.js',)

admin.site.register(Author, AuthorAdmin)
