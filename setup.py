# -*- coding:utf-8 -*-

try:
    import setuptools
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()

import os
import sys

here = os.path.dirname(__file__)
def _read(name):
    try:
        f = open(os.path.join(here, name))
        return f.read()
    except:
        return ""

version = '0.3.0'
name = 'suddendeath'
short_description = '`suddendeath` generates "突然の死" message.'
readme = _read('README')
history = _read('HISTORY.txt')

long_description = readme + "\n" + history

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: Python Software Foundation License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Topic :: Utilities',
    ]

extra = {}

if sys.version_info >= (3, 0):
    if not getattr(setuptools, '_distribute', False):
        raise RuntimeError(
                'You must installed `distribute` to setup suddendeath with Python3')
    extra.update(
        use_2to3=True
    )

setuptools.setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['suddendeath',],
    author='ymotongpoo',
    author_email='ymotongpoo@gmail.com',
    packages = ['suddendeath'],
    url='http://github.com/ymotongpoo/pysuddendeath/',
    license='PSL',
    entry_points = {
        'console_scripts': [
            'suddendeath=suddendeath.__init__:main',
        ],
    },
    test_suite="suddendeath",
    **extra
    )
