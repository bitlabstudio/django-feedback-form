"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/', include('feedback_form.urls')),
    url(r'^$', ListView.as_view(model=User, template_name='base.html')),
)

urlpatterns += staticfiles_urlpatterns()
