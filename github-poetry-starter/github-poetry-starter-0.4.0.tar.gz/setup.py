# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['github_poetry_starter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'github-poetry-starter',
    'version': '0.4.0',
    'description': 'GitHub Actions starter for python with python-poetry',
    'long_description': None,
    'author': 'hexatester',
    'author_email': 'hexatester@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
