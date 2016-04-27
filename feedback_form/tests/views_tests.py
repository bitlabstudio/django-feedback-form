"""Tests for the views of the ``feedback_form`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import views
from ..models import Feedback


class FeedbackCreateViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``FeedbackCreateView`` generic view."""
    view_class = views.FeedbackCreateView

    def setUp(self):
        self.user = mixer.blend('auth.User')

    def test_view(self):
        self.is_callable()
        self.is_callable(user=self.user)
        data = {'feedback-message': 'Foo'}
        self.is_postable(user=self.user, data=data,
                         to_url_name='feedback_form')
        self.assertEqual(Feedback.objects.all().count(), 1)
        self.assertEqual(Feedback.objects.all()[0].message, 'Foo')
        self.assertEqual(Feedback.objects.all()[0].current_url, '/')
        self.is_callable(ajax=True)


class FeedbackCreateViewContentObjectTestCase(ViewRequestFactoryTestMixin,
                                              TestCase):
    """
    Tests for the ``FeedbackCreateView`` generic view, if using a content
    object.

    """
    view_class = views.FeedbackCreateView

    def setUp(self):
        self.user = mixer.blend('auth.User')
        self.content_object = mixer.blend('auth.User')

    def get_view_name(self):
        return 'feedback_form_content_object'

    def get_view_kwargs(self):
        return {
            'c_type': ContentType.objects.get_for_model(
                self.content_object).model,
            'obj_id': self.content_object.pk,
        }

    def test_view(self):
        self.is_callable()
        self.is_callable(user=self.user)
        self.is_not_callable(user=self.user,
                             kwargs={'c_type': 'foo', 'obj_id': '999'})
        self.is_not_callable(user=self.user, kwargs={
            'c_type': ContentType.objects.get_for_model(
                self.content_object).model,
            'obj_id': '999',
        })
        data = {'feedback-message': 'Foo'}
        self.is_postable(user=self.user, data=data,
                         to_url_name='feedback_form')
        self.assertEqual(Feedback.objects.all().count(), 1)
        self.assertEqual(Feedback.objects.all()[0].message, 'Foo')
        self.assertEqual(
            Feedback.objects.all()[0].content_object, self.content_object)
