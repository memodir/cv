# -*- coding: utf-8 -*-

from django.core import mail
from django.test import TestCase

from ..models import User


class UserTestCase(TestCase):

    def test_last_login_default(self):
        user1 = User.objects.create(email='user1@foo.com')
        self.assertIsNone(user1.last_login)

        user2 = User.objects.create_user(email='user2@foo.com')
        self.assertIsNone(user2.last_login)

    def test_user_clean_normalize_email(self):
        user = User(email='foo@BAR.com', password='foo')
        user.clean()
        self.assertEqual(user.email, 'foo@bar.com')

    def test_builtin_user_isactive(self):
        user = User.objects.create(email='foo@bar.com')
        # is_active is true by default
        self.assertIs(user.is_active, True)
        user.is_active = False
        user.save()
        user_fetched = User.objects.get(pk=user.pk)
        # the is_active flag is saved
        self.assertFalse(user_fetched.is_active)

    def test_email_user(self):
        # valid send_mail parameters
        kwargs = {
            "fail_silently": False,
            "auth_user": None,
            "auth_password": None,
            "connection": None,
            "html_message": None,
        }
        abstract_user = User(email='foo@bar.com')
        abstract_user.email_user(
            subject="Subject here",
            message="This is a message",
            from_email="from@domain.com",
            **kwargs
        )
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, "Subject here")
        self.assertEqual(message.body, "This is a message")
        self.assertEqual(message.from_email, "from@domain.com")
        self.assertEqual(message.to, [abstract_user.email])

