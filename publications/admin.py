"""admin of PUBLICAÇÕES"""
from django.contrib import admin
from .models import Publication, Text, Sources

class TextAdmin(admin.TabularInline):
    """Texts of publications"""

    model = Text
admin.site.register(Text)


class SourcesAdmin(admin.TabularInline):
    """Sources of publications"""

    model = Sources
admin.site.register(Sources)


class PublicationAdmin(admin.ModelAdmin):
    """TextAdmin and SourcesAdmin allow the creation of posts, text, and sources in one place"""

    inlines = [TextAdmin, SourcesAdmin]

admin.site.register(Publication, PublicationAdmin)
