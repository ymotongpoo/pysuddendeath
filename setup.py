# -*- coding:utf-8 -*-

import os
import setuptools

HERE = os.path.dirname(__file__)


def _read(name):
    try:
        fp = open(os.path.join(HERE, name))
        return fp.read()
    except:
        return ""

VERSION = '0.3.0'
NAME = 'suddendeath'
SHORT_DESCRIPTION = '`suddendeath` generates "突然の死" message.'
README = _read('README')
HISTORY = _read('HISTORY.txt')

LONG_DESCRIPTION = README + "\n" + HISTORY


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Utilities',
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=['suddendeath'],
    author='ymotongpoo',
    author_email='ymotongpoo@gmail.com',
    packages=['suddendeath'],
    url='http://github.com/ymotongpoo/pysuddendeath/',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'suddendeath=suddendeath.__init__:main',
        ],
    },
    extras_require={
        'test': ['pytest'],
    }
)
