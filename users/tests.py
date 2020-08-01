from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# from django.core.files.uploadedfile import SimpleUploadedFile
from . import forms
from . import views
from . import models


class CustomUserTests(TestCase):
    """
    Tests for custom user creation.
    """

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testadmin", email="test@admin.com", password="assdjf"
        )

        self.assertEqual(admin_user.username, "testadmin")
        self.assertEqual(admin_user.email, "test@admin.com")

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="test", email="test@test.com")

        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@test.com")

        self.assertTrue(user.is_active)

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


class CustomUserModelTests(TestCase):
    """
    Tests for the custom user model.
    """

    def setUp(self):
        # Create test user and recipe
        User = get_user_model()
        self.user = User.objects.create_user(
            username="test3", email="test3@test.com", recipe_author=False
        )

    def test_get_absolute_url(self):
        test_user = models.User.objects.get(pk=1)
        self.assertEquals(test_user.get_absolute_url(), "/users/1/")


class RegistrationPageTests(TestCase):
    def setUp(self):
        url = reverse("users:register")
        self.response = self.client.get(url)
        self.username = "newuser"
        self.email = "newuser@email.com"

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "users/register.html")
        self.assertContains(self.response, "Register")
        self.assertNotContains(self.response, "Should not be on this page")

    def test_registration_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, forms.RegistrationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_register_view(self):
        view = resolve("/users/signup")
        self.assertEqual(view.func.__name__, views.register.__name__)

