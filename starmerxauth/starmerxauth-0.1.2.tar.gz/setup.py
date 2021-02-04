from setuptools import setup, find_packages

setup(
    name="starmerxauth",
    version="0.1.2",
    author="yang",
    author_email="",
    description="starmerx verify jwt",
    license="MIT",
    url="",  # github
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        #"License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
    ],
    install_requires=[
        "PyJWT== 1.7.1",
        "cryptography"
    ],
    zip_safe=True,
)
