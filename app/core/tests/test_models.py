from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successfully"""
        email = 'test@wherever.com'
        password = 'testPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test that the email is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email=email, password=None)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test that the user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password=None)

    def test_create_new_superuser(self):
        """creating a new super user"""

        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123')
        self.assertTrue(user.is_superuser)
        # is_superuser is included as part of the permissionsMixin
        self.assertTrue(user.is_staff)
