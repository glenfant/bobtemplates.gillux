===================
bobtemplates.gillux
===================

Python package templates for `mr.bob <http://pypi.python.org/pypi/mr.bob/>`_.
Please read carefully `mr.bob documentation
<http://mrbob.readthedocs.org/en/latest/index.html>`_ before using this
package.

Installation
============

::

  pip install bobtemplates.gillux

.. admonition::
   Note

   This will install `mr.bob`_ and its requirements too if not already done.

About the templates
===================

``bobtempaltes.gillux`` offers the following templates :

buildout

  A simple minimal zc.buildout based project bootstrap

mybobtemplate

  Make your own **bobtemplate.yourname** package in a few minutes (or more).

nspackage

  A regular Python package with or without namespace, any level with lots of
  goodies.

buildout
--------

Usage ::

  > mrbob [options] bobtemplates.gillux:buildout

This provides a minimal zc.buildout based project, with a ``bootstrap.py``
file and a buildout.cfg file. Takes care of differences between versions 1.x
and 2.x of zc.buildout.

mybobtemplate
-------------

Usage ::

  > mrbob [options] bobtemplates.gillux:mybobtemplate

Make your own **bobtemplate.yourname** package in a few minutes (or more).
Means that you can have the skeleton of a package like ``bobtemplates.gillux``
in some seconds.

You just need to add the content of your template as described in the `mr.bob
documentation`_

nspackage
---------

Usage ::

  > mrbob [options] bobtemplates.gillux:nspackage

A regular Python package bootstrap with following features:

- Any namespaces level you want, even none at all. This is detected with the
  name you provide in the wizard.
- Code targeted to Python 2.4 to 2.7 and 3.x

- Tests with `nose <https://nose.readthedocs.org/en/latest/index.html>`_ and
  `nosexcover <http://pypi.python.org/pypi/nosexcover/>`_. Run them with
  ``nosetests``. Tune your options in generated ``setup.cfg``.

- A `Sphinx <http://sphinx-doc.org/>`_ documentation skeleton. Build the HTML
  doc with ``python setup.py build_sphinx``. The doctest files may optionally
  be automatically included in the doc.

Package files outline::

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
- Make nosetests support optional
- Make Sphinx support optional (overkill for small packages, remove the docs/
  subtree)
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
