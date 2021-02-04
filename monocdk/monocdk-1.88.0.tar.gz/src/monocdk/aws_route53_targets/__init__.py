import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import IConstruct as _IConstruct_5a0f9c5e
from ..aws_apigateway import (
    IDomainName as _IDomainName_2f71106c, RestApi as _RestApi_79aff3d1
)
from ..aws_apigatewayv2 import IDomainName as _IDomainName_a8672666
from ..aws_cloudfront import IDistribution as _IDistribution_685deca5
from ..aws_cognito import UserPoolDomain as _UserPoolDomain_18478017
from ..aws_ec2 import IInterfaceVpcEndpoint as _IInterfaceVpcEndpoint_6081623d
from ..aws_elasticloadbalancing import LoadBalancer as _LoadBalancer_a7de240f
from ..aws_elasticloadbalancingv2 import ILoadBalancerV2 as _ILoadBalancerV2_f1c75d72
from ..aws_route53 import (
    AliasRecordTargetConfig as _AliasRecordTargetConfig_5788d785,
    IAliasRecordTarget as _IAliasRecordTarget_f7c401c2,
    IRecordSet as _IRecordSet_133a645a,
)
from ..aws_s3 import IBucket as _IBucket_73486e29


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class ApiGatewayDomain(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.ApiGatewayDomain",
):
    """(experimental) Defines an API Gateway domain name as the alias target.

    Use the ``ApiGateway`` class if you wish to map the alias to an REST API with a
    domain name defined through the ``RestApiProps.domainName`` prop.

    :stability: experimental
    """

    def __init__(self, domain_name: _IDomainName_2f71106c) -> None:
        """
        :param domain_name: -

        :stability: experimental
        """
        jsii.create(ApiGatewayDomain, self, [domain_name])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class ApiGatewayv2Domain(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.ApiGatewayv2Domain",
):
    """(experimental) Defines an API Gateway V2 domain name as the alias target.

    :stability: experimental
    """

    def __init__(self, domain_name: _IDomainName_a8672666) -> None:
        """
        :param domain_name: -

        :stability: experimental
        """
        jsii.create(ApiGatewayv2Domain, self, [domain_name])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class BucketWebsiteTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.BucketWebsiteTarget",
):
    """(experimental) Use a S3 as an alias record target.

    :stability: experimental
    """

    def __init__(self, bucket: _IBucket_73486e29) -> None:
        """
        :param bucket: -

        :stability: experimental
        """
        jsii.create(BucketWebsiteTarget, self, [bucket])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class ClassicLoadBalancerTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.ClassicLoadBalancerTarget",
):
    """(experimental) Use a classic ELB as an alias record target.

    :stability: experimental
    """

    def __init__(self, load_balancer: _LoadBalancer_a7de240f) -> None:
        """
        :param load_balancer: -

        :stability: experimental
        """
        jsii.create(ClassicLoadBalancerTarget, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class CloudFrontTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.CloudFrontTarget",
):
    """(experimental) Use a CloudFront Distribution as an alias record target.

    :stability: experimental
    """

    def __init__(self, distribution: _IDistribution_685deca5) -> None:
        """
        :param distribution: -

        :stability: experimental
        """
        jsii.create(CloudFrontTarget, self, [distribution])

    @jsii.member(jsii_name="getHostedZoneId")
    @builtins.classmethod
    def get_hosted_zone_id(cls, scope: _IConstruct_5a0f9c5e) -> builtins.str:
        """(experimental) Get the hosted zone id for the current scope.

        :param scope: - scope in which this resource is defined.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "getHostedZoneId", [scope])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CLOUDFRONT_ZONE_ID")
    def CLOUDFRONT_ZONE_ID(cls) -> builtins.str:
        """(experimental) The hosted zone Id if using an alias record in Route53.

        This value never changes.

        :stability: experimental
        """
        return jsii.sget(cls, "CLOUDFRONT_ZONE_ID")


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class InterfaceVpcEndpointTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.InterfaceVpcEndpointTarget",
):
    """(experimental) Set an InterfaceVpcEndpoint as a target for an ARecord.

    :stability: experimental
    """

    def __init__(self, vpc_endpoint: _IInterfaceVpcEndpoint_6081623d) -> None:
        """
        :param vpc_endpoint: -

        :stability: experimental
        """
        jsii.create(InterfaceVpcEndpointTarget, self, [vpc_endpoint])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class LoadBalancerTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.LoadBalancerTarget",
):
    """(experimental) Use an ELBv2 as an alias record target.

    :stability: experimental
    """

    def __init__(self, load_balancer: _ILoadBalancerV2_f1c75d72) -> None:
        """
        :param load_balancer: -

        :stability: experimental
        """
        jsii.create(LoadBalancerTarget, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(_IAliasRecordTarget_f7c401c2)
class UserPoolDomainTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.UserPoolDomainTarget",
):
    """(experimental) Use a user pool domain as an alias record target.

    :stability: experimental
    """

    def __init__(self, domain: _UserPoolDomain_18478017) -> None:
        """
        :param domain: -

        :stability: experimental
        """
        jsii.create(UserPoolDomainTarget, self, [domain])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: _IRecordSet_133a645a) -> _AliasRecordTargetConfig_5788d785:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_record])


class ApiGateway(
    ApiGatewayDomain,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53_targets.ApiGateway",
):
    """(experimental) Defines an API Gateway REST API as the alias target. Requires that the domain name will be defined through ``RestApiProps.domainName``.

    You can direct the alias to any ``apigateway.DomainName`` resource through the
    ``ApiGatewayDomain`` class.

    :stability: experimental
    """

    def __init__(self, api: _RestApi_79aff3d1) -> None:
        """
        :param api: -

        :stability: experimental
        """
        jsii.create(ApiGateway, self, [api])


__all__ = [
    "ApiGateway",
    "ApiGatewayDomain",
    "ApiGatewayv2Domain",
    "BucketWebsiteTarget",
    "ClassicLoadBalancerTarget",
    "CloudFrontTarget",
    "InterfaceVpcEndpointTarget",
    "LoadBalancerTarget",
    "UserPoolDomainTarget",
]

publication.publish()
