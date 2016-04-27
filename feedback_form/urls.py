"""URLs for the ``feedback_form`` app."""
from django.conf.urls import url

from .views import FeedbackCreateView


urlpatterns = [
    url(
        r'^(?P<c_type>[-\w]+)/(?P<obj_id>\d+)/$',
        FeedbackCreateView.as_view(),
        name='feedback_form_content_object'),
    url(r'^$', FeedbackCreateView.as_view(), name='feedback_form'),
]
