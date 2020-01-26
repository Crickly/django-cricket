# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='crickly',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A Django app to store and manage cricket matches.',
    long_description=README,
    url='https://rly.rocks/crickly',
    author='Riley Evans',
    author_email='crickly@rileyevans.co.uk',
    install_requires=[
        'Django>=1.16.0,<2.0.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
