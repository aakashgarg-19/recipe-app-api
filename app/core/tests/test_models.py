"""
Test for models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):
   """Test models."""

   def test_create_user_with_email_successful(self):
      """Test creating a user with an email is successful."""
      email = "test@example.com"
      password = "admin123"
      user = get_user_model().objects.create_user(
         email=email,
         password=password,
      )

      self.assertEqual(user.email, email)
      self.assertTrue(user.check_password(password))

   def test_new_user_email_normalized(self):
      """Test email is not normalized for new user."""
      sample_emails = [
         ['test1@EXAMPLE.com','test1@example.com'],
         ['Test2@example.com','Test2@example.com'],
         ['TEST3@EXAMPLE.COM','TEST3@example.com'],
         ['test4@example.COM','test4@example.com'],
      ]

      for email, excepted_email in sample_emails:
         user = get_user_model().objects.create_user(email, 'admin123')
         self.assertEqual(user.email, excepted_email)

   def test_new_user_without_email_raises_error(self):
      """Test that creating user without email raises a ValueError."""
      with self.assertRaises(ValueError):
         get_user_model().objects.create_user('', 'admin123')

   def test_create_superuser(self):
      """Test creating a superuser."""
      email = "test@example.com"
      password = "admin123"
      user = get_user_model().objects.create_superuser(
         email=email,
         password=password,
      )

      self.assertTrue(user.is_superuser)
      self.assertTrue(user.is_staff)

   def test_create_recipe(self):
      """Test creating a recipe is successful."""
      user = get_user_model().objects.create_user(
         "test@example.com",
         "admin123",
      )
      recipe = models.Recipe.objects.create(
         user = user,
         title = "Sample recipe name",
         time_minutes=5,
         price=Decimal("5.50"),
         description="Sample recipe description",
      )

      self.assertEqual(str(recipe), recipe.title)