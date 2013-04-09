Django Feedback Form
====================

Minified JQuery & Ajax feedback form to handle fast customer requests in Django

Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django 1.4
* South


Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-feedback-form (not available at the moment)

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-feedback-form.git#egg=feedback_form

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'django',
        'feedback_form',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate feedback_form


Usage
-----

TODO


Roadmap
-------

See the issue tracker for current and upcoming features.
