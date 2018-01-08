"""Simple-Salesforce/Multi-Batch Package Setup"""

from setuptools import setup
import textwrap
import sys
import os


pyver_install_requires = []
pyver_tests_require = []
if sys.version_info < (2, 7):
    pyver_install_requires.append('ordereddict>=1.1')
    pyver_tests_require.append('unittest2>=0.5.1')

if sys.version_info < (3, 0):
    pyver_tests_require.append('mock==1.0.1')


setup(
    name='salesforce_batch',
    version='0.1',
    author='NICK CATALANO forked by matt bramfeld',
    author_email='matthew.bramfeld@gmail.com',
    packages=['salesforce_batch',],
    download_url="https://github.com/mbr84/salesforce_batch/archive/0.1.tar.gz",
    url='https://github.com/mbr84/simple-salesforce',
    description='a fork of simple-salesforce with multi-batch jobs.',

    # install_requires=[
    #     'requests[security]'
    # ] + pyver_install_requires,
    # tests_require=[
    #     'nose>=1.3.0',
    #     'pytz>=2014.1.1',
    #     'responses>=0.5.1',
    # ] + pyver_tests_require,
    # test_suite = 'nose.collector',

    keywords='python salesforce job batch salesforce.com',
    classifiers=[]
)
