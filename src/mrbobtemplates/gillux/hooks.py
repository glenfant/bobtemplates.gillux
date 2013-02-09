# -*- coding: utf-8 -*-
"""Hooks for mr.bob. See http://mrbob.readthedocs.org/en/latest/templateauthor.html#hooks"""
import time

def pre_render(config):
    pkgname = "{name1}.{name2}".format(**config.variables)
    ul_pkgname = '=' * len(pkgname)
    add_vars = {
        'pkgname': pkgname,
        'rst_pkgname': "{0}\n{1}\n{0}".format(ul_pkgname, pkgname),
        'creation_year': time.gmtime().tm_year
    }
    config.variables.update(add_vars)
    return

def post_render(config):
    print "Grep for \"FIXME:\" in the generated files"
