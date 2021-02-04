"""
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
![Build](https://github.com/SnapPetal/cdk-simplewebsite-deploy/workflows/Build/badge.svg)
![Release](https://github.com/SnapPetal/cdk-simplewebsite-deploy/workflows/Release/badge.svg?branch=main)

# cdk-simplewebsite-deploy

This is an AWS CDK Construct to simplify deploying a single-page website using either S3 buckets or CloudFront distributions.

## Installation and Usage

### [CreateBasicSite](https://github.com/snappetal/cdk-simplewebsite-deploy/blob/main/API.md#cdk-cloudfront-deploy-createbasicsite)

#### Creates a simple website using S3 buckets with a domain hosted in Route 53.

##### Typescript

```console
npm install cdk-simplewebsite-deploy
```

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
from cdk_simplewebsite_deploy import CreateBasicSite

class PipelineStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting)

        CreateBasicSite(stack, "test-website",
            website_folder="./src/build",
            index_doc="index.html",
            hosted_zone="example.com"
        )
```

##### C#

```console
dotnet add package ThonBecker.CDK.SimpleWebsiteDeploy
```

```cs
using Amazon.CDK;
using ThonBecker.CDK.SimpleWebsiteDeploy;

namespace SimpleWebsiteDeploy
{
    public class PipelineStack : Stack
    {
        internal PipelineStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            new CreateBasicSite(scope, "test-website", new BasicSiteConfiguration()
            {
                WebsiteFolder = "./src/build",
                IndexDoc = "index.html",
                HostedZone = "example.com",
            });
        }
    }
}
```

### [CreateCloudfrontSite](https://github.com/snappetal/cdk-simplewebsite-deploy/blob/main/API.md#cdk-cloudfront-deploy-createcloudfrontsite)

#### Creates a simple website using a CloudFront distribution with a domain hosted in Route 53.

##### Typescript

```console
npm install cdk-simplewebsite-deploy
```

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
from cdk_simplewebsite_deploy import CreateCloudfrontSite

class PipelineStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting)

        CreateCloudfrontSite(stack, "test-website",
            website_folder="./src/dist",
            index_doc="index.html",
            hosted_zone="example.com",
            sub_domain="www.example.com"
        )
```

##### C#

```console
dotnet add package ThonBecker.CDK.SimpleWebsiteDeploy
```

```cs
using Amazon.CDK;
using ThonBecker.CDK.SimpleWebsiteDeploy;

namespace SimpleWebsiteDeploy
{
    public class PipelineStack : Stack
    {
        internal PipelineStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            new CreateCloudfrontSite(scope, "test-website", new CloudfrontSiteConfiguration()
            {
                WebsiteFolder = "./src/build",
                IndexDoc = "index.html",
                HostedZone = "example.com",
                SubDomain = "www.example.com",
            });
        }
    }
}
```

## License

Distributed under the [Apache-2.0](./LICENSE) license.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_cloudfront
import aws_cdk.core


@jsii.data_type(
    jsii_type="cdk-simplewebsite-deploy.BasicSiteConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone": "hostedZone",
        "index_doc": "indexDoc",
        "website_folder": "websiteFolder",
        "error_doc": "errorDoc",
    },
)
class BasicSiteConfiguration:
    def __init__(
        self,
        *,
        hosted_zone: builtins.str,
        index_doc: builtins.str,
        website_folder: builtins.str,
        error_doc: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param hosted_zone: (experimental) Hosted Zone used to create the DNS record for the website.
        :param index_doc: (experimental) The index document of the website.
        :param website_folder: (experimental) Local path to the website folder you want to deploy on S3.
        :param error_doc: (experimental) The error document of the website. Default: - No error document.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "hosted_zone": hosted_zone,
            "index_doc": index_doc,
            "website_folder": website_folder,
        }
        if error_doc is not None:
            self._values["error_doc"] = error_doc

    @builtins.property
    def hosted_zone(self) -> builtins.str:
        """(experimental) Hosted Zone used to create the DNS record for the website.

        :stability: experimental
        """
        result = self._values.get("hosted_zone")
        assert result is not None, "Required property 'hosted_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_doc(self) -> builtins.str:
        """(experimental) The index document of the website.

        :stability: experimental
        """
        result = self._values.get("index_doc")
        assert result is not None, "Required property 'index_doc' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def website_folder(self) -> builtins.str:
        """(experimental) Local path to the website folder you want to deploy on S3.

        :stability: experimental
        """
        result = self._values.get("website_folder")
        assert result is not None, "Required property 'website_folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_doc(self) -> typing.Optional[builtins.str]:
        """(experimental) The error document of the website.

        :default: - No error document.

        :stability: experimental
        """
        result = self._values.get("error_doc")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicSiteConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-simplewebsite-deploy.CloudfrontSiteConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone": "hostedZone",
        "index_doc": "indexDoc",
        "website_folder": "websiteFolder",
        "domain": "domain",
        "error_doc": "errorDoc",
        "price_class": "priceClass",
        "sub_domain": "subDomain",
    },
)
class CloudfrontSiteConfiguration:
    def __init__(
        self,
        *,
        hosted_zone: builtins.str,
        index_doc: builtins.str,
        website_folder: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        error_doc: typing.Optional[builtins.str] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        sub_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param hosted_zone: (experimental) Hosted Zone used to create the DNS record for the website.
        :param index_doc: (experimental) The index document of the website.
        :param website_folder: (experimental) Local path to the website folder you want to deploy on S3.
        :param domain: (experimental) Used to deploy a Cloudfront site with a single domain. e.g. sample.example.com If you include a value for both domain and subDomain, an error will be thrown. Default: - no value
        :param error_doc: (experimental) The error document of the website. Default: - No error document.
        :param price_class: (experimental) The price class determines how many edge locations CloudFront will use for your distribution. Default: PriceClass.PRICE_CLASS_100.
        :param sub_domain: (experimental) The sub-domain name you want to deploy. e.g. www.example.com If you include a value for both domain and subDomain, an error will be thrown. Default: - no value

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "hosted_zone": hosted_zone,
            "index_doc": index_doc,
            "website_folder": website_folder,
        }
        if domain is not None:
            self._values["domain"] = domain
        if error_doc is not None:
            self._values["error_doc"] = error_doc
        if price_class is not None:
            self._values["price_class"] = price_class
        if sub_domain is not None:
            self._values["sub_domain"] = sub_domain

    @builtins.property
    def hosted_zone(self) -> builtins.str:
        """(experimental) Hosted Zone used to create the DNS record for the website.

        :stability: experimental
        """
        result = self._values.get("hosted_zone")
        assert result is not None, "Required property 'hosted_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_doc(self) -> builtins.str:
        """(experimental) The index document of the website.

        :stability: experimental
        """
        result = self._values.get("index_doc")
        assert result is not None, "Required property 'index_doc' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def website_folder(self) -> builtins.str:
        """(experimental) Local path to the website folder you want to deploy on S3.

        :stability: experimental
        """
        result = self._values.get("website_folder")
        assert result is not None, "Required property 'website_folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        """(experimental) Used to deploy a Cloudfront site with a single domain.

        e.g. sample.example.com
        If you include a value for both domain and subDomain,
        an error will be thrown.

        :default: - no value

        :stability: experimental
        """
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_doc(self) -> typing.Optional[builtins.str]:
        """(experimental) The error document of the website.

        :default: - No error document.

        :stability: experimental
        """
        result = self._values.get("error_doc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def price_class(self) -> typing.Optional[aws_cdk.aws_cloudfront.PriceClass]:
        """(experimental) The price class determines how many edge locations CloudFront will use for your distribution.

        :default: PriceClass.PRICE_CLASS_100.

        :see: https://aws.amazon.com/cloudfront/pricing/.
        :stability: experimental
        """
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.PriceClass], result)

    @builtins.property
    def sub_domain(self) -> typing.Optional[builtins.str]:
        """(experimental) The sub-domain name you want to deploy.

        e.g. www.example.com
        If you include a value for both domain and subDomain,
        an error will be thrown.

        :default: - no value

        :stability: experimental
        """
        result = self._values.get("sub_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontSiteConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CreateBasicSite(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-simplewebsite-deploy.CreateBasicSite",
):
    """
    :stability: experimental
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        hosted_zone: builtins.str,
        index_doc: builtins.str,
        website_folder: builtins.str,
        error_doc: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param hosted_zone: (experimental) Hosted Zone used to create the DNS record for the website.
        :param index_doc: (experimental) The index document of the website.
        :param website_folder: (experimental) Local path to the website folder you want to deploy on S3.
        :param error_doc: (experimental) The error document of the website. Default: - No error document.

        :stability: experimental
        """
        props = BasicSiteConfiguration(
            hosted_zone=hosted_zone,
            index_doc=index_doc,
            website_folder=website_folder,
            error_doc=error_doc,
        )

        jsii.create(CreateBasicSite, self, [scope, id, props])


class CreateCloudfrontSite(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-simplewebsite-deploy.CreateCloudfrontSite",
):
    """
    :stability: experimental
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        hosted_zone: builtins.str,
        index_doc: builtins.str,
        website_folder: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        error_doc: typing.Optional[builtins.str] = None,
        price_class: typing.Optional[aws_cdk.aws_cloudfront.PriceClass] = None,
        sub_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param hosted_zone: (experimental) Hosted Zone used to create the DNS record for the website.
        :param index_doc: (experimental) The index document of the website.
        :param website_folder: (experimental) Local path to the website folder you want to deploy on S3.
        :param domain: (experimental) Used to deploy a Cloudfront site with a single domain. e.g. sample.example.com If you include a value for both domain and subDomain, an error will be thrown. Default: - no value
        :param error_doc: (experimental) The error document of the website. Default: - No error document.
        :param price_class: (experimental) The price class determines how many edge locations CloudFront will use for your distribution. Default: PriceClass.PRICE_CLASS_100.
        :param sub_domain: (experimental) The sub-domain name you want to deploy. e.g. www.example.com If you include a value for both domain and subDomain, an error will be thrown. Default: - no value

        :stability: experimental
        """
        props = CloudfrontSiteConfiguration(
            hosted_zone=hosted_zone,
            index_doc=index_doc,
            website_folder=website_folder,
            domain=domain,
            error_doc=error_doc,
            price_class=price_class,
            sub_domain=sub_domain,
        )

        jsii.create(CreateCloudfrontSite, self, [scope, id, props])


__all__ = [
    "BasicSiteConfiguration",
    "CloudfrontSiteConfiguration",
    "CreateBasicSite",
    "CreateCloudfrontSite",
]

publication.publish()
