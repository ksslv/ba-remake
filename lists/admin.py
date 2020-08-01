from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    """
    All admin panel options and functionality for ListAdmin.
    """

    list_display = ("title", "user", "count_recipes")

    search_fields = ("title", "user")

    filter_horizontal = ("recipes",)
