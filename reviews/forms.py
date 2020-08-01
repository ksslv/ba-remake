from django import forms
from . import models


class AddReviewForm(forms.ModelForm):
    """
    A form for adding reviews to be used on the recipe detail page.
    """

    class Meta:
        model = models.Review
        fields = ("review_text", "rating")

        RATING_CHOICES = [(rating, rating) for rating in range(1, 6)]

        widgets = {
            "review_text": forms.Textarea(
                attrs={
                    "required": True,
                    "placeholder": "Write a review...",
                    "class": "p-4 border border-black",
                }
            ),
            "rating": forms.Select(attrs={"required": True}, choices=RATING_CHOICES,),
        }

