Django Feedback Form
====================

Minified JQuery & Ajax feedback/report form to handle fast customer requests in
Django. You can use it as a fast feedback tool and/or to report objects (e.g.
in case of abuse).

Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django
* Django Mailer
* Django Libs
* South


Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-feedback-form

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-feedback-form.git#egg=feedback_form

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'django',
        'mailer',
        'feedback_form',
        'django_libs',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate feedback_form


Usage
-----

First of all add the feedback urls to your main urls.py::

    url(r'^feedback/', include('feedback_form.urls')),

You can use the "normal" feedback view via ``/feedback/`` but in almost every
case you might want to use the ajax template tag. Just add the following code
to e.g. your base.html::

    {% load feedback_tags %}
    {% feedback_form %}

Pretty ugly, eh? Now, you need to add css and js for sure, like this::

    <link href="{{ STATIC_URL }}feedback_form/css/feedback_form.css" type="text/css" media="all" rel="stylesheet" />
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script type="text/javascript" src="{{ STATIC_URL }}feedback_form/js/feedback_form.js"></script>

That's it!
You can also use this app as a report tool. Simply call another url::

    <a href="{% url "feedback_form_content_object" c_type='user' obj_id=user.pk %}">Report this user!</a>

You can easily customize your form by changing static files or by changing the
following ``settings``:

FEEDBACK_FORM_TEXTCOLOR
+++++++++++++++++++++++

By default the text color is white like ``'#fff'``.

FEEDBACK_FORM_COLOR
+++++++++++++++++++

By default the background color is light blue like ``'#6caec9'``.

FEEDBACK_FORM_TEXT
++++++++++++++++++

By default the text in the form is invisible. Just add the html markup you want
to be displayed above the input fields, like::

    <h3>Hi! Do you have feedback or questions?</h3>
    <p>We'll answer as fast as possible.</p>


Roadmap
-------

See the issue tracker for current and upcoming features.
