from django.shortcuts import render, redirect, reverse
from recipes import models as recipe_models
from . import forms


def add_review(request, recipe):
    """
    A view function to add a review to a recipe using reviews_forms.AddReviewForm().
    Returns a redirect to the recipe page. 
    """
    if request.method == "POST":
        form = forms.AddReviewForm(request.POST)

        recipe = recipe_models.Recipe.objects.get(pk=recipe)

        if form.is_valid():
            review = form.save(commit=False)
            # Update `author` and `recipe` fields
            review.recipe = recipe
            review.author = request.user
            review.save()

            return redirect(reverse("recipes:detail", kwargs={"pk": recipe.pk}))
