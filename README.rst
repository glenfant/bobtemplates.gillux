===================
bobtemplates.gillux
===================

Python package templates for `mr.bob <http://pypi.python.org/pypi/mr.bob/>`_.
Please read carefully `mr.bob user documentation
<http://mrbob.readthedocs.org/en/latest/index.html>`_ before using this
package.

Installation
============

.. code:: console

   easy_install bobtemplates.gillux

.. warning::

   `mr.bob`_ is a requirement for ``bobtemplates.gillux``. For a reason I
   didn't investigate in depth, installing with **pip** like this raises a
   mysterious ``UnicodeDecodeError`` when installing the required `mr.bob`_
   package as requirement:

   .. code:: console

      pip install bobtemplates.gillux
      | (lots of noise)
      | UnicodeDecodeError: 'ascii' codec can't decode...

   If you really hate ``easy_install`` and want absolutely use ``pip``, this
   works:

   .. code:: console

      pip install mr.bob
      pip install bobtemplates.gillux

   But I can't understand why ;)

About the templates
===================

``bobtempaltes.gillux`` offers the following templates :

buildout

  A simple minimal zc.buildout based project bootstrap

mybobtemplate

  Make your own **bobtemplate.yourname** bootstrap in a some seconds (or more).

nspackage

  A regular Python package bootstrap with or without namespace, any level with
  lots of goodies.

buildout
--------

Usage:

.. code:: console

   mrbob [options] bobtemplates.gillux:buildout

This provides a minimal zc.buildout based project, with a ``bootstrap.py``
file and a buildout.cfg file. Takes care of differences between versions 1.x
and 2.x of zc.buildout.

mybobtemplate
-------------

Usage:

.. code:: console

   mrbob [options] bobtemplates.gillux:mybobtemplate

Make your own **bobtemplate.yourname** package in a few minutes (or more).
Means that you can have the skeleton of a package like ``bobtemplates.gillux``
in some seconds.

You just need to add the content of your template as described in the `mr.bob
documentation`_

nspackage
---------

Usage:

.. code:: console

   mrbob [options] bobtemplates.gillux:nspackage

A regular Python package bootstrap with following features:

- Any namespaces level you want, even none at all. This is detected with the
  name you provide in the wizard.

- Code targeted to Python 2.4 to 2.7 and 3.x

Two optional features:

- Tests with `nose <https://nose.readthedocs.org/en/latest/index.html>`_ and
  `coverage <http://pypi.python.org/pypi/coverage/>`_. Run them with
  ``nosetests``. Tune your options in generated ``setup.cfg``.

- A `Sphinx <http://sphinx-doc.org/>`_ documentation skeleton. Build the HTML
  doc with ``python setup.py build_sphinx``. The doctest files may optionally
  be automatically included in the doc.

Package files outline (may change depending on options::

  src/<your>/<package>/  # Your package source skeleton
  docs/                  # Sphinx source tree skeleton
  tests/                 # Test module skeleton with nose goodies
  setup.py               # Usual setup script
  setup.cfg
  README.rst
  MANIFEST.in

Then grep - and optionally fix - the ``FIXME:`` that occur in the resulting
files tree for optional stuffs I couldn't fix easily with the regular mr.bob
features.

Read the generated ``README.rst`` in your newly created package for more
information about what you got.

**TODO**

- Provide a `six <http://pypi.python.org/pypi/six/>`_ support option

- Tests inside the source tree (in src/<your>/<package>/tests) OR in the
  package root. Sometimes we prefer to ship source distros with the tests, and
  sometimes (i.e big amount of test data) we prefer to keep a source dist
  small.

Links
=====

Project workspace @ Github (contribute, file issues...):
    https://github.com/glenfant/bobtemplates.gillux
Project page @ Pypi:
    http://pypi.python.org/pypi/bobtemplates.gillux
mr.bob @ Pypi:
    http://pypi.python.org/pypi/mr.bob/
mr.bob @ Readthedocs:
  http://mrbob.readthedocs.org/en/latest/
