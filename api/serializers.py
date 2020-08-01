from rest_framework import serializers
from recipes.models import Recipe
from users.models import User


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "description",
            "ingredients",
            "recipe_prep",
            "author",
            "avg_rating",
            "cover_photo",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "bio",
            "profile_photo",
            "recipe_author",
            "chef_level",
        )
