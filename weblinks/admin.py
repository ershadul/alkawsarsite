from django.contrib import admin
from alkawsarsite.weblinks.models import WebLink

class WebLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(WebLink, WebLinkAdmin)