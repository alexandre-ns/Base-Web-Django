from django.contrib import admin
from .models import Home, About, Contact

# Remember that for the correct display on the site it is necessary that there is at least one page of each with the "active" True field

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
admin.site.register(Home, HomeAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
admin.site.register(About, AboutAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
admin.site.register(Contact, ContactAdmin)

