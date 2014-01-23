"""Tests for the views of the ``feedback_form`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from ..models import Feedback


class FeedbackCreateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``FeedbackCreateView`` generic view."""
    def setUp(self):
        self.user = UserFactory()

    def get_view_name(self):
        return 'feedback_form'

    def test_view(self):
        self.should_be_callable_when_anonymous()
        self.should_be_callable_when_authenticated(self.user)
        data = {'feedback-message': 'Foo'}
        self.is_callable(method='post', data=data)
        self.assertEqual(Feedback.objects.all().count(), 1)
        self.assertEqual(Feedback.objects.all()[0].message, 'Foo')
        self.assertEqual(Feedback.objects.all()[0].current_url, '/feedback/')

        # Test AJAX
        self.is_callable(method='post', data=data, ajax=True)
        self.is_callable(ajax=True)


class FeedbackCreateViewContentObjectTestCase(ViewTestMixin, TestCase):
    """
    Tests for the ``FeedbackCreateView`` generic view, if using a content
    object.

    """
    def setUp(self):
        self.user = UserFactory()
        self.content_object = UserFactory()

    def get_view_name(self):
        return 'feedback_form_content_object'

    def get_view_kwargs(self):
        return {
            'c_type': ContentType.objects.get_for_model(
                self.content_object).model,
            'obj_id': self.content_object.pk,
        }

    def test_view(self):
        self.should_be_callable_when_anonymous()
        self.should_be_callable_when_authenticated(self.user)
        self.is_not_callable(kwargs={'c_type': 'foo', 'obj_id': '999'})
        self.is_not_callable(kwargs={
            'c_type': ContentType.objects.get_for_model(
                self.content_object).model,
            'obj_id': '999',
        })
        data = {'feedback-message': 'Foo'}
        self.is_callable(method='post', data=data)
        self.assertEqual(Feedback.objects.all().count(), 1)
        self.assertEqual(Feedback.objects.all()[0].message, 'Foo')
        self.assertEqual(
            Feedback.objects.all()[0].content_object, self.content_object)
