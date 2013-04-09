"""Admin objects for the ``feedback_form`` app."""
from django.contrib import admin

from .models import Feedback


admin.site.register(Feedback)
