"""Views for the ``feedback_form`` app."""
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import CreateView

from .app_settings import *  # NOQA
from .forms import FeedbackForm
from .models import Feedback


class FeedbackCreateView(CreateView):
    """View to display and handle a feedback create form."""
    model = Feedback
    form_class = FeedbackForm
    ajax_template = 'feedback_form/partials/form_content.html'

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('c_type') and kwargs.get('obj_id'):
            try:
                content_type = ContentType.objects.get(model=kwargs['c_type'])
            except ContentType.DoesNotExist:
                raise Http404
            try:
                self.content_object = content_type.get_object_for_this_type(
                    pk=kwargs['obj_id'])
            except ObjectDoesNotExist:
                raise Http404
        return super(FeedbackCreateView, self).dispatch(
            request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(FeedbackCreateView, self).get_form_kwargs()
        if self.request.user.is_authenticated():
            kwargs.update({'user': self.request.user})
        kwargs.update({
            'url': self.request.META.get('HTTP_REFERER', self.request.path),
            'content_object': self.content_object if hasattr(
                self, 'content_object') else None,
        })
        return kwargs

    def get_template_names(self):
        if self.request.is_ajax():
            return self.ajax_template
        return super(FeedbackCreateView, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(FeedbackCreateView, self).get_context_data(**kwargs)
        context.update({
            'background_color': FEEDBACK_FORM_COLOR,
            'text_color': FEEDBACK_FORM_TEXTCOLOR,
            'text': FEEDBACK_FORM_TEXT,
        })
        if hasattr(self, 'content_object'):
            context.update({'content_object': self.content_object})
        return context

    def get_success_url(self):
        return reverse('feedback_form')
