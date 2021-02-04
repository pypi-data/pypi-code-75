import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from pythondata_cpu_minerva import version_str

setuptools.setup(
    name="pythondata-cpu-minerva",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="""\
Python module containing sources files for Minerva cpu.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/pythondata-cpu-minerva",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'cpu_minerva': ['cpu_minerva/sources/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/litex-hub/pythondata-cpu-minerva/issues",
        "Source Code": "https://github.com/litex-hub/pythondata-cpu-minerva",
    },
)
