# -*- coding: utf-8 -*-
"""Nose style fixtures for test_narrative.rst"""

from nose.tools import nottest, istest

@nottest
def dummy():
    # A sample function that's available from test_narrative.rst
    return None

@nottest
def setup_test(test):
    # http://nose.readthedocs.org/en/latest/doc_tests/test_doctest_fixtures/doctest_fixtures.html
    return

@nottest
def teardown_test(test):
    # http://nose.readthedocs.org/en/latest/doc_tests/test_doctest_fixtures/doctest_fixtures.html
    return

def globs(globs):
    """Additional globals usable from test_narrative.rst"
    """
    my_globs = {
        'dummy': dummy
        }
    globs.update(my_globs)
    return globs
