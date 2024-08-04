from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
 
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_banned')
 
    def is_banned(self, obj):
        return not obj.is_active
 
    is_banned.boolean = True
 
    def ban_users(modeladmin, request, queryset):
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can ban users.")
        queryset.update(is_active=False)
 
    ban_users.short_description = "Ban selected users"
 
    actions = [ban_users]
 
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Website)
admin.site.register(Username)
admin.site.register(TaoPian)