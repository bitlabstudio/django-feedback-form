"""Forms for the ``feedback_form`` app."""
import os

from django import forms
from django.conf import settings

from django_libs.utils_email import send_email

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    A feedback form with modern spam protection.

    :url:

    """
    url = forms.URLField(required=False)

    def __init__(self, user=None, url=None, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.url = None
        if user:
            self.instance.user = user
            del self.fields['email']

    def save(self):
        if not self.cleaned_data.get('url'):
            obj = super(FeedbackForm, self).save()
            send_email(
                '',
                {
                    'url': self.url,
                    'email': obj.user or obj.email,
                    'date': obj.creation_date,
                    'message': obj.message,
                },
                'feedback_form/email/subject.html',
                'feedback_form/email/body.html',
                'feedback_form/email/body_plain.html',
                from_email=settings.FROM_EMAIL,
                recipients=[manager[1] for manager in settings.MANAGERS],
            )
            return obj

    class Media:
        css = {
            'all': (os.path.join(
                settings.STATIC_URL, 'feedback_form/css/feedback_form.css'), )
        }
        js = (
            os.path.join(
                settings.STATIC_URL, 'feedback_form/js/feedback_form.js', ),
        )

    class Meta:
        model = Feedback
        fields = ('email', 'message')
