"""Tests for the forms of the ``feedback_form`` app."""
from django.core import mail
from django.test import TestCase

from mixer.backend.django import mixer

from ..forms import FeedbackForm
from ..models import Feedback


class FeedbackFormTestCase(TestCase):
    """Test for the ``FeedbackForm`` form class."""
    longMessage = True

    def test_form(self):
        data = {
            'feedback-email': 'test@example.com',
            'feedback-message': 'Foo',
            'feedback-url': 'http://www.example.com',
        }
        form = FeedbackForm(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(Feedback.objects.all().count(), 0)

        with self.settings(FEEDBACK_EMAIL_CONFIRMATION=True):
            # Valid post
            data.update({'feedback-url': ''})
            form = FeedbackForm(data=data)
            self.assertTrue(form.is_valid())
            form.save()
            self.assertEqual(len(mail.outbox), 1)
            self.assertEqual(Feedback.objects.count(), 1)
            self.assertEqual(Feedback.objects.all()[0].message, 'Foo')
            self.assertEqual(Feedback.objects.all()[0].email,
                             'test@example.com')

            # Valid post with user account
            user = mixer.blend('auth.User')
            data.update({'feedback-email': ''})
            form = FeedbackForm(data=data, user=user)
            self.assertTrue(form.is_valid())
            form.save()
            self.assertEqual(len(mail.outbox), 2)
            self.assertEqual(Feedback.objects.all().count(), 2)
            self.assertEqual(Feedback.objects.all()[0].message, 'Foo')
            self.assertEqual(Feedback.objects.all()[0].user, user)
