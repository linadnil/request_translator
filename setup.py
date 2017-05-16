#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='hrt',
    version='0.1.0',
    description='Translates raw HTTP requests to Python,Ruby,Php and Bash scripts',
    author='Lin Danil  ',
    author_email='linadnil@mail.ru',
    license='3-clause BSD',
    install_requires=[],
    packages=['hrt', 'hrt.templates'],
    scripts=['bin/hrt'])
