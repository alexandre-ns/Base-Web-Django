from django.contrib import admin
from .models import Publication, Text, Sources

class TextAdmin(admin.TabularInline):
    model = Text
admin.site.register(Text)

class SourcesAdmin(admin.TabularInline):
    model = Sources
admin.site.register(Sources)

# TextAdmin and SourcesAdmin allow the creation of posts, text, and sources in one place
class PublicationAdmin(admin.ModelAdmin):
    inlines = [TextAdmin, SourcesAdmin]

admin.site.register(Publication, PublicationAdmin)
