from django.contrib import admin
from alkawsarsite.feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	search_fields = ['name', 'email', 'feedback']
	list_display = ('id', 'name', 'email', 'feedback', 'created_at',)

        class Media:
                js = ('/static/js/jquery-1.4.2.min.js',
                        '/static/js/tiny_mce/tiny_mce.js',
                        '/static/js/textareas.js',)

admin.site.register(Feedback, FeedbackAdmin)
