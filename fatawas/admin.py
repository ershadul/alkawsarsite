from django.contrib import admin
from alkawsarsite.fatawas.models import Fatawa
from alkawsarsite.issues.models import Issue

def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = "Mark selected items as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_unpublished.short_description = "Mark selected items as unpublished"

class FatawaAdmin(admin.ModelAdmin):
    search_fields = ['headline', 'intro_text']
    ordering = ['-issue', 'serial']
    list_filter = ('language', 'is_published','issue',)
    actions = [make_published, make_unpublished]
    list_display = ('id', 'serial', 'language', 'issue', 'questioner', 'address', 'is_published', )
    list_editable = ('serial',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "issue":
            kwargs["queryset"] = Issue.objects.filter(language=request.language)
        return super(FatawaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(Fatawa, FatawaAdmin)
