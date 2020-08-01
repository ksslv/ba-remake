from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup", views.register, name="register"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]
