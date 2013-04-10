"""Template tags and filters for the ``feedback_form`` app."""
from django import template

from ..app_settings import *  # NOQA
from ..forms import FeedbackForm

register = template.Library()


@register.inclusion_tag('feedback_form/partials/form.html', takes_context=True)
def feedback_form(context):
    """Template tag to render a feedback form."""
    user = None
    if context['request'].user.is_authenticated():
        user = context['request'].user
    return {
        'form': FeedbackForm(url=context['request'].path, user=user),
        'background_color': FEEDBACK_FORM_COLOR,
        'text_color': FEEDBACK_FORM_TEXTCOLOR,
        'text': FEEDBACK_FORM_TEXT,
    }
