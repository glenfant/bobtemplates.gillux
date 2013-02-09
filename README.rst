=====================
mrbobtemplates.gillux
=====================

Python package template for `mr.bob <http://pypi.python.org/pypi/mr.bob/>`_

About the templates
===================

Only one template in this version of ``bobtempaltes.gillux``.

nspackage
---------

A namespace package like ``foo.bar`` with following features :

- Works for Python 2.4 to 2.7
- Tests with **nose** and **nosexcover**. Run them with ``python setup.py
  nosetests``
- A **Sphinx** documentation skeleton. Build the HTML doc with ``python setup.py
  build_sphinx``. The doctest files are automatically included in the doc.

Package files outline::

  src/<your>/<package>/  # Your package source
  docs/                  # Sphinx source tree
  tests/                 # Test module skeleton with nose goodies
  setup.py               # Usual setup script
  setup.cfg
  README.rst
  MANIFEST.in

Usage (short)::

  mrbob -O my.package mrbobtemplates.gillux:nspackage

Then grep - and optionally fix - the ``FIXME:`` that occur in the resulting
files tree for optional stuffs I couldn't fix with the regular mr.bob features.

Links
=====

Project workspace @ Github (contribute, file issues...):
    https://github.com/glenfant/mrbobtemplates.gillux
Pypi:
    http://pypi.python.org/pypi/mrbobtemplates.gillux
