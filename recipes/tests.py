from django.test import TestCase

# from django.urls import reverse
from django.contrib.auth import get_user_model
from . import models as recipe_models

# Create your tests here.
class RecipeTests(TestCase):
    def setUp(self):
        # Create test user and recipe
        User = get_user_model()
        self.user = User.objects.create_user(username="test3", email="test3@test.com")
        self.recipe = recipe_models.Recipe.objects.create(
            title="Cookies 123",
            description="A lot of text, text, text.",
            ingredients="ingredient1, ingredient2",
            recipe_prep="instructions",
            author=self.user,
        )

    def test_recipe(self):
        # Test recipe creation
        self.assertEqual(f"{self.recipe.title}", "Cookies 123")
        self.assertEqual(f"{self.recipe.description}", "A lot of text, text, text.")
        self.assertEqual(f"{self.recipe.ingredients}", "ingredient1, ingredient2")
        self.assertEqual(f"{self.recipe.recipe_prep}", "instructions")
        self.assertEqual(f"{self.recipe.author}", self.user.username)

    def tearDown(self):
        # Clean up testing database
        self.user.delete()
        self.recipe.delete()
