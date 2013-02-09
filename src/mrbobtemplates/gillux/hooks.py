# -*- coding: utf-8 -*-
"""Hooks for mr.bob. See http://mrbob.readthedocs.org/en/latest/templateauthor.html#hooks"""
import os
from pdb import set_trace
import time

def pre_render(config):
    pkgname = config.variables['pkgname']

    ul_pkgname = '=' * len(pkgname)

    ns_names = pkgname.split('.')
    py_ns_pkgnames = []
    for i, ns_name in enumerate(ns_names[1:]):
        name = "'{0}'".format('.'.join(ns_names[:i+1]))
        py_ns_pkgnames.append(name)
    py_ns_pkgnames = ", ".join(py_ns_pkgnames)

    add_vars = {
        'rst_pkgname': "{0}\n{1}\n{0}".format(ul_pkgname, pkgname),
        'creation_year': time.gmtime().tm_year,
        'has_namespaces': len(ns_names) > 1,
        'namespace_packages': py_ns_pkgnames
    }
    config.variables.update(add_vars)
    return

NS_INIT = "__import__('pkg_resources').declare_namespace(__name__)\n"

def post_render(config):
    # We need to rename the "coderoot" package appropriately
    src_root = os.path.join(config.target_directory, 'src')
    pkgname = config.variables['pkgname']
    if config.variables['has_namespaces']:
        # Making the directories
        names = pkgname.split('.')
        os.renames(os.path.join(src_root, 'coderoot'),
                   os.path.join(src_root, *names))

        # And creating the special __init__.py at each level
        for level in xrange(len(names) - 1):
            init_path = names[:level+1] + ['__init__.py']
            with open(os.path.join(src_root, *init_path), 'w') as init_py:
                init_py.write(NS_INIT)
    else:
        # We just need to rename 'coderoot'
        os.rename(os.path.join(src_root, 'coderoot'), os.path.join(src_root, pkgname))

    print "Grep for \"FIXME:\" in the generated files"

