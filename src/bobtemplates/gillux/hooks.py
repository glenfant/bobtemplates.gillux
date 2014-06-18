# -*- coding: utf-8 -*-
"""Hooks for mr.bob. See http://mrbob.readthedocs.org/en/latest/templateauthor.html#hooks"""
import os
import shutil
import time
import six

if six.PY3:
    from urllib.request import urlopen
else:
    from urllib2 import urlopen
import pkg_resources

from mrbob.bobexceptions import ValidationError, SkipQuestion

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
    bootstrap_py_path = target_rel_path(config, 'bootstrap.py')
    with open(bootstrap_py_path, 'w') as bootstrap_py:
        bootstrap_py.write(bootstrap_in.read())

    scm_support_post_render(config)

    # Done
    print("Grep for \"FIXME:\" in the generated files")
    return


###
# mybobtemplate hooks
###


def mybobtemplate_pre_render(config):
    pkgname = 'bobtemplates.' + config.variables['pkgext']
    config.variables['pkgname'] = pkgname
    nspackage_pre_render(config)
    templatenames = config.variables['templatenames']
    add_vars = {
        'templatenames': templatenames.split()
    }
    config.variables.update(add_vars)
    return


def mybobtemplate_post_render(config):
    # Create required templates
    templatenames = config.variables['templatenames']
    for name in templatenames:
        template_dir = target_rel_path(config, 'src', 'coderoot', name)
        os.mkdir(template_dir)
        with open(os.path.join(template_dir, '.mrbob.ini'), 'w') as fh:
            fh.write(MRBOB_INI)

    # Common stuffs
    rename_coderoot(config)
    scm_support_post_render(config)

    # Done
    print("Grep for \"FIXME:\" in the generated files")
    return

MRBOB_INI = """\
[template]
description = FIXME: Please provide a short description for this template
# FIXME: You may need hooks for your template
#        See https://mrbob.readthedocs.org/en/latest/templateauthor.html#post-render-hook
#pre_render = bobtemplates.gillux.hooks:mybobtemplate_pre_render
#post_render = bobtemplates.gillux.hooks:mybobtemplate_post_render

[questions]
# FIXME: Provide the questions for your template here
#        See https://mrbob.readthedocs.org/en/latest/templateauthor.html#writing-questions
"""


###
# nspackage hooks
###

def pkgname_pre_question(config, question):
    """Making a defaut package namefrom distro name
    """
    distroname = config.variables[u'distroname']

    # Check if distro name is suitable for default package name
    import keyword

    if keyword.iskeyword(distroname):
        distroname = u''
    else:
        try:
            exec('import {0}'.format(distroname), {}, {})
            distroname = u''
        except ImportError:
            pass
        except SyntaxError:
            distroname = u''
    question.default = distroname
    return


def doctestinclude_pre_question(config, question):
    """We'll skip this question if the user did not choose Sphinx
    """
    usesphinx = config.variables[u'usesphinx']
    if not usesphinx:
        raise SkipQuestion('Useless')


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


def nspackage_post_render(config):
    """mr.bob Post render hook for the nspackage template
    """
    # We need to rename the "coderoot" package appropriately
    rename_coderoot(config)
    unittests_or_nose(config)
    may_cleanup_sphinx(config)
    scm_support_post_render(config)

    # Done
    print("Grep for \"FIXME:\" in the generated files")
    return


###
# Common hooks and utilities
###

def may_cleanup_sphinx(config):
    """Remove Sphinx bootstrap if we don't need it
    """
    if not config.variables[u'usesphinx']:
        sphinx_root = target_rel_path(config, 'docs')
        shutil.copyfile(os.path.join(sphinx_root, 'changes.rst'), os.path.join(config.target_directory, 'CHANGES.rst'))
        shutil.rmtree(sphinx_root)
    return

def unittests_or_nose(config):
    """Keep resources suited to nosetests or unittests
    """
    if config.variables[u'usenose']:
        rm_rel_path(config, 'tests', 'test_doctests.py')
    else:
        rm_rel_path(config, 'tests', 'test_narrative_fixt.py')
        rm_rel_path(config, 'setup.cfg')
    return

def empty_sphinx_assets(config):
    """We need to clear sphinx README.rst placeholders
    """
    # setuptools / distribute suck. We cannot distribute empty directories
    # so we need to add docs/_templates and docs/_static in the distro but
    # we need to delete them from the built project bootstrap
    if not config.variables[u'usesphinx']:
        for dirname in ('_templates', '_static'):
            rm_rel_path(config, 'docs', dirname, 'README.rst')


def scm_support_post_render(config):
    """Keeps the relevant SCM .xxxignore file
    """
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
        rm_rel_path(config, name)
    return


def scm_post_choice(config, question, answer):
    accepted = ('git', 'bzr', 'hg', 'none')
    answer = answer.lower().strip()
    if answer not in accepted:
        raise ValidationError("'{0}' is not a valid answer.".format(answer))
    return answer


def rename_coderoot(config):
    # Makes namespace directories tree in place of "coderoot"
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
    return


def target_rel_path(config, *path_elts):
    """Relative path -> target directory absolute path
    """
    return os.path.join(config.target_directory, *path_elts)

def rm_rel_path(config, *path_elts):
    """Remove the file or directory at target directory relative path
    """
    file_path = target_rel_path(config, *path_elts)
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
    else:
        os.remove(file_path)
    return

NS_INIT = "__import__('pkg_resources').declare_namespace(__name__)\n"
