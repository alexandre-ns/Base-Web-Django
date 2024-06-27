"""admin of CONTATO E MIDIAS SOCIAIS"""
from django.contrib import admin
from .models import Message, SocialMedia

class MessageAdmin(admin.ModelAdmin):
    """Visualization of messages sent by the users"""

    list_display = ('user_name', 'email_adress', 'sent_on')

    def has_add_permission(self, request):
        """No one is allowed to add"""
        return False

    def has_change_permission(self, request, obj=None):
        """No one is allowed to change"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Only super user can delete"""
        return request.user.is_superuser

admin.site.register(Message, MessageAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
    """Registration and viewing of social networks"""
    list_display = ('name', 'type_media' ,'url')

admin.site.register(SocialMedia, SocialMediaAdmin)
