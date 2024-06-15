from django.contrib import admin
from .models import Publication, Image, Text, GenericContent


class GenericContentAdmin(admin.TabularInline):
    model = GenericContent
admin.site.register(GenericContent)

class ImageAdmin(admin.TabularInline):
    model = Image
admin.site.register(Image)

class TextAdmin(admin.TabularInline):
    model = Text
admin.site.register(Text)

class PublicationAdmin(admin.ModelAdmin):
    inlines = [GenericContentAdmin,]
    '''list_display = ('name_user', 'age_user')

    def name_user(self, obj):
        return f"{obj.name}"
    
    def age_user(self, obj):
        return f"{obj.age}"

    name_user.short_description = 'Nome do Usuário'
    age_user.short_description = 'Idade do Usuário'''
admin.site.register(Publication, PublicationAdmin)


'''class TextAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'age_user')

    def name_user(self, obj):
        return f"{obj.name}"
    
    def age_user(self, obj):
        return f"{obj.age}"

    name_user.short_description = 'Nome do Usuário'
    age_user.short_description = 'Idade do Usuário
admin.site.register(Text, TextAdmin)'''