#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from setuptools import setup


with open('phonenumber_filter/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-phonenumber-filter',
    version=version,
    packages=['phonenumber_filter'],
    # license='MIT License',
    # include_package_data=True,
    description=(
        'A simple Django filter that will format and print a phone number in '
        'a template.'
    ),
    url='http://github.com/foundertherapy/django-phonenumber-filter/',
    download_url='https://github.com/foundertherapy/django-phonenumber-filter/archive/v1.0.tar.gz',
    author='Dana Spiegel',
    author_email='dana@foundertherapy.co',
    install_requires=[
        'Django>=1.7',
        'phonenumber>=7',
    ],
    keywords=['phonenumber', 'django', 'filter', 'format', ],
)
