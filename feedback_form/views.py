"""Views for the ``feedback_form`` app."""
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from .forms import FeedbackForm
from .models import Feedback


class FeedbackCreateView(CreateView):
    """View to display and handle a feedback create form."""
    model = Feedback
    form_class = FeedbackForm

    def get_form_kwargs(self):
        kwargs = super(FeedbackCreateView, self).get_form_kwargs()
        if self.request.user.is_authenticated():
            kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('feedback_form')
