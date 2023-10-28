from django.contrib import admin

from .models import UserProfile, Role

# Register your models here.
admin.site.register(Role)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('email__startswith',)

    def display_roles(self, obj):
        return ", ".join([role.name for role in obj.roles.all()])
    display_roles.short_description = "Roles"
