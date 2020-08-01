from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ 
    Custom User model. 
    """

    CHEF_LVL_1 = "beginner"
    CHEF_LVL_2 = "home_cook"
    CHEF_LVL_3 = "pro"

    CHEF_LVL_CHOICES = (
        (CHEF_LVL_1, "Just starting out"),
        (CHEF_LVL_2, "Home cook"),
        (CHEF_LVL_3, "Professional"),
    )

    # Upload all profile photos to uploads/profile_photos; `uploads` is set is settings.py
    profile_photo = models.ImageField(upload_to="profile_photos", blank=True)
    bio = models.TextField(default="", blank=True)
    chef_level = models.CharField(choices=CHEF_LVL_CHOICES, max_length=20, blank=True)
    recipe_author = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

