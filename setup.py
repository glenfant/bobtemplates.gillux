# -*- coding: utf-8 -*-
"""bobtemplates.gillux"""

from setuptools import setup, find_packages
import os

_version = '1.1.0'
_test_packages = []

_this_directory = os.path.abspath(os.path.dirname(__file__))

def _read(*names):
    return open(os.path.join(_this_directory, *names), 'r').read().strip()


setup(
    name='bobtemplates.gillux',
    version=_version,
    description="Python project bootstraps for mr.bob: usual Python distro, buildout, and mr.bob template",
    long_description=_read('README.rst') + '\n\n' + _read('CHANGES.rst'),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords='mr.bob template',
    author='Gilles Lenfant',
    author_email='gilles.lenfant@gmail.com',
    url='http://pypi.python.org/pypi/bobtemplates.gillux',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'mr.bob'],
    entry_points={
        'bobtemplates': [
            'nspackage=bobtemplates.gillux:nspackage',
            'buildout=bobtemplates.gillux:buildout',
            'mybobtemplate=bobtemplates.gillux:mybobtemplate'
        ]
    },
    tests_require=_test_packages,
    extra_requires={
        'test': _test_packages
    }
)
