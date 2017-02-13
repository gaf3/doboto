#!/usr/bin/env python

from distutils.core import setup
import os

setup(
    name='doboto',
    version="0.3.2",
    description="BOTO-like library for interacting with the Digital Ocean API",
    packages=['doboto'],
    long_description="BOTO-like library for interacting with the Digital Ocean API",
    author="Digital Ocean Data Team",
    author_email="swe-data@do.co",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
)
