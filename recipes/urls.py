from django.urls import path
from . import views


app_name = "recipes"

urlpatterns = [
    # ex: recipes/1
    path("<int:pk>", views.recipe_detail, name="detail"),
]
