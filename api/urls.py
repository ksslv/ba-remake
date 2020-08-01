from django.urls import path, include
from .views import RecipeAPIView, RecipeDetailAPIView, UserAPIView

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", RecipeAPIView.as_view()),
    path("recipes/<int:pk>/", RecipeDetailAPIView.as_view()),
    path("users/", UserAPIView.as_view()),
]

