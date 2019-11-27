# ======================
# Aficionado
#
# Description:
# A basic AWS Lambda
# wrapper for python
#
# Author: Samuel Hornsey
# ======================

from setuptools import setup, find_packages

setup(
  name='aficionado',
  version='dev',
  packages=find_packages(),
  author='Samuel Hornsey',
  author_email='me@samuelhornsey.com',
  description='A basic AWS Lambda wrapper for python',
  long_description=open('README.md').read(),
  url='https://github.com/SamuelHornsey/aficionado',
  project_urls={
    'Bug Tracker': 'https://github.com/SamuelHornsey/aficionado/issues',
    'Documentation': 'https://github.com/SamuelHornsey/aficionado',
    'Source Code': 'https://github.com/SamuelHornsey/aficionado'
  },
  license='MIT'
)