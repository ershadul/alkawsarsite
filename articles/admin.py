from django.contrib import admin
from alkawsarsite.articles.models import Article

def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = "Mark selected items as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_unpublished.short_description = "Mark selected items as unpublished"

def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)
make_featured.short_description = "Mark selected items as featured"

def make_not_featured(modeladmin, request, queryset):
    queryset.update(is_featured=False)
make_not_featured.short_description = "Mark selected items as not featured"

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['headline', 'intro_text', 'body_text']
    list_filter = ('language', 'is_featured', 'is_published', 'issue',)
    ordering = ['-id']
    exclude = ['author_description', 'slug_headline', 'highlighted_text', 'n_comments', 'n_clicks', 'tags', 'url', 'guid']
    actions = [make_published, make_unpublished, make_featured, make_not_featured]
    list_display = ('id', 'headline', 'issue', 'is_featured', 'is_published', 'order', 'n_clicks',)
    list_editable = ('headline', 'is_published', 'is_featured', 'order',)
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('language', 'issue', 'section',)
        }),
        ('Article\'s Content options', {
            'fields': ('headline', 'intro_text', 'body_text',)
        }),
        ('Author(s)', {
            'fields': ('author_name', 'authors',)
        }),
        ('Advanced Options', {
            'fields': ('is_published', 'order', 'is_featured',)
        }),
    )

    class Media:
        js = ('/static/js/jquery-1.4.2.min.js',
              '/static/js/tiny_mce/tiny_mce.js',
              '/static/js/textareas.js',)

admin.site.register(Article, ArticleAdmin)
