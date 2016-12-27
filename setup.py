# coding: utf-8

import os

from setuptools import setup

VERSION = '0.1.0'

setup(
    maintainer='John Hu',
    maintainer_email='ushuz@xiachufang.com',
    name='uwsgimon',
    version=VERSION,
    description='uWSGI Monitor',
    license='MIT',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    scripts=['uwsgimon'],
    install_requires = ['simplejson']
)
