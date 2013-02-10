===================
bobtemplates.gillux
===================

Python package template for `mr.bob <http://pypi.python.org/pypi/mr.bob/>`_

About the templates
===================

Only one template in this version of ``bobtempaltes.gillux``.

nspackage
---------

A regular Python package like (possibly with namespace like ``foo.bar``) with following features :

- Code targeted to Python 2.4 to 2.7
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

  mrbob -O my.package bobtemplates.gillux:nspackage

Then grep - and optionally fix - the ``FIXME:`` that occur in the resulting
files tree for optional stuffs I couldn't fix easily with the regular mr.bob
features.

Read the generated ``README.rst`` in your newly created package for more
information about what you got.

**TODO**

- Provide a Python 3.x option
- Provide a `six <http://pypi.python.org/pypi/six/>`_ support option
- Add "ignored files list" for most popular SCMs (git, mercurial, bzr, svn)
- Make nosetests and sphinx supports optional

Links
=====

Project workspace @ Github (contribute, file issues...):
    https://github.com/glenfant/bobtemplates.gillux
Pypi:
    http://pypi.python.org/pypi/bobtemplates.gillux
``mr.bob`` @ Pypi
    http://pypi.python.org/pypi/mr.bob/
``mr.bob`` @ readthedocs.org
  http://mrbob.readthedocs.org/en/latest/
