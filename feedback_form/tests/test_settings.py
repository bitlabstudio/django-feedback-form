"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True

SITE_ID = 1

APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'feedback_form.tests.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../app_static')
MEDIA_ROOT = os.path.join(APP_ROOT, '../app_media')
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [os.path.join(APP_ROOT, 'tests/test_app/templates')],
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.request',
        )
    }
}]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_libs',
    'mailer',
]

INTERNAL_APPS = [
    'feedback_form',
    'feedback_form.tests.test_app',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

SECRET_KEY = 'foobar'

ADMINS = (('Foo Bar', 'foo@example.com'), )
FROM_EMAIL = ADMINS[0][1]

EMAIL_BACKEND = 'mailer.backend.DbBackend'
MAILER_EMAIL_BACKEND = 'django_libs.test_email_backend.EmailBackend'
TEST_EMAIL_BACKEND_RECIPIENTS = ADMINS

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = FROM_EMAIL
EMAIL_HOST_PASSWORD = "YOUR_PASSWORD"
EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = FROM_EMAIL
SERVER_EMAIL = FROM_EMAIL
EMAIL_USE_TLS = True

# App related settings
FEEDBACK_FORM_TEXTCOLOR = '#eee'
FEEDBACK_FORM_COLOR = '#000000'
FEEDBACK_FORM_TEXT = """
<h3>Hi! Do you have feedback or questions?</h3>
<p>We'll answer as fast as possible.</p>
"""
