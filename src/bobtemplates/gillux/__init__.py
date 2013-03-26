# -*- coding: utf-8 -*-
"""
===================
bobtemplates.gillux
===================

A bunch of templates for mr.bob
"""
import sys
import logging
import pkg_resources

# Support for mrbob experimental feature (not yet released)
try:
    from mrbob import register_template
except ImportError:
    register_template = lambda x, y="": None

# Custom logger
LOG = logging.getLogger(name=__name__)
if sys.version_info < (2, 7):
    class NullHandler(logging.Handler):
        """Copied from Python 2.7 to avoid getting `No handlers could be found
        for logger "xxx"` http://bugs.python.org/issue16539
        """
        def handle(self, record):
            pass
        def emit(self, record):
            pass
        def createLock(self):
            self.lock = None
else:
    from logging import NullHandler

LOG.addHandler(NullHandler())

# PEP 0396 style version marker
try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    LOG.warning("Could not get the package version from pkg_resources")
    __version__ = 'unknown'

# Templates registration

nspackage = register_template('nspackage')
buildout = register_template('buildout')
mybobtemplate = register_template('mybobtemplate')
