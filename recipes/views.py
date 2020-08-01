from random import randint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponse
from django.db.models import Max
from reviews import forms as review_forms
from reviews import models as review_models
from . import models


def all_recipes(request):
    """
    Produces a list of all added recipes with pagination; 3 recipes per page. 

    Returns an HttpResponse to a request.
    """

    recipes = models.Recipe.objects.all()
    paginator = Paginator(object_list=recipes, per_page=3)
    page = request.GET.get("page")
    recipes = paginator.get_page(number=page)

    return render(request, "recipes/home.html", context={"recipes": recipes})


def recipe_detail(request, pk):
    """
    Serves a particular recipe to the recipes/detail page.

    Returns an HttpResponse.
    """

    # Check for wheter current user has already reviewed a recipe
    if request.user.is_authenticated:
        has_reviewed = review_models.Review.objects.filter(
            author=request.user, recipe=pk
        ).exists()
    else:
        has_reviewed = False

    # "Leave a review" form to be passed to context dict
    review_form = review_forms.AddReviewForm()

    try:
        recipe = models.Recipe.objects.get(pk=pk)
        return render(
            request,
            "recipes/detail.html",
            context={
                "recipe": recipe,
                "review_form": review_form,
                "has_reviewed": has_reviewed,
            },
        )
    except models.Recipe.DoesNotExist:
        # TODO: create a separate custom 404 page and redirect there
        raise Http404("Recipe does not exist")
