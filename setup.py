#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from setuptools import setup, find_packages


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
    packages=find_packages(),
    # license='MIT License',
    # include_package_data=True,
    description=(
        'A simple Django filter that will format and print a phone number in '
        'a template.'
    ),
    url='http://github.com/foundertherapy/django-phonenumber-filter/',
    download_url='https://github.com/foundertherapy/django-phonenumber-filter/archive/1.0.0.tar.gz',
    author='Dana Spiegel',
    author_email='dana@foundertherapy.co',
    install_requires=[
        'Django>=1.7',
        'phonenumbers>=7',
    ],
    keywords=['phonenumber', 'django', 'filter', 'format', ],
)
