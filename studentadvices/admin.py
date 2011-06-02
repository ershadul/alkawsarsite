from django.contrib import admin
from alkawsarsite.studentadvices.models import StudentAdvice

class StudentAdviceAdmin(admin.ModelAdmin):
    search_fields = ['question', 'questioner', 'serial']
    list_filter = ('language', 'issue', 'is_published',)
    ordering = ['-issue']
    
    list_display = ('id', 'language', 'serial', 'questioner', 'address', )

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(StudentAdvice, StudentAdviceAdmin)
