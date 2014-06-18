Changes log
===========

1.1.0
-----

- nspackage: Distro name and package (Python) name can be distinct.
  [glenfant]

- nspackage: Use of nosetests + coverage is optional
  [glenfant]

- nspackage: Sphinx doc skeleton is optional
  [glenfant]

1.0.0
-----

- Added the "mybobtemplate" template for new bobtemplates.xxx packages skeletons.
  [glenfant]

- Added .xxignore files for git, bazaar and mercurial to the "buildout" template.
  [glenfant]

- setuptools/distribute don't let us distribute empty directories. So we need to put
  a marker file in some directories then remove them.
  [glenfant]

1.0.0b1
-------

- Python 3 support (alpha). Please feeback
  [glenfant]

- Added the "buildout" template, a minimal zc.buildout project bootstrap
  [glenfant]

- Added .xxignore files for git, bazaar and mercurial
  [glenfant]

- Gone through the weirdness of include_package_data, package_data and MANIFEST.in
  This setuptools / distribute feature really sucks
  [glenfant]

1.0.0a2
-------

- Improved README about namespaces support.
  [glenfant]

- Renamed mrbobtemplates.gillux -> bobtemplates.gillux as in standard policy
  http://mrbob.readthedocs.org/en/latest/userguide.html#collection-of-community-managed-templates
  [glenfant]

1.0.0a1
-------

- First public version
  [glenfant]
