"""Tests for the views of the ``feedback_form`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin


class FeedbackCreateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``FeedbackCreateView`` generic view."""
    longMessage = True

    def setUp(self):
        self.user = UserFactory()

    def get_view_name(self):
        return 'feedback_form'

    def test_view(self):
        self.should_be_callable_when_anonymous()
        self.should_be_callable_when_authenticated(self.user)
