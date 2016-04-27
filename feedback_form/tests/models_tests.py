"""Tests for the models of the ``feedback_form`` app."""
from django.test import TestCase

from mixer.backend.django import mixer


class FeedbackTestCase(TestCase):
    """Tests for the ``Feedback`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test if the ``Feedback`` model instantiates."""
        feedback = mixer.blend('feedback_form.Feedback')
        self.assertTrue(str(feedback))
        feedback = mixer.blend('feedback_form.Feedback',
                               user=mixer.blend('auth.User'))
        self.assertTrue(str(feedback))
        feedback = mixer.blend('feedback_form.Feedback', email='')
        self.assertTrue(str(feedback))
