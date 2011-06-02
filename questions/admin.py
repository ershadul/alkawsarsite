from django.contrib import admin

from alkawsarsite.questions.models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'question', 'serial']
    list_filter = ('is_answered',)
    list_display = ('id', 'name', 'email', 'question', 'is_answered', 'serial',)

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(Question, QuestionAdmin)
