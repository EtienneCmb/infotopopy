#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
 
 
 
setup(name='infotopo',
 
      version='0.1',
 
      url='https://github.com/pierrebaudot/infotopopy/',
 
      license='BSD 3-Clause "New" or "Revised" License',
 
      author='Pierre Baudot',
 
      author_email='pierre.baudot@gmail.com',
 
      description='Manage configuration files',
 
      packages=find_packages(exclude=['tests']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=['mpmath>=1.1.0', 'numpy>=1.1.0','networkx>=2.3'])