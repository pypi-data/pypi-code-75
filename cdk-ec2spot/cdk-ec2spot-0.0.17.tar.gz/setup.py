import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-ec2spot",
    "version": "0.0.17",
    "description": "CDK construct library for EC2 Spot",
    "license": "Apache-2.0",
    "url": "https://github.com/pahud/cdk-ec2spot.git",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<pahudnet@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pahud/cdk-ec2spot.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_ec2spot",
        "cdk_ec2spot._jsii"
    ],
    "package_data": {
        "cdk_ec2spot._jsii": [
            "cdk-ec2spot@0.0.17.jsii.tgz"
        ],
        "cdk_ec2spot": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-autoscaling>=1.73.0, <2.0.0",
        "aws-cdk.aws-ec2>=1.73.0, <2.0.0",
        "aws-cdk.aws-iam>=1.73.0, <2.0.0",
        "aws-cdk.core>=1.73.0, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.19.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
