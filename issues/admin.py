from django.contrib import admin
from alkawsarsite.issues.models import Issue

class IssueAdmin(admin.ModelAdmin):
    search_fields = ['title', 'year', 'month', 'issue_year', 'issue_number']
    list_filter = ('language', 'year', 'month', 'is_published',)
    ordering = ['-year']
    exclude = ['url', 'guid']
    list_display = ('id', 'language', 'title', 'title_alias', 'is_published', 'year', 'month',)
    list_editable = ('title', 'title_alias', 'is_published', 'year', 'month',)


    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(Issue, IssueAdmin)
