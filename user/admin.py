from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'age_user')

    def name_user(self, obj):
        return f"{obj.name}"
    
    def age_user(self, obj):
        return f"{obj.age}"

    name_user.short_description = 'Nome do Usuário'
    age_user.short_description = 'Idade do Usuário'
admin.site.register(User, UserAdmin)