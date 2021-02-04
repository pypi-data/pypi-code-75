#!/usr/bin/env python
"""
Setup script for the `iolink` package.
"""

import setuptools

setuptools.setup(
    name='iolink',
    author='Maxim-Trinamic Software Team',
    author_email='pypi.trinamic@maximintegrated.com',
    description='IO-Link Adapter Interface',
    url='https://github.com/trinamic/iolink',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT',
)
