"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.coolpackage


_g = globals()
_g.update(build_package_configs(
    project_name='coolpackage',
    version=lsst.coolpackage.version.__version__))
