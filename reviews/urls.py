from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [path("add/<int:recipe>", views.add_review, name="add")]
