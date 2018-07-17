# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.test import TestCase, modify_settings

from ..models import User


class EmailAuthBackendTest(TestCase):
    """
    Tests for the EmailAuthBackend using the customized User model.
    """
    backend = 'myaccount.authentication.EmailAuthBackend'

    UserModel = User

    user_credentials = {'email': 'test@bar.com', 'password': 'test'}

    def setUp(self):
        self.patched_settings = modify_settings(
            AUTHENTICATION_BACKENDS={'append': self.backend},
        )
        self.patched_settings.enable()
        self.user = User.objects.create_user(**self.user_credentials)
        self.superuser = User.objects.create_superuser(
            email='admin@example.com',
            password='test',
        )

    def tearDown(self):
        self.patched_settings.disable()

    def test_authenticate_inactive(self):
        # normal active user can authenticate successfully
        self.assertEqual(authenticate(**self.user_credentials), self.user)

        # An inactive user can't authenticate.
        self.user.is_active = False
        self.user.save()
        self.assertIsNone(authenticate(**self.user_credentials))
