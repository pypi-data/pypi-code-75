import setuptools

setuptools.setup(
    name="NightWindGameLib",
    version="0.6.2",
    author="Nova_NightWind0311",
    author_email="",
    description="Some little games",
    long_description_content_type="text/markdown",
    url="https://github.com/",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        "arcade>=2.5.1",
        "pymunk<=5.7.0",
        "pygame>=2.0.0",
        "PySide2>=5.15.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)