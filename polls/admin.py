from django.contrib import admin
from .models import User, OlaroomProfile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", "username")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'country', 'twitter', 'website'
    )
admin.site.register(OlaroomProfile, ProfileAdmin)