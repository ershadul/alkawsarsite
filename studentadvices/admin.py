from django.contrib import admin
from alkawsarsite.studentadvices.models import StudentAdvice
from alkawsarsite.issues.models import Issue

class StudentAdviceAdmin(admin.ModelAdmin):
    search_fields = ['question', 'questioner', 'serial']
    list_filter = ('language', 'issue', 'is_published',)
    ordering = ['-issue']
    
    list_display = ('id', 'language', 'serial', 'questioner', 'address', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "issue":
            kwargs["queryset"] = Issue.objects.filter(language=request.language)
        return super(StudentAdviceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(StudentAdvice, StudentAdviceAdmin)
