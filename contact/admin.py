from django.contrib import admin
from .models import Message, SocialMedia

# only show messages sent by the users
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'email_adress')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Message, MessageAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_media' ,'url')
admin.site.register(SocialMedia, SocialMediaAdmin)