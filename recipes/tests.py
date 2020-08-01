from django.test import TestCase

# from django.urls import reverse
from django.contrib.auth import get_user_model
from . import models as recipe_models


class RecipeModelTests(TestCase):
    """ Class of tests to check the Recipe model """

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="test3", email="test3@test.com")
        self.recipe = recipe_models.Recipe.objects.create(
            title="Cookies 123",
            description="A lot of text, text, text.",
            ingredients="ingredient1, ingredient2",
            recipe_prep="instructions",
            author=self.user,
        )

    def tearDown(self):
        # Clean up testing database
        self.user.delete()
        self.recipe.delete()

    def test_recipe_model(self):
        self.assertEqual(f"{self.recipe.title}", "Cookies 123")
        self.assertEqual(f"{self.recipe.description}", "A lot of text, text, text.")
        self.assertEqual(f"{self.recipe.ingredients}", "ingredient1, ingredient2")
        self.assertEqual(f"{self.recipe.recipe_prep}", "instructions")
        self.assertEqual(f"{self.recipe.author}", self.user.username)

    def test_get_absolute_url(self):
        test_recipe = recipe_models.Recipe.objects.get(pk=1)
        self.assertEquals(test_recipe.get_absolute_url(), "/recipes/1")

    def test___str___(self):
        self.assertEqual(str(self.recipe), self.recipe.title)
