from django.contrib import admin
from .models import Publication, Text, Home, About, Contact, Message, Social_Media

class TextAdmin(admin.TabularInline):
    model = Text
admin.site.register(Text)

class PublicationAdmin(admin.ModelAdmin):
    inlines = [TextAdmin,]
    '''list_display = ('name_user', 'age_user')

    def name_user(self, obj):
        return f"{obj.name}"
    
    def age_user(self, obj):
        return f"{obj.age}"

    name_user.short_description = 'Nome do Usuário'
    age_user.short_description = 'Idade do Usuário'''
admin.site.register(Publication, PublicationAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')

admin.site.register(Home, HomeAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')

admin.site.register(About, AboutAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')

admin.site.register(Contact, ContactAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_adress')

admin.site.register(Message, MessageAdmin)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_media' ,'url')

admin.site.register(Social_Media, SocialMediaAdmin)