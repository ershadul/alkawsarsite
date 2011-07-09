from django.contrib import admin

from server_errors.models import ServerError

class ServerErrorAdmin(admin.ModelAdmin):
    search_fields = ['title', 'error_type', 'description']
    date_hierarchy = 'created_at'
    list_display = ('title', 'error_type', 'priority', 'status', \
                    'created_at', 'comment',)
    ordering = ['-created_at']
    list_filter = ('error_type', 'priority', 'status',)

admin.site.register(ServerError, ServerErrorAdmin)