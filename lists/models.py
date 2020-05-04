from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStampedModel):
    """ 
    List model definition. 
    
    "Groups" together a bunch of recipes.
    
    """

    title = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="lists", blank=True)

    def __str__(self):
        return self.title

    def count_recipes(self):
        # To be used and displayed on the admin panel.
        # count() call performs a SELECT COUNT(*) behind the scenes
        return self.recipes.count()

    count_recipes.short_description = "Recipes in a list"
