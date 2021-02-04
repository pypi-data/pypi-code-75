import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_e0a482dc,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    Resource as _Resource_abff4495,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_ec2 import (
    IVpc as _IVpc_6d1f76c4, IVpcEndpointService as _IVpcEndpointService_30207308
)
from ..aws_iam import (
    IPrincipal as _IPrincipal_93b48231,
    IRole as _IRole_59af6f50,
    Role as _Role_95e2afa4,
)


@jsii.data_type(
    jsii_type="monocdk.aws_route53.AliasRecordTargetConfig",
    jsii_struct_bases=[],
    name_mapping={"dns_name": "dnsName", "hosted_zone_id": "hostedZoneId"},
)
class AliasRecordTargetConfig:
    def __init__(self, *, dns_name: builtins.str, hosted_zone_id: builtins.str) -> None:
        """(experimental) Represents the properties of an alias target destination.

        :param dns_name: (experimental) DNS name of the target.
        :param hosted_zone_id: (experimental) Hosted zone ID of the target.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "dns_name": dns_name,
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def dns_name(self) -> builtins.str:
        """(experimental) DNS name of the target.

        :stability: experimental
        """
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return result

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        """(experimental) Hosted zone ID of the target.

        :stability: experimental
        """
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasRecordTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CaaRecordValue",
    jsii_struct_bases=[],
    name_mapping={"flag": "flag", "tag": "tag", "value": "value"},
)
class CaaRecordValue:
    def __init__(
        self,
        *,
        flag: jsii.Number,
        tag: "CaaTag",
        value: builtins.str,
    ) -> None:
        """(experimental) Properties for a CAA record value.

        :param flag: (experimental) The flag.
        :param tag: (experimental) The tag.
        :param value: (experimental) The value associated with the tag.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "flag": flag,
            "tag": tag,
            "value": value,
        }

    @builtins.property
    def flag(self) -> jsii.Number:
        """(experimental) The flag.

        :stability: experimental
        """
        result = self._values.get("flag")
        assert result is not None, "Required property 'flag' is missing"
        return result

    @builtins.property
    def tag(self) -> "CaaTag":
        """(experimental) The tag.

        :stability: experimental
        """
        result = self._values.get("tag")
        assert result is not None, "Required property 'tag' is missing"
        return result

    @builtins.property
    def value(self) -> builtins.str:
        """(experimental) The value associated with the tag.

        :stability: experimental
        """
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaaRecordValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_route53.CaaTag")
class CaaTag(enum.Enum):
    """(experimental) The CAA tag.

    :stability: experimental
    """

    ISSUE = "ISSUE"
    """(experimental) Explicity authorizes a single certificate authority to issue a certificate (any type) for the hostname.

    :stability: experimental
    """
    ISSUEWILD = "ISSUEWILD"
    """(experimental) Explicity authorizes a single certificate authority to issue a wildcard certificate (and only wildcard) for the hostname.

    :stability: experimental
    """
    IODEF = "IODEF"
    """(experimental) Specifies a URL to which a certificate authority may report policy violations.

    :stability: experimental
    """


@jsii.implements(_IInspectable_82c04a63)
class CfnDNSSEC(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CfnDNSSEC",
):
    """A CloudFormation ``AWS::Route53::DNSSEC``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html
    :cloudformationResource: AWS::Route53::DNSSEC
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
    ) -> None:
        """Create a new ``AWS::Route53::DNSSEC``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param hosted_zone_id: ``AWS::Route53::DNSSEC.HostedZoneId``.
        """
        props = CfnDNSSECProps(hosted_zone_id=hosted_zone_id)

        jsii.create(CfnDNSSEC, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        """``AWS::Route53::DNSSEC.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html#cfn-route53-dnssec-hostedzoneid
        """
        return jsii.get(self, "hostedZoneId")

    @hosted_zone_id.setter # type: ignore
    def hosted_zone_id(self, value: builtins.str) -> None:
        jsii.set(self, "hostedZoneId", value)


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CfnDNSSECProps",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId"},
)
class CfnDNSSECProps:
    def __init__(self, *, hosted_zone_id: builtins.str) -> None:
        """Properties for defining a ``AWS::Route53::DNSSEC``.

        :param hosted_zone_id: ``AWS::Route53::DNSSEC.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        """``AWS::Route53::DNSSEC.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html#cfn-route53-dnssec-hostedzoneid
        """
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDNSSECProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnHealthCheck(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CfnHealthCheck",
):
    """A CloudFormation ``AWS::Route53::HealthCheck``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
    :cloudformationResource: AWS::Route53::HealthCheck
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        health_check_config: typing.Union["CfnHealthCheck.HealthCheckConfigProperty", _IResolvable_a771d0ef],
        health_check_tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHealthCheck.HealthCheckTagProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::Route53::HealthCheck``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param health_check_config: ``AWS::Route53::HealthCheck.HealthCheckConfig``.
        :param health_check_tags: ``AWS::Route53::HealthCheck.HealthCheckTags``.
        """
        props = CfnHealthCheckProps(
            health_check_config=health_check_config,
            health_check_tags=health_check_tags,
        )

        jsii.create(CfnHealthCheck, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrHealthCheckId")
    def attr_health_check_id(self) -> builtins.str:
        """
        :cloudformationAttribute: HealthCheckId
        """
        return jsii.get(self, "attrHealthCheckId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="healthCheckConfig")
    def health_check_config(
        self,
    ) -> typing.Union["CfnHealthCheck.HealthCheckConfigProperty", _IResolvable_a771d0ef]:
        """``AWS::Route53::HealthCheck.HealthCheckConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
        """
        return jsii.get(self, "healthCheckConfig")

    @health_check_config.setter # type: ignore
    def health_check_config(
        self,
        value: typing.Union["CfnHealthCheck.HealthCheckConfigProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "healthCheckConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="healthCheckTags")
    def health_check_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHealthCheck.HealthCheckTagProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::Route53::HealthCheck.HealthCheckTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
        """
        return jsii.get(self, "healthCheckTags")

    @health_check_tags.setter # type: ignore
    def health_check_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHealthCheck.HealthCheckTagProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "healthCheckTags", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHealthCheck.AlarmIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "region": "region"},
    )
    class AlarmIdentifierProperty:
        def __init__(self, *, name: builtins.str, region: builtins.str) -> None:
            """
            :param name: ``CfnHealthCheck.AlarmIdentifierProperty.Name``.
            :param region: ``CfnHealthCheck.AlarmIdentifierProperty.Region``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "region": region,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnHealthCheck.AlarmIdentifierProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def region(self) -> builtins.str:
            """``CfnHealthCheck.AlarmIdentifierProperty.Region``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-region
            """
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHealthCheck.HealthCheckConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "alarm_identifier": "alarmIdentifier",
            "child_health_checks": "childHealthChecks",
            "enable_sni": "enableSni",
            "failure_threshold": "failureThreshold",
            "fully_qualified_domain_name": "fullyQualifiedDomainName",
            "health_threshold": "healthThreshold",
            "insufficient_data_health_status": "insufficientDataHealthStatus",
            "inverted": "inverted",
            "ip_address": "ipAddress",
            "measure_latency": "measureLatency",
            "port": "port",
            "regions": "regions",
            "request_interval": "requestInterval",
            "resource_path": "resourcePath",
            "search_string": "searchString",
        },
    )
    class HealthCheckConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            alarm_identifier: typing.Optional[typing.Union["CfnHealthCheck.AlarmIdentifierProperty", _IResolvable_a771d0ef]] = None,
            child_health_checks: typing.Optional[typing.List[builtins.str]] = None,
            enable_sni: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            failure_threshold: typing.Optional[jsii.Number] = None,
            fully_qualified_domain_name: typing.Optional[builtins.str] = None,
            health_threshold: typing.Optional[jsii.Number] = None,
            insufficient_data_health_status: typing.Optional[builtins.str] = None,
            inverted: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            ip_address: typing.Optional[builtins.str] = None,
            measure_latency: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            port: typing.Optional[jsii.Number] = None,
            regions: typing.Optional[typing.List[builtins.str]] = None,
            request_interval: typing.Optional[jsii.Number] = None,
            resource_path: typing.Optional[builtins.str] = None,
            search_string: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param type: ``CfnHealthCheck.HealthCheckConfigProperty.Type``.
            :param alarm_identifier: ``CfnHealthCheck.HealthCheckConfigProperty.AlarmIdentifier``.
            :param child_health_checks: ``CfnHealthCheck.HealthCheckConfigProperty.ChildHealthChecks``.
            :param enable_sni: ``CfnHealthCheck.HealthCheckConfigProperty.EnableSNI``.
            :param failure_threshold: ``CfnHealthCheck.HealthCheckConfigProperty.FailureThreshold``.
            :param fully_qualified_domain_name: ``CfnHealthCheck.HealthCheckConfigProperty.FullyQualifiedDomainName``.
            :param health_threshold: ``CfnHealthCheck.HealthCheckConfigProperty.HealthThreshold``.
            :param insufficient_data_health_status: ``CfnHealthCheck.HealthCheckConfigProperty.InsufficientDataHealthStatus``.
            :param inverted: ``CfnHealthCheck.HealthCheckConfigProperty.Inverted``.
            :param ip_address: ``CfnHealthCheck.HealthCheckConfigProperty.IPAddress``.
            :param measure_latency: ``CfnHealthCheck.HealthCheckConfigProperty.MeasureLatency``.
            :param port: ``CfnHealthCheck.HealthCheckConfigProperty.Port``.
            :param regions: ``CfnHealthCheck.HealthCheckConfigProperty.Regions``.
            :param request_interval: ``CfnHealthCheck.HealthCheckConfigProperty.RequestInterval``.
            :param resource_path: ``CfnHealthCheck.HealthCheckConfigProperty.ResourcePath``.
            :param search_string: ``CfnHealthCheck.HealthCheckConfigProperty.SearchString``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if alarm_identifier is not None:
                self._values["alarm_identifier"] = alarm_identifier
            if child_health_checks is not None:
                self._values["child_health_checks"] = child_health_checks
            if enable_sni is not None:
                self._values["enable_sni"] = enable_sni
            if failure_threshold is not None:
                self._values["failure_threshold"] = failure_threshold
            if fully_qualified_domain_name is not None:
                self._values["fully_qualified_domain_name"] = fully_qualified_domain_name
            if health_threshold is not None:
                self._values["health_threshold"] = health_threshold
            if insufficient_data_health_status is not None:
                self._values["insufficient_data_health_status"] = insufficient_data_health_status
            if inverted is not None:
                self._values["inverted"] = inverted
            if ip_address is not None:
                self._values["ip_address"] = ip_address
            if measure_latency is not None:
                self._values["measure_latency"] = measure_latency
            if port is not None:
                self._values["port"] = port
            if regions is not None:
                self._values["regions"] = regions
            if request_interval is not None:
                self._values["request_interval"] = request_interval
            if resource_path is not None:
                self._values["resource_path"] = resource_path
            if search_string is not None:
                self._values["search_string"] = search_string

        @builtins.property
        def type(self) -> builtins.str:
            """``CfnHealthCheck.HealthCheckConfigProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-type
            """
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return result

        @builtins.property
        def alarm_identifier(
            self,
        ) -> typing.Optional[typing.Union["CfnHealthCheck.AlarmIdentifierProperty", _IResolvable_a771d0ef]]:
            """``CfnHealthCheck.HealthCheckConfigProperty.AlarmIdentifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-alarmidentifier
            """
            result = self._values.get("alarm_identifier")
            return result

        @builtins.property
        def child_health_checks(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnHealthCheck.HealthCheckConfigProperty.ChildHealthChecks``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-childhealthchecks
            """
            result = self._values.get("child_health_checks")
            return result

        @builtins.property
        def enable_sni(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnHealthCheck.HealthCheckConfigProperty.EnableSNI``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-enablesni
            """
            result = self._values.get("enable_sni")
            return result

        @builtins.property
        def failure_threshold(self) -> typing.Optional[jsii.Number]:
            """``CfnHealthCheck.HealthCheckConfigProperty.FailureThreshold``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-failurethreshold
            """
            result = self._values.get("failure_threshold")
            return result

        @builtins.property
        def fully_qualified_domain_name(self) -> typing.Optional[builtins.str]:
            """``CfnHealthCheck.HealthCheckConfigProperty.FullyQualifiedDomainName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-fullyqualifieddomainname
            """
            result = self._values.get("fully_qualified_domain_name")
            return result

        @builtins.property
        def health_threshold(self) -> typing.Optional[jsii.Number]:
            """``CfnHealthCheck.HealthCheckConfigProperty.HealthThreshold``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-healththreshold
            """
            result = self._values.get("health_threshold")
            return result

        @builtins.property
        def insufficient_data_health_status(self) -> typing.Optional[builtins.str]:
            """``CfnHealthCheck.HealthCheckConfigProperty.InsufficientDataHealthStatus``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-insufficientdatahealthstatus
            """
            result = self._values.get("insufficient_data_health_status")
            return result

        @builtins.property
        def inverted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnHealthCheck.HealthCheckConfigProperty.Inverted``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-inverted
            """
            result = self._values.get("inverted")
            return result

        @builtins.property
        def ip_address(self) -> typing.Optional[builtins.str]:
            """``CfnHealthCheck.HealthCheckConfigProperty.IPAddress``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-ipaddress
            """
            result = self._values.get("ip_address")
            return result

        @builtins.property
        def measure_latency(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnHealthCheck.HealthCheckConfigProperty.MeasureLatency``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-measurelatency
            """
            result = self._values.get("measure_latency")
            return result

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            """``CfnHealthCheck.HealthCheckConfigProperty.Port``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-port
            """
            result = self._values.get("port")
            return result

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnHealthCheck.HealthCheckConfigProperty.Regions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-regions
            """
            result = self._values.get("regions")
            return result

        @builtins.property
        def request_interval(self) -> typing.Optional[jsii.Number]:
            """``CfnHealthCheck.HealthCheckConfigProperty.RequestInterval``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-requestinterval
            """
            result = self._values.get("request_interval")
            return result

        @builtins.property
        def resource_path(self) -> typing.Optional[builtins.str]:
            """``CfnHealthCheck.HealthCheckConfigProperty.ResourcePath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-resourcepath
            """
            result = self._values.get("resource_path")
            return result

        @builtins.property
        def search_string(self) -> typing.Optional[builtins.str]:
            """``CfnHealthCheck.HealthCheckConfigProperty.SearchString``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-searchstring
            """
            result = self._values.get("search_string")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHealthCheck.HealthCheckTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class HealthCheckTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            """
            :param key: ``CfnHealthCheck.HealthCheckTagProperty.Key``.
            :param value: ``CfnHealthCheck.HealthCheckTagProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            """``CfnHealthCheck.HealthCheckTagProperty.Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthcheck-healthchecktag-key
            """
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return result

        @builtins.property
        def value(self) -> builtins.str:
            """``CfnHealthCheck.HealthCheckTagProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthcheck-healthchecktag-value
            """
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CfnHealthCheckProps",
    jsii_struct_bases=[],
    name_mapping={
        "health_check_config": "healthCheckConfig",
        "health_check_tags": "healthCheckTags",
    },
)
class CfnHealthCheckProps:
    def __init__(
        self,
        *,
        health_check_config: typing.Union[CfnHealthCheck.HealthCheckConfigProperty, _IResolvable_a771d0ef],
        health_check_tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnHealthCheck.HealthCheckTagProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Route53::HealthCheck``.

        :param health_check_config: ``AWS::Route53::HealthCheck.HealthCheckConfig``.
        :param health_check_tags: ``AWS::Route53::HealthCheck.HealthCheckTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "health_check_config": health_check_config,
        }
        if health_check_tags is not None:
            self._values["health_check_tags"] = health_check_tags

    @builtins.property
    def health_check_config(
        self,
    ) -> typing.Union[CfnHealthCheck.HealthCheckConfigProperty, _IResolvable_a771d0ef]:
        """``AWS::Route53::HealthCheck.HealthCheckConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
        """
        result = self._values.get("health_check_config")
        assert result is not None, "Required property 'health_check_config' is missing"
        return result

    @builtins.property
    def health_check_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnHealthCheck.HealthCheckTagProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::Route53::HealthCheck.HealthCheckTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
        """
        result = self._values.get("health_check_tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHealthCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnHostedZone(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CfnHostedZone",
):
    """A CloudFormation ``AWS::Route53::HostedZone``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
    :cloudformationResource: AWS::Route53::HostedZone
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        hosted_zone_config: typing.Optional[typing.Union["CfnHostedZone.HostedZoneConfigProperty", _IResolvable_a771d0ef]] = None,
        hosted_zone_tags: typing.Optional[typing.List["CfnHostedZone.HostedZoneTagProperty"]] = None,
        query_logging_config: typing.Optional[typing.Union["CfnHostedZone.QueryLoggingConfigProperty", _IResolvable_a771d0ef]] = None,
        vpcs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHostedZone.VPCProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::Route53::HostedZone``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Route53::HostedZone.Name``.
        :param hosted_zone_config: ``AWS::Route53::HostedZone.HostedZoneConfig``.
        :param hosted_zone_tags: ``AWS::Route53::HostedZone.HostedZoneTags``.
        :param query_logging_config: ``AWS::Route53::HostedZone.QueryLoggingConfig``.
        :param vpcs: ``AWS::Route53::HostedZone.VPCs``.
        """
        props = CfnHostedZoneProps(
            name=name,
            hosted_zone_config=hosted_zone_config,
            hosted_zone_tags=hosted_zone_tags,
            query_logging_config=query_logging_config,
            vpcs=vpcs,
        )

        jsii.create(CfnHostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        """
        :cloudformationAttribute: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrNameServers")
    def attr_name_servers(self) -> typing.List[builtins.str]:
        """
        :cloudformationAttribute: NameServers
        """
        return jsii.get(self, "attrNameServers")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::Route53::HostedZone.HostedZoneTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzonetags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Route53::HostedZone.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneConfig")
    def hosted_zone_config(
        self,
    ) -> typing.Optional[typing.Union["CfnHostedZone.HostedZoneConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Route53::HostedZone.HostedZoneConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzoneconfig
        """
        return jsii.get(self, "hostedZoneConfig")

    @hosted_zone_config.setter # type: ignore
    def hosted_zone_config(
        self,
        value: typing.Optional[typing.Union["CfnHostedZone.HostedZoneConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "hostedZoneConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="queryLoggingConfig")
    def query_logging_config(
        self,
    ) -> typing.Optional[typing.Union["CfnHostedZone.QueryLoggingConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Route53::HostedZone.QueryLoggingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-queryloggingconfig
        """
        return jsii.get(self, "queryLoggingConfig")

    @query_logging_config.setter # type: ignore
    def query_logging_config(
        self,
        value: typing.Optional[typing.Union["CfnHostedZone.QueryLoggingConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "queryLoggingConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="vpcs")
    def vpcs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHostedZone.VPCProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::Route53::HostedZone.VPCs``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-vpcs
        """
        return jsii.get(self, "vpcs")

    @vpcs.setter # type: ignore
    def vpcs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHostedZone.VPCProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "vpcs", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHostedZone.HostedZoneConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"comment": "comment"},
    )
    class HostedZoneConfigProperty:
        def __init__(self, *, comment: typing.Optional[builtins.str] = None) -> None:
            """
            :param comment: ``CfnHostedZone.HostedZoneConfigProperty.Comment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if comment is not None:
                self._values["comment"] = comment

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            """``CfnHostedZone.HostedZoneConfigProperty.Comment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html#cfn-route53-hostedzone-hostedzoneconfig-comment
            """
            result = self._values.get("comment")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HostedZoneConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHostedZone.HostedZoneTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class HostedZoneTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            """
            :param key: ``CfnHostedZone.HostedZoneTagProperty.Key``.
            :param value: ``CfnHostedZone.HostedZoneTagProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            """``CfnHostedZone.HostedZoneTagProperty.Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html#cfn-route53-hostedzone-hostedzonetag-key
            """
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return result

        @builtins.property
        def value(self) -> builtins.str:
            """``CfnHostedZone.HostedZoneTagProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html#cfn-route53-hostedzone-hostedzonetag-value
            """
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HostedZoneTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHostedZone.QueryLoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs_log_group_arn": "cloudWatchLogsLogGroupArn"},
    )
    class QueryLoggingConfigProperty:
        def __init__(self, *, cloud_watch_logs_log_group_arn: builtins.str) -> None:
            """
            :param cloud_watch_logs_log_group_arn: ``CfnHostedZone.QueryLoggingConfigProperty.CloudWatchLogsLogGroupArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cloud_watch_logs_log_group_arn": cloud_watch_logs_log_group_arn,
            }

        @builtins.property
        def cloud_watch_logs_log_group_arn(self) -> builtins.str:
            """``CfnHostedZone.QueryLoggingConfigProperty.CloudWatchLogsLogGroupArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html#cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn
            """
            result = self._values.get("cloud_watch_logs_log_group_arn")
            assert result is not None, "Required property 'cloud_watch_logs_log_group_arn' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryLoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnHostedZone.VPCProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_id": "vpcId", "vpc_region": "vpcRegion"},
    )
    class VPCProperty:
        def __init__(self, *, vpc_id: builtins.str, vpc_region: builtins.str) -> None:
            """
            :param vpc_id: ``CfnHostedZone.VPCProperty.VPCId``.
            :param vpc_region: ``CfnHostedZone.VPCProperty.VPCRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "vpc_id": vpc_id,
                "vpc_region": vpc_region,
            }

        @builtins.property
        def vpc_id(self) -> builtins.str:
            """``CfnHostedZone.VPCProperty.VPCId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html#cfn-route53-hostedzone-vpc-vpcid
            """
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return result

        @builtins.property
        def vpc_region(self) -> builtins.str:
            """``CfnHostedZone.VPCProperty.VPCRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html#cfn-route53-hostedzone-vpc-vpcregion
            """
            result = self._values.get("vpc_region")
            assert result is not None, "Required property 'vpc_region' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CfnHostedZoneProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "hosted_zone_config": "hostedZoneConfig",
        "hosted_zone_tags": "hostedZoneTags",
        "query_logging_config": "queryLoggingConfig",
        "vpcs": "vpcs",
    },
)
class CfnHostedZoneProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        hosted_zone_config: typing.Optional[typing.Union[CfnHostedZone.HostedZoneConfigProperty, _IResolvable_a771d0ef]] = None,
        hosted_zone_tags: typing.Optional[typing.List[CfnHostedZone.HostedZoneTagProperty]] = None,
        query_logging_config: typing.Optional[typing.Union[CfnHostedZone.QueryLoggingConfigProperty, _IResolvable_a771d0ef]] = None,
        vpcs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnHostedZone.VPCProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Route53::HostedZone``.

        :param name: ``AWS::Route53::HostedZone.Name``.
        :param hosted_zone_config: ``AWS::Route53::HostedZone.HostedZoneConfig``.
        :param hosted_zone_tags: ``AWS::Route53::HostedZone.HostedZoneTags``.
        :param query_logging_config: ``AWS::Route53::HostedZone.QueryLoggingConfig``.
        :param vpcs: ``AWS::Route53::HostedZone.VPCs``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if hosted_zone_config is not None:
            self._values["hosted_zone_config"] = hosted_zone_config
        if hosted_zone_tags is not None:
            self._values["hosted_zone_tags"] = hosted_zone_tags
        if query_logging_config is not None:
            self._values["query_logging_config"] = query_logging_config
        if vpcs is not None:
            self._values["vpcs"] = vpcs

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Route53::HostedZone.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def hosted_zone_config(
        self,
    ) -> typing.Optional[typing.Union[CfnHostedZone.HostedZoneConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Route53::HostedZone.HostedZoneConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzoneconfig
        """
        result = self._values.get("hosted_zone_config")
        return result

    @builtins.property
    def hosted_zone_tags(
        self,
    ) -> typing.Optional[typing.List[CfnHostedZone.HostedZoneTagProperty]]:
        """``AWS::Route53::HostedZone.HostedZoneTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzonetags
        """
        result = self._values.get("hosted_zone_tags")
        return result

    @builtins.property
    def query_logging_config(
        self,
    ) -> typing.Optional[typing.Union[CfnHostedZone.QueryLoggingConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Route53::HostedZone.QueryLoggingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-queryloggingconfig
        """
        result = self._values.get("query_logging_config")
        return result

    @builtins.property
    def vpcs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnHostedZone.VPCProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::Route53::HostedZone.VPCs``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-vpcs
        """
        result = self._values.get("vpcs")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnKeySigningKey(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CfnKeySigningKey",
):
    """A CloudFormation ``AWS::Route53::KeySigningKey``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html
    :cloudformationResource: AWS::Route53::KeySigningKey
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
        key_management_service_arn: builtins.str,
        name: builtins.str,
        status: builtins.str,
    ) -> None:
        """Create a new ``AWS::Route53::KeySigningKey``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param hosted_zone_id: ``AWS::Route53::KeySigningKey.HostedZoneId``.
        :param key_management_service_arn: ``AWS::Route53::KeySigningKey.KeyManagementServiceArn``.
        :param name: ``AWS::Route53::KeySigningKey.Name``.
        :param status: ``AWS::Route53::KeySigningKey.Status``.
        """
        props = CfnKeySigningKeyProps(
            hosted_zone_id=hosted_zone_id,
            key_management_service_arn=key_management_service_arn,
            name=name,
            status=status,
        )

        jsii.create(CfnKeySigningKey, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-hostedzoneid
        """
        return jsii.get(self, "hostedZoneId")

    @hosted_zone_id.setter # type: ignore
    def hosted_zone_id(self, value: builtins.str) -> None:
        jsii.set(self, "hostedZoneId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="keyManagementServiceArn")
    def key_management_service_arn(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.KeyManagementServiceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-keymanagementservicearn
        """
        return jsii.get(self, "keyManagementServiceArn")

    @key_management_service_arn.setter # type: ignore
    def key_management_service_arn(self, value: builtins.str) -> None:
        jsii.set(self, "keyManagementServiceArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-status
        """
        return jsii.get(self, "status")

    @status.setter # type: ignore
    def status(self, value: builtins.str) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CfnKeySigningKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_id": "hostedZoneId",
        "key_management_service_arn": "keyManagementServiceArn",
        "name": "name",
        "status": "status",
    },
)
class CfnKeySigningKeyProps:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        key_management_service_arn: builtins.str,
        name: builtins.str,
        status: builtins.str,
    ) -> None:
        """Properties for defining a ``AWS::Route53::KeySigningKey``.

        :param hosted_zone_id: ``AWS::Route53::KeySigningKey.HostedZoneId``.
        :param key_management_service_arn: ``AWS::Route53::KeySigningKey.KeyManagementServiceArn``.
        :param name: ``AWS::Route53::KeySigningKey.Name``.
        :param status: ``AWS::Route53::KeySigningKey.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "key_management_service_arn": key_management_service_arn,
            "name": name,
            "status": status,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-hostedzoneid
        """
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return result

    @builtins.property
    def key_management_service_arn(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.KeyManagementServiceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-keymanagementservicearn
        """
        result = self._values.get("key_management_service_arn")
        assert result is not None, "Required property 'key_management_service_arn' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def status(self) -> builtins.str:
        """``AWS::Route53::KeySigningKey.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-status
        """
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeySigningKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnRecordSet(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CfnRecordSet",
):
    """A CloudFormation ``AWS::Route53::RecordSet``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
    :cloudformationResource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        alias_target: typing.Optional[typing.Union["CfnRecordSet.AliasTargetProperty", _IResolvable_a771d0ef]] = None,
        comment: typing.Optional[builtins.str] = None,
        failover: typing.Optional[builtins.str] = None,
        geo_location: typing.Optional[typing.Union["CfnRecordSet.GeoLocationProperty", _IResolvable_a771d0ef]] = None,
        health_check_id: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        region: typing.Optional[builtins.str] = None,
        resource_records: typing.Optional[typing.List[builtins.str]] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::Route53::RecordSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Route53::RecordSet.Name``.
        :param type: ``AWS::Route53::RecordSet.Type``.
        :param alias_target: ``AWS::Route53::RecordSet.AliasTarget``.
        :param comment: ``AWS::Route53::RecordSet.Comment``.
        :param failover: ``AWS::Route53::RecordSet.Failover``.
        :param geo_location: ``AWS::Route53::RecordSet.GeoLocation``.
        :param health_check_id: ``AWS::Route53::RecordSet.HealthCheckId``.
        :param hosted_zone_id: ``AWS::Route53::RecordSet.HostedZoneId``.
        :param hosted_zone_name: ``AWS::Route53::RecordSet.HostedZoneName``.
        :param multi_value_answer: ``AWS::Route53::RecordSet.MultiValueAnswer``.
        :param region: ``AWS::Route53::RecordSet.Region``.
        :param resource_records: ``AWS::Route53::RecordSet.ResourceRecords``.
        :param set_identifier: ``AWS::Route53::RecordSet.SetIdentifier``.
        :param ttl: ``AWS::Route53::RecordSet.TTL``.
        :param weight: ``AWS::Route53::RecordSet.Weight``.
        """
        props = CfnRecordSetProps(
            name=name,
            type=type,
            alias_target=alias_target,
            comment=comment,
            failover=failover,
            geo_location=geo_location,
            health_check_id=health_check_id,
            hosted_zone_id=hosted_zone_id,
            hosted_zone_name=hosted_zone_name,
            multi_value_answer=multi_value_answer,
            region=region,
            resource_records=resource_records,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(CfnRecordSet, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Route53::RecordSet.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        """``AWS::Route53::RecordSet.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type
        """
        return jsii.get(self, "type")

    @type.setter # type: ignore
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="aliasTarget")
    def alias_target(
        self,
    ) -> typing.Optional[typing.Union["CfnRecordSet.AliasTargetProperty", _IResolvable_a771d0ef]]:
        """``AWS::Route53::RecordSet.AliasTarget``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget
        """
        return jsii.get(self, "aliasTarget")

    @alias_target.setter # type: ignore
    def alias_target(
        self,
        value: typing.Optional[typing.Union["CfnRecordSet.AliasTargetProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "aliasTarget", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.Comment``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment
        """
        return jsii.get(self, "comment")

    @comment.setter # type: ignore
    def comment(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "comment", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="failover")
    def failover(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.Failover``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover
        """
        return jsii.get(self, "failover")

    @failover.setter # type: ignore
    def failover(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "failover", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="geoLocation")
    def geo_location(
        self,
    ) -> typing.Optional[typing.Union["CfnRecordSet.GeoLocationProperty", _IResolvable_a771d0ef]]:
        """``AWS::Route53::RecordSet.GeoLocation``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation
        """
        return jsii.get(self, "geoLocation")

    @geo_location.setter # type: ignore
    def geo_location(
        self,
        value: typing.Optional[typing.Union["CfnRecordSet.GeoLocationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "geoLocation", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="healthCheckId")
    def health_check_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.HealthCheckId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid
        """
        return jsii.get(self, "healthCheckId")

    @health_check_id.setter # type: ignore
    def health_check_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "healthCheckId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid
        """
        return jsii.get(self, "hostedZoneId")

    @hosted_zone_id.setter # type: ignore
    def hosted_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hostedZoneId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.HostedZoneName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename
        """
        return jsii.get(self, "hostedZoneName")

    @hosted_zone_name.setter # type: ignore
    def hosted_zone_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hostedZoneName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="multiValueAnswer")
    def multi_value_answer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Route53::RecordSet.MultiValueAnswer``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer
        """
        return jsii.get(self, "multiValueAnswer")

    @multi_value_answer.setter # type: ignore
    def multi_value_answer(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "multiValueAnswer", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.Region``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region
        """
        return jsii.get(self, "region")

    @region.setter # type: ignore
    def region(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "region", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resourceRecords")
    def resource_records(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Route53::RecordSet.ResourceRecords``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords
        """
        return jsii.get(self, "resourceRecords")

    @resource_records.setter # type: ignore
    def resource_records(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "resourceRecords", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="setIdentifier")
    def set_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.SetIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier
        """
        return jsii.get(self, "setIdentifier")

    @set_identifier.setter # type: ignore
    def set_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "setIdentifier", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.TTL``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl
        """
        return jsii.get(self, "ttl")

    @ttl.setter # type: ignore
    def ttl(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ttl", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="weight")
    def weight(self) -> typing.Optional[jsii.Number]:
        """``AWS::Route53::RecordSet.Weight``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight
        """
        return jsii.get(self, "weight")

    @weight.setter # type: ignore
    def weight(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "weight", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnRecordSet.AliasTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_name": "dnsName",
            "hosted_zone_id": "hostedZoneId",
            "evaluate_target_health": "evaluateTargetHealth",
        },
    )
    class AliasTargetProperty:
        def __init__(
            self,
            *,
            dns_name: builtins.str,
            hosted_zone_id: builtins.str,
            evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param dns_name: ``CfnRecordSet.AliasTargetProperty.DNSName``.
            :param hosted_zone_id: ``CfnRecordSet.AliasTargetProperty.HostedZoneId``.
            :param evaluate_target_health: ``CfnRecordSet.AliasTargetProperty.EvaluateTargetHealth``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "dns_name": dns_name,
                "hosted_zone_id": hosted_zone_id,
            }
            if evaluate_target_health is not None:
                self._values["evaluate_target_health"] = evaluate_target_health

        @builtins.property
        def dns_name(self) -> builtins.str:
            """``CfnRecordSet.AliasTargetProperty.DNSName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-dnshostname
            """
            result = self._values.get("dns_name")
            assert result is not None, "Required property 'dns_name' is missing"
            return result

        @builtins.property
        def hosted_zone_id(self) -> builtins.str:
            """``CfnRecordSet.AliasTargetProperty.HostedZoneId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid
            """
            result = self._values.get("hosted_zone_id")
            assert result is not None, "Required property 'hosted_zone_id' is missing"
            return result

        @builtins.property
        def evaluate_target_health(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnRecordSet.AliasTargetProperty.EvaluateTargetHealth``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
            """
            result = self._values.get("evaluate_target_health")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AliasTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnRecordSet.GeoLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "continent_code": "continentCode",
            "country_code": "countryCode",
            "subdivision_code": "subdivisionCode",
        },
    )
    class GeoLocationProperty:
        def __init__(
            self,
            *,
            continent_code: typing.Optional[builtins.str] = None,
            country_code: typing.Optional[builtins.str] = None,
            subdivision_code: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param continent_code: ``CfnRecordSet.GeoLocationProperty.ContinentCode``.
            :param country_code: ``CfnRecordSet.GeoLocationProperty.CountryCode``.
            :param subdivision_code: ``CfnRecordSet.GeoLocationProperty.SubdivisionCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if continent_code is not None:
                self._values["continent_code"] = continent_code
            if country_code is not None:
                self._values["country_code"] = country_code
            if subdivision_code is not None:
                self._values["subdivision_code"] = subdivision_code

        @builtins.property
        def continent_code(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSet.GeoLocationProperty.ContinentCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-continentcode
            """
            result = self._values.get("continent_code")
            return result

        @builtins.property
        def country_code(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSet.GeoLocationProperty.CountryCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode
            """
            result = self._values.get("country_code")
            return result

        @builtins.property
        def subdivision_code(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSet.GeoLocationProperty.SubdivisionCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode
            """
            result = self._values.get("subdivision_code")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnRecordSetGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CfnRecordSetGroup",
):
    """A CloudFormation ``AWS::Route53::RecordSetGroup``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
    :cloudformationResource: AWS::Route53::RecordSetGroup
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        record_sets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnRecordSetGroup.RecordSetProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::Route53::RecordSetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param comment: ``AWS::Route53::RecordSetGroup.Comment``.
        :param hosted_zone_id: ``AWS::Route53::RecordSetGroup.HostedZoneId``.
        :param hosted_zone_name: ``AWS::Route53::RecordSetGroup.HostedZoneName``.
        :param record_sets: ``AWS::Route53::RecordSetGroup.RecordSets``.
        """
        props = CfnRecordSetGroupProps(
            comment=comment,
            hosted_zone_id=hosted_zone_id,
            hosted_zone_name=hosted_zone_name,
            record_sets=record_sets,
        )

        jsii.create(CfnRecordSetGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSetGroup.Comment``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-comment
        """
        return jsii.get(self, "comment")

    @comment.setter # type: ignore
    def comment(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "comment", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSetGroup.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzoneid
        """
        return jsii.get(self, "hostedZoneId")

    @hosted_zone_id.setter # type: ignore
    def hosted_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hostedZoneId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSetGroup.HostedZoneName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzonename
        """
        return jsii.get(self, "hostedZoneName")

    @hosted_zone_name.setter # type: ignore
    def hosted_zone_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hostedZoneName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="recordSets")
    def record_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnRecordSetGroup.RecordSetProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::Route53::RecordSetGroup.RecordSets``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-recordsets
        """
        return jsii.get(self, "recordSets")

    @record_sets.setter # type: ignore
    def record_sets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnRecordSetGroup.RecordSetProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "recordSets", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnRecordSetGroup.AliasTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_name": "dnsName",
            "hosted_zone_id": "hostedZoneId",
            "evaluate_target_health": "evaluateTargetHealth",
        },
    )
    class AliasTargetProperty:
        def __init__(
            self,
            *,
            dns_name: builtins.str,
            hosted_zone_id: builtins.str,
            evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param dns_name: ``CfnRecordSetGroup.AliasTargetProperty.DNSName``.
            :param hosted_zone_id: ``CfnRecordSetGroup.AliasTargetProperty.HostedZoneId``.
            :param evaluate_target_health: ``CfnRecordSetGroup.AliasTargetProperty.EvaluateTargetHealth``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "dns_name": dns_name,
                "hosted_zone_id": hosted_zone_id,
            }
            if evaluate_target_health is not None:
                self._values["evaluate_target_health"] = evaluate_target_health

        @builtins.property
        def dns_name(self) -> builtins.str:
            """``CfnRecordSetGroup.AliasTargetProperty.DNSName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-dnshostname
            """
            result = self._values.get("dns_name")
            assert result is not None, "Required property 'dns_name' is missing"
            return result

        @builtins.property
        def hosted_zone_id(self) -> builtins.str:
            """``CfnRecordSetGroup.AliasTargetProperty.HostedZoneId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid
            """
            result = self._values.get("hosted_zone_id")
            assert result is not None, "Required property 'hosted_zone_id' is missing"
            return result

        @builtins.property
        def evaluate_target_health(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnRecordSetGroup.AliasTargetProperty.EvaluateTargetHealth``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
            """
            result = self._values.get("evaluate_target_health")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AliasTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnRecordSetGroup.GeoLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "continent_code": "continentCode",
            "country_code": "countryCode",
            "subdivision_code": "subdivisionCode",
        },
    )
    class GeoLocationProperty:
        def __init__(
            self,
            *,
            continent_code: typing.Optional[builtins.str] = None,
            country_code: typing.Optional[builtins.str] = None,
            subdivision_code: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param continent_code: ``CfnRecordSetGroup.GeoLocationProperty.ContinentCode``.
            :param country_code: ``CfnRecordSetGroup.GeoLocationProperty.CountryCode``.
            :param subdivision_code: ``CfnRecordSetGroup.GeoLocationProperty.SubdivisionCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if continent_code is not None:
                self._values["continent_code"] = continent_code
            if country_code is not None:
                self._values["country_code"] = country_code
            if subdivision_code is not None:
                self._values["subdivision_code"] = subdivision_code

        @builtins.property
        def continent_code(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.GeoLocationProperty.ContinentCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordsetgroup-geolocation-continentcode
            """
            result = self._values.get("continent_code")
            return result

        @builtins.property
        def country_code(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.GeoLocationProperty.CountryCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode
            """
            result = self._values.get("country_code")
            return result

        @builtins.property
        def subdivision_code(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.GeoLocationProperty.SubdivisionCode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode
            """
            result = self._values.get("subdivision_code")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_route53.CfnRecordSetGroup.RecordSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "type": "type",
            "alias_target": "aliasTarget",
            "comment": "comment",
            "failover": "failover",
            "geo_location": "geoLocation",
            "health_check_id": "healthCheckId",
            "hosted_zone_id": "hostedZoneId",
            "hosted_zone_name": "hostedZoneName",
            "multi_value_answer": "multiValueAnswer",
            "region": "region",
            "resource_records": "resourceRecords",
            "set_identifier": "setIdentifier",
            "ttl": "ttl",
            "weight": "weight",
        },
    )
    class RecordSetProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            alias_target: typing.Optional[typing.Union["CfnRecordSetGroup.AliasTargetProperty", _IResolvable_a771d0ef]] = None,
            comment: typing.Optional[builtins.str] = None,
            failover: typing.Optional[builtins.str] = None,
            geo_location: typing.Optional[typing.Union["CfnRecordSetGroup.GeoLocationProperty", _IResolvable_a771d0ef]] = None,
            health_check_id: typing.Optional[builtins.str] = None,
            hosted_zone_id: typing.Optional[builtins.str] = None,
            hosted_zone_name: typing.Optional[builtins.str] = None,
            multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            region: typing.Optional[builtins.str] = None,
            resource_records: typing.Optional[typing.List[builtins.str]] = None,
            set_identifier: typing.Optional[builtins.str] = None,
            ttl: typing.Optional[builtins.str] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param name: ``CfnRecordSetGroup.RecordSetProperty.Name``.
            :param type: ``CfnRecordSetGroup.RecordSetProperty.Type``.
            :param alias_target: ``CfnRecordSetGroup.RecordSetProperty.AliasTarget``.
            :param comment: ``CfnRecordSetGroup.RecordSetProperty.Comment``.
            :param failover: ``CfnRecordSetGroup.RecordSetProperty.Failover``.
            :param geo_location: ``CfnRecordSetGroup.RecordSetProperty.GeoLocation``.
            :param health_check_id: ``CfnRecordSetGroup.RecordSetProperty.HealthCheckId``.
            :param hosted_zone_id: ``CfnRecordSetGroup.RecordSetProperty.HostedZoneId``.
            :param hosted_zone_name: ``CfnRecordSetGroup.RecordSetProperty.HostedZoneName``.
            :param multi_value_answer: ``CfnRecordSetGroup.RecordSetProperty.MultiValueAnswer``.
            :param region: ``CfnRecordSetGroup.RecordSetProperty.Region``.
            :param resource_records: ``CfnRecordSetGroup.RecordSetProperty.ResourceRecords``.
            :param set_identifier: ``CfnRecordSetGroup.RecordSetProperty.SetIdentifier``.
            :param ttl: ``CfnRecordSetGroup.RecordSetProperty.TTL``.
            :param weight: ``CfnRecordSetGroup.RecordSetProperty.Weight``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if alias_target is not None:
                self._values["alias_target"] = alias_target
            if comment is not None:
                self._values["comment"] = comment
            if failover is not None:
                self._values["failover"] = failover
            if geo_location is not None:
                self._values["geo_location"] = geo_location
            if health_check_id is not None:
                self._values["health_check_id"] = health_check_id
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id
            if hosted_zone_name is not None:
                self._values["hosted_zone_name"] = hosted_zone_name
            if multi_value_answer is not None:
                self._values["multi_value_answer"] = multi_value_answer
            if region is not None:
                self._values["region"] = region
            if resource_records is not None:
                self._values["resource_records"] = resource_records
            if set_identifier is not None:
                self._values["set_identifier"] = set_identifier
            if ttl is not None:
                self._values["ttl"] = ttl
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnRecordSetGroup.RecordSetProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def type(self) -> builtins.str:
            """``CfnRecordSetGroup.RecordSetProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type
            """
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return result

        @builtins.property
        def alias_target(
            self,
        ) -> typing.Optional[typing.Union["CfnRecordSetGroup.AliasTargetProperty", _IResolvable_a771d0ef]]:
            """``CfnRecordSetGroup.RecordSetProperty.AliasTarget``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget
            """
            result = self._values.get("alias_target")
            return result

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.Comment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment
            """
            result = self._values.get("comment")
            return result

        @builtins.property
        def failover(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.Failover``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover
            """
            result = self._values.get("failover")
            return result

        @builtins.property
        def geo_location(
            self,
        ) -> typing.Optional[typing.Union["CfnRecordSetGroup.GeoLocationProperty", _IResolvable_a771d0ef]]:
            """``CfnRecordSetGroup.RecordSetProperty.GeoLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation
            """
            result = self._values.get("geo_location")
            return result

        @builtins.property
        def health_check_id(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.HealthCheckId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid
            """
            result = self._values.get("health_check_id")
            return result

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.HostedZoneId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid
            """
            result = self._values.get("hosted_zone_id")
            return result

        @builtins.property
        def hosted_zone_name(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.HostedZoneName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename
            """
            result = self._values.get("hosted_zone_name")
            return result

        @builtins.property
        def multi_value_answer(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnRecordSetGroup.RecordSetProperty.MultiValueAnswer``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer
            """
            result = self._values.get("multi_value_answer")
            return result

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.Region``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region
            """
            result = self._values.get("region")
            return result

        @builtins.property
        def resource_records(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnRecordSetGroup.RecordSetProperty.ResourceRecords``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords
            """
            result = self._values.get("resource_records")
            return result

        @builtins.property
        def set_identifier(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.SetIdentifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier
            """
            result = self._values.get("set_identifier")
            return result

        @builtins.property
        def ttl(self) -> typing.Optional[builtins.str]:
            """``CfnRecordSetGroup.RecordSetProperty.TTL``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl
            """
            result = self._values.get("ttl")
            return result

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            """``CfnRecordSetGroup.RecordSetProperty.Weight``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight
            """
            result = self._values.get("weight")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CfnRecordSetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "hosted_zone_id": "hostedZoneId",
        "hosted_zone_name": "hostedZoneName",
        "record_sets": "recordSets",
    },
)
class CfnRecordSetGroupProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        record_sets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnRecordSetGroup.RecordSetProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Route53::RecordSetGroup``.

        :param comment: ``AWS::Route53::RecordSetGroup.Comment``.
        :param hosted_zone_id: ``AWS::Route53::RecordSetGroup.HostedZoneId``.
        :param hosted_zone_name: ``AWS::Route53::RecordSetGroup.HostedZoneName``.
        :param record_sets: ``AWS::Route53::RecordSetGroup.RecordSets``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if hosted_zone_id is not None:
            self._values["hosted_zone_id"] = hosted_zone_id
        if hosted_zone_name is not None:
            self._values["hosted_zone_name"] = hosted_zone_name
        if record_sets is not None:
            self._values["record_sets"] = record_sets

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSetGroup.Comment``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-comment
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSetGroup.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzoneid
        """
        result = self._values.get("hosted_zone_id")
        return result

    @builtins.property
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSetGroup.HostedZoneName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzonename
        """
        result = self._values.get("hosted_zone_name")
        return result

    @builtins.property
    def record_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnRecordSetGroup.RecordSetProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::Route53::RecordSetGroup.RecordSets``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-recordsets
        """
        result = self._values.get("record_sets")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordSetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CfnRecordSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "alias_target": "aliasTarget",
        "comment": "comment",
        "failover": "failover",
        "geo_location": "geoLocation",
        "health_check_id": "healthCheckId",
        "hosted_zone_id": "hostedZoneId",
        "hosted_zone_name": "hostedZoneName",
        "multi_value_answer": "multiValueAnswer",
        "region": "region",
        "resource_records": "resourceRecords",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
    },
)
class CfnRecordSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        alias_target: typing.Optional[typing.Union[CfnRecordSet.AliasTargetProperty, _IResolvable_a771d0ef]] = None,
        comment: typing.Optional[builtins.str] = None,
        failover: typing.Optional[builtins.str] = None,
        geo_location: typing.Optional[typing.Union[CfnRecordSet.GeoLocationProperty, _IResolvable_a771d0ef]] = None,
        health_check_id: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        region: typing.Optional[builtins.str] = None,
        resource_records: typing.Optional[typing.List[builtins.str]] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::Route53::RecordSet``.

        :param name: ``AWS::Route53::RecordSet.Name``.
        :param type: ``AWS::Route53::RecordSet.Type``.
        :param alias_target: ``AWS::Route53::RecordSet.AliasTarget``.
        :param comment: ``AWS::Route53::RecordSet.Comment``.
        :param failover: ``AWS::Route53::RecordSet.Failover``.
        :param geo_location: ``AWS::Route53::RecordSet.GeoLocation``.
        :param health_check_id: ``AWS::Route53::RecordSet.HealthCheckId``.
        :param hosted_zone_id: ``AWS::Route53::RecordSet.HostedZoneId``.
        :param hosted_zone_name: ``AWS::Route53::RecordSet.HostedZoneName``.
        :param multi_value_answer: ``AWS::Route53::RecordSet.MultiValueAnswer``.
        :param region: ``AWS::Route53::RecordSet.Region``.
        :param resource_records: ``AWS::Route53::RecordSet.ResourceRecords``.
        :param set_identifier: ``AWS::Route53::RecordSet.SetIdentifier``.
        :param ttl: ``AWS::Route53::RecordSet.TTL``.
        :param weight: ``AWS::Route53::RecordSet.Weight``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if alias_target is not None:
            self._values["alias_target"] = alias_target
        if comment is not None:
            self._values["comment"] = comment
        if failover is not None:
            self._values["failover"] = failover
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if health_check_id is not None:
            self._values["health_check_id"] = health_check_id
        if hosted_zone_id is not None:
            self._values["hosted_zone_id"] = hosted_zone_id
        if hosted_zone_name is not None:
            self._values["hosted_zone_name"] = hosted_zone_name
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if region is not None:
            self._values["region"] = region
        if resource_records is not None:
            self._values["resource_records"] = resource_records
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Route53::RecordSet.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def type(self) -> builtins.str:
        """``AWS::Route53::RecordSet.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    @builtins.property
    def alias_target(
        self,
    ) -> typing.Optional[typing.Union[CfnRecordSet.AliasTargetProperty, _IResolvable_a771d0ef]]:
        """``AWS::Route53::RecordSet.AliasTarget``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget
        """
        result = self._values.get("alias_target")
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.Comment``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def failover(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.Failover``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover
        """
        result = self._values.get("failover")
        return result

    @builtins.property
    def geo_location(
        self,
    ) -> typing.Optional[typing.Union[CfnRecordSet.GeoLocationProperty, _IResolvable_a771d0ef]]:
        """``AWS::Route53::RecordSet.GeoLocation``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation
        """
        result = self._values.get("geo_location")
        return result

    @builtins.property
    def health_check_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.HealthCheckId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid
        """
        result = self._values.get("health_check_id")
        return result

    @builtins.property
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.HostedZoneId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid
        """
        result = self._values.get("hosted_zone_id")
        return result

    @builtins.property
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.HostedZoneName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename
        """
        result = self._values.get("hosted_zone_name")
        return result

    @builtins.property
    def multi_value_answer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Route53::RecordSet.MultiValueAnswer``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer
        """
        result = self._values.get("multi_value_answer")
        return result

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.Region``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region
        """
        result = self._values.get("region")
        return result

    @builtins.property
    def resource_records(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Route53::RecordSet.ResourceRecords``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords
        """
        result = self._values.get("resource_records")
        return result

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.SetIdentifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier
        """
        result = self._values.get("set_identifier")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        """``AWS::Route53::RecordSet.TTL``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """``AWS::Route53::RecordSet.Weight``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CommonHostedZoneProps",
    jsii_struct_bases=[],
    name_mapping={
        "zone_name": "zoneName",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
    },
)
class CommonHostedZoneProps:
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Common properties to create a Route 53 hosted zone.

        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone_name": zone_name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn

    @builtins.property
    def zone_name(self) -> builtins.str:
        """(experimental) The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.

        :stability: experimental
        """
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) Any comments that you want to include about the hosted zone.

        :default: none

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        """(experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled

        :stability: experimental
        """
        result = self._values.get("query_logs_log_group_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CrossAccountZoneDelegationRecord(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CrossAccountZoneDelegationRecord",
):
    """(experimental) A Cross Account Zone Delegation record.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        delegated_zone: "IHostedZone",
        delegation_role: _IRole_59af6f50,
        parent_hosted_zone_id: builtins.str,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param delegated_zone: (experimental) The zone to be delegated.
        :param delegation_role: (experimental) The delegation role in the parent account.
        :param parent_hosted_zone_id: (experimental) The hosted zone id in the parent account.
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.days(2)

        :stability: experimental
        """
        props = CrossAccountZoneDelegationRecordProps(
            delegated_zone=delegated_zone,
            delegation_role=delegation_role,
            parent_hosted_zone_id=parent_hosted_zone_id,
            ttl=ttl,
        )

        jsii.create(CrossAccountZoneDelegationRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CrossAccountZoneDelegationRecordProps",
    jsii_struct_bases=[],
    name_mapping={
        "delegated_zone": "delegatedZone",
        "delegation_role": "delegationRole",
        "parent_hosted_zone_id": "parentHostedZoneId",
        "ttl": "ttl",
    },
)
class CrossAccountZoneDelegationRecordProps:
    def __init__(
        self,
        *,
        delegated_zone: "IHostedZone",
        delegation_role: _IRole_59af6f50,
        parent_hosted_zone_id: builtins.str,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Construction properties for a CrossAccountZoneDelegationRecord.

        :param delegated_zone: (experimental) The zone to be delegated.
        :param delegation_role: (experimental) The delegation role in the parent account.
        :param parent_hosted_zone_id: (experimental) The hosted zone id in the parent account.
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.days(2)

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "delegated_zone": delegated_zone,
            "delegation_role": delegation_role,
            "parent_hosted_zone_id": parent_hosted_zone_id,
        }
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def delegated_zone(self) -> "IHostedZone":
        """(experimental) The zone to be delegated.

        :stability: experimental
        """
        result = self._values.get("delegated_zone")
        assert result is not None, "Required property 'delegated_zone' is missing"
        return result

    @builtins.property
    def delegation_role(self) -> _IRole_59af6f50:
        """(experimental) The delegation role in the parent account.

        :stability: experimental
        """
        result = self._values.get("delegation_role")
        assert result is not None, "Required property 'delegation_role' is missing"
        return result

    @builtins.property
    def parent_hosted_zone_id(self) -> builtins.str:
        """(experimental) The hosted zone id in the parent account.

        :stability: experimental
        """
        result = self._values.get("parent_hosted_zone_id")
        assert result is not None, "Required property 'parent_hosted_zone_id' is missing"
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.days(2)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrossAccountZoneDelegationRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.HostedZoneAttributes",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId", "zone_name": "zoneName"},
)
class HostedZoneAttributes:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        zone_name: builtins.str,
    ) -> None:
        """(experimental) Reference to a hosted zone.

        :param hosted_zone_id: (experimental) Identifier of the hosted zone.
        :param zone_name: (experimental) Name of the hosted zone.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "zone_name": zone_name,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        """(experimental) Identifier of the hosted zone.

        :stability: experimental
        """
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return result

    @builtins.property
    def zone_name(self) -> builtins.str:
        """(experimental) Name of the hosted zone.

        :stability: experimental
        """
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.HostedZoneProps",
    jsii_struct_bases=[CommonHostedZoneProps],
    name_mapping={
        "zone_name": "zoneName",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
        "vpcs": "vpcs",
    },
)
class HostedZoneProps(CommonHostedZoneProps):
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
        vpcs: typing.Optional[typing.List[_IVpc_6d1f76c4]] = None,
    ) -> None:
        """(experimental) Properties of a new hosted zone.

        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        :param vpcs: (experimental) A VPC that you want to associate with this hosted zone. When you specify this property, a private hosted zone will be created. You can associate additional VPCs to this private zone using ``addVpc(vpc)``. Default: public (no VPCs associated)

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone_name": zone_name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn
        if vpcs is not None:
            self._values["vpcs"] = vpcs

    @builtins.property
    def zone_name(self) -> builtins.str:
        """(experimental) The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.

        :stability: experimental
        """
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) Any comments that you want to include about the hosted zone.

        :default: none

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        """(experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled

        :stability: experimental
        """
        result = self._values.get("query_logs_log_group_arn")
        return result

    @builtins.property
    def vpcs(self) -> typing.Optional[typing.List[_IVpc_6d1f76c4]]:
        """(experimental) A VPC that you want to associate with this hosted zone.

        When you specify
        this property, a private hosted zone will be created.

        You can associate additional VPCs to this private zone using ``addVpc(vpc)``.

        :default: public (no VPCs associated)

        :stability: experimental
        """
        result = self._values.get("vpcs")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.HostedZoneProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "private_zone": "privateZone",
        "vpc_id": "vpcId",
    },
)
class HostedZoneProviderProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        private_zone: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Zone properties for looking up the Hosted Zone.

        :param domain_name: (experimental) The zone domain e.g. example.com.
        :param private_zone: (experimental) Whether the zone that is being looked up is a private hosted zone. Default: false
        :param vpc_id: (experimental) Specifies the ID of the VPC associated with a private hosted zone. If a VPC ID is provided and privateZone is false, no results will be returned and an error will be raised Default: - No VPC ID

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if private_zone is not None:
            self._values["private_zone"] = private_zone
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def domain_name(self) -> builtins.str:
        """(experimental) The zone domain e.g. example.com.

        :stability: experimental
        """
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return result

    @builtins.property
    def private_zone(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether the zone that is being looked up is a private hosted zone.

        :default: false

        :stability: experimental
        """
        result = self._values.get("private_zone")
        return result

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        """(experimental) Specifies the ID of the VPC associated with a private hosted zone.

        If a VPC ID is provided and privateZone is false, no results will be returned
        and an error will be raised

        :default: - No VPC ID

        :stability: experimental
        """
        result = self._values.get("vpc_id")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_route53.IAliasRecordTarget")
class IAliasRecordTarget(typing_extensions.Protocol):
    """(experimental) Classes that are valid alias record targets, like CloudFront distributions and load balancers, should implement this interface.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAliasRecordTargetProxy

    @jsii.member(jsii_name="bind")
    def bind(self, record: "IRecordSet") -> AliasRecordTargetConfig:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param record: -

        :stability: experimental
        """
        ...


class _IAliasRecordTargetProxy:
    """(experimental) Classes that are valid alias record targets, like CloudFront distributions and load balancers, should implement this interface.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_route53.IAliasRecordTarget"

    @jsii.member(jsii_name="bind")
    def bind(self, record: "IRecordSet") -> AliasRecordTargetConfig:
        """(experimental) Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param record: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [record])


@jsii.interface(jsii_type="monocdk.aws_route53.IHostedZone")
class IHostedZone(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) Imported or created hosted zone.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IHostedZoneProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        """(experimental) ARN of this hosted zone, such as arn:${Partition}:route53:::hostedzone/${Id}.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        """(experimental) ID of this hosted zone, such as "Z23ABC4XYZL05B".

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> builtins.str:
        """(experimental) FQDN of this hosted zone.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        :stability: experimental
        :attribute: true
        """
        ...


class _IHostedZoneProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) Imported or created hosted zone.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_route53.IHostedZone"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        """(experimental) ARN of this hosted zone, such as arn:${Partition}:route53:::hostedzone/${Id}.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "hostedZoneArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        """(experimental) ID of this hosted zone, such as "Z23ABC4XYZL05B".

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "hostedZoneId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> builtins.str:
        """(experimental) FQDN of this hosted zone.

        :stability: experimental
        """
        return jsii.get(self, "zoneName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "hostedZoneNameServers")


@jsii.interface(jsii_type="monocdk.aws_route53.IPrivateHostedZone")
class IPrivateHostedZone(IHostedZone, typing_extensions.Protocol):
    """(experimental) Represents a Route 53 private hosted zone.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IPrivateHostedZoneProxy


class _IPrivateHostedZoneProxy(
    jsii.proxy_for(IHostedZone) # type: ignore
):
    """(experimental) Represents a Route 53 private hosted zone.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_route53.IPrivateHostedZone"
    pass


@jsii.interface(jsii_type="monocdk.aws_route53.IPublicHostedZone")
class IPublicHostedZone(IHostedZone, typing_extensions.Protocol):
    """(experimental) Represents a Route 53 public hosted zone.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IPublicHostedZoneProxy


class _IPublicHostedZoneProxy(
    jsii.proxy_for(IHostedZone) # type: ignore
):
    """(experimental) Represents a Route 53 public hosted zone.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_route53.IPublicHostedZone"
    pass


@jsii.interface(jsii_type="monocdk.aws_route53.IRecordSet")
class IRecordSet(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) A record set.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IRecordSetProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        """(experimental) The domain name of the record.

        :stability: experimental
        """
        ...


class _IRecordSetProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) A record set.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_route53.IRecordSet"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        """(experimental) The domain name of the record.

        :stability: experimental
        """
        return jsii.get(self, "domainName")


@jsii.data_type(
    jsii_type="monocdk.aws_route53.MxRecordValue",
    jsii_struct_bases=[],
    name_mapping={"host_name": "hostName", "priority": "priority"},
)
class MxRecordValue:
    def __init__(self, *, host_name: builtins.str, priority: jsii.Number) -> None:
        """(experimental) Properties for a MX record value.

        :param host_name: (experimental) The mail server host name.
        :param priority: (experimental) The priority.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
            "priority": priority,
        }

    @builtins.property
    def host_name(self) -> builtins.str:
        """(experimental) The mail server host name.

        :stability: experimental
        """
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return result

    @builtins.property
    def priority(self) -> jsii.Number:
        """(experimental) The priority.

        :stability: experimental
        """
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MxRecordValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.PrivateHostedZoneProps",
    jsii_struct_bases=[CommonHostedZoneProps],
    name_mapping={
        "zone_name": "zoneName",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
        "vpc": "vpc",
    },
)
class PrivateHostedZoneProps(CommonHostedZoneProps):
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
        vpc: _IVpc_6d1f76c4,
    ) -> None:
        """(experimental) Properties to create a Route 53 private hosted zone.

        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        :param vpc: (experimental) A VPC that you want to associate with this hosted zone. Private hosted zones must be associated with at least one VPC. You can associated additional VPCs using ``addVpc(vpc)``.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone_name": zone_name,
            "vpc": vpc,
        }
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn

    @builtins.property
    def zone_name(self) -> builtins.str:
        """(experimental) The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.

        :stability: experimental
        """
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) Any comments that you want to include about the hosted zone.

        :default: none

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        """(experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled

        :stability: experimental
        """
        result = self._values.get("query_logs_log_group_arn")
        return result

    @builtins.property
    def vpc(self) -> _IVpc_6d1f76c4:
        """(experimental) A VPC that you want to associate with this hosted zone.

        Private hosted zones must be associated with at least one VPC. You can
        associated additional VPCs using ``addVpc(vpc)``.

        :stability: experimental
        """
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.PublicHostedZoneProps",
    jsii_struct_bases=[CommonHostedZoneProps],
    name_mapping={
        "zone_name": "zoneName",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
        "caa_amazon": "caaAmazon",
        "cross_account_zone_delegation_principal": "crossAccountZoneDelegationPrincipal",
    },
)
class PublicHostedZoneProps(CommonHostedZoneProps):
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
        caa_amazon: typing.Optional[builtins.bool] = None,
        cross_account_zone_delegation_principal: typing.Optional[_IPrincipal_93b48231] = None,
    ) -> None:
        """(experimental) Construction properties for a PublicHostedZone.

        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        :param caa_amazon: (experimental) Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only. Default: false
        :param cross_account_zone_delegation_principal: (experimental) A principal which is trusted to assume a role for zone delegation. Default: - No delegation configuration

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone_name": zone_name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn
        if caa_amazon is not None:
            self._values["caa_amazon"] = caa_amazon
        if cross_account_zone_delegation_principal is not None:
            self._values["cross_account_zone_delegation_principal"] = cross_account_zone_delegation_principal

    @builtins.property
    def zone_name(self) -> builtins.str:
        """(experimental) The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.

        :stability: experimental
        """
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) Any comments that you want to include about the hosted zone.

        :default: none

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        """(experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled

        :stability: experimental
        """
        result = self._values.get("query_logs_log_group_arn")
        return result

    @builtins.property
    def caa_amazon(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only.

        :default: false

        :stability: experimental
        """
        result = self._values.get("caa_amazon")
        return result

    @builtins.property
    def cross_account_zone_delegation_principal(
        self,
    ) -> typing.Optional[_IPrincipal_93b48231]:
        """(experimental) A principal which is trusted to assume a role for zone delegation.

        :default: - No delegation configuration

        :stability: experimental
        """
        result = self._values.get("cross_account_zone_delegation_principal")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRecordSet)
class RecordSet(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.RecordSet",
):
    """(experimental) A record set.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        record_type: "RecordType",
        target: "RecordTarget",
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param record_type: (experimental) The record type.
        :param target: (experimental) The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = RecordSetProps(
            record_type=record_type,
            target=target,
            zone=zone,
            comment=comment,
            record_name=record_name,
            ttl=ttl,
        )

        jsii.create(RecordSet, self, [scope, id, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        """(experimental) The domain name of the record.

        :stability: experimental
        """
        return jsii.get(self, "domainName")


@jsii.data_type(
    jsii_type="monocdk.aws_route53.RecordSetOptions",
    jsii_struct_bases=[],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
    },
)
class RecordSetOptions:
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Options for a RecordSet.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.RecordSetProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "record_type": "recordType",
        "target": "target",
    },
)
class RecordSetProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        record_type: "RecordType",
        target: "RecordTarget",
    ) -> None:
        """(experimental) Construction properties for a RecordSet.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param record_type: (experimental) The record type.
        :param target: (experimental) The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "record_type": record_type,
            "target": target,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def record_type(self) -> "RecordType":
        """(experimental) The record type.

        :stability: experimental
        """
        result = self._values.get("record_type")
        assert result is not None, "Required property 'record_type' is missing"
        return result

    @builtins.property
    def target(self) -> "RecordTarget":
        """(experimental) The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.

        :stability: experimental
        """
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RecordTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.RecordTarget",
):
    """(experimental) Type union for a record that accepts multiple types of target.

    :stability: experimental
    """

    def __init__(
        self,
        values: typing.Optional[typing.List[builtins.str]] = None,
        alias_target: typing.Optional[IAliasRecordTarget] = None,
    ) -> None:
        """
        :param values: correspond with the chosen record type (e.g. for 'A' Type, specify one or more IP addresses).
        :param alias_target: alias for targets such as CloudFront distribution to route traffic to.

        :stability: experimental
        """
        jsii.create(RecordTarget, self, [values, alias_target])

    @jsii.member(jsii_name="fromAlias")
    @builtins.classmethod
    def from_alias(cls, alias_target: IAliasRecordTarget) -> "RecordTarget":
        """(experimental) Use an alias as target.

        :param alias_target: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromAlias", [alias_target])

    @jsii.member(jsii_name="fromIpAddresses")
    @builtins.classmethod
    def from_ip_addresses(cls, *ip_addresses: builtins.str) -> "RecordTarget":
        """(experimental) Use ip addresses as target.

        :param ip_addresses: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromIpAddresses", [*ip_addresses])

    @jsii.member(jsii_name="fromValues")
    @builtins.classmethod
    def from_values(cls, *values: builtins.str) -> "RecordTarget":
        """(experimental) Use string values as target.

        :param values: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromValues", [*values])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="aliasTarget")
    def alias_target(self) -> typing.Optional[IAliasRecordTarget]:
        """(experimental) alias for targets such as CloudFront distribution to route traffic to.

        :stability: experimental
        """
        return jsii.get(self, "aliasTarget")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="values")
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) correspond with the chosen record type (e.g. for 'A' Type, specify one or more IP addresses).

        :stability: experimental
        """
        return jsii.get(self, "values")


@jsii.enum(jsii_type="monocdk.aws_route53.RecordType")
class RecordType(enum.Enum):
    """(experimental) The record type.

    :stability: experimental
    """

    A = "A"
    """(experimental) route traffic to a resource, such as a web server, using an IPv4 address in dotted decimal notation.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#AFormat
    :stability: experimental
    """
    AAAA = "AAAA"
    """(experimental) route traffic to a resource, such as a web server, using an IPv6 address in colon-separated hexadecimal format.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#AAAAFormat
    :stability: experimental
    """
    CAA = "CAA"
    """(experimental) A CAA record specifies which certificate authorities (CAs) are allowed to issue certificates for a domain or subdomain.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CAAFormat
    :stability: experimental
    """
    CNAME = "CNAME"
    """(experimental) A CNAME record maps DNS queries for the name of the current record, such as acme.example.com, to another domain (example.com or example.net) or subdomain (acme.example.com or zenith.example.org).

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CNAMEFormat
    :stability: experimental
    """
    MX = "MX"
    """(experimental) An MX record specifies the names of your mail servers and, if you have two or more mail servers, the priority order.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#MXFormat
    :stability: experimental
    """
    NAPTR = "NAPTR"
    """(experimental) A Name Authority Pointer (NAPTR) is a type of record that is used by Dynamic Delegation Discovery System (DDDS) applications to convert one value to another or to replace one value with another.

    For example, one common use is to convert phone numbers into SIP URIs.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#NAPTRFormat
    :stability: experimental
    """
    NS = "NS"
    """(experimental) An NS record identifies the name servers for the hosted zone.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#NSFormat
    :stability: experimental
    """
    PTR = "PTR"
    """(experimental) A PTR record maps an IP address to the corresponding domain name.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#PTRFormat
    :stability: experimental
    """
    SOA = "SOA"
    """(experimental) A start of authority (SOA) record provides information about a domain and the corresponding Amazon Route 53 hosted zone.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SOAFormat
    :stability: experimental
    """
    SPF = "SPF"
    """(experimental) SPF records were formerly used to verify the identity of the sender of email messages.

    Instead of an SPF record, we recommend that you create a TXT record that contains the applicable value.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SPFFormat
    :stability: experimental
    """
    SRV = "SRV"
    """(experimental) An SRV record Value element consists of four space-separated values.

    The first three values are
    decimal numbers representing priority, weight, and port. The fourth value is a domain name.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SRVFormat
    :stability: experimental
    """
    TXT = "TXT"
    """(experimental) A TXT record contains one or more strings that are enclosed in double quotation marks (").

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#TXTFormat
    :stability: experimental
    """


class SrvRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.SrvRecord",
):
    """(experimental) A DNS SRV record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        values: typing.List["SrvRecordValue"],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param values: (experimental) The values.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = SrvRecordProps(
            values=values, zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(SrvRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.SrvRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "values": "values",
    },
)
class SrvRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        values: typing.List["SrvRecordValue"],
    ) -> None:
        """(experimental) Construction properties for a SrvRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param values: (experimental) The values.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def values(self) -> typing.List["SrvRecordValue"]:
        """(experimental) The values.

        :stability: experimental
        """
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SrvRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.SrvRecordValue",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "port": "port",
        "priority": "priority",
        "weight": "weight",
    },
)
class SrvRecordValue:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        port: jsii.Number,
        priority: jsii.Number,
        weight: jsii.Number,
    ) -> None:
        """(experimental) Properties for a SRV record value.

        :param host_name: (experimental) The server host name.
        :param port: (experimental) The port.
        :param priority: (experimental) The priority.
        :param weight: (experimental) The weight.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
            "port": port,
            "priority": priority,
            "weight": weight,
        }

    @builtins.property
    def host_name(self) -> builtins.str:
        """(experimental) The server host name.

        :stability: experimental
        """
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return result

    @builtins.property
    def port(self) -> jsii.Number:
        """(experimental) The port.

        :stability: experimental
        """
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return result

    @builtins.property
    def priority(self) -> jsii.Number:
        """(experimental) The priority.

        :stability: experimental
        """
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return result

    @builtins.property
    def weight(self) -> jsii.Number:
        """(experimental) The weight.

        :stability: experimental
        """
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SrvRecordValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TxtRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.TxtRecord",
):
    """(experimental) A DNS TXT record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        values: typing.List[builtins.str],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param values: (experimental) The text values.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = TxtRecordProps(
            values=values, zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(TxtRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.TxtRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "values": "values",
    },
)
class TxtRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        values: typing.List[builtins.str],
    ) -> None:
        """(experimental) Construction properties for a TxtRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param values: (experimental) The text values.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        """(experimental) The text values.

        :stability: experimental
        """
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TxtRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcEndpointServiceDomainName(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.VpcEndpointServiceDomainName",
):
    """(experimental) A Private DNS configuration for a VPC endpoint service.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        endpoint_service: _IVpcEndpointService_30207308,
        public_hosted_zone: IPublicHostedZone,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param domain_name: (experimental) The domain name to use. This domain name must be owned by this account (registered through Route53), or delegated to this account. Domain ownership will be verified by AWS before private DNS can be used.
        :param endpoint_service: (experimental) The VPC Endpoint Service to configure Private DNS for.
        :param public_hosted_zone: (experimental) The public hosted zone to use for the domain.

        :stability: experimental
        """
        props = VpcEndpointServiceDomainNameProps(
            domain_name=domain_name,
            endpoint_service=endpoint_service,
            public_hosted_zone=public_hosted_zone,
        )

        jsii.create(VpcEndpointServiceDomainName, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.VpcEndpointServiceDomainNameProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "endpoint_service": "endpointService",
        "public_hosted_zone": "publicHostedZone",
    },
)
class VpcEndpointServiceDomainNameProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        endpoint_service: _IVpcEndpointService_30207308,
        public_hosted_zone: IPublicHostedZone,
    ) -> None:
        """(experimental) Properties to configure a VPC Endpoint Service domain name.

        :param domain_name: (experimental) The domain name to use. This domain name must be owned by this account (registered through Route53), or delegated to this account. Domain ownership will be verified by AWS before private DNS can be used.
        :param endpoint_service: (experimental) The VPC Endpoint Service to configure Private DNS for.
        :param public_hosted_zone: (experimental) The public hosted zone to use for the domain.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "endpoint_service": endpoint_service,
            "public_hosted_zone": public_hosted_zone,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        """(experimental) The domain name to use.

        This domain name must be owned by this account (registered through Route53),
        or delegated to this account. Domain ownership will be verified by AWS before
        private DNS can be used.

        :see: https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-dns-validation.html
        :stability: experimental
        """
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return result

    @builtins.property
    def endpoint_service(self) -> _IVpcEndpointService_30207308:
        """(experimental) The VPC Endpoint Service to configure Private DNS for.

        :stability: experimental
        """
        result = self._values.get("endpoint_service")
        assert result is not None, "Required property 'endpoint_service' is missing"
        return result

    @builtins.property
    def public_hosted_zone(self) -> IPublicHostedZone:
        """(experimental) The public hosted zone to use for the domain.

        :stability: experimental
        """
        result = self._values.get("public_hosted_zone")
        assert result is not None, "Required property 'public_hosted_zone' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcEndpointServiceDomainNameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_route53.ZoneDelegationOptions",
    jsii_struct_bases=[],
    name_mapping={"comment": "comment", "ttl": "ttl"},
)
class ZoneDelegationOptions:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Options available when creating a delegation relationship from one PublicHostedZone to another.

        :param comment: (experimental) A comment to add on the DNS record created to incorporate the delegation. Default: none
        :param ttl: (experimental) The TTL (Time To Live) of the DNS delegation record in DNS caches. Default: 172800

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the DNS record created to incorporate the delegation.

        :default: none

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The TTL (Time To Live) of the DNS delegation record in DNS caches.

        :default: 172800

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneDelegationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneDelegationRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.ZoneDelegationRecord",
):
    """(experimental) A record to delegate further lookups to a different set of name servers.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name_servers: typing.List[builtins.str],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param name_servers: (experimental) The name servers to report in the delegation records.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = ZoneDelegationRecordProps(
            name_servers=name_servers,
            zone=zone,
            comment=comment,
            record_name=record_name,
            ttl=ttl,
        )

        jsii.create(ZoneDelegationRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.ZoneDelegationRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "name_servers": "nameServers",
    },
)
class ZoneDelegationRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        name_servers: typing.List[builtins.str],
    ) -> None:
        """(experimental) Construction properties for a ZoneDelegationRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param name_servers: (experimental) The name servers to report in the delegation records.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "name_servers": name_servers,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def name_servers(self) -> typing.List[builtins.str]:
        """(experimental) The name servers to report in the delegation records.

        :stability: experimental
        """
        result = self._values.get("name_servers")
        assert result is not None, "Required property 'name_servers' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneDelegationRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ARecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.ARecord",
):
    """(experimental) A DNS A record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        target: RecordTarget,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param target: (experimental) The target.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = ARecordProps(
            target=target, zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(ARecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.ARecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "target": "target",
    },
)
class ARecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        target: RecordTarget,
    ) -> None:
        """(experimental) Construction properties for a ARecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param target: (experimental) The target.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "target": target,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def target(self) -> RecordTarget:
        """(experimental) The target.

        :stability: experimental
        """
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ARecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AaaaRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.AaaaRecord",
):
    """(experimental) A DNS AAAA record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        target: RecordTarget,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param target: (experimental) The target.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = AaaaRecordProps(
            target=target, zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(AaaaRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.AaaaRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "target": "target",
    },
)
class AaaaRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        target: RecordTarget,
    ) -> None:
        """(experimental) Construction properties for a AaaaRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param target: (experimental) The target.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "target": target,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def target(self) -> RecordTarget:
        """(experimental) The target.

        :stability: experimental
        """
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AaaaRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AddressRecordTarget(
    RecordTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.AddressRecordTarget",
):
    """(deprecated) Target for a DNS A Record.

    :deprecated: Use RecordTarget

    :stability: deprecated
    """

    def __init__(
        self,
        values: typing.Optional[typing.List[builtins.str]] = None,
        alias_target: typing.Optional[IAliasRecordTarget] = None,
    ) -> None:
        """
        :param values: correspond with the chosen record type (e.g. for 'A' Type, specify one or more IP addresses).
        :param alias_target: alias for targets such as CloudFront distribution to route traffic to.

        :stability: experimental
        """
        jsii.create(AddressRecordTarget, self, [values, alias_target])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CaaAmazonRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
    },
)
class CaaAmazonRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Construction properties for a CaaAmazonRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaaAmazonRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CaaRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CaaRecord",
):
    """(experimental) A DNS CAA record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        values: typing.List[CaaRecordValue],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param values: (experimental) The values.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = CaaRecordProps(
            values=values, zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(CaaRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CaaRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "values": "values",
    },
)
class CaaRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        values: typing.List[CaaRecordValue],
    ) -> None:
        """(experimental) Construction properties for a CaaRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param values: (experimental) The values.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def values(self) -> typing.List[CaaRecordValue]:
        """(experimental) The values.

        :stability: experimental
        """
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaaRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CnameRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CnameRecord",
):
    """(experimental) A DNS CNAME record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param domain_name: (experimental) The domain name.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = CnameRecordProps(
            domain_name=domain_name,
            zone=zone,
            comment=comment,
            record_name=record_name,
            ttl=ttl,
        )

        jsii.create(CnameRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.CnameRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "domain_name": "domainName",
    },
)
class CnameRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        domain_name: builtins.str,
    ) -> None:
        """(experimental) Construction properties for a CnameRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param domain_name: (experimental) The domain name.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "domain_name": domain_name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def domain_name(self) -> builtins.str:
        """(experimental) The domain name.

        :stability: experimental
        """
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CnameRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IHostedZone)
class HostedZone(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.HostedZone",
):
    """(experimental) Container for records, and records contain information about how to route traffic for a specific domain, such as example.com and its subdomains (acme.example.com, zenith.example.com).

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        vpcs: typing.Optional[typing.List[_IVpc_6d1f76c4]] = None,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param vpcs: (experimental) A VPC that you want to associate with this hosted zone. When you specify this property, a private hosted zone will be created. You can associate additional VPCs to this private zone using ``addVpc(vpc)``. Default: public (no VPCs associated)
        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        :stability: experimental
        """
        props = HostedZoneProps(
            vpcs=vpcs,
            zone_name=zone_name,
            comment=comment,
            query_logs_log_group_arn=query_logs_log_group_arn,
        )

        jsii.create(HostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="fromHostedZoneAttributes")
    @builtins.classmethod
    def from_hosted_zone_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
        zone_name: builtins.str,
    ) -> IHostedZone:
        """(experimental) Imports a hosted zone from another stack.

        Use when both hosted zone ID and hosted zone name are known.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param hosted_zone_id: (experimental) Identifier of the hosted zone.
        :param zone_name: (experimental) Name of the hosted zone.

        :stability: experimental
        """
        attrs = HostedZoneAttributes(
            hosted_zone_id=hosted_zone_id, zone_name=zone_name
        )

        return jsii.sinvoke(cls, "fromHostedZoneAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="fromHostedZoneId")
    @builtins.classmethod
    def from_hosted_zone_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        hosted_zone_id: builtins.str,
    ) -> IHostedZone:
        """(experimental) Import a Route 53 hosted zone defined either outside the CDK, or in a different CDK stack.

        Use when hosted zone ID is known. Hosted zone name becomes unavailable through this query.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param hosted_zone_id: the ID of the hosted zone to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromHostedZoneId", [scope, id, hosted_zone_id])

    @jsii.member(jsii_name="fromLookup")
    @builtins.classmethod
    def from_lookup(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        private_zone: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> IHostedZone:
        """(experimental) Lookup a hosted zone in the current account/region based on query parameters.

        Requires environment, you must specify env for the stack.

        Use to easily query hosted zones.

        :param scope: -
        :param id: -
        :param domain_name: (experimental) The zone domain e.g. example.com.
        :param private_zone: (experimental) Whether the zone that is being looked up is a private hosted zone. Default: false
        :param vpc_id: (experimental) Specifies the ID of the VPC associated with a private hosted zone. If a VPC ID is provided and privateZone is false, no results will be returned and an error will be raised Default: - No VPC ID

        :see: https://docs.aws.amazon.com/cdk/latest/guide/environments.html
        :stability: experimental
        """
        query = HostedZoneProviderProps(
            domain_name=domain_name, private_zone=private_zone, vpc_id=vpc_id
        )

        return jsii.sinvoke(cls, "fromLookup", [scope, id, query])

    @jsii.member(jsii_name="addVpc")
    def add_vpc(self, vpc: _IVpc_6d1f76c4) -> None:
        """(experimental) Add another VPC to this private hosted zone.

        :param vpc: the other VPC to add.

        :stability: experimental
        """
        return jsii.invoke(self, "addVpc", [vpc])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        """(experimental) ARN of this hosted zone, such as arn:${Partition}:route53:::hostedzone/${Id}.

        :stability: experimental
        """
        return jsii.get(self, "hostedZoneArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        """(experimental) ID of this hosted zone, such as "Z23ABC4XYZL05B".

        :stability: experimental
        """
        return jsii.get(self, "hostedZoneId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="vpcs")
    def _vpcs(self) -> typing.List[CfnHostedZone.VPCProperty]:
        """(experimental) VPCs to which this hosted zone will be added.

        :stability: experimental
        """
        return jsii.get(self, "vpcs")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> builtins.str:
        """(experimental) FQDN of this hosted zone.

        :stability: experimental
        """
        return jsii.get(self, "zoneName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        :stability: experimental
        """
        return jsii.get(self, "hostedZoneNameServers")


class MxRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.MxRecord",
):
    """(experimental) A DNS MX record.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        values: typing.List[MxRecordValue],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param values: (experimental) The values.
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = MxRecordProps(
            values=values, zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(MxRecord, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_route53.MxRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "record_name": "recordName",
        "ttl": "ttl",
        "values": "values",
    },
)
class MxRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
        values: typing.List[MxRecordValue],
    ) -> None:
        """(experimental) Construction properties for a MxRecord.

        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param values: (experimental) The values.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if record_name is not None:
            self._values["record_name"] = record_name
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def zone(self) -> IHostedZone:
        """(experimental) The hosted zone in which to define the new record.

        :stability: experimental
        """
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return result

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        """(experimental) A comment to add on the record.

        :default: no comment

        :stability: experimental
        """
        result = self._values.get("comment")
        return result

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The domain name for this record.

        :default: zone root

        :stability: experimental
        """
        result = self._values.get("record_name")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The resource record cache time to live (TTL).

        :default: Duration.minutes(30)

        :stability: experimental
        """
        result = self._values.get("ttl")
        return result

    @builtins.property
    def values(self) -> typing.List[MxRecordValue]:
        """(experimental) The values.

        :stability: experimental
        """
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MxRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPrivateHostedZone)
class PrivateHostedZone(
    HostedZone,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.PrivateHostedZone",
):
    """(experimental) Create a Route53 private hosted zone for use in one or more VPCs.

    Note that ``enableDnsHostnames`` and ``enableDnsSupport`` must have been enabled
    for the VPC you're configuring for private hosted zones.

    :stability: experimental
    :resource: AWS::Route53::HostedZone
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        vpc: _IVpc_6d1f76c4,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param vpc: (experimental) A VPC that you want to associate with this hosted zone. Private hosted zones must be associated with at least one VPC. You can associated additional VPCs using ``addVpc(vpc)``.
        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        :stability: experimental
        """
        props = PrivateHostedZoneProps(
            vpc=vpc,
            zone_name=zone_name,
            comment=comment,
            query_logs_log_group_arn=query_logs_log_group_arn,
        )

        jsii.create(PrivateHostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="fromPrivateHostedZoneId")
    @builtins.classmethod
    def from_private_hosted_zone_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        private_hosted_zone_id: builtins.str,
    ) -> IPrivateHostedZone:
        """(experimental) Import a Route 53 private hosted zone defined either outside the CDK, or in a different CDK stack.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param private_hosted_zone_id: the ID of the private hosted zone to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromPrivateHostedZoneId", [scope, id, private_hosted_zone_id])


@jsii.implements(IPublicHostedZone)
class PublicHostedZone(
    HostedZone,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.PublicHostedZone",
):
    """(experimental) Create a Route53 public hosted zone.

    :stability: experimental
    :resource: AWS::Route53::HostedZone
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        caa_amazon: typing.Optional[builtins.bool] = None,
        cross_account_zone_delegation_principal: typing.Optional[_IPrincipal_93b48231] = None,
        zone_name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param caa_amazon: (experimental) Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only. Default: false
        :param cross_account_zone_delegation_principal: (experimental) A principal which is trusted to assume a role for zone delegation. Default: - No delegation configuration
        :param zone_name: (experimental) The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param comment: (experimental) Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: (experimental) The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        :stability: experimental
        """
        props = PublicHostedZoneProps(
            caa_amazon=caa_amazon,
            cross_account_zone_delegation_principal=cross_account_zone_delegation_principal,
            zone_name=zone_name,
            comment=comment,
            query_logs_log_group_arn=query_logs_log_group_arn,
        )

        jsii.create(PublicHostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="fromPublicHostedZoneId")
    @builtins.classmethod
    def from_public_hosted_zone_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        public_hosted_zone_id: builtins.str,
    ) -> IPublicHostedZone:
        """(experimental) Import a Route 53 public hosted zone defined either outside the CDK, or in a different CDK stack.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param public_hosted_zone_id: the ID of the public hosted zone to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromPublicHostedZoneId", [scope, id, public_hosted_zone_id])

    @jsii.member(jsii_name="addDelegation")
    def add_delegation(
        self,
        delegate: IPublicHostedZone,
        *,
        comment: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Adds a delegation from this zone to a designated zone.

        :param delegate: the zone being delegated to.
        :param comment: (experimental) A comment to add on the DNS record created to incorporate the delegation. Default: none
        :param ttl: (experimental) The TTL (Time To Live) of the DNS delegation record in DNS caches. Default: 172800

        :stability: experimental
        """
        opts = ZoneDelegationOptions(comment=comment, ttl=ttl)

        return jsii.invoke(self, "addDelegation", [delegate, opts])

    @jsii.member(jsii_name="addVpc")
    def add_vpc(self, _vpc: _IVpc_6d1f76c4) -> None:
        """(experimental) Add another VPC to this private hosted zone.

        :param _vpc: -

        :stability: experimental
        """
        return jsii.invoke(self, "addVpc", [_vpc])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="crossAccountZoneDelegationRole")
    def cross_account_zone_delegation_role(self) -> typing.Optional[_Role_95e2afa4]:
        """(experimental) Role for cross account zone delegation.

        :stability: experimental
        """
        return jsii.get(self, "crossAccountZoneDelegationRole")


class CaaAmazonRecord(
    CaaRecord,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_route53.CaaAmazonRecord",
):
    """(experimental) A DNS Amazon CAA record.

    A CAA record to restrict certificate authorities allowed
    to issue certificates for a domain to Amazon only.

    :stability: experimental
    :resource: AWS::Route53::RecordSet
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        record_name: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param zone: (experimental) The hosted zone in which to define the new record.
        :param comment: (experimental) A comment to add on the record. Default: no comment
        :param record_name: (experimental) The domain name for this record. Default: zone root
        :param ttl: (experimental) The resource record cache time to live (TTL). Default: Duration.minutes(30)

        :stability: experimental
        """
        props = CaaAmazonRecordProps(
            zone=zone, comment=comment, record_name=record_name, ttl=ttl
        )

        jsii.create(CaaAmazonRecord, self, [scope, id, props])


__all__ = [
    "ARecord",
    "ARecordProps",
    "AaaaRecord",
    "AaaaRecordProps",
    "AddressRecordTarget",
    "AliasRecordTargetConfig",
    "CaaAmazonRecord",
    "CaaAmazonRecordProps",
    "CaaRecord",
    "CaaRecordProps",
    "CaaRecordValue",
    "CaaTag",
    "CfnDNSSEC",
    "CfnDNSSECProps",
    "CfnHealthCheck",
    "CfnHealthCheckProps",
    "CfnHostedZone",
    "CfnHostedZoneProps",
    "CfnKeySigningKey",
    "CfnKeySigningKeyProps",
    "CfnRecordSet",
    "CfnRecordSetGroup",
    "CfnRecordSetGroupProps",
    "CfnRecordSetProps",
    "CnameRecord",
    "CnameRecordProps",
    "CommonHostedZoneProps",
    "CrossAccountZoneDelegationRecord",
    "CrossAccountZoneDelegationRecordProps",
    "HostedZone",
    "HostedZoneAttributes",
    "HostedZoneProps",
    "HostedZoneProviderProps",
    "IAliasRecordTarget",
    "IHostedZone",
    "IPrivateHostedZone",
    "IPublicHostedZone",
    "IRecordSet",
    "MxRecord",
    "MxRecordProps",
    "MxRecordValue",
    "PrivateHostedZone",
    "PrivateHostedZoneProps",
    "PublicHostedZone",
    "PublicHostedZoneProps",
    "RecordSet",
    "RecordSetOptions",
    "RecordSetProps",
    "RecordTarget",
    "RecordType",
    "SrvRecord",
    "SrvRecordProps",
    "SrvRecordValue",
    "TxtRecord",
    "TxtRecordProps",
    "VpcEndpointServiceDomainName",
    "VpcEndpointServiceDomainNameProps",
    "ZoneDelegationOptions",
    "ZoneDelegationRecord",
    "ZoneDelegationRecordProps",
]

publication.publish()
