from random import randint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponse
from django.db.models import Max
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

    try:
        recipe = models.Recipe.objects.get(pk=pk)
        return render(request, "recipes/detail.html", context={"recipe": recipe})
    except models.Recipe.DoesNotExist:
        # TODO: create a separate custom 404 page and redirect there
        raise Http404("Recipe does not exist")
