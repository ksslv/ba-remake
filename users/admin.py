from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ 
    Customizing the User admin.
    
    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom User Profile",
            {"fields": ("profile_photo", "bio", "chef_level", "recipe_author")},
        ),
    )

    list_filter = UserAdmin.list_filter + ("recipe_author",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "chef_level",
        "recipe_author",
        "is_staff",
        "is_superuser",
    )
