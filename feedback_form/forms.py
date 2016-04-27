"""Forms for the ``feedback_form`` app."""
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse

from django_libs.utils_email import send_email

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    A feedback form with modern spam protection.

    :url: Field to trap spam bots.

    """
    url = forms.URLField(required=False)

    def __init__(self, user=None, url=None, prefix='feedback',
                 content_object=None, *args, **kwargs):
        self.content_object = content_object
        super(FeedbackForm, self).__init__(prefix='feedback', *args, **kwargs)
        if url:
            self.instance.current_url = url
        if user:
            self.instance.user = user
            del self.fields['email']
        else:
            self.fields['email'].required = True

    def save(self):
        if not self.cleaned_data.get('url'):
            self.instance.content_object = self.content_object
            self.instance = super(FeedbackForm, self).save()
            send_email(
                '',
                {
                    'url': reverse('admin:feedback_form_feedback_change',
                                   args=(self.instance.id, )),
                    'feedback': self.instance,
                },
                'feedback_form/email/subject.html',
                'feedback_form/email/body.html',
                from_email=settings.FROM_EMAIL,
                recipients=[manager[1] for manager in settings.MANAGERS],
            )
            if getattr(settings, 'FEEDBACK_EMAIL_CONFIRMATION', False):
                email = None
                if self.instance.email:
                    email = self.instance.email
                elif self.instance.user.email:
                    email = self.instance.user.email
                if email:
                    send_email(
                        '', {},
                        'feedback_form/email/confirmation_subject.html',
                        'feedback_form/email/confirmation_body.html',
                        from_email=settings.FROM_EMAIL,
                        recipients=[email],
                    )
            return self.instance

    class Media:
        css = {'all': ('feedback_form/css/feedback_form.css'), }
        js = ('feedback_form/js/feedback_form.js', )

    class Meta:
        model = Feedback
        fields = ('email', 'message')
