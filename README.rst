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

   Please read https://github.com/pypa/pip/pull/1473 about this.

About the templates
===================

``bobtempaltes.gillux`` offers the following templates :

`nspackage`_

  A regular Python package bootstrap with or without namespace, any level with
  lots of goodies.

`buildout`_

  A simple minimal zc.buildout based project bootstrap

`mybobtemplate`_

  Make your own **bobtemplate.yourname** bootstrap in a some seconds (or more).

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
``nosetests``. Tune your options in generated ``setup.cfg``. By default, tests
will be "dicovered" automatically (Python 2.7 or 3.3 ``unittest``), or with
``unittest2`` for other Python versions.

- A `Sphinx <http://sphinx-doc.org/>`_ documentation skeleton. Build the HTML
  doc with ``python setup.py build_sphinx``. The doctest files may optionally
  be automatically included in the doc.

Package files outline (may change depending on options)::

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

.. rubric:: nspackage questions

Your full name?

  Your full name (like "John Doe")

Your short name?

  Your short name (like "jdoe"). Usually your PyPI or Github login is a good idea.

Your mail address?

  This mail address will not appear on the PyPI page of this distro.

Distribution name?

  The name of the distro that will be used to install with pip. As ``pip
  install (this name)``. Make sure that it is not yet used by any of the
  50000+ packages known by PyPI.

Package name - can be with namespaces ("foo.bar.baz") or not ("foo")?

  The name your package is known by Python like in "import foo.bar.baz".
  Namespace packages are automatically detected for the structure of the
  package directory tree and the registration in ``setup.py``.

Package description?

  What will be in this distro's PyPI page subtitle and in the packages
  listing.

Organization?

  The team ou company that owns the package copyright.

Use nose tests [true|false]?

  If you're a nosetests fan, otherwise the tests layout will use the now
  classical tests auto discovery feature of ``unittest`` or ``unittest2`` for
  older versions of Python.

Add a Sphinx doc skeleton [true|false]?

  Big Python projects should have a Sphinx doc. This option provides a Sphinx
  layout prepared for your project in the ``docs`` directory. You just need to
  type ``python setup.py build_sphinx`` to build the HTML doc.

Include doctest files in Sphinx doc [true|false]?

  A copy of all your doctest files (``tests/test_*.txt``) will be included in
  the Sphinx documentation. Of course, this question does not appear if you
  answered **false** to the previous question.

What SCM do you plan to use [git|hg|bzr|none]?

  We provide some cookies for Git, Mercurial and Bazaar in the form of a
  ``.gitignore`` or whatever's SCM suited exclude files.

.. rubric:: TODO

- Provide a `six <http://pypi.python.org/pypi/six/>`_ support option

- Tests inside the source tree (in src/<your>/<package>/tests) OR in the
  package root. Sometimes we prefer to ship source distros with the tests, and
  sometimes (i.e big amount of test data) we prefer to keep a source dist
  small.

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
user documentation`_

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
