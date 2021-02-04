#!/usr/bin/env python

from __future__ import absolute_import
def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('pyclaw', parent_package, top_path)
    config.add_data_files('log.config')
    config.add_subpackage('classic')
    config.add_subpackage('sharpclaw')
    config.add_subpackage('fileio')
    config.add_subpackage('limiters')
    config.add_subpackage('examples', subpackage_path='pyclaw/examples')
    config.add_subpackage('tests')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
