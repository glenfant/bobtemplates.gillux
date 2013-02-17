# -*- coding: utf-8 -*-
"""Hooks for mr.bob. See http://mrbob.readthedocs.org/en/latest/templateauthor.html#hooks"""
import os
import time
import six

if six.PY3:
    from urllib.request import urlopen
else:
    from urllib2 import urlopen
import pkg_resources

try:
    from mrbob.exceptions import ValidationError
except ImportError:
    # FIXME: Temporary
    class ValidationError(Exception):
        pass

###
# nspackage hooks
###


def nspackage_pre_render(config):
    pkgname = config.variables['pkgname']

    ul_pkgname = '=' * len(pkgname)

    ns_names = pkgname.split('.')
    py_ns_pkgnames = []
    for i, ns_name in enumerate(ns_names[1:]):
        name = "'{0}'".format('.'.join(ns_names[:i + 1]))
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

def scm_post_choice(config, question, answer):
    accepted = ('git', 'bzr', 'hg', 'none')
    answer = answer.lower().strip()
    if answer not in accepted:
        raise ValidationError("'{0}' is not a valid answer.".format(answer))
    return answer


NS_INIT = "__import__('pkg_resources').declare_namespace(__name__)\n"


def nspackage_post_render(config):
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
            init_path = names[:level + 1] + ['__init__.py']
            with open(os.path.join(src_root, *init_path), 'w') as init_py:
                init_py.write(NS_INIT)
    else:
        # We just need to rename 'coderoot'
        os.rename(os.path.join(src_root, 'coderoot'), os.path.join(src_root, pkgname))

    # Must remove the SCM files .xxxignore we don't need
    to_remove = {
        # Useless files for scm choice
        'none': ('.hgignore', '.gitignore', '.bzrignore'),
        'hg': ('.gitignore', '.bzrignore'),
        'git': ('.hgignore', '.bzrignore'),
        'bzr': ('.gitignore', '.hgignore')
    }
    scm = config.variables['scmsupport']
    for name in to_remove[scm]:
        path = os.path.join(config.target_directory, name)
        os.remove(path)

    print("Grep for \"FIXME:\" in the generated files")
    return

###
# buildout hooks
###


def buildout_pre_render(config):
    bo_version = config.variables['bo_version']
    main_bo_version = int(pkg_resources.parse_version(bo_version)[0])
    add_vars = {
        'main_bo_version': main_bo_version
    }
    config.variables.update(add_vars)
    return


def buildout_post_render(config):
    main_bo_version = config.variables['main_bo_version']

    # We have different bootstraps depending on zc.buildout version
    # http://pypi.python.org/pypi/zc.buildout
    bootstrap_url = "http://downloads.buildout.org/{0}/bootstrap.py".format(main_bo_version)
    bootstrap_in = urlopen(bootstrap_url)
    bootstrap_py_path = os.path.join(config.target_directory, 'bootstrap.py')
    with open(bootstrap_py_path, 'w') as bootstrap_py:
        bootstrap_py.write(bootstrap_in.read())
    return
