# -*- coding: utf-8 -*-
"""mrbobtemplates.gillux"""

from setuptools import setup, find_packages
import os


_version = '1.0.0'
_test_packages = []

_THIS_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

def _read(*names):
    return open(os.path.join(_THIS_DIRECTORY, *names), 'r').read().strip()


setup(
    name='mrbobtemplates.gillux',
    version=_version,
    description="Templates for mr.bob",
    long_description=_read('README.rst', 'CHANGES.rst'),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords='mr.bob template',
    author='Gilles Lenfant',
    author_email='gilles.lenfant@gmail.com',
    url='http://pypi.python.org/',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['mrbobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'mr.bob'],
    entry_points={
        'bobtemplates': [
            'nspackage=mrbobtemplates.gillux:NSPackage'
        ]
    },
    tests_require=_test_packages,
    extra_requires={
        'test': _test_packages
    }
)
