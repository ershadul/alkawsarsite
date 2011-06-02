from django.contrib import admin
from alkawsarsite.contentcategories.models import ContentCategory

class ContentCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at',)

admin.site.register(ContentCategory, ContentCategoryAdmin)
