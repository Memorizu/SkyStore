from django.contrib import admin

from version.models import Version


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'is_active',)
    list_filter = ('product', 'is_active')