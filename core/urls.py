from django.urls import path
from recipes import views as recipe_views

app_name = "core"

urlpatterns = [path("", recipe_views.all_recipes, name="home")]
