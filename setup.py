#!/usr/bin/env python

from distutils.core import setup
import os

our_dir = os.path.abspath(os.path.dirname(__file__))
__version__ = open(our_dir + "/VERSION", "r").readline().strip()

setup(
    name='doboto',
    version=__version__,
    description="doboto",
    long_description="BOTO-like library for interacting with the Digital Ocean API",
    author="Digital Ocean Data Team",
    author_email="swe-data@do.co",
    classifiers=[
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.7'
    ],
)
