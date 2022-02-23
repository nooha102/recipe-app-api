from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email = "nooha@gmail.com"
        password = "password123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normalised(self):

        email = "nooha@GMAIL.COM"
        password = "password123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email.lower())


    def test_create_user_with_invalid_email(self):

        with self.assertRaises(ValueError):
            email = None
            password = "password123"
            get_user_model().objects.create_user(email=email, password=password)


    def test_create_superuser(self):

        user = get_user_model().objects.create_superuser("nooha@gmail.com", "pass123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)