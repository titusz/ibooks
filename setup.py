#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

setup(
    name='ibooks',
    version=version,
    py_modules=['ibooks'],
    url='http://github.com/titusz/ibooks',
    license='BSD',
    author='titusz',
    author_email='tp@py7.de',
    description='iBooks Author cover and metadata extraction',
    long_description=README + '\n\n' + NEWS,
    entry_points={
        'console_scripts': ['ibooks = ibooks:cli']
    },
    keywords='ibooks author metadata cover extraction epub epub3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: System :: Filesystems',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
