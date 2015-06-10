Django Phone Number Filter
==========================

.. image:: https://circleci.com/gh/foundertherapy/django-phonenumber-filter.png
   :target: https://circleci.com/gh/foundertherapy/django-phonenumber-filter

About
-----

``django-phonenumber-filter`` is a Django app that will format and print a 
phonenumber in a template.

Getting Started
---------------

    $ pip install django-phonenumber-filter

Add "phonenumber_filter" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = (
        ...
        'phonenumber_filter',
    )

Then, in your template, load the ``phonenumber_filter`` template tag library:

    {% load phonenumber_filters %}

To format and print a phone number, use the ``phonenumber`` filter:

    {{ raw_phone_number|phonenumber }}
    
If you want to format the phone number for a particular country, include the
optional country code:

    {{ raw_phone_number|phonenumber:"IL" }}
    
International and E164 formats are also supported:

    {{ raw_phone_number|phonenumber_international:"IL" }}
    {{ raw_phone_number|phonenumber_e164:"IL" }}
