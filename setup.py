#!/usr/bin/env python
import sys

if 'develop' in sys.argv:
    # use setuptools for develop, but nothing else
    from setuptools import setup
else:
    from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

#with open('CHANGES') as file:
#    long_description += file.read()


from pyradex import __version__ as version

setup(name='pyradex',
      version=version,
      description='Python-RADEX',
      long_description=long_description,
      author='Adam Ginsburg & Julia Kamenetzky',
      author_email='adam.g.ginsburg@gmail.com',
      url='http://github.com/keflavich/pyradex/',
      packages=['pyradex'],
     )