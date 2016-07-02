from django.contrib import admin

from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'name', 'hits', 'redirect_url')
    list_filter = ('created',)
    search_fields = ('url', 'name', 'redirect_url')
