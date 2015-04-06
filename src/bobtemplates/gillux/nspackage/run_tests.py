#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=================
Running all tests
=================

To have a fine grained control over the tests to run, you may use with Python
2.7 and later::

  python -m unittest -h

If you have unittest2, use the ``unit2`` command instead::

  unit2 -h
"""
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from tests import all_tests

unittest.TextTestRunner(verbosity=2).run(all_tests())
