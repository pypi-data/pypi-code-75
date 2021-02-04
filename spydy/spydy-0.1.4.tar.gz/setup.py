from setuptools import setup, find_packages
from codecs import open
from os import path


__version__ = '0.1.4'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='spydy',
    version=__version__,
    description='基于Pipeline的快速爬虫框架（支持异步）',
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    url='https://github.com/superjcd/spydy',
    download_url='https://github.com/superjcd/spydy/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    entry_points={
        'console_scripts': [
            'spydy=spydy.main:fire',
        ],
    },
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Jiang Chaodi',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='929760274@qq.com'
)
