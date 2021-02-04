#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['whooper']

package_data = \
{'': ['*']}

install_requires = \
['boto3 >=1.17.1', 'redshift-connector >=2.0.873']

setup(name='whooper',
      version='0.0.0',
      description='Convenience wrappers for connecting to AWS S3 and Redshift',
      author='Nick Buker',
      author_email='nickbuker@gmail.com',
      url='https://github.com/nickbuker/whooper',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.6,<4',
     )
