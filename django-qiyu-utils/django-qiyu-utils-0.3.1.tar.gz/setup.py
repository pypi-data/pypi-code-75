# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_qiyu_utils']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.1,<3.2']

setup_kwargs = {
    'name': 'django-qiyu-utils',
    'version': '0.3.1',
    'description': 'Django 辅助工具类',
    'long_description': '# django utils for internal use\n\nQiYuTech Django Utils(Only for internal use)\n\n![PyPI - Version](https://img.shields.io/pypi/v/django-qiyu-utils)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-qiyu-utils)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/django-qiyu-utils)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/django-qiyu-utils)\n![GitHub repo size](https://img.shields.io/github/repo-size/qiyutechdev/django-qiyu-utils)\n![Lines of code](https://img.shields.io/tokei/lines/github/qiyutechdev/django-qiyu-utils)\n\n# WARNING\n\n    USE IT AT YOUR OWN RISK!!\n',
    'author': 'dev',
    'author_email': 'dev@qiyutech.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
