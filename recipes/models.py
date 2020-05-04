from django.db import models
from django.urls import reverse
from core import models as core_models


class Recipe(core_models.TimeStampedModel):
    """ 
    Recipe model deifnition.

    Includes avg_rating(), cover_photo() methods that are used in admin panel and/or views.
    
    """

    title = models.CharField(max_length=140)
    description = models.TextField()
    ingredients = models.TextField()
    recipe_prep = models.TextField()
    author = models.ForeignKey(
        "users.User", related_name="recipe", on_delete=models.CASCADE
    )

    # TODO: finish tags
    # tags = models.ManyToManyField("Tag", related_name="recipe", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # To be used in URL reversals: reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
        # Makes sure urls are dynamic
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    def avg_rating(self):
        # Average the recipe rating across all Review inst's that have relation to a particular instance of Recipe model
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating

        if len(all_reviews) != 0:
            return round(all_ratings / len(all_reviews), 2)
        else:
            return None

    def cover_photo(self):
        # TODO: remove slicing if I'm only keeping one photo per recipe
        (photo,) = self.photos.all()[:1]
        return photo.file.url


# class Tag(core_models.TimeStampedModel):
#     pass


class Photo(core_models.TimeStampedModel):
    """
    Photo model definition.

    Associate added photos to the particular instance of Recipe.
    """

    description = models.CharField(max_length=140)
    file = models.ImageField(upload_to="recipe_photos")
    recipe = models.ForeignKey(
        "Recipe", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description
