from django import forms
from . import models


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("review_text", "rating")
