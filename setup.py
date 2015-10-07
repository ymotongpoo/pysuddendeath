# -*- coding:utf-8 -*-

try:
    import setuptools
    from setuptools.command.test import test as TestCommand
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

version = '0.2.3'
name = 'suddendeath'
short_description = '`suddendeath` generates "突然の死" message.'
readme = _read('README')
history = _read('HISTORY.txt')

long_description = readme + "\n" + history


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: Python Software Foundation License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.5',
    'Topic :: Utilities',
]

setuptools.setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['suddendeath',],
    author='ymotongpoo',
    author_email='ymotongpoo@gmail.com',
    packages=['suddendeath'],
    url='http://github.com/ymotongpoo/pysuddendeath/',
    license='PSL',
    entry_points={
        'console_scripts': [
            'suddendeath=suddendeath.__init__:main',
        ],
    },
    tests_require=['pytest'],
    cmdclass={
        'test': PyTest,
    }
)
