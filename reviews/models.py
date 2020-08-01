from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """
    Review model deifnition.
    """

    review_text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    date_posted = core_models.TimeStampedModel.created
    author = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        "recipes.Recipe", related_name="reviews", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.recipe} POSTED BY {self.author}: {self.review_text}"
