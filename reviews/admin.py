from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Review Info", {"fields": ("recipe", "author", "rating", "review_text")}),
    )

    list_display = (
        "recipe",
        "author",
        "rating",
        "review_text",
    )

    list_filter = (
        "recipe",
        "author",
        "rating",
    )

