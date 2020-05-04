from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class CustomUserTests(TestCase):
    """
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
