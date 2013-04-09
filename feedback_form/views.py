"""Views for the ``feedback_form`` app."""
from django.views.generic import CreateView

from .models import Feedback


class FeedbackCreateView(CreateView):
    """View to display and handle a feedback create form."""
    model = Feedback
