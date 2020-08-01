from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    """
    Inline configuration for Django's admin on the Photo model.
    """

    model = models.Photo


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ 
    Admin panel options and functionality for the Recipe model.
    """

    # Automatically gathers all photos that have an FK to *this* Recipe instance
    inlines = [
        PhotoInline,
    ]

    fieldsets = (
        ("Recipe Post Info", {"fields": ("title", "author", "description")},),
        ("Recipe Post Body", {"fields": ("ingredients", "recipe_prep")}),
    )

    list_display = (
        "title",
        "author",
        "avg_rating",
        "description",
        "ingredients",
        "recipe_prep",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ 
    Admin panel options and functionality for the Photos model.
    """

    list_display = ("description", "recipe", "get_preview")

    def get_preview(self, obj):
        return mark_safe(f'<img width="40px" src="{obj.file.url}" />')

    get_preview.short_description = "Preview"
