# -*- coding: utf-8 -*-

from django.test import TestCase

from ..models import User


class UserManagerTestCase(TestCase):

    def test_create_user(self):
        email = 'bar@foo.com'
        user = User.objects.create_user(email)
        self.assertEqual(user.email, email)
        self.assertFalse(user.has_usable_password())

    def test_empty_username(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(email='')

    def test_create_user_is_staff(self):
        email = 'foo@bar.com'
        user = User.objects.create_user(email, is_staff=True)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)

    def test_create_super_user_raises_error_on_false_is_superuser(self):
        with self.assertRaisesMessage(ValueError,
                                      'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                email='test@test.com', password='test', is_superuser=False)

    def test_create_superuser_raises_error_on_false_is_staff(self):
        with self.assertRaisesMessage(ValueError,
                                      'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                email='test@test.com', password='test', is_staff=False)
