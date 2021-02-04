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
    AssetHashType as _AssetHashType_49193809,
    BundlingDockerImage as _BundlingDockerImage_86dee600,
    BundlingOptions as _BundlingOptions_ab115a99,
    CfnParameter as _CfnParameter_3e6f99ac,
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    ConstructNode as _ConstructNode_33e3628c,
    Duration as _Duration_070aa057,
    IConstruct as _IConstruct_5a0f9c5e,
    IDependable as _IDependable_1175c9f7,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    IgnoreMode as _IgnoreMode_31d8bf46,
    RemovalPolicy as _RemovalPolicy_c97e7a20,
    Resource as _Resource_abff4495,
    ResourceProps as _ResourceProps_9b554c0f,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..assets import FollowMode as _FollowMode_98b05cc5
from ..aws_applicationautoscaling import (
    BaseTargetTrackingProps as _BaseTargetTrackingProps_e4402570,
    ScalingSchedule as _ScalingSchedule_6c3fc38f,
    Schedule as _Schedule_c2a5a45d,
)
from ..aws_cloudwatch import (
    Metric as _Metric_5b2b8e58,
    MetricOptions as _MetricOptions_1c185ae8,
    Unit as _Unit_113c79f9,
)
from ..aws_codeguruprofiler import IProfilingGroup as _IProfilingGroup_418eb20c
from ..aws_ec2 import (
    Connections as _Connections_57ccbda9,
    IConnectable as _IConnectable_c1c0e72c,
    ISecurityGroup as _ISecurityGroup_cdbba9d3,
    IVpc as _IVpc_6d1f76c4,
    SubnetSelection as _SubnetSelection_1284e62c,
)
from ..aws_ecr import IRepository as _IRepository_8b4d2894
from ..aws_ecr_assets import (
    DockerImageAssetOptions as _DockerImageAssetOptions_6764a0de
)
from ..aws_efs import IAccessPoint as _IAccessPoint_180f72ec
from ..aws_iam import (
    Grant as _Grant_bcb5eae7,
    IGrantable as _IGrantable_4c5a91d1,
    IPrincipal as _IPrincipal_93b48231,
    IRole as _IRole_59af6f50,
    PolicyStatement as _PolicyStatement_296fe8a3,
)
from ..aws_kms import IKey as _IKey_36930160
from ..aws_logs import (
    ILogGroup as _ILogGroup_846e17a0,
    LogRetention as _LogRetention_7657fb8a,
    LogRetentionProps as _LogRetentionProps_99b4e2db,
    LogRetentionRetryOptions as _LogRetentionRetryOptions_c6b3d73a,
    RetentionDays as _RetentionDays_6c560d31,
)
from ..aws_s3 import IBucket as _IBucket_73486e29, Location as _Location_cce991ca
from ..aws_s3_assets import AssetOptions as _AssetOptions_bd2996da
from ..aws_sqs import IQueue as _IQueue_45a01ab4


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.AliasAttributes",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName", "alias_version": "aliasVersion"},
)
class AliasAttributes:
    def __init__(self, *, alias_name: builtins.str, alias_version: "IVersion") -> None:
        """
        :param alias_name: 
        :param alias_version: 

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "alias_version": alias_version,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        """
        :stability: experimental
        """
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return result

    @builtins.property
    def alias_version(self) -> "IVersion":
        """
        :stability: experimental
        """
        result = self._values.get("alias_version")
        assert result is not None, "Required property 'alias_version' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.AssetImageCodeProps",
    jsii_struct_bases=[_DockerImageAssetOptions_6764a0de],
    name_mapping={
        "exclude": "exclude",
        "follow": "follow",
        "ignore_mode": "ignoreMode",
        "extra_hash": "extraHash",
        "build_args": "buildArgs",
        "file": "file",
        "repository_name": "repositoryName",
        "target": "target",
        "cmd": "cmd",
        "entrypoint": "entrypoint",
    },
)
class AssetImageCodeProps(_DockerImageAssetOptions_6764a0de):
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.List[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        repository_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """(experimental) Properties to initialize a new AssetImage.

        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '
        :param extra_hash: (deprecated) Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param build_args: (experimental) Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param file: (experimental) Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - the default ECR repository for CDK assets
        :param target: (experimental) Docker target to build to. Default: - no target
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow is not None:
            self._values["follow"] = follow
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash
        if build_args is not None:
            self._values["build_args"] = build_args
        if file is not None:
            self._values["file"] = file
        if repository_name is not None:
            self._values["repository_name"] = repository_name
        if target is not None:
            self._values["target"] = target
        if cmd is not None:
            self._values["cmd"] = cmd
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        """(deprecated) Glob patterns to exclude from the copy.

        :default: nothing is excluded

        :stability: deprecated
        """
        result = self._values.get("exclude")
        return result

    @builtins.property
    def follow(self) -> typing.Optional[_FollowMode_98b05cc5]:
        """(deprecated) A strategy for how to handle symlinks.

        :default: Never

        :stability: deprecated
        """
        result = self._values.get("follow")
        return result

    @builtins.property
    def ignore_mode(self) -> typing.Optional[_IgnoreMode_31d8bf46]:
        """(deprecated) The ignore behavior to use for exclude patterns.

        :default:

        - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the
        '

        :stability: deprecated
        :aws-cdk: /aws-ecr-assets:dockerIgnoreSupport' flag is set.
        """
        result = self._values.get("ignore_mode")
        return result

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.str]:
        """(deprecated) Extra information to encode into the fingerprint (e.g. build instructions and other inputs).

        :default: - hash is only based on source content

        :stability: deprecated
        """
        result = self._values.get("extra_hash")
        return result

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) Build args to pass to the ``docker build`` command.

        Since Docker build arguments are resolved before deployment, keys and
        values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or
        ``queue.queueUrl``).

        :default: - no build args are passed

        :stability: experimental
        """
        result = self._values.get("build_args")
        return result

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        """(experimental) Path to the Dockerfile (relative to the directory).

        :default: 'Dockerfile'

        :stability: experimental
        """
        result = self._values.get("file")
        return result

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        """(deprecated) ECR repository name.

        Specify this property if you need to statically address the image, e.g.
        from a Kubernetes Pod. Note, this is only the repository name, without the
        registry and the tag parts.

        :default: - the default ECR repository for CDK assets

        :deprecated:

        to control the location of docker image assets, please override
        ``Stack.addDockerImageAsset``. this feature will be removed in future
        releases.

        :stability: deprecated
        """
        result = self._values.get("repository_name")
        return result

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        """(experimental) Docker target to build to.

        :default: - no target

        :stability: experimental
        """
        result = self._values.get("target")
        return result

    @builtins.property
    def cmd(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Specify or override the CMD on the specified Docker image or Dockerfile.

        This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``.

        :default: - use the CMD specified in the docker image or Dockerfile.

        :see: https://docs.docker.com/engine/reference/builder/#cmd
        :stability: experimental
        """
        result = self._values.get("cmd")
        return result

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile.

        An ENTRYPOINT allows you to configure a container that will run as an executable.
        This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``.

        :default: - use the ENTRYPOINT in the docker image or Dockerfile.

        :see: https://docs.docker.com/engine/reference/builder/#entrypoint
        :stability: experimental
        """
        result = self._values.get("entrypoint")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetImageCodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.AutoScalingOptions",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class AutoScalingOptions:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Properties for enabling Lambda autoscaling.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
        }
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        """(experimental) Maximum capacity to scale to.

        :stability: experimental
        """
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return result

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        """(experimental) Minimum capacity to scale to.

        :default: 1

        :stability: experimental
        """
        result = self._values.get("min_capacity")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAlias(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnAlias",
):
    """A CloudFormation ``AWS::Lambda::Alias``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html
    :cloudformationResource: AWS::Lambda::Alias
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        function_name: builtins.str,
        function_version: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrency_config: typing.Optional[typing.Union["CfnAlias.ProvisionedConcurrencyConfigurationProperty", _IResolvable_a771d0ef]] = None,
        routing_config: typing.Optional[typing.Union["CfnAlias.AliasRoutingConfigurationProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::Alias``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param function_name: ``AWS::Lambda::Alias.FunctionName``.
        :param function_version: ``AWS::Lambda::Alias.FunctionVersion``.
        :param name: ``AWS::Lambda::Alias.Name``.
        :param description: ``AWS::Lambda::Alias.Description``.
        :param provisioned_concurrency_config: ``AWS::Lambda::Alias.ProvisionedConcurrencyConfig``.
        :param routing_config: ``AWS::Lambda::Alias.RoutingConfig``.
        """
        props = CfnAliasProps(
            function_name=function_name,
            function_version=function_version,
            name=name,
            description=description,
            provisioned_concurrency_config=provisioned_concurrency_config,
            routing_config=routing_config,
        )

        jsii.create(CfnAlias, self, [scope, id, props])

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
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::Alias.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter # type: ignore
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> builtins.str:
        """``AWS::Lambda::Alias.FunctionVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionversion
        """
        return jsii.get(self, "functionVersion")

    @function_version.setter # type: ignore
    def function_version(self, value: builtins.str) -> None:
        jsii.set(self, "functionVersion", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Lambda::Alias.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Alias.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisionedConcurrencyConfig")
    def provisioned_concurrency_config(
        self,
    ) -> typing.Optional[typing.Union["CfnAlias.ProvisionedConcurrencyConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Alias.ProvisionedConcurrencyConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig
        """
        return jsii.get(self, "provisionedConcurrencyConfig")

    @provisioned_concurrency_config.setter # type: ignore
    def provisioned_concurrency_config(
        self,
        value: typing.Optional[typing.Union["CfnAlias.ProvisionedConcurrencyConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "provisionedConcurrencyConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="routingConfig")
    def routing_config(
        self,
    ) -> typing.Optional[typing.Union["CfnAlias.AliasRoutingConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Alias.RoutingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-routingconfig
        """
        return jsii.get(self, "routingConfig")

    @routing_config.setter # type: ignore
    def routing_config(
        self,
        value: typing.Optional[typing.Union["CfnAlias.AliasRoutingConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "routingConfig", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnAlias.AliasRoutingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"additional_version_weights": "additionalVersionWeights"},
    )
    class AliasRoutingConfigurationProperty:
        def __init__(
            self,
            *,
            additional_version_weights: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlias.VersionWeightProperty", _IResolvable_a771d0ef]]],
        ) -> None:
            """
            :param additional_version_weights: ``CfnAlias.AliasRoutingConfigurationProperty.AdditionalVersionWeights``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "additional_version_weights": additional_version_weights,
            }

        @builtins.property
        def additional_version_weights(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlias.VersionWeightProperty", _IResolvable_a771d0ef]]]:
            """``CfnAlias.AliasRoutingConfigurationProperty.AdditionalVersionWeights``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html#cfn-lambda-alias-aliasroutingconfiguration-additionalversionweights
            """
            result = self._values.get("additional_version_weights")
            assert result is not None, "Required property 'additional_version_weights' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AliasRoutingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnAlias.ProvisionedConcurrencyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
        },
    )
    class ProvisionedConcurrencyConfigurationProperty:
        def __init__(self, *, provisioned_concurrent_executions: jsii.Number) -> None:
            """
            :param provisioned_concurrent_executions: ``CfnAlias.ProvisionedConcurrencyConfigurationProperty.ProvisionedConcurrentExecutions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "provisioned_concurrent_executions": provisioned_concurrent_executions,
            }

        @builtins.property
        def provisioned_concurrent_executions(self) -> jsii.Number:
            """``CfnAlias.ProvisionedConcurrencyConfigurationProperty.ProvisionedConcurrentExecutions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html#cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions
            """
            result = self._values.get("provisioned_concurrent_executions")
            assert result is not None, "Required property 'provisioned_concurrent_executions' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedConcurrencyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnAlias.VersionWeightProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_version": "functionVersion",
            "function_weight": "functionWeight",
        },
    )
    class VersionWeightProperty:
        def __init__(
            self,
            *,
            function_version: builtins.str,
            function_weight: jsii.Number,
        ) -> None:
            """
            :param function_version: ``CfnAlias.VersionWeightProperty.FunctionVersion``.
            :param function_weight: ``CfnAlias.VersionWeightProperty.FunctionWeight``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "function_version": function_version,
                "function_weight": function_weight,
            }

        @builtins.property
        def function_version(self) -> builtins.str:
            """``CfnAlias.VersionWeightProperty.FunctionVersion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionversion
            """
            result = self._values.get("function_version")
            assert result is not None, "Required property 'function_version' is missing"
            return result

        @builtins.property
        def function_weight(self) -> jsii.Number:
            """``CfnAlias.VersionWeightProperty.FunctionWeight``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionweight
            """
            result = self._values.get("function_weight")
            assert result is not None, "Required property 'function_weight' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VersionWeightProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "function_version": "functionVersion",
        "name": "name",
        "description": "description",
        "provisioned_concurrency_config": "provisionedConcurrencyConfig",
        "routing_config": "routingConfig",
    },
)
class CfnAliasProps:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        function_version: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrency_config: typing.Optional[typing.Union[CfnAlias.ProvisionedConcurrencyConfigurationProperty, _IResolvable_a771d0ef]] = None,
        routing_config: typing.Optional[typing.Union[CfnAlias.AliasRoutingConfigurationProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::Alias``.

        :param function_name: ``AWS::Lambda::Alias.FunctionName``.
        :param function_version: ``AWS::Lambda::Alias.FunctionVersion``.
        :param name: ``AWS::Lambda::Alias.Name``.
        :param description: ``AWS::Lambda::Alias.Description``.
        :param provisioned_concurrency_config: ``AWS::Lambda::Alias.ProvisionedConcurrencyConfig``.
        :param routing_config: ``AWS::Lambda::Alias.RoutingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
            "function_version": function_version,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if provisioned_concurrency_config is not None:
            self._values["provisioned_concurrency_config"] = provisioned_concurrency_config
        if routing_config is not None:
            self._values["routing_config"] = routing_config

    @builtins.property
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::Alias.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionname
        """
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return result

    @builtins.property
    def function_version(self) -> builtins.str:
        """``AWS::Lambda::Alias.FunctionVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionversion
        """
        result = self._values.get("function_version")
        assert result is not None, "Required property 'function_version' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Lambda::Alias.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Alias.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def provisioned_concurrency_config(
        self,
    ) -> typing.Optional[typing.Union[CfnAlias.ProvisionedConcurrencyConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Alias.ProvisionedConcurrencyConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig
        """
        result = self._values.get("provisioned_concurrency_config")
        return result

    @builtins.property
    def routing_config(
        self,
    ) -> typing.Optional[typing.Union[CfnAlias.AliasRoutingConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Alias.RoutingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-routingconfig
        """
        result = self._values.get("routing_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnCodeSigningConfig(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnCodeSigningConfig",
):
    """A CloudFormation ``AWS::Lambda::CodeSigningConfig``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html
    :cloudformationResource: AWS::Lambda::CodeSigningConfig
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        allowed_publishers: typing.Union["CfnCodeSigningConfig.AllowedPublishersProperty", _IResolvable_a771d0ef],
        code_signing_policies: typing.Optional[typing.Union["CfnCodeSigningConfig.CodeSigningPoliciesProperty", _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::CodeSigningConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param allowed_publishers: ``AWS::Lambda::CodeSigningConfig.AllowedPublishers``.
        :param code_signing_policies: ``AWS::Lambda::CodeSigningConfig.CodeSigningPolicies``.
        :param description: ``AWS::Lambda::CodeSigningConfig.Description``.
        """
        props = CfnCodeSigningConfigProps(
            allowed_publishers=allowed_publishers,
            code_signing_policies=code_signing_policies,
            description=description,
        )

        jsii.create(CfnCodeSigningConfig, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCodeSigningConfigArn")
    def attr_code_signing_config_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: CodeSigningConfigArn
        """
        return jsii.get(self, "attrCodeSigningConfigArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrCodeSigningConfigId")
    def attr_code_signing_config_id(self) -> builtins.str:
        """
        :cloudformationAttribute: CodeSigningConfigId
        """
        return jsii.get(self, "attrCodeSigningConfigId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="allowedPublishers")
    def allowed_publishers(
        self,
    ) -> typing.Union["CfnCodeSigningConfig.AllowedPublishersProperty", _IResolvable_a771d0ef]:
        """``AWS::Lambda::CodeSigningConfig.AllowedPublishers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers
        """
        return jsii.get(self, "allowedPublishers")

    @allowed_publishers.setter # type: ignore
    def allowed_publishers(
        self,
        value: typing.Union["CfnCodeSigningConfig.AllowedPublishersProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "allowedPublishers", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="codeSigningPolicies")
    def code_signing_policies(
        self,
    ) -> typing.Optional[typing.Union["CfnCodeSigningConfig.CodeSigningPoliciesProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::CodeSigningConfig.CodeSigningPolicies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies
        """
        return jsii.get(self, "codeSigningPolicies")

    @code_signing_policies.setter # type: ignore
    def code_signing_policies(
        self,
        value: typing.Optional[typing.Union["CfnCodeSigningConfig.CodeSigningPoliciesProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "codeSigningPolicies", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::CodeSigningConfig.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnCodeSigningConfig.AllowedPublishersProperty",
        jsii_struct_bases=[],
        name_mapping={"signing_profile_version_arns": "signingProfileVersionArns"},
    )
    class AllowedPublishersProperty:
        def __init__(
            self,
            *,
            signing_profile_version_arns: typing.List[builtins.str],
        ) -> None:
            """
            :param signing_profile_version_arns: ``CfnCodeSigningConfig.AllowedPublishersProperty.SigningProfileVersionArns``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "signing_profile_version_arns": signing_profile_version_arns,
            }

        @builtins.property
        def signing_profile_version_arns(self) -> typing.List[builtins.str]:
            """``CfnCodeSigningConfig.AllowedPublishersProperty.SigningProfileVersionArns``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html#cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns
            """
            result = self._values.get("signing_profile_version_arns")
            assert result is not None, "Required property 'signing_profile_version_arns' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AllowedPublishersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnCodeSigningConfig.CodeSigningPoliciesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "untrusted_artifact_on_deployment": "untrustedArtifactOnDeployment",
        },
    )
    class CodeSigningPoliciesProperty:
        def __init__(self, *, untrusted_artifact_on_deployment: builtins.str) -> None:
            """
            :param untrusted_artifact_on_deployment: ``CfnCodeSigningConfig.CodeSigningPoliciesProperty.UntrustedArtifactOnDeployment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "untrusted_artifact_on_deployment": untrusted_artifact_on_deployment,
            }

        @builtins.property
        def untrusted_artifact_on_deployment(self) -> builtins.str:
            """``CfnCodeSigningConfig.CodeSigningPoliciesProperty.UntrustedArtifactOnDeployment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html#cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment
            """
            result = self._values.get("untrusted_artifact_on_deployment")
            assert result is not None, "Required property 'untrusted_artifact_on_deployment' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeSigningPoliciesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnCodeSigningConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_publishers": "allowedPublishers",
        "code_signing_policies": "codeSigningPolicies",
        "description": "description",
    },
)
class CfnCodeSigningConfigProps:
    def __init__(
        self,
        *,
        allowed_publishers: typing.Union[CfnCodeSigningConfig.AllowedPublishersProperty, _IResolvable_a771d0ef],
        code_signing_policies: typing.Optional[typing.Union[CfnCodeSigningConfig.CodeSigningPoliciesProperty, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::CodeSigningConfig``.

        :param allowed_publishers: ``AWS::Lambda::CodeSigningConfig.AllowedPublishers``.
        :param code_signing_policies: ``AWS::Lambda::CodeSigningConfig.CodeSigningPolicies``.
        :param description: ``AWS::Lambda::CodeSigningConfig.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_publishers": allowed_publishers,
        }
        if code_signing_policies is not None:
            self._values["code_signing_policies"] = code_signing_policies
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def allowed_publishers(
        self,
    ) -> typing.Union[CfnCodeSigningConfig.AllowedPublishersProperty, _IResolvable_a771d0ef]:
        """``AWS::Lambda::CodeSigningConfig.AllowedPublishers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers
        """
        result = self._values.get("allowed_publishers")
        assert result is not None, "Required property 'allowed_publishers' is missing"
        return result

    @builtins.property
    def code_signing_policies(
        self,
    ) -> typing.Optional[typing.Union[CfnCodeSigningConfig.CodeSigningPoliciesProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::CodeSigningConfig.CodeSigningPolicies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies
        """
        result = self._values.get("code_signing_policies")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::CodeSigningConfig.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description
        """
        result = self._values.get("description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeSigningConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnEventInvokeConfig(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnEventInvokeConfig",
):
    """A CloudFormation ``AWS::Lambda::EventInvokeConfig``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html
    :cloudformationResource: AWS::Lambda::EventInvokeConfig
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        function_name: builtins.str,
        qualifier: builtins.str,
        destination_config: typing.Optional[typing.Union["CfnEventInvokeConfig.DestinationConfigProperty", _IResolvable_a771d0ef]] = None,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::EventInvokeConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param function_name: ``AWS::Lambda::EventInvokeConfig.FunctionName``.
        :param qualifier: ``AWS::Lambda::EventInvokeConfig.Qualifier``.
        :param destination_config: ``AWS::Lambda::EventInvokeConfig.DestinationConfig``.
        :param maximum_event_age_in_seconds: ``AWS::Lambda::EventInvokeConfig.MaximumEventAgeInSeconds``.
        :param maximum_retry_attempts: ``AWS::Lambda::EventInvokeConfig.MaximumRetryAttempts``.
        """
        props = CfnEventInvokeConfigProps(
            function_name=function_name,
            qualifier=qualifier,
            destination_config=destination_config,
            maximum_event_age_in_seconds=maximum_event_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
        )

        jsii.create(CfnEventInvokeConfig, self, [scope, id, props])

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
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::EventInvokeConfig.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter # type: ignore
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        """``AWS::Lambda::EventInvokeConfig.Qualifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-qualifier
        """
        return jsii.get(self, "qualifier")

    @qualifier.setter # type: ignore
    def qualifier(self, value: builtins.str) -> None:
        jsii.set(self, "qualifier", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> typing.Optional[typing.Union["CfnEventInvokeConfig.DestinationConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventInvokeConfig.DestinationConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig
        """
        return jsii.get(self, "destinationConfig")

    @destination_config.setter # type: ignore
    def destination_config(
        self,
        value: typing.Optional[typing.Union["CfnEventInvokeConfig.DestinationConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "destinationConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventInvokeConfig.MaximumEventAgeInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumeventageinseconds
        """
        return jsii.get(self, "maximumEventAgeInSeconds")

    @maximum_event_age_in_seconds.setter # type: ignore
    def maximum_event_age_in_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maximumEventAgeInSeconds", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventInvokeConfig.MaximumRetryAttempts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumretryattempts
        """
        return jsii.get(self, "maximumRetryAttempts")

    @maximum_retry_attempts.setter # type: ignore
    def maximum_retry_attempts(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maximumRetryAttempts", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventInvokeConfig.DestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"on_failure": "onFailure", "on_success": "onSuccess"},
    )
    class DestinationConfigProperty:
        def __init__(
            self,
            *,
            on_failure: typing.Optional[typing.Union["CfnEventInvokeConfig.OnFailureProperty", _IResolvable_a771d0ef]] = None,
            on_success: typing.Optional[typing.Union["CfnEventInvokeConfig.OnSuccessProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param on_failure: ``CfnEventInvokeConfig.DestinationConfigProperty.OnFailure``.
            :param on_success: ``CfnEventInvokeConfig.DestinationConfigProperty.OnSuccess``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if on_failure is not None:
                self._values["on_failure"] = on_failure
            if on_success is not None:
                self._values["on_success"] = on_success

        @builtins.property
        def on_failure(
            self,
        ) -> typing.Optional[typing.Union["CfnEventInvokeConfig.OnFailureProperty", _IResolvable_a771d0ef]]:
            """``CfnEventInvokeConfig.DestinationConfigProperty.OnFailure``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure
            """
            result = self._values.get("on_failure")
            return result

        @builtins.property
        def on_success(
            self,
        ) -> typing.Optional[typing.Union["CfnEventInvokeConfig.OnSuccessProperty", _IResolvable_a771d0ef]]:
            """``CfnEventInvokeConfig.DestinationConfigProperty.OnSuccess``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess
            """
            result = self._values.get("on_success")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventInvokeConfig.OnFailureProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class OnFailureProperty:
        def __init__(self, *, destination: builtins.str) -> None:
            """
            :param destination: ``CfnEventInvokeConfig.OnFailureProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "destination": destination,
            }

        @builtins.property
        def destination(self) -> builtins.str:
            """``CfnEventInvokeConfig.OnFailureProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure-destination
            """
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnFailureProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventInvokeConfig.OnSuccessProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class OnSuccessProperty:
        def __init__(self, *, destination: builtins.str) -> None:
            """
            :param destination: ``CfnEventInvokeConfig.OnSuccessProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "destination": destination,
            }

        @builtins.property
        def destination(self) -> builtins.str:
            """``CfnEventInvokeConfig.OnSuccessProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess-destination
            """
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnSuccessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnEventInvokeConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "qualifier": "qualifier",
        "destination_config": "destinationConfig",
        "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
    },
)
class CfnEventInvokeConfigProps:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        qualifier: builtins.str,
        destination_config: typing.Optional[typing.Union[CfnEventInvokeConfig.DestinationConfigProperty, _IResolvable_a771d0ef]] = None,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::EventInvokeConfig``.

        :param function_name: ``AWS::Lambda::EventInvokeConfig.FunctionName``.
        :param qualifier: ``AWS::Lambda::EventInvokeConfig.Qualifier``.
        :param destination_config: ``AWS::Lambda::EventInvokeConfig.DestinationConfig``.
        :param maximum_event_age_in_seconds: ``AWS::Lambda::EventInvokeConfig.MaximumEventAgeInSeconds``.
        :param maximum_retry_attempts: ``AWS::Lambda::EventInvokeConfig.MaximumRetryAttempts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
            "qualifier": qualifier,
        }
        if destination_config is not None:
            self._values["destination_config"] = destination_config
        if maximum_event_age_in_seconds is not None:
            self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts

    @builtins.property
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::EventInvokeConfig.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-functionname
        """
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return result

    @builtins.property
    def qualifier(self) -> builtins.str:
        """``AWS::Lambda::EventInvokeConfig.Qualifier``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-qualifier
        """
        result = self._values.get("qualifier")
        assert result is not None, "Required property 'qualifier' is missing"
        return result

    @builtins.property
    def destination_config(
        self,
    ) -> typing.Optional[typing.Union[CfnEventInvokeConfig.DestinationConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventInvokeConfig.DestinationConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig
        """
        result = self._values.get("destination_config")
        return result

    @builtins.property
    def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventInvokeConfig.MaximumEventAgeInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumeventageinseconds
        """
        result = self._values.get("maximum_event_age_in_seconds")
        return result

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventInvokeConfig.MaximumRetryAttempts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumretryattempts
        """
        result = self._values.get("maximum_retry_attempts")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventInvokeConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnEventSourceMapping(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnEventSourceMapping",
):
    """A CloudFormation ``AWS::Lambda::EventSourceMapping``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
    :cloudformationResource: AWS::Lambda::EventSourceMapping
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        function_name: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        destination_config: typing.Optional[typing.Union["CfnEventSourceMapping.DestinationConfigProperty", _IResolvable_a771d0ef]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        event_source_arn: typing.Optional[builtins.str] = None,
        function_response_types: typing.Optional[typing.List[builtins.str]] = None,
        maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        partial_batch_response: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        queues: typing.Optional[typing.List[builtins.str]] = None,
        self_managed_event_source: typing.Optional[typing.Union["CfnEventSourceMapping.SelfManagedEventSourceProperty", _IResolvable_a771d0ef]] = None,
        source_access_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnEventSourceMapping.SourceAccessConfigurationProperty", _IResolvable_a771d0ef]]]] = None,
        starting_position: typing.Optional[builtins.str] = None,
        topics: typing.Optional[typing.List[builtins.str]] = None,
        tumbling_window_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::EventSourceMapping``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param function_name: ``AWS::Lambda::EventSourceMapping.FunctionName``.
        :param batch_size: ``AWS::Lambda::EventSourceMapping.BatchSize``.
        :param bisect_batch_on_function_error: ``AWS::Lambda::EventSourceMapping.BisectBatchOnFunctionError``.
        :param destination_config: ``AWS::Lambda::EventSourceMapping.DestinationConfig``.
        :param enabled: ``AWS::Lambda::EventSourceMapping.Enabled``.
        :param event_source_arn: ``AWS::Lambda::EventSourceMapping.EventSourceArn``.
        :param function_response_types: ``AWS::Lambda::EventSourceMapping.FunctionResponseTypes``.
        :param maximum_batching_window_in_seconds: ``AWS::Lambda::EventSourceMapping.MaximumBatchingWindowInSeconds``.
        :param maximum_record_age_in_seconds: ``AWS::Lambda::EventSourceMapping.MaximumRecordAgeInSeconds``.
        :param maximum_retry_attempts: ``AWS::Lambda::EventSourceMapping.MaximumRetryAttempts``.
        :param parallelization_factor: ``AWS::Lambda::EventSourceMapping.ParallelizationFactor``.
        :param partial_batch_response: ``AWS::Lambda::EventSourceMapping.PartialBatchResponse``.
        :param queues: ``AWS::Lambda::EventSourceMapping.Queues``.
        :param self_managed_event_source: ``AWS::Lambda::EventSourceMapping.SelfManagedEventSource``.
        :param source_access_configurations: ``AWS::Lambda::EventSourceMapping.SourceAccessConfigurations``.
        :param starting_position: ``AWS::Lambda::EventSourceMapping.StartingPosition``.
        :param topics: ``AWS::Lambda::EventSourceMapping.Topics``.
        :param tumbling_window_in_seconds: ``AWS::Lambda::EventSourceMapping.TumblingWindowInSeconds``.
        """
        props = CfnEventSourceMappingProps(
            function_name=function_name,
            batch_size=batch_size,
            bisect_batch_on_function_error=bisect_batch_on_function_error,
            destination_config=destination_config,
            enabled=enabled,
            event_source_arn=event_source_arn,
            function_response_types=function_response_types,
            maximum_batching_window_in_seconds=maximum_batching_window_in_seconds,
            maximum_record_age_in_seconds=maximum_record_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
            parallelization_factor=parallelization_factor,
            partial_batch_response=partial_batch_response,
            queues=queues,
            self_managed_event_source=self_managed_event_source,
            source_access_configurations=source_access_configurations,
            starting_position=starting_position,
            topics=topics,
            tumbling_window_in_seconds=tumbling_window_in_seconds,
        )

        jsii.create(CfnEventSourceMapping, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::EventSourceMapping.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter # type: ignore
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="batchSize")
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.BatchSize``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize
        """
        return jsii.get(self, "batchSize")

    @batch_size.setter # type: ignore
    def batch_size(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "batchSize", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="bisectBatchOnFunctionError")
    def bisect_batch_on_function_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.BisectBatchOnFunctionError``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror
        """
        return jsii.get(self, "bisectBatchOnFunctionError")

    @bisect_batch_on_function_error.setter # type: ignore
    def bisect_batch_on_function_error(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "bisectBatchOnFunctionError", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> typing.Optional[typing.Union["CfnEventSourceMapping.DestinationConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.DestinationConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig
        """
        return jsii.get(self, "destinationConfig")

    @destination_config.setter # type: ignore
    def destination_config(
        self,
        value: typing.Optional[typing.Union["CfnEventSourceMapping.DestinationConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "destinationConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.Enabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled
        """
        return jsii.get(self, "enabled")

    @enabled.setter # type: ignore
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="eventSourceArn")
    def event_source_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::EventSourceMapping.EventSourceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn
        """
        return jsii.get(self, "eventSourceArn")

    @event_source_arn.setter # type: ignore
    def event_source_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "eventSourceArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionResponseTypes")
    def function_response_types(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::EventSourceMapping.FunctionResponseTypes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes
        """
        return jsii.get(self, "functionResponseTypes")

    @function_response_types.setter # type: ignore
    def function_response_types(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "functionResponseTypes", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.MaximumBatchingWindowInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds
        """
        return jsii.get(self, "maximumBatchingWindowInSeconds")

    @maximum_batching_window_in_seconds.setter # type: ignore
    def maximum_batching_window_in_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "maximumBatchingWindowInSeconds", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.MaximumRecordAgeInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds
        """
        return jsii.get(self, "maximumRecordAgeInSeconds")

    @maximum_record_age_in_seconds.setter # type: ignore
    def maximum_record_age_in_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "maximumRecordAgeInSeconds", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.MaximumRetryAttempts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts
        """
        return jsii.get(self, "maximumRetryAttempts")

    @maximum_retry_attempts.setter # type: ignore
    def maximum_retry_attempts(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maximumRetryAttempts", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parallelizationFactor")
    def parallelization_factor(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.ParallelizationFactor``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor
        """
        return jsii.get(self, "parallelizationFactor")

    @parallelization_factor.setter # type: ignore
    def parallelization_factor(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "parallelizationFactor", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="partialBatchResponse")
    def partial_batch_response(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.PartialBatchResponse``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-partialbatchresponse
        """
        return jsii.get(self, "partialBatchResponse")

    @partial_batch_response.setter # type: ignore
    def partial_batch_response(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "partialBatchResponse", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="queues")
    def queues(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::EventSourceMapping.Queues``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues
        """
        return jsii.get(self, "queues")

    @queues.setter # type: ignore
    def queues(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "queues", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="selfManagedEventSource")
    def self_managed_event_source(
        self,
    ) -> typing.Optional[typing.Union["CfnEventSourceMapping.SelfManagedEventSourceProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.SelfManagedEventSource``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource
        """
        return jsii.get(self, "selfManagedEventSource")

    @self_managed_event_source.setter # type: ignore
    def self_managed_event_source(
        self,
        value: typing.Optional[typing.Union["CfnEventSourceMapping.SelfManagedEventSourceProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "selfManagedEventSource", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourceAccessConfigurations")
    def source_access_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnEventSourceMapping.SourceAccessConfigurationProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::Lambda::EventSourceMapping.SourceAccessConfigurations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations
        """
        return jsii.get(self, "sourceAccessConfigurations")

    @source_access_configurations.setter # type: ignore
    def source_access_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnEventSourceMapping.SourceAccessConfigurationProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "sourceAccessConfigurations", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="startingPosition")
    def starting_position(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::EventSourceMapping.StartingPosition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition
        """
        return jsii.get(self, "startingPosition")

    @starting_position.setter # type: ignore
    def starting_position(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "startingPosition", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="topics")
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::EventSourceMapping.Topics``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics
        """
        return jsii.get(self, "topics")

    @topics.setter # type: ignore
    def topics(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "topics", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tumblingWindowInSeconds")
    def tumbling_window_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.TumblingWindowInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds
        """
        return jsii.get(self, "tumblingWindowInSeconds")

    @tumbling_window_in_seconds.setter # type: ignore
    def tumbling_window_in_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "tumblingWindowInSeconds", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventSourceMapping.DestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"on_failure": "onFailure"},
    )
    class DestinationConfigProperty:
        def __init__(
            self,
            *,
            on_failure: typing.Optional[typing.Union["CfnEventSourceMapping.OnFailureProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param on_failure: ``CfnEventSourceMapping.DestinationConfigProperty.OnFailure``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if on_failure is not None:
                self._values["on_failure"] = on_failure

        @builtins.property
        def on_failure(
            self,
        ) -> typing.Optional[typing.Union["CfnEventSourceMapping.OnFailureProperty", _IResolvable_a771d0ef]]:
            """``CfnEventSourceMapping.DestinationConfigProperty.OnFailure``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html#cfn-lambda-eventsourcemapping-destinationconfig-onfailure
            """
            result = self._values.get("on_failure")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventSourceMapping.EndpointsProperty",
        jsii_struct_bases=[],
        name_mapping={"kafka_bootstrap_servers": "kafkaBootstrapServers"},
    )
    class EndpointsProperty:
        def __init__(
            self,
            *,
            kafka_bootstrap_servers: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param kafka_bootstrap_servers: ``CfnEventSourceMapping.EndpointsProperty.KafkaBootstrapServers``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if kafka_bootstrap_servers is not None:
                self._values["kafka_bootstrap_servers"] = kafka_bootstrap_servers

        @builtins.property
        def kafka_bootstrap_servers(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnEventSourceMapping.EndpointsProperty.KafkaBootstrapServers``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html#cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers
            """
            result = self._values.get("kafka_bootstrap_servers")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventSourceMapping.OnFailureProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class OnFailureProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param destination: ``CfnEventSourceMapping.OnFailureProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            """``CfnEventSourceMapping.OnFailureProperty.Destination``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html#cfn-lambda-eventsourcemapping-onfailure-destination
            """
            result = self._values.get("destination")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnFailureProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventSourceMapping.SelfManagedEventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoints": "endpoints"},
    )
    class SelfManagedEventSourceProperty:
        def __init__(
            self,
            *,
            endpoints: typing.Optional[typing.Union["CfnEventSourceMapping.EndpointsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param endpoints: ``CfnEventSourceMapping.SelfManagedEventSourceProperty.Endpoints``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if endpoints is not None:
                self._values["endpoints"] = endpoints

        @builtins.property
        def endpoints(
            self,
        ) -> typing.Optional[typing.Union["CfnEventSourceMapping.EndpointsProperty", _IResolvable_a771d0ef]]:
            """``CfnEventSourceMapping.SelfManagedEventSourceProperty.Endpoints``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints
            """
            result = self._values.get("endpoints")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedEventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnEventSourceMapping.SourceAccessConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "uri": "uri"},
    )
    class SourceAccessConfigurationProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            uri: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param type: ``CfnEventSourceMapping.SourceAccessConfigurationProperty.Type``.
            :param uri: ``CfnEventSourceMapping.SourceAccessConfigurationProperty.URI``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if uri is not None:
                self._values["uri"] = uri

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            """``CfnEventSourceMapping.SourceAccessConfigurationProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-type
            """
            result = self._values.get("type")
            return result

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            """``CfnEventSourceMapping.SourceAccessConfigurationProperty.URI``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-uri
            """
            result = self._values.get("uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceAccessConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnEventSourceMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "batch_size": "batchSize",
        "bisect_batch_on_function_error": "bisectBatchOnFunctionError",
        "destination_config": "destinationConfig",
        "enabled": "enabled",
        "event_source_arn": "eventSourceArn",
        "function_response_types": "functionResponseTypes",
        "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
        "maximum_record_age_in_seconds": "maximumRecordAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
        "parallelization_factor": "parallelizationFactor",
        "partial_batch_response": "partialBatchResponse",
        "queues": "queues",
        "self_managed_event_source": "selfManagedEventSource",
        "source_access_configurations": "sourceAccessConfigurations",
        "starting_position": "startingPosition",
        "topics": "topics",
        "tumbling_window_in_seconds": "tumblingWindowInSeconds",
    },
)
class CfnEventSourceMappingProps:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        destination_config: typing.Optional[typing.Union[CfnEventSourceMapping.DestinationConfigProperty, _IResolvable_a771d0ef]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        event_source_arn: typing.Optional[builtins.str] = None,
        function_response_types: typing.Optional[typing.List[builtins.str]] = None,
        maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        partial_batch_response: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        queues: typing.Optional[typing.List[builtins.str]] = None,
        self_managed_event_source: typing.Optional[typing.Union[CfnEventSourceMapping.SelfManagedEventSourceProperty, _IResolvable_a771d0ef]] = None,
        source_access_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnEventSourceMapping.SourceAccessConfigurationProperty, _IResolvable_a771d0ef]]]] = None,
        starting_position: typing.Optional[builtins.str] = None,
        topics: typing.Optional[typing.List[builtins.str]] = None,
        tumbling_window_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::EventSourceMapping``.

        :param function_name: ``AWS::Lambda::EventSourceMapping.FunctionName``.
        :param batch_size: ``AWS::Lambda::EventSourceMapping.BatchSize``.
        :param bisect_batch_on_function_error: ``AWS::Lambda::EventSourceMapping.BisectBatchOnFunctionError``.
        :param destination_config: ``AWS::Lambda::EventSourceMapping.DestinationConfig``.
        :param enabled: ``AWS::Lambda::EventSourceMapping.Enabled``.
        :param event_source_arn: ``AWS::Lambda::EventSourceMapping.EventSourceArn``.
        :param function_response_types: ``AWS::Lambda::EventSourceMapping.FunctionResponseTypes``.
        :param maximum_batching_window_in_seconds: ``AWS::Lambda::EventSourceMapping.MaximumBatchingWindowInSeconds``.
        :param maximum_record_age_in_seconds: ``AWS::Lambda::EventSourceMapping.MaximumRecordAgeInSeconds``.
        :param maximum_retry_attempts: ``AWS::Lambda::EventSourceMapping.MaximumRetryAttempts``.
        :param parallelization_factor: ``AWS::Lambda::EventSourceMapping.ParallelizationFactor``.
        :param partial_batch_response: ``AWS::Lambda::EventSourceMapping.PartialBatchResponse``.
        :param queues: ``AWS::Lambda::EventSourceMapping.Queues``.
        :param self_managed_event_source: ``AWS::Lambda::EventSourceMapping.SelfManagedEventSource``.
        :param source_access_configurations: ``AWS::Lambda::EventSourceMapping.SourceAccessConfigurations``.
        :param starting_position: ``AWS::Lambda::EventSourceMapping.StartingPosition``.
        :param topics: ``AWS::Lambda::EventSourceMapping.Topics``.
        :param tumbling_window_in_seconds: ``AWS::Lambda::EventSourceMapping.TumblingWindowInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
        }
        if batch_size is not None:
            self._values["batch_size"] = batch_size
        if bisect_batch_on_function_error is not None:
            self._values["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if destination_config is not None:
            self._values["destination_config"] = destination_config
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_source_arn is not None:
            self._values["event_source_arn"] = event_source_arn
        if function_response_types is not None:
            self._values["function_response_types"] = function_response_types
        if maximum_batching_window_in_seconds is not None:
            self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
        if maximum_record_age_in_seconds is not None:
            self._values["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts
        if parallelization_factor is not None:
            self._values["parallelization_factor"] = parallelization_factor
        if partial_batch_response is not None:
            self._values["partial_batch_response"] = partial_batch_response
        if queues is not None:
            self._values["queues"] = queues
        if self_managed_event_source is not None:
            self._values["self_managed_event_source"] = self_managed_event_source
        if source_access_configurations is not None:
            self._values["source_access_configurations"] = source_access_configurations
        if starting_position is not None:
            self._values["starting_position"] = starting_position
        if topics is not None:
            self._values["topics"] = topics
        if tumbling_window_in_seconds is not None:
            self._values["tumbling_window_in_seconds"] = tumbling_window_in_seconds

    @builtins.property
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::EventSourceMapping.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname
        """
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return result

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.BatchSize``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize
        """
        result = self._values.get("batch_size")
        return result

    @builtins.property
    def bisect_batch_on_function_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.BisectBatchOnFunctionError``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror
        """
        result = self._values.get("bisect_batch_on_function_error")
        return result

    @builtins.property
    def destination_config(
        self,
    ) -> typing.Optional[typing.Union[CfnEventSourceMapping.DestinationConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.DestinationConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig
        """
        result = self._values.get("destination_config")
        return result

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.Enabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def event_source_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::EventSourceMapping.EventSourceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn
        """
        result = self._values.get("event_source_arn")
        return result

    @builtins.property
    def function_response_types(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::EventSourceMapping.FunctionResponseTypes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes
        """
        result = self._values.get("function_response_types")
        return result

    @builtins.property
    def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.MaximumBatchingWindowInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds
        """
        result = self._values.get("maximum_batching_window_in_seconds")
        return result

    @builtins.property
    def maximum_record_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.MaximumRecordAgeInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds
        """
        result = self._values.get("maximum_record_age_in_seconds")
        return result

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.MaximumRetryAttempts``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts
        """
        result = self._values.get("maximum_retry_attempts")
        return result

    @builtins.property
    def parallelization_factor(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.ParallelizationFactor``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor
        """
        result = self._values.get("parallelization_factor")
        return result

    @builtins.property
    def partial_batch_response(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.PartialBatchResponse``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-partialbatchresponse
        """
        result = self._values.get("partial_batch_response")
        return result

    @builtins.property
    def queues(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::EventSourceMapping.Queues``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues
        """
        result = self._values.get("queues")
        return result

    @builtins.property
    def self_managed_event_source(
        self,
    ) -> typing.Optional[typing.Union[CfnEventSourceMapping.SelfManagedEventSourceProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::EventSourceMapping.SelfManagedEventSource``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource
        """
        result = self._values.get("self_managed_event_source")
        return result

    @builtins.property
    def source_access_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnEventSourceMapping.SourceAccessConfigurationProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::Lambda::EventSourceMapping.SourceAccessConfigurations``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations
        """
        result = self._values.get("source_access_configurations")
        return result

    @builtins.property
    def starting_position(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::EventSourceMapping.StartingPosition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition
        """
        result = self._values.get("starting_position")
        return result

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::EventSourceMapping.Topics``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics
        """
        result = self._values.get("topics")
        return result

    @builtins.property
    def tumbling_window_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::EventSourceMapping.TumblingWindowInSeconds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds
        """
        result = self._values.get("tumbling_window_in_seconds")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventSourceMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnFunction(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnFunction",
):
    """A CloudFormation ``AWS::Lambda::Function``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
    :cloudformationResource: AWS::Lambda::Function
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        code: typing.Union["CfnFunction.CodeProperty", _IResolvable_a771d0ef],
        role: builtins.str,
        code_signing_config_arn: typing.Optional[builtins.str] = None,
        dead_letter_config: typing.Optional[typing.Union["CfnFunction.DeadLetterConfigProperty", _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Union["CfnFunction.EnvironmentProperty", _IResolvable_a771d0ef]] = None,
        file_system_configs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnFunction.FileSystemConfigProperty", _IResolvable_a771d0ef]]]] = None,
        function_name: typing.Optional[builtins.str] = None,
        handler: typing.Optional[builtins.str] = None,
        image_config: typing.Optional[typing.Union["CfnFunction.ImageConfigProperty", _IResolvable_a771d0ef]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        layers: typing.Optional[typing.List[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        package_type: typing.Optional[builtins.str] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        runtime: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        tracing_config: typing.Optional[typing.Union["CfnFunction.TracingConfigProperty", _IResolvable_a771d0ef]] = None,
        vpc_config: typing.Optional[typing.Union["CfnFunction.VpcConfigProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::Function``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param code: ``AWS::Lambda::Function.Code``.
        :param role: ``AWS::Lambda::Function.Role``.
        :param code_signing_config_arn: ``AWS::Lambda::Function.CodeSigningConfigArn``.
        :param dead_letter_config: ``AWS::Lambda::Function.DeadLetterConfig``.
        :param description: ``AWS::Lambda::Function.Description``.
        :param environment: ``AWS::Lambda::Function.Environment``.
        :param file_system_configs: ``AWS::Lambda::Function.FileSystemConfigs``.
        :param function_name: ``AWS::Lambda::Function.FunctionName``.
        :param handler: ``AWS::Lambda::Function.Handler``.
        :param image_config: ``AWS::Lambda::Function.ImageConfig``.
        :param kms_key_arn: ``AWS::Lambda::Function.KmsKeyArn``.
        :param layers: ``AWS::Lambda::Function.Layers``.
        :param memory_size: ``AWS::Lambda::Function.MemorySize``.
        :param package_type: ``AWS::Lambda::Function.PackageType``.
        :param reserved_concurrent_executions: ``AWS::Lambda::Function.ReservedConcurrentExecutions``.
        :param runtime: ``AWS::Lambda::Function.Runtime``.
        :param tags: ``AWS::Lambda::Function.Tags``.
        :param timeout: ``AWS::Lambda::Function.Timeout``.
        :param tracing_config: ``AWS::Lambda::Function.TracingConfig``.
        :param vpc_config: ``AWS::Lambda::Function.VpcConfig``.
        """
        props = CfnFunctionProps(
            code=code,
            role=role,
            code_signing_config_arn=code_signing_config_arn,
            dead_letter_config=dead_letter_config,
            description=description,
            environment=environment,
            file_system_configs=file_system_configs,
            function_name=function_name,
            handler=handler,
            image_config=image_config,
            kms_key_arn=kms_key_arn,
            layers=layers,
            memory_size=memory_size,
            package_type=package_type,
            reserved_concurrent_executions=reserved_concurrent_executions,
            runtime=runtime,
            tags=tags,
            timeout=timeout,
            tracing_config=tracing_config,
            vpc_config=vpc_config,
        )

        jsii.create(CfnFunction, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::Lambda::Function.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Union["CfnFunction.CodeProperty", _IResolvable_a771d0ef]:
        """``AWS::Lambda::Function.Code``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-code
        """
        return jsii.get(self, "code")

    @code.setter # type: ignore
    def code(
        self,
        value: typing.Union["CfnFunction.CodeProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "code", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        """``AWS::Lambda::Function.Role``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role
        """
        return jsii.get(self, "role")

    @role.setter # type: ignore
    def role(self, value: builtins.str) -> None:
        jsii.set(self, "role", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.CodeSigningConfigArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-codesigningconfigarn
        """
        return jsii.get(self, "codeSigningConfigArn")

    @code_signing_config_arn.setter # type: ignore
    def code_signing_config_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "codeSigningConfigArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFunction.DeadLetterConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.DeadLetterConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-deadletterconfig
        """
        return jsii.get(self, "deadLetterConfig")

    @dead_letter_config.setter # type: ignore
    def dead_letter_config(
        self,
        value: typing.Optional[typing.Union["CfnFunction.DeadLetterConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "deadLetterConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="environment")
    def environment(
        self,
    ) -> typing.Optional[typing.Union["CfnFunction.EnvironmentProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.Environment``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-environment
        """
        return jsii.get(self, "environment")

    @environment.setter # type: ignore
    def environment(
        self,
        value: typing.Optional[typing.Union["CfnFunction.EnvironmentProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "environment", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="fileSystemConfigs")
    def file_system_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnFunction.FileSystemConfigProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::Lambda::Function.FileSystemConfigs``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-filesystemconfigs
        """
        return jsii.get(self, "fileSystemConfigs")

    @file_system_configs.setter # type: ignore
    def file_system_configs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnFunction.FileSystemConfigProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "fileSystemConfigs", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter # type: ignore
    def function_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="handler")
    def handler(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.Handler``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-handler
        """
        return jsii.get(self, "handler")

    @handler.setter # type: ignore
    def handler(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "handler", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="imageConfig")
    def image_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFunction.ImageConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.ImageConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig
        """
        return jsii.get(self, "imageConfig")

    @image_config.setter # type: ignore
    def image_config(
        self,
        value: typing.Optional[typing.Union["CfnFunction.ImageConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "imageConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.KmsKeyArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn
        """
        return jsii.get(self, "kmsKeyArn")

    @kms_key_arn.setter # type: ignore
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="layers")
    def layers(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::Function.Layers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-layers
        """
        return jsii.get(self, "layers")

    @layers.setter # type: ignore
    def layers(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "layers", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::Function.MemorySize``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize
        """
        return jsii.get(self, "memorySize")

    @memory_size.setter # type: ignore
    def memory_size(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "memorySize", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="packageType")
    def package_type(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.PackageType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-packagetype
        """
        return jsii.get(self, "packageType")

    @package_type.setter # type: ignore
    def package_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "packageType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::Function.ReservedConcurrentExecutions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-reservedconcurrentexecutions
        """
        return jsii.get(self, "reservedConcurrentExecutions")

    @reserved_concurrent_executions.setter # type: ignore
    def reserved_concurrent_executions(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "reservedConcurrentExecutions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.Runtime``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime
        """
        return jsii.get(self, "runtime")

    @runtime.setter # type: ignore
    def runtime(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "runtime", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::Function.Timeout``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout
        """
        return jsii.get(self, "timeout")

    @timeout.setter # type: ignore
    def timeout(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "timeout", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tracingConfig")
    def tracing_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFunction.TracingConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.TracingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tracingconfig
        """
        return jsii.get(self, "tracingConfig")

    @tracing_config.setter # type: ignore
    def tracing_config(
        self,
        value: typing.Optional[typing.Union["CfnFunction.TracingConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "tracingConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFunction.VpcConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.VpcConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-vpcconfig
        """
        return jsii.get(self, "vpcConfig")

    @vpc_config.setter # type: ignore
    def vpc_config(
        self,
        value: typing.Optional[typing.Union["CfnFunction.VpcConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.CodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "s3_object_version": "s3ObjectVersion",
            "zip_file": "zipFile",
        },
    )
    class CodeProperty:
        def __init__(
            self,
            *,
            image_uri: typing.Optional[builtins.str] = None,
            s3_bucket: typing.Optional[builtins.str] = None,
            s3_key: typing.Optional[builtins.str] = None,
            s3_object_version: typing.Optional[builtins.str] = None,
            zip_file: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param image_uri: ``CfnFunction.CodeProperty.ImageUri``.
            :param s3_bucket: ``CfnFunction.CodeProperty.S3Bucket``.
            :param s3_key: ``CfnFunction.CodeProperty.S3Key``.
            :param s3_object_version: ``CfnFunction.CodeProperty.S3ObjectVersion``.
            :param zip_file: ``CfnFunction.CodeProperty.ZipFile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if image_uri is not None:
                self._values["image_uri"] = image_uri
            if s3_bucket is not None:
                self._values["s3_bucket"] = s3_bucket
            if s3_key is not None:
                self._values["s3_key"] = s3_key
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version
            if zip_file is not None:
                self._values["zip_file"] = zip_file

        @builtins.property
        def image_uri(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.CodeProperty.ImageUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri
            """
            result = self._values.get("image_uri")
            return result

        @builtins.property
        def s3_bucket(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.CodeProperty.S3Bucket``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3bucket
            """
            result = self._values.get("s3_bucket")
            return result

        @builtins.property
        def s3_key(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.CodeProperty.S3Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3key
            """
            result = self._values.get("s3_key")
            return result

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.CodeProperty.S3ObjectVersion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3objectversion
            """
            result = self._values.get("s3_object_version")
            return result

        @builtins.property
        def zip_file(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.CodeProperty.ZipFile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile
            """
            result = self._values.get("zip_file")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.DeadLetterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"target_arn": "targetArn"},
    )
    class DeadLetterConfigProperty:
        def __init__(self, *, target_arn: typing.Optional[builtins.str] = None) -> None:
            """
            :param target_arn: ``CfnFunction.DeadLetterConfigProperty.TargetArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if target_arn is not None:
                self._values["target_arn"] = target_arn

        @builtins.property
        def target_arn(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.DeadLetterConfigProperty.TargetArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html#cfn-lambda-function-deadletterconfig-targetarn
            """
            result = self._values.get("target_arn")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeadLetterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"variables": "variables"},
    )
    class EnvironmentProperty:
        def __init__(
            self,
            *,
            variables: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            """
            :param variables: ``CfnFunction.EnvironmentProperty.Variables``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if variables is not None:
                self._values["variables"] = variables

        @builtins.property
        def variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
            """``CfnFunction.EnvironmentProperty.Variables``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html#cfn-lambda-function-environment-variables
            """
            result = self._values.get("variables")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.FileSystemConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "local_mount_path": "localMountPath"},
    )
    class FileSystemConfigProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            local_mount_path: builtins.str,
        ) -> None:
            """
            :param arn: ``CfnFunction.FileSystemConfigProperty.Arn``.
            :param local_mount_path: ``CfnFunction.FileSystemConfigProperty.LocalMountPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "local_mount_path": local_mount_path,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            """``CfnFunction.FileSystemConfigProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-arn
            """
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return result

        @builtins.property
        def local_mount_path(self) -> builtins.str:
            """``CfnFunction.FileSystemConfigProperty.LocalMountPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-localmountpath
            """
            result = self._values.get("local_mount_path")
            assert result is not None, "Required property 'local_mount_path' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileSystemConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.ImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "entry_point": "entryPoint",
            "working_directory": "workingDirectory",
        },
    )
    class ImageConfigProperty:
        def __init__(
            self,
            *,
            command: typing.Optional[typing.List[builtins.str]] = None,
            entry_point: typing.Optional[typing.List[builtins.str]] = None,
            working_directory: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param command: ``CfnFunction.ImageConfigProperty.Command``.
            :param entry_point: ``CfnFunction.ImageConfigProperty.EntryPoint``.
            :param working_directory: ``CfnFunction.ImageConfigProperty.WorkingDirectory``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if command is not None:
                self._values["command"] = command
            if entry_point is not None:
                self._values["entry_point"] = entry_point
            if working_directory is not None:
                self._values["working_directory"] = working_directory

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnFunction.ImageConfigProperty.Command``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-command
            """
            result = self._values.get("command")
            return result

        @builtins.property
        def entry_point(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnFunction.ImageConfigProperty.EntryPoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-entrypoint
            """
            result = self._values.get("entry_point")
            return result

        @builtins.property
        def working_directory(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.ImageConfigProperty.WorkingDirectory``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-workingdirectory
            """
            result = self._values.get("working_directory")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.TracingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class TracingConfigProperty:
        def __init__(self, *, mode: typing.Optional[builtins.str] = None) -> None:
            """
            :param mode: ``CfnFunction.TracingConfigProperty.Mode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if mode is not None:
                self._values["mode"] = mode

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            """``CfnFunction.TracingConfigProperty.Mode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html#cfn-lambda-function-tracingconfig-mode
            """
            result = self._values.get("mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TracingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnFunction.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnet_ids: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnFunction.VpcConfigProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnFunction.VpcConfigProperty.SubnetIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnFunction.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            """``CfnFunction.VpcConfigProperty.SubnetIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-subnetids
            """
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "code": "code",
        "role": "role",
        "code_signing_config_arn": "codeSigningConfigArn",
        "dead_letter_config": "deadLetterConfig",
        "description": "description",
        "environment": "environment",
        "file_system_configs": "fileSystemConfigs",
        "function_name": "functionName",
        "handler": "handler",
        "image_config": "imageConfig",
        "kms_key_arn": "kmsKeyArn",
        "layers": "layers",
        "memory_size": "memorySize",
        "package_type": "packageType",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "runtime": "runtime",
        "tags": "tags",
        "timeout": "timeout",
        "tracing_config": "tracingConfig",
        "vpc_config": "vpcConfig",
    },
)
class CfnFunctionProps:
    def __init__(
        self,
        *,
        code: typing.Union[CfnFunction.CodeProperty, _IResolvable_a771d0ef],
        role: builtins.str,
        code_signing_config_arn: typing.Optional[builtins.str] = None,
        dead_letter_config: typing.Optional[typing.Union[CfnFunction.DeadLetterConfigProperty, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Union[CfnFunction.EnvironmentProperty, _IResolvable_a771d0ef]] = None,
        file_system_configs: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnFunction.FileSystemConfigProperty, _IResolvable_a771d0ef]]]] = None,
        function_name: typing.Optional[builtins.str] = None,
        handler: typing.Optional[builtins.str] = None,
        image_config: typing.Optional[typing.Union[CfnFunction.ImageConfigProperty, _IResolvable_a771d0ef]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        layers: typing.Optional[typing.List[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        package_type: typing.Optional[builtins.str] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        runtime: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        tracing_config: typing.Optional[typing.Union[CfnFunction.TracingConfigProperty, _IResolvable_a771d0ef]] = None,
        vpc_config: typing.Optional[typing.Union[CfnFunction.VpcConfigProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::Function``.

        :param code: ``AWS::Lambda::Function.Code``.
        :param role: ``AWS::Lambda::Function.Role``.
        :param code_signing_config_arn: ``AWS::Lambda::Function.CodeSigningConfigArn``.
        :param dead_letter_config: ``AWS::Lambda::Function.DeadLetterConfig``.
        :param description: ``AWS::Lambda::Function.Description``.
        :param environment: ``AWS::Lambda::Function.Environment``.
        :param file_system_configs: ``AWS::Lambda::Function.FileSystemConfigs``.
        :param function_name: ``AWS::Lambda::Function.FunctionName``.
        :param handler: ``AWS::Lambda::Function.Handler``.
        :param image_config: ``AWS::Lambda::Function.ImageConfig``.
        :param kms_key_arn: ``AWS::Lambda::Function.KmsKeyArn``.
        :param layers: ``AWS::Lambda::Function.Layers``.
        :param memory_size: ``AWS::Lambda::Function.MemorySize``.
        :param package_type: ``AWS::Lambda::Function.PackageType``.
        :param reserved_concurrent_executions: ``AWS::Lambda::Function.ReservedConcurrentExecutions``.
        :param runtime: ``AWS::Lambda::Function.Runtime``.
        :param tags: ``AWS::Lambda::Function.Tags``.
        :param timeout: ``AWS::Lambda::Function.Timeout``.
        :param tracing_config: ``AWS::Lambda::Function.TracingConfig``.
        :param vpc_config: ``AWS::Lambda::Function.VpcConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "code": code,
            "role": role,
        }
        if code_signing_config_arn is not None:
            self._values["code_signing_config_arn"] = code_signing_config_arn
        if dead_letter_config is not None:
            self._values["dead_letter_config"] = dead_letter_config
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if file_system_configs is not None:
            self._values["file_system_configs"] = file_system_configs
        if function_name is not None:
            self._values["function_name"] = function_name
        if handler is not None:
            self._values["handler"] = handler
        if image_config is not None:
            self._values["image_config"] = image_config
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if layers is not None:
            self._values["layers"] = layers
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if package_type is not None:
            self._values["package_type"] = package_type
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if runtime is not None:
            self._values["runtime"] = runtime
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing_config is not None:
            self._values["tracing_config"] = tracing_config
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def code(self) -> typing.Union[CfnFunction.CodeProperty, _IResolvable_a771d0ef]:
        """``AWS::Lambda::Function.Code``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-code
        """
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return result

    @builtins.property
    def role(self) -> builtins.str:
        """``AWS::Lambda::Function.Role``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role
        """
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return result

    @builtins.property
    def code_signing_config_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.CodeSigningConfigArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-codesigningconfigarn
        """
        result = self._values.get("code_signing_config_arn")
        return result

    @builtins.property
    def dead_letter_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFunction.DeadLetterConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.DeadLetterConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-deadletterconfig
        """
        result = self._values.get("dead_letter_config")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Union[CfnFunction.EnvironmentProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.Environment``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-environment
        """
        result = self._values.get("environment")
        return result

    @builtins.property
    def file_system_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnFunction.FileSystemConfigProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::Lambda::Function.FileSystemConfigs``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-filesystemconfigs
        """
        result = self._values.get("file_system_configs")
        return result

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionname
        """
        result = self._values.get("function_name")
        return result

    @builtins.property
    def handler(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.Handler``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-handler
        """
        result = self._values.get("handler")
        return result

    @builtins.property
    def image_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFunction.ImageConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.ImageConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig
        """
        result = self._values.get("image_config")
        return result

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.KmsKeyArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn
        """
        result = self._values.get("kms_key_arn")
        return result

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::Function.Layers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-layers
        """
        result = self._values.get("layers")
        return result

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::Function.MemorySize``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize
        """
        result = self._values.get("memory_size")
        return result

    @builtins.property
    def package_type(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.PackageType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-packagetype
        """
        result = self._values.get("package_type")
        return result

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::Function.ReservedConcurrentExecutions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-reservedconcurrentexecutions
        """
        result = self._values.get("reserved_concurrent_executions")
        return result

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Function.Runtime``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime
        """
        result = self._values.get("runtime")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::Lambda::Function.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        """``AWS::Lambda::Function.Timeout``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout
        """
        result = self._values.get("timeout")
        return result

    @builtins.property
    def tracing_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFunction.TracingConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.TracingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tracingconfig
        """
        result = self._values.get("tracing_config")
        return result

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFunction.VpcConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Function.VpcConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-vpcconfig
        """
        result = self._values.get("vpc_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnLayerVersion(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnLayerVersion",
):
    """A CloudFormation ``AWS::Lambda::LayerVersion``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html
    :cloudformationResource: AWS::Lambda::LayerVersion
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        content: typing.Union["CfnLayerVersion.ContentProperty", _IResolvable_a771d0ef],
        compatible_runtimes: typing.Optional[typing.List[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        layer_name: typing.Optional[builtins.str] = None,
        license_info: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::LayerVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: ``AWS::Lambda::LayerVersion.Content``.
        :param compatible_runtimes: ``AWS::Lambda::LayerVersion.CompatibleRuntimes``.
        :param description: ``AWS::Lambda::LayerVersion.Description``.
        :param layer_name: ``AWS::Lambda::LayerVersion.LayerName``.
        :param license_info: ``AWS::Lambda::LayerVersion.LicenseInfo``.
        """
        props = CfnLayerVersionProps(
            content=content,
            compatible_runtimes=compatible_runtimes,
            description=description,
            layer_name=layer_name,
            license_info=license_info,
        )

        jsii.create(CfnLayerVersion, self, [scope, id, props])

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
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Union["CfnLayerVersion.ContentProperty", _IResolvable_a771d0ef]:
        """``AWS::Lambda::LayerVersion.Content``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-content
        """
        return jsii.get(self, "content")

    @content.setter # type: ignore
    def content(
        self,
        value: typing.Union["CfnLayerVersion.ContentProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="compatibleRuntimes")
    def compatible_runtimes(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::LayerVersion.CompatibleRuntimes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatibleruntimes
        """
        return jsii.get(self, "compatibleRuntimes")

    @compatible_runtimes.setter # type: ignore
    def compatible_runtimes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "compatibleRuntimes", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersion.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="layerName")
    def layer_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersion.LayerName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-layername
        """
        return jsii.get(self, "layerName")

    @layer_name.setter # type: ignore
    def layer_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "layerName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="licenseInfo")
    def license_info(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersion.LicenseInfo``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-licenseinfo
        """
        return jsii.get(self, "licenseInfo")

    @license_info.setter # type: ignore
    def license_info(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "licenseInfo", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnLayerVersion.ContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "s3_object_version": "s3ObjectVersion",
        },
    )
    class ContentProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_key: builtins.str,
            s3_object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param s3_bucket: ``CfnLayerVersion.ContentProperty.S3Bucket``.
            :param s3_key: ``CfnLayerVersion.ContentProperty.S3Key``.
            :param s3_object_version: ``CfnLayerVersion.ContentProperty.S3ObjectVersion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            """``CfnLayerVersion.ContentProperty.S3Bucket``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3bucket
            """
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return result

        @builtins.property
        def s3_key(self) -> builtins.str:
            """``CfnLayerVersion.ContentProperty.S3Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3key
            """
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return result

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            """``CfnLayerVersion.ContentProperty.S3ObjectVersion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3objectversion
            """
            result = self._values.get("s3_object_version")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnLayerVersionPermission(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnLayerVersionPermission",
):
    """A CloudFormation ``AWS::Lambda::LayerVersionPermission``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html
    :cloudformationResource: AWS::Lambda::LayerVersionPermission
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        action: builtins.str,
        layer_version_arn: builtins.str,
        principal: builtins.str,
        organization_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::LayerVersionPermission``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::Lambda::LayerVersionPermission.Action``.
        :param layer_version_arn: ``AWS::Lambda::LayerVersionPermission.LayerVersionArn``.
        :param principal: ``AWS::Lambda::LayerVersionPermission.Principal``.
        :param organization_id: ``AWS::Lambda::LayerVersionPermission.OrganizationId``.
        """
        props = CfnLayerVersionPermissionProps(
            action=action,
            layer_version_arn=layer_version_arn,
            principal=principal,
            organization_id=organization_id,
        )

        jsii.create(CfnLayerVersionPermission, self, [scope, id, props])

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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        """``AWS::Lambda::LayerVersionPermission.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-action
        """
        return jsii.get(self, "action")

    @action.setter # type: ignore
    def action(self, value: builtins.str) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="layerVersionArn")
    def layer_version_arn(self) -> builtins.str:
        """``AWS::Lambda::LayerVersionPermission.LayerVersionArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-layerversionarn
        """
        return jsii.get(self, "layerVersionArn")

    @layer_version_arn.setter # type: ignore
    def layer_version_arn(self, value: builtins.str) -> None:
        jsii.set(self, "layerVersionArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        """``AWS::Lambda::LayerVersionPermission.Principal``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-principal
        """
        return jsii.get(self, "principal")

    @principal.setter # type: ignore
    def principal(self, value: builtins.str) -> None:
        jsii.set(self, "principal", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersionPermission.OrganizationId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-organizationid
        """
        return jsii.get(self, "organizationId")

    @organization_id.setter # type: ignore
    def organization_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "organizationId", value)


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnLayerVersionPermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "layer_version_arn": "layerVersionArn",
        "principal": "principal",
        "organization_id": "organizationId",
    },
)
class CfnLayerVersionPermissionProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        layer_version_arn: builtins.str,
        principal: builtins.str,
        organization_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::LayerVersionPermission``.

        :param action: ``AWS::Lambda::LayerVersionPermission.Action``.
        :param layer_version_arn: ``AWS::Lambda::LayerVersionPermission.LayerVersionArn``.
        :param principal: ``AWS::Lambda::LayerVersionPermission.Principal``.
        :param organization_id: ``AWS::Lambda::LayerVersionPermission.OrganizationId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "layer_version_arn": layer_version_arn,
            "principal": principal,
        }
        if organization_id is not None:
            self._values["organization_id"] = organization_id

    @builtins.property
    def action(self) -> builtins.str:
        """``AWS::Lambda::LayerVersionPermission.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-action
        """
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return result

    @builtins.property
    def layer_version_arn(self) -> builtins.str:
        """``AWS::Lambda::LayerVersionPermission.LayerVersionArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-layerversionarn
        """
        result = self._values.get("layer_version_arn")
        assert result is not None, "Required property 'layer_version_arn' is missing"
        return result

    @builtins.property
    def principal(self) -> builtins.str:
        """``AWS::Lambda::LayerVersionPermission.Principal``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-principal
        """
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return result

    @builtins.property
    def organization_id(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersionPermission.OrganizationId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-organizationid
        """
        result = self._values.get("organization_id")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLayerVersionPermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnLayerVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "compatible_runtimes": "compatibleRuntimes",
        "description": "description",
        "layer_name": "layerName",
        "license_info": "licenseInfo",
    },
)
class CfnLayerVersionProps:
    def __init__(
        self,
        *,
        content: typing.Union[CfnLayerVersion.ContentProperty, _IResolvable_a771d0ef],
        compatible_runtimes: typing.Optional[typing.List[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        layer_name: typing.Optional[builtins.str] = None,
        license_info: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::LayerVersion``.

        :param content: ``AWS::Lambda::LayerVersion.Content``.
        :param compatible_runtimes: ``AWS::Lambda::LayerVersion.CompatibleRuntimes``.
        :param description: ``AWS::Lambda::LayerVersion.Description``.
        :param layer_name: ``AWS::Lambda::LayerVersion.LayerName``.
        :param license_info: ``AWS::Lambda::LayerVersion.LicenseInfo``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if compatible_runtimes is not None:
            self._values["compatible_runtimes"] = compatible_runtimes
        if description is not None:
            self._values["description"] = description
        if layer_name is not None:
            self._values["layer_name"] = layer_name
        if license_info is not None:
            self._values["license_info"] = license_info

    @builtins.property
    def content(
        self,
    ) -> typing.Union[CfnLayerVersion.ContentProperty, _IResolvable_a771d0ef]:
        """``AWS::Lambda::LayerVersion.Content``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-content
        """
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return result

    @builtins.property
    def compatible_runtimes(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Lambda::LayerVersion.CompatibleRuntimes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatibleruntimes
        """
        result = self._values.get("compatible_runtimes")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersion.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def layer_name(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersion.LayerName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-layername
        """
        result = self._values.get("layer_name")
        return result

    @builtins.property
    def license_info(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::LayerVersion.LicenseInfo``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-licenseinfo
        """
        result = self._values.get("license_info")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLayerVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnParametersCodeProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name_param": "bucketNameParam",
        "object_key_param": "objectKeyParam",
    },
)
class CfnParametersCodeProps:
    def __init__(
        self,
        *,
        bucket_name_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
        object_key_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
    ) -> None:
        """(experimental) Construction properties for {@link CfnParametersCode}.

        :param bucket_name_param: (experimental) The CloudFormation parameter that represents the name of the S3 Bucket where the Lambda code will be located in. Must be of type 'String'. Default: a new parameter will be created
        :param object_key_param: (experimental) The CloudFormation parameter that represents the path inside the S3 Bucket where the Lambda code will be located at. Must be of type 'String'. Default: a new parameter will be created

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name_param is not None:
            self._values["bucket_name_param"] = bucket_name_param
        if object_key_param is not None:
            self._values["object_key_param"] = object_key_param

    @builtins.property
    def bucket_name_param(self) -> typing.Optional[_CfnParameter_3e6f99ac]:
        """(experimental) The CloudFormation parameter that represents the name of the S3 Bucket where the Lambda code will be located in.

        Must be of type 'String'.

        :default: a new parameter will be created

        :stability: experimental
        """
        result = self._values.get("bucket_name_param")
        return result

    @builtins.property
    def object_key_param(self) -> typing.Optional[_CfnParameter_3e6f99ac]:
        """(experimental) The CloudFormation parameter that represents the path inside the S3 Bucket where the Lambda code will be located at.

        Must be of type 'String'.

        :default: a new parameter will be created

        :stability: experimental
        """
        result = self._values.get("object_key_param")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParametersCodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnPermission(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnPermission",
):
    """A CloudFormation ``AWS::Lambda::Permission``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html
    :cloudformationResource: AWS::Lambda::Permission
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        action: builtins.str,
        function_name: builtins.str,
        principal: builtins.str,
        event_source_token: typing.Optional[builtins.str] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::Permission``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::Lambda::Permission.Action``.
        :param function_name: ``AWS::Lambda::Permission.FunctionName``.
        :param principal: ``AWS::Lambda::Permission.Principal``.
        :param event_source_token: ``AWS::Lambda::Permission.EventSourceToken``.
        :param source_account: ``AWS::Lambda::Permission.SourceAccount``.
        :param source_arn: ``AWS::Lambda::Permission.SourceArn``.
        """
        props = CfnPermissionProps(
            action=action,
            function_name=function_name,
            principal=principal,
            event_source_token=event_source_token,
            source_account=source_account,
            source_arn=source_arn,
        )

        jsii.create(CfnPermission, self, [scope, id, props])

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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        """``AWS::Lambda::Permission.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-action
        """
        return jsii.get(self, "action")

    @action.setter # type: ignore
    def action(self, value: builtins.str) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::Permission.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter # type: ignore
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        """``AWS::Lambda::Permission.Principal``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principal
        """
        return jsii.get(self, "principal")

    @principal.setter # type: ignore
    def principal(self, value: builtins.str) -> None:
        jsii.set(self, "principal", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="eventSourceToken")
    def event_source_token(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Permission.EventSourceToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-eventsourcetoken
        """
        return jsii.get(self, "eventSourceToken")

    @event_source_token.setter # type: ignore
    def event_source_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "eventSourceToken", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourceAccount")
    def source_account(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Permission.SourceAccount``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourceaccount
        """
        return jsii.get(self, "sourceAccount")

    @source_account.setter # type: ignore
    def source_account(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sourceAccount", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Permission.SourceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourcearn
        """
        return jsii.get(self, "sourceArn")

    @source_arn.setter # type: ignore
    def source_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sourceArn", value)


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnPermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "function_name": "functionName",
        "principal": "principal",
        "event_source_token": "eventSourceToken",
        "source_account": "sourceAccount",
        "source_arn": "sourceArn",
    },
)
class CfnPermissionProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        function_name: builtins.str,
        principal: builtins.str,
        event_source_token: typing.Optional[builtins.str] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::Permission``.

        :param action: ``AWS::Lambda::Permission.Action``.
        :param function_name: ``AWS::Lambda::Permission.FunctionName``.
        :param principal: ``AWS::Lambda::Permission.Principal``.
        :param event_source_token: ``AWS::Lambda::Permission.EventSourceToken``.
        :param source_account: ``AWS::Lambda::Permission.SourceAccount``.
        :param source_arn: ``AWS::Lambda::Permission.SourceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "function_name": function_name,
            "principal": principal,
        }
        if event_source_token is not None:
            self._values["event_source_token"] = event_source_token
        if source_account is not None:
            self._values["source_account"] = source_account
        if source_arn is not None:
            self._values["source_arn"] = source_arn

    @builtins.property
    def action(self) -> builtins.str:
        """``AWS::Lambda::Permission.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-action
        """
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return result

    @builtins.property
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::Permission.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionname
        """
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return result

    @builtins.property
    def principal(self) -> builtins.str:
        """``AWS::Lambda::Permission.Principal``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principal
        """
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return result

    @builtins.property
    def event_source_token(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Permission.EventSourceToken``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-eventsourcetoken
        """
        result = self._values.get("event_source_token")
        return result

    @builtins.property
    def source_account(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Permission.SourceAccount``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourceaccount
        """
        result = self._values.get("source_account")
        return result

    @builtins.property
    def source_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Permission.SourceArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourcearn
        """
        result = self._values.get("source_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnVersion(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnVersion",
):
    """A CloudFormation ``AWS::Lambda::Version``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html
    :cloudformationResource: AWS::Lambda::Version
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        function_name: builtins.str,
        code_sha256: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrency_config: typing.Optional[typing.Union["CfnVersion.ProvisionedConcurrencyConfigurationProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::Lambda::Version``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param function_name: ``AWS::Lambda::Version.FunctionName``.
        :param code_sha256: ``AWS::Lambda::Version.CodeSha256``.
        :param description: ``AWS::Lambda::Version.Description``.
        :param provisioned_concurrency_config: ``AWS::Lambda::Version.ProvisionedConcurrencyConfig``.
        """
        props = CfnVersionProps(
            function_name=function_name,
            code_sha256=code_sha256,
            description=description,
            provisioned_concurrency_config=provisioned_concurrency_config,
        )

        jsii.create(CfnVersion, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        """
        :cloudformationAttribute: Version
        """
        return jsii.get(self, "attrVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::Version.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter # type: ignore
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="codeSha256")
    def code_sha256(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Version.CodeSha256``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-codesha256
        """
        return jsii.get(self, "codeSha256")

    @code_sha256.setter # type: ignore
    def code_sha256(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "codeSha256", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Version.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="provisionedConcurrencyConfig")
    def provisioned_concurrency_config(
        self,
    ) -> typing.Optional[typing.Union["CfnVersion.ProvisionedConcurrencyConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Version.ProvisionedConcurrencyConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-provisionedconcurrencyconfig
        """
        return jsii.get(self, "provisionedConcurrencyConfig")

    @provisioned_concurrency_config.setter # type: ignore
    def provisioned_concurrency_config(
        self,
        value: typing.Optional[typing.Union["CfnVersion.ProvisionedConcurrencyConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "provisionedConcurrencyConfig", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lambda.CfnVersion.ProvisionedConcurrencyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
        },
    )
    class ProvisionedConcurrencyConfigurationProperty:
        def __init__(self, *, provisioned_concurrent_executions: jsii.Number) -> None:
            """
            :param provisioned_concurrent_executions: ``CfnVersion.ProvisionedConcurrencyConfigurationProperty.ProvisionedConcurrentExecutions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "provisioned_concurrent_executions": provisioned_concurrent_executions,
            }

        @builtins.property
        def provisioned_concurrent_executions(self) -> jsii.Number:
            """``CfnVersion.ProvisionedConcurrencyConfigurationProperty.ProvisionedConcurrentExecutions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html#cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions
            """
            result = self._values.get("provisioned_concurrent_executions")
            assert result is not None, "Required property 'provisioned_concurrent_executions' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedConcurrencyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CfnVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "code_sha256": "codeSha256",
        "description": "description",
        "provisioned_concurrency_config": "provisionedConcurrencyConfig",
    },
)
class CfnVersionProps:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        code_sha256: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrency_config: typing.Optional[typing.Union[CfnVersion.ProvisionedConcurrencyConfigurationProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Lambda::Version``.

        :param function_name: ``AWS::Lambda::Version.FunctionName``.
        :param code_sha256: ``AWS::Lambda::Version.CodeSha256``.
        :param description: ``AWS::Lambda::Version.Description``.
        :param provisioned_concurrency_config: ``AWS::Lambda::Version.ProvisionedConcurrencyConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
        }
        if code_sha256 is not None:
            self._values["code_sha256"] = code_sha256
        if description is not None:
            self._values["description"] = description
        if provisioned_concurrency_config is not None:
            self._values["provisioned_concurrency_config"] = provisioned_concurrency_config

    @builtins.property
    def function_name(self) -> builtins.str:
        """``AWS::Lambda::Version.FunctionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-functionname
        """
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return result

    @builtins.property
    def code_sha256(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Version.CodeSha256``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-codesha256
        """
        result = self._values.get("code_sha256")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Lambda::Version.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def provisioned_concurrency_config(
        self,
    ) -> typing.Optional[typing.Union[CfnVersion.ProvisionedConcurrencyConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::Lambda::Version.ProvisionedConcurrencyConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-provisionedconcurrencyconfig
        """
        result = self._values.get("provisioned_concurrency_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Code(metaclass=jsii.JSIIAbstractClass, jsii_type="monocdk.aws_lambda.Code"):
    """(experimental) Represents the Lambda Handler Code.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _CodeProxy

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(Code, self, [])

    @jsii.member(jsii_name="asset")
    @builtins.classmethod
    def asset(cls, path: builtins.str) -> "AssetCode":
        """(deprecated) DEPRECATED.

        :param path: -

        :deprecated: use ``fromAsset``

        :stability: deprecated
        """
        return jsii.sinvoke(cls, "asset", [path])

    @jsii.member(jsii_name="bucket")
    @builtins.classmethod
    def bucket(
        cls,
        bucket: _IBucket_73486e29,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "S3Code":
        """(deprecated) DEPRECATED.

        :param bucket: -
        :param key: -
        :param object_version: -

        :deprecated: use ``fromBucket``

        :stability: deprecated
        """
        return jsii.sinvoke(cls, "bucket", [bucket, key, object_version])

    @jsii.member(jsii_name="cfnParameters")
    @builtins.classmethod
    def cfn_parameters(
        cls,
        *,
        bucket_name_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
        object_key_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
    ) -> "CfnParametersCode":
        """(deprecated) DEPRECATED.

        :param bucket_name_param: (experimental) The CloudFormation parameter that represents the name of the S3 Bucket where the Lambda code will be located in. Must be of type 'String'. Default: a new parameter will be created
        :param object_key_param: (experimental) The CloudFormation parameter that represents the path inside the S3 Bucket where the Lambda code will be located at. Must be of type 'String'. Default: a new parameter will be created

        :deprecated: use ``fromCfnParameters``

        :stability: deprecated
        """
        props = CfnParametersCodeProps(
            bucket_name_param=bucket_name_param, object_key_param=object_key_param
        )

        return jsii.sinvoke(cls, "cfnParameters", [props])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.List[_IGrantable_4c5a91d1]] = None,
        source_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.List[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_49193809] = None,
        bundling: typing.Optional[_BundlingOptions_ab115a99] = None,
    ) -> "AssetCode":
        """(experimental) Loads the function code from a local disk path.

        :param path: Either a directory with the Lambda code bundle or a .zip file.
        :param readers: (experimental) A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param source_hash: (deprecated) Custom hash to use when identifying the specific version of the asset. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the source hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the source hash, you will need to make sure it is updated every time the source changes, or otherwise it is possible that some deployments will not be invalidated. Default: - automatically calculate source hash based on the contents of the source file or directory.
        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '
        :param asset_hash: (experimental) Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: (experimental) Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: (experimental) Bundle the asset by executing a command in a Docker container. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise

        :stability: experimental
        """
        options = _AssetOptions_bd2996da(
            readers=readers,
            source_hash=source_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
        )

        return jsii.sinvoke(cls, "fromAsset", [path, options])

    @jsii.member(jsii_name="fromAssetImage")
    @builtins.classmethod
    def from_asset_image(
        cls,
        directory: builtins.str,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        repository_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.List[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
    ) -> "AssetImageCode":
        """(experimental) Create an ECR image from the specified asset and bind it as the Lambda code.

        :param directory: the directory from which the asset must be created.
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param build_args: (experimental) Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param file: (experimental) Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - the default ECR repository for CDK assets
        :param target: (experimental) Docker target to build to. Default: - no target
        :param extra_hash: (deprecated) Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '

        :stability: experimental
        """
        props = AssetImageCodeProps(
            cmd=cmd,
            entrypoint=entrypoint,
            build_args=build_args,
            file=file,
            repository_name=repository_name,
            target=target,
            extra_hash=extra_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
        )

        return jsii.sinvoke(cls, "fromAssetImage", [directory, props])

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: _IBucket_73486e29,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "S3Code":
        """(experimental) Lambda handler code as an S3 object.

        :param bucket: The S3 bucket.
        :param key: The object key.
        :param object_version: Optional S3 object version.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromBucket", [bucket, key, object_version])

    @jsii.member(jsii_name="fromCfnParameters")
    @builtins.classmethod
    def from_cfn_parameters(
        cls,
        *,
        bucket_name_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
        object_key_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
    ) -> "CfnParametersCode":
        """(experimental) Creates a new Lambda source defined using CloudFormation parameters.

        :param bucket_name_param: (experimental) The CloudFormation parameter that represents the name of the S3 Bucket where the Lambda code will be located in. Must be of type 'String'. Default: a new parameter will be created
        :param object_key_param: (experimental) The CloudFormation parameter that represents the path inside the S3 Bucket where the Lambda code will be located at. Must be of type 'String'. Default: a new parameter will be created

        :return: a new instance of ``CfnParametersCode``

        :stability: experimental
        """
        props = CfnParametersCodeProps(
            bucket_name_param=bucket_name_param, object_key_param=object_key_param
        )

        return jsii.sinvoke(cls, "fromCfnParameters", [props])

    @jsii.member(jsii_name="fromEcrImage")
    @builtins.classmethod
    def from_ecr_image(
        cls,
        repository: _IRepository_8b4d2894,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> "EcrImageCode":
        """(experimental) Use an existing ECR image as the Lambda code.

        :param repository: the ECR repository that the image is in.
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param tag: (experimental) The image tag to use when pulling the image from ECR. Default: 'latest'

        :stability: experimental
        """
        props = EcrImageCodeProps(cmd=cmd, entrypoint=entrypoint, tag=tag)

        return jsii.sinvoke(cls, "fromEcrImage", [repository, props])

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(cls, code: builtins.str) -> "InlineCode":
        """(experimental) Inline code for Lambda handler.

        :param code: The actual handler code (limited to 4KiB).

        :return: ``LambdaInlineCode`` with inline code.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromInline", [code])

    @jsii.member(jsii_name="inline")
    @builtins.classmethod
    def inline(cls, code: builtins.str) -> "InlineCode":
        """(deprecated) DEPRECATED.

        :param code: -

        :deprecated: use ``fromInline``

        :stability: deprecated
        """
        return jsii.sinvoke(cls, "inline", [code])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: _Construct_e78e779f) -> "CodeConfig":
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="bindToResource")
    def bind_to_resource(
        self,
        _resource: _CfnResource_e0a482dc,
        *,
        resource_property: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Called after the CFN function resource has been created to allow the code class to bind to it.

        Specifically it's required to allow assets to add
        metadata for tooling like SAM CLI to be able to find their origins.

        :param _resource: -
        :param resource_property: (experimental) The name of the CloudFormation property to annotate with asset metadata. Default: Code

        :stability: experimental
        """
        _options = ResourceBindOptions(resource_property=resource_property)

        return jsii.invoke(self, "bindToResource", [_resource, _options])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    @abc.abstractmethod
    def is_inline(self) -> builtins.bool:
        """(deprecated) Determines whether this Code is inline code or not.

        :deprecated:

        this value is ignored since inline is now determined based on the
        the ``inlineCode`` field of ``CodeConfig`` returned from ``bind()``.

        :stability: deprecated
        """
        ...


class _CodeProxy(Code):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_e78e779f) -> "CodeConfig":
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [scope])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(deprecated) Determines whether this Code is inline code or not.

        :deprecated:

        this value is ignored since inline is now determined based on the
        the ``inlineCode`` field of ``CodeConfig`` returned from ``bind()``.

        :stability: deprecated
        """
        return jsii.get(self, "isInline")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CodeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "inline_code": "inlineCode",
        "s3_location": "s3Location",
    },
)
class CodeConfig:
    def __init__(
        self,
        *,
        image: typing.Optional["CodeImageConfig"] = None,
        inline_code: typing.Optional[builtins.str] = None,
        s3_location: typing.Optional[_Location_cce991ca] = None,
    ) -> None:
        """(experimental) Result of binding ``Code`` into a ``Function``.

        :param image: (experimental) Docker image configuration (mutually exclusive with ``s3Location`` and ``inlineCode``). Default: - code is not an ECR container image
        :param inline_code: (experimental) Inline code (mutually exclusive with ``s3Location`` and ``image``). Default: - code is not inline code
        :param s3_location: (experimental) The location of the code in S3 (mutually exclusive with ``inlineCode`` and ``image``). Default: - code is not an s3 location

        :stability: experimental
        """
        if isinstance(image, dict):
            image = CodeImageConfig(**image)
        if isinstance(s3_location, dict):
            s3_location = _Location_cce991ca(**s3_location)
        self._values: typing.Dict[str, typing.Any] = {}
        if image is not None:
            self._values["image"] = image
        if inline_code is not None:
            self._values["inline_code"] = inline_code
        if s3_location is not None:
            self._values["s3_location"] = s3_location

    @builtins.property
    def image(self) -> typing.Optional["CodeImageConfig"]:
        """(experimental) Docker image configuration (mutually exclusive with ``s3Location`` and ``inlineCode``).

        :default: - code is not an ECR container image

        :stability: experimental
        """
        result = self._values.get("image")
        return result

    @builtins.property
    def inline_code(self) -> typing.Optional[builtins.str]:
        """(experimental) Inline code (mutually exclusive with ``s3Location`` and ``image``).

        :default: - code is not inline code

        :stability: experimental
        """
        result = self._values.get("inline_code")
        return result

    @builtins.property
    def s3_location(self) -> typing.Optional[_Location_cce991ca]:
        """(experimental) The location of the code in S3 (mutually exclusive with ``inlineCode`` and ``image``).

        :default: - code is not an s3 location

        :stability: experimental
        """
        result = self._values.get("s3_location")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.CodeImageConfig",
    jsii_struct_bases=[],
    name_mapping={"image_uri": "imageUri", "cmd": "cmd", "entrypoint": "entrypoint"},
)
class CodeImageConfig:
    def __init__(
        self,
        *,
        image_uri: builtins.str,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """(experimental) Result of the bind when an ECR image is used.

        :param image_uri: (experimental) URI to the Docker image.
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "image_uri": image_uri,
        }
        if cmd is not None:
            self._values["cmd"] = cmd
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint

    @builtins.property
    def image_uri(self) -> builtins.str:
        """(experimental) URI to the Docker image.

        :stability: experimental
        """
        result = self._values.get("image_uri")
        assert result is not None, "Required property 'image_uri' is missing"
        return result

    @builtins.property
    def cmd(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Specify or override the CMD on the specified Docker image or Dockerfile.

        This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``.

        :default: - use the CMD specified in the docker image or Dockerfile.

        :see: https://docs.docker.com/engine/reference/builder/#cmd
        :stability: experimental
        """
        result = self._values.get("cmd")
        return result

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile.

        An ENTRYPOINT allows you to configure a container that will run as an executable.
        This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``.

        :default: - use the ENTRYPOINT in the docker image or Dockerfile.

        :see: https://docs.docker.com/engine/reference/builder/#entrypoint
        :stability: experimental
        """
        result = self._values.get("entrypoint")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.DestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DestinationConfig:
    def __init__(self, *, destination: builtins.str) -> None:
        """(experimental) A destination configuration.

        :param destination: (experimental) The Amazon Resource Name (ARN) of the destination resource.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the destination resource.

        :stability: experimental
        """
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.DestinationOptions",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class DestinationOptions:
    def __init__(self, *, type: "DestinationType") -> None:
        """(experimental) Options when binding a destination to a function.

        :param type: (experimental) The destination type.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> "DestinationType":
        """(experimental) The destination type.

        :stability: experimental
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_lambda.DestinationType")
class DestinationType(enum.Enum):
    """(experimental) The type of destination.

    :stability: experimental
    """

    FAILURE = "FAILURE"
    """(experimental) Failure.

    :stability: experimental
    """
    SUCCESS = "SUCCESS"
    """(experimental) Success.

    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.DlqDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DlqDestinationConfig:
    def __init__(self, *, destination: builtins.str) -> None:
        """(experimental) A destination configuration.

        :param destination: (experimental) The Amazon Resource Name (ARN) of the destination resource.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the destination resource.

        :stability: experimental
        """
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlqDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DockerImageCode(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_lambda.DockerImageCode",
):
    """(experimental) Code property for the DockerImageFunction construct.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _DockerImageCodeProxy

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(DockerImageCode, self, [])

    @jsii.member(jsii_name="fromEcr")
    @builtins.classmethod
    def from_ecr(
        cls,
        repository: _IRepository_8b4d2894,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> "DockerImageCode":
        """(experimental) Use an existing ECR image as the Lambda code.

        :param repository: the ECR repository that the image is in.
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param tag: (experimental) The image tag to use when pulling the image from ECR. Default: 'latest'

        :stability: experimental
        """
        props = EcrImageCodeProps(cmd=cmd, entrypoint=entrypoint, tag=tag)

        return jsii.sinvoke(cls, "fromEcr", [repository, props])

    @jsii.member(jsii_name="fromImageAsset")
    @builtins.classmethod
    def from_image_asset(
        cls,
        directory: builtins.str,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        repository_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.List[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
    ) -> "DockerImageCode":
        """(experimental) Create an ECR image from the specified asset and bind it as the Lambda code.

        :param directory: the directory from which the asset must be created.
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param build_args: (experimental) Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param file: (experimental) Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - the default ECR repository for CDK assets
        :param target: (experimental) Docker target to build to. Default: - no target
        :param extra_hash: (deprecated) Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '

        :stability: experimental
        """
        props = AssetImageCodeProps(
            cmd=cmd,
            entrypoint=entrypoint,
            build_args=build_args,
            file=file,
            repository_name=repository_name,
            target=target,
            extra_hash=extra_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
        )

        return jsii.sinvoke(cls, "fromImageAsset", [directory, props])


class _DockerImageCodeProxy(DockerImageCode):
    pass


class EcrImageCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.EcrImageCode",
):
    """(experimental) Represents a Docker image in ECR that can be bound as Lambda Code.

    :stability: experimental
    """

    def __init__(
        self,
        repository: _IRepository_8b4d2894,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param repository: -
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param tag: (experimental) The image tag to use when pulling the image from ECR. Default: 'latest'

        :stability: experimental
        """
        props = EcrImageCodeProps(cmd=cmd, entrypoint=entrypoint, tag=tag)

        jsii.create(EcrImageCode, self, [repository, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _: _Construct_e78e779f) -> CodeConfig:
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(experimental) Determines whether this Code is inline code or not.

        :stability: experimental
        """
        return jsii.get(self, "isInline")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.EcrImageCodeProps",
    jsii_struct_bases=[],
    name_mapping={"cmd": "cmd", "entrypoint": "entrypoint", "tag": "tag"},
)
class EcrImageCodeProps:
    def __init__(
        self,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties to initialize a new EcrImageCode.

        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param tag: (experimental) The image tag to use when pulling the image from ECR. Default: 'latest'

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if cmd is not None:
            self._values["cmd"] = cmd
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def cmd(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Specify or override the CMD on the specified Docker image or Dockerfile.

        This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``.

        :default: - use the CMD specified in the docker image or Dockerfile.

        :see: https://docs.docker.com/engine/reference/builder/#cmd
        :stability: experimental
        """
        result = self._values.get("cmd")
        return result

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile.

        An ENTRYPOINT allows you to configure a container that will run as an executable.
        This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``.

        :default: - use the ENTRYPOINT in the docker image or Dockerfile.

        :see: https://docs.docker.com/engine/reference/builder/#entrypoint
        :stability: experimental
        """
        result = self._values.get("entrypoint")
        return result

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        """(experimental) The image tag to use when pulling the image from ECR.

        :default: 'latest'

        :stability: experimental
        """
        result = self._values.get("tag")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcrImageCodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.EnvironmentOptions",
    jsii_struct_bases=[],
    name_mapping={"remove_in_edge": "removeInEdge"},
)
class EnvironmentOptions:
    def __init__(
        self,
        *,
        remove_in_edge: typing.Optional[builtins.bool] = None,
    ) -> None:
        """(experimental) Environment variables options.

        :param remove_in_edge: (experimental) When used in Lambda@Edge via edgeArn() API, these environment variables will be removed. If not set, an error will be thrown. Default: false - using the function in Lambda

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if remove_in_edge is not None:
            self._values["remove_in_edge"] = remove_in_edge

    @builtins.property
    def remove_in_edge(self) -> typing.Optional[builtins.bool]:
        """(experimental) When used in Lambda@Edge via edgeArn() API, these environment variables will be removed.

        If not set, an error will be thrown.

        :default: false - using the function in Lambda

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-requirements-limits.html#lambda-requirements-lambda-function-configuration
        :stability: experimental
        :Edge: will throw
        """
        result = self._values.get("remove_in_edge")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventInvokeConfig(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.EventInvokeConfig",
):
    """(experimental) Configure options for asynchronous invocation on a version or an alias.

    By default, Lambda retries an asynchronous invocation twice if the function
    returns an error. It retains events in a queue for up to six hours. When an
    event fails all processing attempts or stays in the asynchronous invocation
    queue for too long, Lambda discards it.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        function: "IFunction",
        qualifier: typing.Optional[builtins.str] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IDestination"] = None,
        on_success: typing.Optional["IDestination"] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param function: (experimental) The Lambda function.
        :param qualifier: (experimental) The qualifier. Default: - latest version
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        props = EventInvokeConfigProps(
            function=function,
            qualifier=qualifier,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(EventInvokeConfig, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.EventInvokeConfigOptions",
    jsii_struct_bases=[],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
    },
)
class EventInvokeConfigOptions:
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IDestination"] = None,
        on_success: typing.Optional["IDestination"] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Options to add an EventInvokeConfig to a function.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventInvokeConfigOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.EventInvokeConfigProps",
    jsii_struct_bases=[EventInvokeConfigOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "function": "function",
        "qualifier": "qualifier",
    },
)
class EventInvokeConfigProps(EventInvokeConfigOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IDestination"] = None,
        on_success: typing.Optional["IDestination"] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        function: "IFunction",
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for an EventInvokeConfig.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param function: (experimental) The Lambda function.
        :param qualifier: (experimental) The qualifier. Default: - latest version

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function": function,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if qualifier is not None:
            self._values["qualifier"] = qualifier

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def function(self) -> "IFunction":
        """(experimental) The Lambda function.

        :stability: experimental
        """
        result = self._values.get("function")
        assert result is not None, "Required property 'function' is missing"
        return result

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        """(experimental) The qualifier.

        :default: - latest version

        :stability: experimental
        """
        result = self._values.get("qualifier")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventInvokeConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.EventSourceMappingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "event_source_arn": "eventSourceArn",
        "batch_size": "batchSize",
        "bisect_batch_on_error": "bisectBatchOnError",
        "enabled": "enabled",
        "kafka_topic": "kafkaTopic",
        "max_batching_window": "maxBatchingWindow",
        "max_record_age": "maxRecordAge",
        "on_failure": "onFailure",
        "parallelization_factor": "parallelizationFactor",
        "retry_attempts": "retryAttempts",
        "starting_position": "startingPosition",
    },
)
class EventSourceMappingOptions:
    def __init__(
        self,
        *,
        event_source_arn: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_070aa057] = None,
        max_record_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IEventSourceDlq"] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        starting_position: typing.Optional["StartingPosition"] = None,
    ) -> None:
        """
        :param event_source_arn: (experimental) The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: (experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param bisect_batch_on_error: (experimental) If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: (experimental) Set to false to disable the event source upon creation. Default: true
        :param kafka_topic: (experimental) The name of the Kafka topic. Default: - no topic
        :param max_batching_window: (experimental) The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_record_age: (experimental) The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: (experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: (experimental) The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param starting_position: (experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "event_source_arn": event_source_arn,
        }
        if batch_size is not None:
            self._values["batch_size"] = batch_size
        if bisect_batch_on_error is not None:
            self._values["bisect_batch_on_error"] = bisect_batch_on_error
        if enabled is not None:
            self._values["enabled"] = enabled
        if kafka_topic is not None:
            self._values["kafka_topic"] = kafka_topic
        if max_batching_window is not None:
            self._values["max_batching_window"] = max_batching_window
        if max_record_age is not None:
            self._values["max_record_age"] = max_record_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if parallelization_factor is not None:
            self._values["parallelization_factor"] = parallelization_factor
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if starting_position is not None:
            self._values["starting_position"] = starting_position

    @builtins.property
    def event_source_arn(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the event source.

        Any record added to
        this stream can invoke the Lambda function.

        :stability: experimental
        """
        result = self._values.get("event_source_arn")
        assert result is not None, "Required property 'event_source_arn' is missing"
        return result

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """(experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.

        Your function receives an
        event with all the retrieved records.

        Valid Range: Minimum value of 1. Maximum value of 10000.

        :default:

        - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records.
        Both the default and maximum for Amazon SQS are 10 messages.

        :stability: experimental
        """
        result = self._values.get("batch_size")
        return result

    @builtins.property
    def bisect_batch_on_error(self) -> typing.Optional[builtins.bool]:
        """(experimental) If the function returns an error, split the batch in two and retry.

        :default: false

        :stability: experimental
        """
        result = self._values.get("bisect_batch_on_error")
        return result

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) Set to false to disable the event source upon creation.

        :default: true

        :stability: experimental
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def kafka_topic(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the Kafka topic.

        :default: - no topic

        :stability: experimental
        """
        result = self._values.get("kafka_topic")
        return result

    @builtins.property
    def max_batching_window(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum amount of time to gather records before invoking the function.

        Maximum of Duration.minutes(5)

        :default: Duration.seconds(0)

        :stability: experimental
        """
        result = self._values.get("max_batching_window")
        return result

    @builtins.property
    def max_record_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a record that Lambda sends to a function for processing.

        Valid Range:

        - Minimum value of 60 seconds
        - Maximum value of 7 days

        :default: - infinite or until the record expires.

        :stability: experimental
        """
        result = self._values.get("max_record_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional["IEventSourceDlq"]:
        """(experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

        :default: discarded records are ignored

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def parallelization_factor(self) -> typing.Optional[jsii.Number]:
        """(experimental) The number of batches to process from each shard concurrently.

        Valid Range:

        - Minimum value of 1
        - Maximum value of 10

        :default: 1

        :stability: experimental
        """
        result = self._values.get("parallelization_factor")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Set to ``undefined`` if you want lambda to keep retrying infinitely or until
        the record expires.

        Valid Range:

        - Minimum value of 0
        - Maximum value of 10000

        :default: - infinite or until the record expires.

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def starting_position(self) -> typing.Optional["StartingPosition"]:
        """(experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading.

        :default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :see: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType
        :stability: experimental
        """
        result = self._values.get("starting_position")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSourceMappingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.EventSourceMappingProps",
    jsii_struct_bases=[EventSourceMappingOptions],
    name_mapping={
        "event_source_arn": "eventSourceArn",
        "batch_size": "batchSize",
        "bisect_batch_on_error": "bisectBatchOnError",
        "enabled": "enabled",
        "kafka_topic": "kafkaTopic",
        "max_batching_window": "maxBatchingWindow",
        "max_record_age": "maxRecordAge",
        "on_failure": "onFailure",
        "parallelization_factor": "parallelizationFactor",
        "retry_attempts": "retryAttempts",
        "starting_position": "startingPosition",
        "target": "target",
    },
)
class EventSourceMappingProps(EventSourceMappingOptions):
    def __init__(
        self,
        *,
        event_source_arn: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_070aa057] = None,
        max_record_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IEventSourceDlq"] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        starting_position: typing.Optional["StartingPosition"] = None,
        target: "IFunction",
    ) -> None:
        """(experimental) Properties for declaring a new event source mapping.

        :param event_source_arn: (experimental) The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: (experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param bisect_batch_on_error: (experimental) If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: (experimental) Set to false to disable the event source upon creation. Default: true
        :param kafka_topic: (experimental) The name of the Kafka topic. Default: - no topic
        :param max_batching_window: (experimental) The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_record_age: (experimental) The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: (experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: (experimental) The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param starting_position: (experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.
        :param target: (experimental) The target AWS Lambda function.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "event_source_arn": event_source_arn,
            "target": target,
        }
        if batch_size is not None:
            self._values["batch_size"] = batch_size
        if bisect_batch_on_error is not None:
            self._values["bisect_batch_on_error"] = bisect_batch_on_error
        if enabled is not None:
            self._values["enabled"] = enabled
        if kafka_topic is not None:
            self._values["kafka_topic"] = kafka_topic
        if max_batching_window is not None:
            self._values["max_batching_window"] = max_batching_window
        if max_record_age is not None:
            self._values["max_record_age"] = max_record_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if parallelization_factor is not None:
            self._values["parallelization_factor"] = parallelization_factor
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if starting_position is not None:
            self._values["starting_position"] = starting_position

    @builtins.property
    def event_source_arn(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the event source.

        Any record added to
        this stream can invoke the Lambda function.

        :stability: experimental
        """
        result = self._values.get("event_source_arn")
        assert result is not None, "Required property 'event_source_arn' is missing"
        return result

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """(experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.

        Your function receives an
        event with all the retrieved records.

        Valid Range: Minimum value of 1. Maximum value of 10000.

        :default:

        - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records.
        Both the default and maximum for Amazon SQS are 10 messages.

        :stability: experimental
        """
        result = self._values.get("batch_size")
        return result

    @builtins.property
    def bisect_batch_on_error(self) -> typing.Optional[builtins.bool]:
        """(experimental) If the function returns an error, split the batch in two and retry.

        :default: false

        :stability: experimental
        """
        result = self._values.get("bisect_batch_on_error")
        return result

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) Set to false to disable the event source upon creation.

        :default: true

        :stability: experimental
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def kafka_topic(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the Kafka topic.

        :default: - no topic

        :stability: experimental
        """
        result = self._values.get("kafka_topic")
        return result

    @builtins.property
    def max_batching_window(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum amount of time to gather records before invoking the function.

        Maximum of Duration.minutes(5)

        :default: Duration.seconds(0)

        :stability: experimental
        """
        result = self._values.get("max_batching_window")
        return result

    @builtins.property
    def max_record_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a record that Lambda sends to a function for processing.

        Valid Range:

        - Minimum value of 60 seconds
        - Maximum value of 7 days

        :default: - infinite or until the record expires.

        :stability: experimental
        """
        result = self._values.get("max_record_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional["IEventSourceDlq"]:
        """(experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

        :default: discarded records are ignored

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def parallelization_factor(self) -> typing.Optional[jsii.Number]:
        """(experimental) The number of batches to process from each shard concurrently.

        Valid Range:

        - Minimum value of 1
        - Maximum value of 10

        :default: 1

        :stability: experimental
        """
        result = self._values.get("parallelization_factor")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Set to ``undefined`` if you want lambda to keep retrying infinitely or until
        the record expires.

        Valid Range:

        - Minimum value of 0
        - Maximum value of 10000

        :default: - infinite or until the record expires.

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def starting_position(self) -> typing.Optional["StartingPosition"]:
        """(experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading.

        :default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :see: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType
        :stability: experimental
        """
        result = self._values.get("starting_position")
        return result

    @builtins.property
    def target(self) -> "IFunction":
        """(experimental) The target AWS Lambda function.

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
        return "EventSourceMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FileSystem(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_lambda.FileSystem"):
    """(experimental) Represents the filesystem for the Lambda function.

    :stability: experimental
    """

    def __init__(
        self,
        *,
        arn: builtins.str,
        local_mount_path: builtins.str,
        connections: typing.Optional[_Connections_57ccbda9] = None,
        dependency: typing.Optional[typing.List[_IDependable_1175c9f7]] = None,
        policies: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
    ) -> None:
        """
        :param arn: (experimental) ARN of the access point.
        :param local_mount_path: (experimental) mount path in the lambda runtime environment.
        :param connections: (experimental) connections object used to allow ingress traffic from lambda function. Default: - no connections required to add extra ingress rules for Lambda function
        :param dependency: (experimental) array of IDependable that lambda function depends on. Default: - no dependency
        :param policies: (experimental) additional IAM policies required for the lambda function. Default: - no additional policies required

        :stability: experimental
        """
        config = FileSystemConfig(
            arn=arn,
            local_mount_path=local_mount_path,
            connections=connections,
            dependency=dependency,
            policies=policies,
        )

        jsii.create(FileSystem, self, [config])

    @jsii.member(jsii_name="fromEfsAccessPoint")
    @builtins.classmethod
    def from_efs_access_point(
        cls,
        ap: _IAccessPoint_180f72ec,
        mount_path: builtins.str,
    ) -> "FileSystem":
        """(experimental) mount the filesystem from Amazon EFS.

        :param ap: the Amazon EFS access point.
        :param mount_path: the target path in the lambda runtime environment.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromEfsAccessPoint", [ap, mount_path])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="config")
    def config(self) -> "FileSystemConfig":
        """(experimental) the FileSystem configurations for the Lambda function.

        :stability: experimental
        """
        return jsii.get(self, "config")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.FileSystemConfig",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "local_mount_path": "localMountPath",
        "connections": "connections",
        "dependency": "dependency",
        "policies": "policies",
    },
)
class FileSystemConfig:
    def __init__(
        self,
        *,
        arn: builtins.str,
        local_mount_path: builtins.str,
        connections: typing.Optional[_Connections_57ccbda9] = None,
        dependency: typing.Optional[typing.List[_IDependable_1175c9f7]] = None,
        policies: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
    ) -> None:
        """(experimental) FileSystem configurations for the Lambda function.

        :param arn: (experimental) ARN of the access point.
        :param local_mount_path: (experimental) mount path in the lambda runtime environment.
        :param connections: (experimental) connections object used to allow ingress traffic from lambda function. Default: - no connections required to add extra ingress rules for Lambda function
        :param dependency: (experimental) array of IDependable that lambda function depends on. Default: - no dependency
        :param policies: (experimental) additional IAM policies required for the lambda function. Default: - no additional policies required

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "local_mount_path": local_mount_path,
        }
        if connections is not None:
            self._values["connections"] = connections
        if dependency is not None:
            self._values["dependency"] = dependency
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def arn(self) -> builtins.str:
        """(experimental) ARN of the access point.

        :stability: experimental
        """
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return result

    @builtins.property
    def local_mount_path(self) -> builtins.str:
        """(experimental) mount path in the lambda runtime environment.

        :stability: experimental
        """
        result = self._values.get("local_mount_path")
        assert result is not None, "Required property 'local_mount_path' is missing"
        return result

    @builtins.property
    def connections(self) -> typing.Optional[_Connections_57ccbda9]:
        """(experimental) connections object used to allow ingress traffic from lambda function.

        :default: - no connections required to add extra ingress rules for Lambda function

        :stability: experimental
        """
        result = self._values.get("connections")
        return result

    @builtins.property
    def dependency(self) -> typing.Optional[typing.List[_IDependable_1175c9f7]]:
        """(experimental) array of IDependable that lambda function depends on.

        :default: - no dependency

        :stability: experimental
        """
        result = self._values.get("dependency")
        return result

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[_PolicyStatement_296fe8a3]]:
        """(experimental) additional IAM policies required for the lambda function.

        :default: - no additional policies required

        :stability: experimental
        """
        result = self._values.get("policies")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.FunctionAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "function_arn": "functionArn",
        "role": "role",
        "same_environment": "sameEnvironment",
        "security_group": "securityGroup",
        "security_group_id": "securityGroupId",
    },
)
class FunctionAttributes:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        role: typing.Optional[_IRole_59af6f50] = None,
        same_environment: typing.Optional[builtins.bool] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Represents a Lambda function defined outside of this stack.

        :param function_arn: (experimental) The ARN of the Lambda function. Format: arn::lambda:::function:
        :param role: (experimental) The IAM execution role associated with this function. If the role is not specified, any role-related operations will no-op.
        :param same_environment: (experimental) Setting this property informs the CDK that the imported function is in the same environment as the stack. This affects certain behaviours such as, whether this function's permission can be modified. When not configured, the CDK attempts to auto-determine this. For environment agnostic stacks, i.e., stacks where the account is not specified with the ``env`` property, this is determined to be false. Set this to property *ONLY IF* the imported function is in the same account as the stack it's imported in. Default: - depends: true, if the Stack is configured with an explicit ``env`` (account and region) and the account is the same as this function. For environment-agnostic stacks this will default to ``false``.
        :param security_group: (experimental) The security group of this Lambda, if in a VPC. This needs to be given in order to support allowing connections to this Lambda.
        :param security_group_id: (deprecated) Id of the security group of this Lambda, if in a VPC. This needs to be given in order to support allowing connections to this Lambda.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
        }
        if role is not None:
            self._values["role"] = role
        if same_environment is not None:
            self._values["same_environment"] = same_environment
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_group_id is not None:
            self._values["security_group_id"] = security_group_id

    @builtins.property
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN of the Lambda function.

        Format: arn::lambda:::function:

        :stability: experimental
        """
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM execution role associated with this function.

        If the role is not specified, any role-related operations will no-op.

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    @builtins.property
    def same_environment(self) -> typing.Optional[builtins.bool]:
        """(experimental) Setting this property informs the CDK that the imported function is in the same environment as the stack.

        This affects certain behaviours such as, whether this function's permission can be modified.
        When not configured, the CDK attempts to auto-determine this. For environment agnostic stacks, i.e., stacks
        where the account is not specified with the ``env`` property, this is determined to be false.

        Set this to property *ONLY IF* the imported function is in the same account as the stack
        it's imported in.

        :default:

        - depends: true, if the Stack is configured with an explicit ``env`` (account and region) and the account is the same as this function.
        For environment-agnostic stacks this will default to ``false``.

        :stability: experimental
        """
        result = self._values.get("same_environment")
        return result

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_cdbba9d3]:
        """(experimental) The security group of this Lambda, if in a VPC.

        This needs to be given in order to support allowing connections
        to this Lambda.

        :stability: experimental
        """
        result = self._values.get("security_group")
        return result

    @builtins.property
    def security_group_id(self) -> typing.Optional[builtins.str]:
        """(deprecated) Id of the security group of this Lambda, if in a VPC.

        This needs to be given in order to support allowing connections
        to this Lambda.

        :deprecated: use ``securityGroup`` instead

        :stability: deprecated
        """
        result = self._values.get("security_group_id")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.FunctionOptions",
    jsii_struct_bases=[EventInvokeConfigOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class FunctionOptions(EventInvokeConfigOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IDestination"] = None,
        on_success: typing.Optional["IDestination"] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional["VersionOptions"] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List["IEventSource"]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List["ILayerVersion"]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional["LogRetentionRetryOptions"] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional["Tracing"] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
    ) -> None:
        """(experimental) Non runtime options.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified

        :stability: experimental
        """
        if isinstance(current_version_options, dict):
            current_version_options = VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true

        :stability: experimental
        """
        result = self._values.get("allow_all_outbound")
        return result

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        """(experimental) Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        :stability: experimental
        """
        result = self._values.get("allow_public_subnet")
        return result

    @builtins.property
    def current_version_options(self) -> typing.Optional["VersionOptions"]:
        """(experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``

        :stability: experimental
        """
        result = self._values.get("current_version_options")
        return result

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_45a01ab4]:
        """(experimental) The SQS queue to use if DLQ is enabled.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue")
        return result

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue_enabled")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the function.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.

        :stability: experimental
        """
        result = self._values.get("environment")
        return result

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_IKey_36930160]:
        """(experimental) The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).

        :stability: experimental
        """
        result = self._values.get("environment_encryption")
        return result

    @builtins.property
    def events(self) -> typing.Optional[typing.List["IEventSource"]]:
        """(experimental) Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.

        :stability: experimental
        """
        result = self._values.get("events")
        return result

    @builtins.property
    def filesystem(self) -> typing.Optional[FileSystem]:
        """(experimental) The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem

        :stability: experimental
        """
        result = self._values.get("filesystem")
        return result

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.

        :stability: experimental
        """
        result = self._values.get("function_name")
        return result

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[_PolicyStatement_296fe8a3]]:
        """(experimental) Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.

        :stability: experimental
        """
        result = self._values.get("initial_policy")
        return result

    @builtins.property
    def layers(self) -> typing.Optional[typing.List["ILayerVersion"]]:
        """(experimental) A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by mulitple functions.

        :default: - No layers.

        :stability: experimental
        """
        result = self._values.get("layers")
        return result

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_6c560d31]:
        """(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE

        :stability: experimental
        """
        result = self._values.get("log_retention")
        return result

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional["LogRetentionRetryOptions"]:
        """(experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.

        :stability: experimental
        """
        result = self._values.get("log_retention_retry_options")
        return result

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.

        :stability: experimental
        """
        result = self._values.get("log_retention_role")
        return result

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """(experimental) The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128

        :stability: experimental
        """
        result = self._values.get("memory_size")
        return result

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling")
        return result

    @builtins.property
    def profiling_group(self) -> typing.Optional[_IProfilingGroup_418eb20c]:
        """(experimental) Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling_group")
        return result

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        :stability: experimental
        """
        result = self._values.get("reserved_concurrent_executions")
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_cdbba9d3]:
        """(deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead.

        Only used if 'vpc' is supplied.

        Use securityGroups property instead.
        Function constructor will throw an error if both are specified.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroups prop, a dedicated security
        group will be created for this function.

        :deprecated: - This property is deprecated, use securityGroups instead

        :stability: deprecated
        """
        result = self._values.get("security_group")
        return result

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]]:
        """(experimental) The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.

        :stability: experimental
        """
        result = self._values.get("security_groups")
        return result

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)

        :stability: experimental
        """
        result = self._values.get("timeout")
        return result

    @builtins.property
    def tracing(self) -> typing.Optional["Tracing"]:
        """(experimental) Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled

        :stability: experimental
        """
        result = self._values.get("tracing")
        return result

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_6d1f76c4]:
        """(experimental) VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.

        :default: - Function is not placed within a VPC.

        :stability: experimental
        """
        result = self._values.get("vpc")
        return result

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        """(experimental) Where to place the network interfaces within the VPC.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified

        :stability: experimental
        """
        result = self._values.get("vpc_subnets")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.FunctionProps",
    jsii_struct_bases=[FunctionOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "code": "code",
        "handler": "handler",
        "runtime": "runtime",
    },
)
class FunctionProps(FunctionOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional["IDestination"] = None,
        on_success: typing.Optional["IDestination"] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional["VersionOptions"] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List["IEventSource"]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List["ILayerVersion"]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional["LogRetentionRetryOptions"] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional["Tracing"] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        code: Code,
        handler: builtins.str,
        runtime: "Runtime",
    ) -> None:
        """
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param code: (experimental) The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: (experimental) The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: (experimental) The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.

        :stability: experimental
        """
        if isinstance(current_version_options, dict):
            current_version_options = VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {
            "code": code,
            "handler": handler,
            "runtime": runtime,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional["IDestination"]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true

        :stability: experimental
        """
        result = self._values.get("allow_all_outbound")
        return result

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        """(experimental) Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        :stability: experimental
        """
        result = self._values.get("allow_public_subnet")
        return result

    @builtins.property
    def current_version_options(self) -> typing.Optional["VersionOptions"]:
        """(experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``

        :stability: experimental
        """
        result = self._values.get("current_version_options")
        return result

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_45a01ab4]:
        """(experimental) The SQS queue to use if DLQ is enabled.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue")
        return result

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue_enabled")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the function.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.

        :stability: experimental
        """
        result = self._values.get("environment")
        return result

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_IKey_36930160]:
        """(experimental) The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).

        :stability: experimental
        """
        result = self._values.get("environment_encryption")
        return result

    @builtins.property
    def events(self) -> typing.Optional[typing.List["IEventSource"]]:
        """(experimental) Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.

        :stability: experimental
        """
        result = self._values.get("events")
        return result

    @builtins.property
    def filesystem(self) -> typing.Optional[FileSystem]:
        """(experimental) The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem

        :stability: experimental
        """
        result = self._values.get("filesystem")
        return result

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.

        :stability: experimental
        """
        result = self._values.get("function_name")
        return result

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[_PolicyStatement_296fe8a3]]:
        """(experimental) Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.

        :stability: experimental
        """
        result = self._values.get("initial_policy")
        return result

    @builtins.property
    def layers(self) -> typing.Optional[typing.List["ILayerVersion"]]:
        """(experimental) A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by mulitple functions.

        :default: - No layers.

        :stability: experimental
        """
        result = self._values.get("layers")
        return result

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_6c560d31]:
        """(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE

        :stability: experimental
        """
        result = self._values.get("log_retention")
        return result

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional["LogRetentionRetryOptions"]:
        """(experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.

        :stability: experimental
        """
        result = self._values.get("log_retention_retry_options")
        return result

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.

        :stability: experimental
        """
        result = self._values.get("log_retention_role")
        return result

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """(experimental) The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128

        :stability: experimental
        """
        result = self._values.get("memory_size")
        return result

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling")
        return result

    @builtins.property
    def profiling_group(self) -> typing.Optional[_IProfilingGroup_418eb20c]:
        """(experimental) Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling_group")
        return result

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        :stability: experimental
        """
        result = self._values.get("reserved_concurrent_executions")
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_cdbba9d3]:
        """(deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead.

        Only used if 'vpc' is supplied.

        Use securityGroups property instead.
        Function constructor will throw an error if both are specified.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroups prop, a dedicated security
        group will be created for this function.

        :deprecated: - This property is deprecated, use securityGroups instead

        :stability: deprecated
        """
        result = self._values.get("security_group")
        return result

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]]:
        """(experimental) The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.

        :stability: experimental
        """
        result = self._values.get("security_groups")
        return result

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)

        :stability: experimental
        """
        result = self._values.get("timeout")
        return result

    @builtins.property
    def tracing(self) -> typing.Optional["Tracing"]:
        """(experimental) Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled

        :stability: experimental
        """
        result = self._values.get("tracing")
        return result

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_6d1f76c4]:
        """(experimental) VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.

        :default: - Function is not placed within a VPC.

        :stability: experimental
        """
        result = self._values.get("vpc")
        return result

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        """(experimental) Where to place the network interfaces within the VPC.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified

        :stability: experimental
        """
        result = self._values.get("vpc_subnets")
        return result

    @builtins.property
    def code(self) -> Code:
        """(experimental) The source code of your Lambda function.

        You can point to a file in an
        Amazon Simple Storage Service (Amazon S3) bucket or specify your source
        code as inline text.

        :stability: experimental
        """
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return result

    @builtins.property
    def handler(self) -> builtins.str:
        """(experimental) The name of the method within your code that Lambda calls to execute your function.

        The format includes the file name. It can also include
        namespaces and other qualifiers, depending on the runtime.
        For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel.

        Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image.

        NOTE: If you specify your source code as inline text by specifying the
        ZipFile property within the Code property, specify index.function_name as
        the handler.

        :stability: experimental
        """
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return result

    @builtins.property
    def runtime(self) -> "Runtime":
        """(experimental) The runtime environment for the Lambda function that you are uploading.

        For valid values, see the Runtime property in the AWS Lambda Developer
        Guide.

        Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.

        :stability: experimental
        """
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Handler(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_lambda.Handler"):
    """(experimental) Lambda function handler.

    :stability: experimental
    """

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="FROM_IMAGE")
    def FROM_IMAGE(cls) -> builtins.str:
        """(experimental) A special handler when the function handler is part of a Docker image.

        :stability: experimental
        """
        return jsii.sget(cls, "FROM_IMAGE")


@jsii.interface(jsii_type="monocdk.aws_lambda.IDestination")
class IDestination(typing_extensions.Protocol):
    """(experimental) A Lambda destination.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IDestinationProxy

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _Construct_e78e779f,
        fn: "IFunction",
        *,
        type: DestinationType,
    ) -> DestinationConfig:
        """(experimental) Binds this destination to the Lambda function.

        :param scope: -
        :param fn: -
        :param type: (experimental) The destination type.

        :stability: experimental
        """
        ...


class _IDestinationProxy:
    """(experimental) A Lambda destination.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IDestination"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _Construct_e78e779f,
        fn: "IFunction",
        *,
        type: DestinationType,
    ) -> DestinationConfig:
        """(experimental) Binds this destination to the Lambda function.

        :param scope: -
        :param fn: -
        :param type: (experimental) The destination type.

        :stability: experimental
        """
        options = DestinationOptions(type=type)

        return jsii.invoke(self, "bind", [scope, fn, options])


@jsii.interface(jsii_type="monocdk.aws_lambda.IEventSource")
class IEventSource(typing_extensions.Protocol):
    """(experimental) An abstract class which represents an AWS Lambda event source.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IEventSourceProxy

    @jsii.member(jsii_name="bind")
    def bind(self, target: "IFunction") -> None:
        """(experimental) Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: That lambda function to bind to.

        :stability: experimental
        """
        ...


class _IEventSourceProxy:
    """(experimental) An abstract class which represents an AWS Lambda event source.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IEventSource"

    @jsii.member(jsii_name="bind")
    def bind(self, target: "IFunction") -> None:
        """(experimental) Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: That lambda function to bind to.

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [target])


@jsii.interface(jsii_type="monocdk.aws_lambda.IEventSourceDlq")
class IEventSourceDlq(typing_extensions.Protocol):
    """(experimental) A DLQ for an event source.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IEventSourceDlqProxy

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        target: "IEventSourceMapping",
        target_handler: "IFunction",
    ) -> DlqDestinationConfig:
        """(experimental) Returns the DLQ destination config of the DLQ.

        :param target: -
        :param target_handler: -

        :stability: experimental
        """
        ...


class _IEventSourceDlqProxy:
    """(experimental) A DLQ for an event source.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IEventSourceDlq"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        target: "IEventSourceMapping",
        target_handler: "IFunction",
    ) -> DlqDestinationConfig:
        """(experimental) Returns the DLQ destination config of the DLQ.

        :param target: -
        :param target_handler: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [target, target_handler])


@jsii.interface(jsii_type="monocdk.aws_lambda.IEventSourceMapping")
class IEventSourceMapping(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) Represents an event source mapping for a lambda function.

    :see: https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IEventSourceMappingProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="eventSourceMappingId")
    def event_source_mapping_id(self) -> builtins.str:
        """(experimental) The identifier for this EventSourceMapping.

        :stability: experimental
        :attribute: true
        """
        ...


class _IEventSourceMappingProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) Represents an event source mapping for a lambda function.

    :see: https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IEventSourceMapping"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="eventSourceMappingId")
    def event_source_mapping_id(self) -> builtins.str:
        """(experimental) The identifier for this EventSourceMapping.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "eventSourceMappingId")


@jsii.interface(jsii_type="monocdk.aws_lambda.IFunction")
class IFunction(
    _IResource_8c1dbbbd,
    _IConnectable_c1c0e72c,
    _IGrantable_4c5a91d1,
    typing_extensions.Protocol,
):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IFunctionProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN fo the function.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) The name of the function.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isBoundToVpc")
    def is_bound_to_vpc(self) -> builtins.bool:
        """(experimental) Whether or not this Lambda function was bound to a VPC.

        If this is is ``false``, trying to access the ``connections`` object will fail.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> "IVersion":
        """(experimental) The ``$LATEST`` version of this function.

        Note that this is reference to a non-specific AWS Lambda version, which
        means the function this version refers to can return different results in
        different invocations.

        To obtain a reference to an explicit version which references the current
        function configuration, use ``lambdaFunction.currentVersion`` instead.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addEventSource")
    def add_event_source(self, source: IEventSource) -> None:
        """(experimental) Adds an event source to this function.

        Event sources are implemented in the @aws-cdk/aws-lambda-event-sources module.

        The following example adds an SQS Queue as an event source::

           import { SqsEventSource } from '@aws-cdk/aws-lambda-event-sources';
           myFunction.addEventSource(new SqsEventSource(myQueue));

        :param source: -

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addEventSourceMapping")
    def add_event_source_mapping(
        self,
        id: builtins.str,
        *,
        event_source_arn: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_070aa057] = None,
        max_record_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IEventSourceDlq] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        starting_position: typing.Optional["StartingPosition"] = None,
    ) -> "EventSourceMapping":
        """(experimental) Adds an event source that maps to this AWS Lambda function.

        :param id: construct ID.
        :param event_source_arn: (experimental) The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: (experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param bisect_batch_on_error: (experimental) If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: (experimental) Set to false to disable the event source upon creation. Default: true
        :param kafka_topic: (experimental) The name of the Kafka topic. Default: - no topic
        :param max_batching_window: (experimental) The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_record_age: (experimental) The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: (experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: (experimental) The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param starting_position: (experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        principal: _IPrincipal_93b48231,
        action: typing.Optional[builtins.str] = None,
        event_source_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[_Construct_e78e779f] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Adds a permission to the Lambda resource policy.

        :param id: The id ƒor the permission construct.
        :param principal: (experimental) The entity for which you are granting permission to invoke the Lambda function. This entity can be any valid AWS service principal, such as s3.amazonaws.com or sns.amazonaws.com, or, if you are granting cross-account permission, an AWS account ID. For example, you might want to allow a custom application in another AWS account to push events to Lambda by invoking your function. The principal can be either an AccountPrincipal or a ServicePrincipal.
        :param action: (experimental) The Lambda actions that you want to allow in this statement. For example, you can specify lambda:CreateFunction to specify a certain action, or use a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a list of actions, see Actions and Condition Context Keys for AWS Lambda in the IAM User Guide. Default: 'lambda:InvokeFunction'
        :param event_source_token: (experimental) A unique token that must be supplied by the principal invoking the function. Default: The caller would not need to present a token.
        :param scope: (experimental) The scope to which the permission constructs be attached. The default is the Lambda function construct itself, but this would need to be different in cases such as cross-stack references where the Permissions would need to sit closer to the consumer of this permission (i.e., the caller). Default: - The instance of lambda.IFunction
        :param source_account: (experimental) The AWS account ID (without hyphens) of the source owner. For example, if you specify an S3 bucket in the SourceArn property, this value is the bucket owner's account ID. You can use this property to ensure that all source principals are owned by a specific account.
        :param source_arn: (experimental) The ARN of a resource that is invoking your function. When granting Amazon Simple Storage Service (Amazon S3) permission to invoke your function, specify this property with the bucket ARN as its value. This ensures that events generated only from the specified bucket, not just any bucket from any AWS account that creates a mapping to your function, can invoke the function.

        :see: Permission for details.
        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_296fe8a3) -> None:
        """(experimental) Adds a statement to the IAM role assumed by the instance.

        :param statement: -

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="configureAsyncInvoke")
    def configure_async_invoke(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Configures options for asynchronous invocation.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(self, identity: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        """(experimental) Grant the given identity permissions to invoke this Lambda.

        :param identity: -

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Return the given named metric for this Lambda Return the given named metric for this Function.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="metricDuration")
    def metric_duration(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the Duration of this Lambda How long execution of this Lambda takes.

        Average over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="metricErrors")
    def metric_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) How many invocations of this Lambda fail.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="metricInvocations")
    def metric_invocations(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of invocations of this Lambda How often this Lambda is invoked.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="metricThrottles")
    def metric_throttles(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of throttled invocations of this Lambda How often this Lambda is throttled.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        ...


class _IFunctionProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore
    jsii.proxy_for(_IConnectable_c1c0e72c), # type: ignore
    jsii.proxy_for(_IGrantable_4c5a91d1), # type: ignore
):
    """
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IFunction"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN fo the function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) The name of the function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "functionName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isBoundToVpc")
    def is_bound_to_vpc(self) -> builtins.bool:
        """(experimental) Whether or not this Lambda function was bound to a VPC.

        If this is is ``false``, trying to access the ``connections`` object will fail.

        :stability: experimental
        """
        return jsii.get(self, "isBoundToVpc")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> "IVersion":
        """(experimental) The ``$LATEST`` version of this function.

        Note that this is reference to a non-specific AWS Lambda version, which
        means the function this version refers to can return different results in
        different invocations.

        To obtain a reference to an explicit version which references the current
        function configuration, use ``lambdaFunction.currentVersion`` instead.

        :stability: experimental
        """
        return jsii.get(self, "latestVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        return jsii.get(self, "permissionsNode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        :stability: experimental
        """
        return jsii.get(self, "role")

    @jsii.member(jsii_name="addEventSource")
    def add_event_source(self, source: IEventSource) -> None:
        """(experimental) Adds an event source to this function.

        Event sources are implemented in the @aws-cdk/aws-lambda-event-sources module.

        The following example adds an SQS Queue as an event source::

           import { SqsEventSource } from '@aws-cdk/aws-lambda-event-sources';
           myFunction.addEventSource(new SqsEventSource(myQueue));

        :param source: -

        :stability: experimental
        """
        return jsii.invoke(self, "addEventSource", [source])

    @jsii.member(jsii_name="addEventSourceMapping")
    def add_event_source_mapping(
        self,
        id: builtins.str,
        *,
        event_source_arn: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_070aa057] = None,
        max_record_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IEventSourceDlq] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        starting_position: typing.Optional["StartingPosition"] = None,
    ) -> "EventSourceMapping":
        """(experimental) Adds an event source that maps to this AWS Lambda function.

        :param id: construct ID.
        :param event_source_arn: (experimental) The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: (experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param bisect_batch_on_error: (experimental) If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: (experimental) Set to false to disable the event source upon creation. Default: true
        :param kafka_topic: (experimental) The name of the Kafka topic. Default: - no topic
        :param max_batching_window: (experimental) The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_record_age: (experimental) The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: (experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: (experimental) The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param starting_position: (experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :stability: experimental
        """
        options = EventSourceMappingOptions(
            event_source_arn=event_source_arn,
            batch_size=batch_size,
            bisect_batch_on_error=bisect_batch_on_error,
            enabled=enabled,
            kafka_topic=kafka_topic,
            max_batching_window=max_batching_window,
            max_record_age=max_record_age,
            on_failure=on_failure,
            parallelization_factor=parallelization_factor,
            retry_attempts=retry_attempts,
            starting_position=starting_position,
        )

        return jsii.invoke(self, "addEventSourceMapping", [id, options])

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        principal: _IPrincipal_93b48231,
        action: typing.Optional[builtins.str] = None,
        event_source_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[_Construct_e78e779f] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Adds a permission to the Lambda resource policy.

        :param id: The id ƒor the permission construct.
        :param principal: (experimental) The entity for which you are granting permission to invoke the Lambda function. This entity can be any valid AWS service principal, such as s3.amazonaws.com or sns.amazonaws.com, or, if you are granting cross-account permission, an AWS account ID. For example, you might want to allow a custom application in another AWS account to push events to Lambda by invoking your function. The principal can be either an AccountPrincipal or a ServicePrincipal.
        :param action: (experimental) The Lambda actions that you want to allow in this statement. For example, you can specify lambda:CreateFunction to specify a certain action, or use a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a list of actions, see Actions and Condition Context Keys for AWS Lambda in the IAM User Guide. Default: 'lambda:InvokeFunction'
        :param event_source_token: (experimental) A unique token that must be supplied by the principal invoking the function. Default: The caller would not need to present a token.
        :param scope: (experimental) The scope to which the permission constructs be attached. The default is the Lambda function construct itself, but this would need to be different in cases such as cross-stack references where the Permissions would need to sit closer to the consumer of this permission (i.e., the caller). Default: - The instance of lambda.IFunction
        :param source_account: (experimental) The AWS account ID (without hyphens) of the source owner. For example, if you specify an S3 bucket in the SourceArn property, this value is the bucket owner's account ID. You can use this property to ensure that all source principals are owned by a specific account.
        :param source_arn: (experimental) The ARN of a resource that is invoking your function. When granting Amazon Simple Storage Service (Amazon S3) permission to invoke your function, specify this property with the bucket ARN as its value. This ensures that events generated only from the specified bucket, not just any bucket from any AWS account that creates a mapping to your function, can invoke the function.

        :see: Permission for details.
        :stability: experimental
        """
        permission = Permission(
            principal=principal,
            action=action,
            event_source_token=event_source_token,
            scope=scope,
            source_account=source_account,
            source_arn=source_arn,
        )

        return jsii.invoke(self, "addPermission", [id, permission])

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_296fe8a3) -> None:
        """(experimental) Adds a statement to the IAM role assumed by the instance.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToRolePolicy", [statement])

    @jsii.member(jsii_name="configureAsyncInvoke")
    def configure_async_invoke(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Configures options for asynchronous invocation.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        options = EventInvokeConfigOptions(
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return jsii.invoke(self, "configureAsyncInvoke", [options])

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(self, identity: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        """(experimental) Grant the given identity permissions to invoke this Lambda.

        :param identity: -

        :stability: experimental
        """
        return jsii.invoke(self, "grantInvoke", [identity])

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Return the given named metric for this Lambda Return the given named metric for this Function.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricDuration")
    def metric_duration(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the Duration of this Lambda How long execution of this Lambda takes.

        Average over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricDuration", [props])

    @jsii.member(jsii_name="metricErrors")
    def metric_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) How many invocations of this Lambda fail.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricErrors", [props])

    @jsii.member(jsii_name="metricInvocations")
    def metric_invocations(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of invocations of this Lambda How often this Lambda is invoked.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricInvocations", [props])

    @jsii.member(jsii_name="metricThrottles")
    def metric_throttles(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of throttled invocations of this Lambda How often this Lambda is throttled.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricThrottles", [props])


@jsii.interface(jsii_type="monocdk.aws_lambda.ILayerVersion")
class ILayerVersion(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ILayerVersionProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="layerVersionArn")
    def layer_version_arn(self) -> builtins.str:
        """(experimental) The ARN of the Lambda Layer version that this Layer defines.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="compatibleRuntimes")
    def compatible_runtimes(self) -> typing.Optional[typing.List["Runtime"]]:
        """(experimental) The runtimes compatible with this Layer.

        :default: Runtime.All

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        account_id: builtins.str,
        organization_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add permission for this layer version to specific entities.

        Usage within
        the same account where the layer is defined is always allowed and does not
        require calling this method. Note that the principal that creates the
        Lambda function using the layer (for example, a CloudFormation changeset
        execution role) also needs to have the ``lambda:GetLayerVersion``
        permission on the layer version.

        :param id: the ID of the grant in the construct tree.
        :param account_id: (experimental) The AWS Account id of the account that is authorized to use a Lambda Layer Version. The wild-card ``'*'`` can be used to grant access to "any" account (or any account in an organization when ``organizationId`` is specified).
        :param organization_id: (experimental) The ID of the AWS Organization to which the grant is restricted. Can only be specified if ``accountId`` is ``'*'``

        :stability: experimental
        """
        ...


class _ILayerVersionProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.ILayerVersion"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="layerVersionArn")
    def layer_version_arn(self) -> builtins.str:
        """(experimental) The ARN of the Lambda Layer version that this Layer defines.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "layerVersionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="compatibleRuntimes")
    def compatible_runtimes(self) -> typing.Optional[typing.List["Runtime"]]:
        """(experimental) The runtimes compatible with this Layer.

        :default: Runtime.All

        :stability: experimental
        """
        return jsii.get(self, "compatibleRuntimes")

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        account_id: builtins.str,
        organization_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add permission for this layer version to specific entities.

        Usage within
        the same account where the layer is defined is always allowed and does not
        require calling this method. Note that the principal that creates the
        Lambda function using the layer (for example, a CloudFormation changeset
        execution role) also needs to have the ``lambda:GetLayerVersion``
        permission on the layer version.

        :param id: the ID of the grant in the construct tree.
        :param account_id: (experimental) The AWS Account id of the account that is authorized to use a Lambda Layer Version. The wild-card ``'*'`` can be used to grant access to "any" account (or any account in an organization when ``organizationId`` is specified).
        :param organization_id: (experimental) The ID of the AWS Organization to which the grant is restricted. Can only be specified if ``accountId`` is ``'*'``

        :stability: experimental
        """
        permission = LayerVersionPermission(
            account_id=account_id, organization_id=organization_id
        )

        return jsii.invoke(self, "addPermission", [id, permission])


@jsii.interface(jsii_type="monocdk.aws_lambda.IScalableFunctionAttribute")
class IScalableFunctionAttribute(_IConstruct_5a0f9c5e, typing_extensions.Protocol):
    """(experimental) Interface for scalable attributes.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IScalableFunctionAttributeProxy

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: _Schedule_c2a5a45d,
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        """(experimental) Scale out or in based on schedule.

        :param id: -
        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="scaleOnUtilization")
    def scale_on_utilization(
        self,
        *,
        utilization_target: jsii.Number,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Scale out or in to keep utilization at a given level.

        The utilization is tracked by the
        LambdaProvisionedConcurrencyUtilization metric, emitted by lambda. See:
        https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-concurrency

        :param utilization_target: (experimental) Utilization target for the attribute. For example, .5 indicates that 50 percent of allocated provisioned concurrency is in use.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        """
        ...


class _IScalableFunctionAttributeProxy(
    jsii.proxy_for(_IConstruct_5a0f9c5e) # type: ignore
):
    """(experimental) Interface for scalable attributes.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IScalableFunctionAttribute"

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: _Schedule_c2a5a45d,
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        """(experimental) Scale out or in based on schedule.

        :param id: -
        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        """
        actions = _ScalingSchedule_6c3fc38f(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
        )

        return jsii.invoke(self, "scaleOnSchedule", [id, actions])

    @jsii.member(jsii_name="scaleOnUtilization")
    def scale_on_utilization(
        self,
        *,
        utilization_target: jsii.Number,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Scale out or in to keep utilization at a given level.

        The utilization is tracked by the
        LambdaProvisionedConcurrencyUtilization metric, emitted by lambda. See:
        https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-concurrency

        :param utilization_target: (experimental) Utilization target for the attribute. For example, .5 indicates that 50 percent of allocated provisioned concurrency is in use.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        """
        options = UtilizationScalingOptions(
            utilization_target=utilization_target,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return jsii.invoke(self, "scaleOnUtilization", [options])


@jsii.interface(jsii_type="monocdk.aws_lambda.IVersion")
class IVersion(IFunction, typing_extensions.Protocol):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IVersionProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="edgeArn")
    def edge_arn(self) -> builtins.str:
        """(experimental) The ARN of the version for Lambda@Edge.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> IFunction:
        """(experimental) The underlying AWS Lambda function.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        """(experimental) The most recently deployed version of this function.

        :stability: experimental
        :attribute: true
        """
        ...

    @jsii.member(jsii_name="addAlias")
    def add_alias(
        self,
        alias_name: builtins.str,
        *,
        additional_versions: typing.Optional[typing.List["VersionWeight"]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> "Alias":
        """(experimental) Defines an alias for this version.

        :param alias_name: The name of the alias.
        :param additional_versions: (experimental) Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is Example:: version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: (experimental) Description for the alias. Default: No description
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        ...


class _IVersionProxy(
    jsii.proxy_for(IFunction) # type: ignore
):
    """
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IVersion"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="edgeArn")
    def edge_arn(self) -> builtins.str:
        """(experimental) The ARN of the version for Lambda@Edge.

        :stability: experimental
        """
        return jsii.get(self, "edgeArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> IFunction:
        """(experimental) The underlying AWS Lambda function.

        :stability: experimental
        """
        return jsii.get(self, "lambda")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        """(experimental) The most recently deployed version of this function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "version")

    @jsii.member(jsii_name="addAlias")
    def add_alias(
        self,
        alias_name: builtins.str,
        *,
        additional_versions: typing.Optional[typing.List["VersionWeight"]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> "Alias":
        """(experimental) Defines an alias for this version.

        :param alias_name: The name of the alias.
        :param additional_versions: (experimental) Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is Example:: version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: (experimental) Description for the alias. Default: No description
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        options = AliasOptions(
            additional_versions=additional_versions,
            description=description,
            provisioned_concurrent_executions=provisioned_concurrent_executions,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return jsii.invoke(self, "addAlias", [alias_name, options])


class InlineCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.InlineCode",
):
    """(experimental) Lambda code from an inline string (limited to 4KiB).

    :stability: experimental
    """

    def __init__(self, code: builtins.str) -> None:
        """
        :param code: -

        :stability: experimental
        """
        jsii.create(InlineCode, self, [code])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _Construct_e78e779f) -> CodeConfig:
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _scope: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_scope])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(experimental) Determines whether this Code is inline code or not.

        :stability: experimental
        """
        return jsii.get(self, "isInline")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LambdaRuntimeProps",
    jsii_struct_bases=[],
    name_mapping={
        "bundling_docker_image": "bundlingDockerImage",
        "supports_code_guru_profiling": "supportsCodeGuruProfiling",
        "supports_inline_code": "supportsInlineCode",
    },
)
class LambdaRuntimeProps:
    def __init__(
        self,
        *,
        bundling_docker_image: typing.Optional[builtins.str] = None,
        supports_code_guru_profiling: typing.Optional[builtins.bool] = None,
        supports_inline_code: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param bundling_docker_image: (experimental) The Docker image name to be used for bundling in this runtime. Default: - the latest docker image "amazon/aws-sam-cli-build-image-" from https://hub.docker.com/u/amazon
        :param supports_code_guru_profiling: (experimental) Whether this runtime is integrated with and supported for profiling using Amazon CodeGuru Profiler. Default: false
        :param supports_inline_code: (experimental) Whether the ``ZipFile`` (aka inline code) property can be used with this runtime. Default: false

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if bundling_docker_image is not None:
            self._values["bundling_docker_image"] = bundling_docker_image
        if supports_code_guru_profiling is not None:
            self._values["supports_code_guru_profiling"] = supports_code_guru_profiling
        if supports_inline_code is not None:
            self._values["supports_inline_code"] = supports_inline_code

    @builtins.property
    def bundling_docker_image(self) -> typing.Optional[builtins.str]:
        """(experimental) The Docker image name to be used for bundling in this runtime.

        :default: - the latest docker image "amazon/aws-sam-cli-build-image-" from https://hub.docker.com/u/amazon

        :stability: experimental
        """
        result = self._values.get("bundling_docker_image")
        return result

    @builtins.property
    def supports_code_guru_profiling(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether this runtime is integrated with and supported for profiling using Amazon CodeGuru Profiler.

        :default: false

        :stability: experimental
        """
        result = self._values.get("supports_code_guru_profiling")
        return result

    @builtins.property
    def supports_inline_code(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether the ``ZipFile`` (aka inline code) property can be used with this runtime.

        :default: false

        :stability: experimental
        """
        result = self._values.get("supports_inline_code")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaRuntimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILayerVersion)
class LayerVersion(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.LayerVersion",
):
    """(experimental) Defines a new Lambda Layer version.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        code: Code,
        compatible_runtimes: typing.Optional[typing.List["Runtime"]] = None,
        description: typing.Optional[builtins.str] = None,
        layer_version_name: typing.Optional[builtins.str] = None,
        license: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param code: (experimental) The content of this Layer. Using ``Code.fromInline`` is not supported.
        :param compatible_runtimes: (experimental) The runtimes compatible with this Layer. Default: - All runtimes are supported.
        :param description: (experimental) The description the this Lambda Layer. Default: - No description.
        :param layer_version_name: (experimental) The name of the layer. Default: - A name will be generated.
        :param license: (experimental) The SPDX licence identifier or URL to the license file for this layer. Default: - No license information will be recorded.

        :stability: experimental
        """
        props = LayerVersionProps(
            code=code,
            compatible_runtimes=compatible_runtimes,
            description=description,
            layer_version_name=layer_version_name,
            license=license,
        )

        jsii.create(LayerVersion, self, [scope, id, props])

    @jsii.member(jsii_name="fromLayerVersionArn")
    @builtins.classmethod
    def from_layer_version_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        layer_version_arn: builtins.str,
    ) -> ILayerVersion:
        """(experimental) Imports a layer version by ARN.

        Assumes it is compatible with all Lambda runtimes.

        :param scope: -
        :param id: -
        :param layer_version_arn: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromLayerVersionArn", [scope, id, layer_version_arn])

    @jsii.member(jsii_name="fromLayerVersionAttributes")
    @builtins.classmethod
    def from_layer_version_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        layer_version_arn: builtins.str,
        compatible_runtimes: typing.Optional[typing.List["Runtime"]] = None,
    ) -> ILayerVersion:
        """(experimental) Imports a Layer that has been defined externally.

        :param scope: the parent Construct that will use the imported layer.
        :param id: the id of the imported layer in the construct tree.
        :param layer_version_arn: (experimental) The ARN of the LayerVersion.
        :param compatible_runtimes: (experimental) The list of compatible runtimes with this Layer.

        :stability: experimental
        """
        attrs = LayerVersionAttributes(
            layer_version_arn=layer_version_arn,
            compatible_runtimes=compatible_runtimes,
        )

        return jsii.sinvoke(cls, "fromLayerVersionAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        account_id: builtins.str,
        organization_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add permission for this layer version to specific entities.

        Usage within
        the same account where the layer is defined is always allowed and does not
        require calling this method. Note that the principal that creates the
        Lambda function using the layer (for example, a CloudFormation changeset
        execution role) also needs to have the ``lambda:GetLayerVersion``
        permission on the layer version.

        :param id: -
        :param account_id: (experimental) The AWS Account id of the account that is authorized to use a Lambda Layer Version. The wild-card ``'*'`` can be used to grant access to "any" account (or any account in an organization when ``organizationId`` is specified).
        :param organization_id: (experimental) The ID of the AWS Organization to which the grant is restricted. Can only be specified if ``accountId`` is ``'*'``

        :stability: experimental
        """
        permission = LayerVersionPermission(
            account_id=account_id, organization_id=organization_id
        )

        return jsii.invoke(self, "addPermission", [id, permission])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="layerVersionArn")
    def layer_version_arn(self) -> builtins.str:
        """(experimental) The ARN of the Lambda Layer version that this Layer defines.

        :stability: experimental
        """
        return jsii.get(self, "layerVersionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="compatibleRuntimes")
    def compatible_runtimes(self) -> typing.Optional[typing.List["Runtime"]]:
        """(experimental) The runtimes compatible with this Layer.

        :stability: experimental
        """
        return jsii.get(self, "compatibleRuntimes")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LayerVersionAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "layer_version_arn": "layerVersionArn",
        "compatible_runtimes": "compatibleRuntimes",
    },
)
class LayerVersionAttributes:
    def __init__(
        self,
        *,
        layer_version_arn: builtins.str,
        compatible_runtimes: typing.Optional[typing.List["Runtime"]] = None,
    ) -> None:
        """(experimental) Properties necessary to import a LayerVersion.

        :param layer_version_arn: (experimental) The ARN of the LayerVersion.
        :param compatible_runtimes: (experimental) The list of compatible runtimes with this Layer.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "layer_version_arn": layer_version_arn,
        }
        if compatible_runtimes is not None:
            self._values["compatible_runtimes"] = compatible_runtimes

    @builtins.property
    def layer_version_arn(self) -> builtins.str:
        """(experimental) The ARN of the LayerVersion.

        :stability: experimental
        """
        result = self._values.get("layer_version_arn")
        assert result is not None, "Required property 'layer_version_arn' is missing"
        return result

    @builtins.property
    def compatible_runtimes(self) -> typing.Optional[typing.List["Runtime"]]:
        """(experimental) The list of compatible runtimes with this Layer.

        :stability: experimental
        """
        result = self._values.get("compatible_runtimes")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LayerVersionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "layer_version_name": "layerVersionName",
        "license": "license",
    },
)
class LayerVersionOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        layer_version_name: typing.Optional[builtins.str] = None,
        license: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Non runtime options.

        :param description: (experimental) The description the this Lambda Layer. Default: - No description.
        :param layer_version_name: (experimental) The name of the layer. Default: - A name will be generated.
        :param license: (experimental) The SPDX licence identifier or URL to the license file for this layer. Default: - No license information will be recorded.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if layer_version_name is not None:
            self._values["layer_version_name"] = layer_version_name
        if license is not None:
            self._values["license"] = license

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) The description the this Lambda Layer.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def layer_version_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the layer.

        :default: - A name will be generated.

        :stability: experimental
        """
        result = self._values.get("layer_version_name")
        return result

    @builtins.property
    def license(self) -> typing.Optional[builtins.str]:
        """(experimental) The SPDX licence identifier or URL to the license file for this layer.

        :default: - No license information will be recorded.

        :stability: experimental
        """
        result = self._values.get("license")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LayerVersionPermission",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId", "organization_id": "organizationId"},
)
class LayerVersionPermission:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        organization_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Identification of an account (or organization) that is allowed to access a Lambda Layer Version.

        :param account_id: (experimental) The AWS Account id of the account that is authorized to use a Lambda Layer Version. The wild-card ``'*'`` can be used to grant access to "any" account (or any account in an organization when ``organizationId`` is specified).
        :param organization_id: (experimental) The ID of the AWS Organization to which the grant is restricted. Can only be specified if ``accountId`` is ``'*'``

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
        }
        if organization_id is not None:
            self._values["organization_id"] = organization_id

    @builtins.property
    def account_id(self) -> builtins.str:
        """(experimental) The AWS Account id of the account that is authorized to use a Lambda Layer Version.

        The wild-card ``'*'`` can be
        used to grant access to "any" account (or any account in an organization when ``organizationId`` is specified).

        :stability: experimental
        """
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return result

    @builtins.property
    def organization_id(self) -> typing.Optional[builtins.str]:
        """(experimental) The ID of the AWS Organization to which the grant is restricted.

        Can only be specified if ``accountId`` is ``'*'``

        :stability: experimental
        """
        result = self._values.get("organization_id")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LayerVersionProps",
    jsii_struct_bases=[LayerVersionOptions],
    name_mapping={
        "description": "description",
        "layer_version_name": "layerVersionName",
        "license": "license",
        "code": "code",
        "compatible_runtimes": "compatibleRuntimes",
    },
)
class LayerVersionProps(LayerVersionOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        layer_version_name: typing.Optional[builtins.str] = None,
        license: typing.Optional[builtins.str] = None,
        code: Code,
        compatible_runtimes: typing.Optional[typing.List["Runtime"]] = None,
    ) -> None:
        """
        :param description: (experimental) The description the this Lambda Layer. Default: - No description.
        :param layer_version_name: (experimental) The name of the layer. Default: - A name will be generated.
        :param license: (experimental) The SPDX licence identifier or URL to the license file for this layer. Default: - No license information will be recorded.
        :param code: (experimental) The content of this Layer. Using ``Code.fromInline`` is not supported.
        :param compatible_runtimes: (experimental) The runtimes compatible with this Layer. Default: - All runtimes are supported.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "code": code,
        }
        if description is not None:
            self._values["description"] = description
        if layer_version_name is not None:
            self._values["layer_version_name"] = layer_version_name
        if license is not None:
            self._values["license"] = license
        if compatible_runtimes is not None:
            self._values["compatible_runtimes"] = compatible_runtimes

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) The description the this Lambda Layer.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def layer_version_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the layer.

        :default: - A name will be generated.

        :stability: experimental
        """
        result = self._values.get("layer_version_name")
        return result

    @builtins.property
    def license(self) -> typing.Optional[builtins.str]:
        """(experimental) The SPDX licence identifier or URL to the license file for this layer.

        :default: - No license information will be recorded.

        :stability: experimental
        """
        result = self._values.get("license")
        return result

    @builtins.property
    def code(self) -> Code:
        """(experimental) The content of this Layer.

        Using ``Code.fromInline`` is not supported.

        :stability: experimental
        """
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return result

    @builtins.property
    def compatible_runtimes(self) -> typing.Optional[typing.List["Runtime"]]:
        """(experimental) The runtimes compatible with this Layer.

        :default: - All runtimes are supported.

        :stability: experimental
        """
        result = self._values.get("compatible_runtimes")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogRetention(
    _LogRetention_7657fb8a,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.LogRetention",
):
    """(deprecated) Creates a custom resource to control the retention policy of a CloudWatch Logs log group.

    The log group is created if it doesn't already exist. The policy
    is removed when ``retentionDays`` is ``undefined`` or equal to ``Infinity``.

    :deprecated: use ``LogRetention`` from '

    :stability: deprecated
    :aws-cdk: /aws-logs' instead
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        log_group_name: builtins.str,
        retention: _RetentionDays_6c560d31,
        log_group_region: typing.Optional[builtins.str] = None,
        log_retention_retry_options: typing.Optional[_LogRetentionRetryOptions_c6b3d73a] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param log_group_name: (experimental) The log group name.
        :param retention: (experimental) The number of days log events are kept in CloudWatch Logs.
        :param log_group_region: (experimental) The region where the log group should be created. Default: - same region as the stack
        :param log_retention_retry_options: (experimental) Retry options for all AWS API calls. Default: - AWS SDK default retry options
        :param role: (experimental) The IAM role for the Lambda function associated with the custom resource. Default: - A new role is created

        :stability: deprecated
        """
        props = LogRetentionProps(
            log_group_name=log_group_name,
            retention=retention,
            log_group_region=log_group_region,
            log_retention_retry_options=log_retention_retry_options,
            role=role,
        )

        jsii.create(LogRetention, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LogRetentionProps",
    jsii_struct_bases=[_LogRetentionProps_99b4e2db],
    name_mapping={
        "log_group_name": "logGroupName",
        "retention": "retention",
        "log_group_region": "logGroupRegion",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "role": "role",
    },
)
class LogRetentionProps(_LogRetentionProps_99b4e2db):
    def __init__(
        self,
        *,
        log_group_name: builtins.str,
        retention: _RetentionDays_6c560d31,
        log_group_region: typing.Optional[builtins.str] = None,
        log_retention_retry_options: typing.Optional[_LogRetentionRetryOptions_c6b3d73a] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        """(deprecated) Construction properties for a LogRetention.

        :param log_group_name: (experimental) The log group name.
        :param retention: (experimental) The number of days log events are kept in CloudWatch Logs.
        :param log_group_region: (experimental) The region where the log group should be created. Default: - same region as the stack
        :param log_retention_retry_options: (experimental) Retry options for all AWS API calls. Default: - AWS SDK default retry options
        :param role: (experimental) The IAM role for the Lambda function associated with the custom resource. Default: - A new role is created

        :deprecated: use ``LogRetentionProps`` from '

        :stability: deprecated
        :aws-cdk: /aws-logs' instead
        """
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = _LogRetentionRetryOptions_c6b3d73a(**log_retention_retry_options)
        self._values: typing.Dict[str, typing.Any] = {
            "log_group_name": log_group_name,
            "retention": retention,
        }
        if log_group_region is not None:
            self._values["log_group_region"] = log_group_region
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def log_group_name(self) -> builtins.str:
        """(experimental) The log group name.

        :stability: experimental
        """
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return result

    @builtins.property
    def retention(self) -> _RetentionDays_6c560d31:
        """(experimental) The number of days log events are kept in CloudWatch Logs.

        :stability: experimental
        """
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return result

    @builtins.property
    def log_group_region(self) -> typing.Optional[builtins.str]:
        """(experimental) The region where the log group should be created.

        :default: - same region as the stack

        :stability: experimental
        """
        result = self._values.get("log_group_region")
        return result

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[_LogRetentionRetryOptions_c6b3d73a]:
        """(experimental) Retry options for all AWS API calls.

        :default: - AWS SDK default retry options

        :stability: experimental
        """
        result = self._values.get("log_retention_retry_options")
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role for the Lambda function associated with the custom resource.

        :default: - A new role is created

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogRetentionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.LogRetentionRetryOptions",
    jsii_struct_bases=[_LogRetentionRetryOptions_c6b3d73a],
    name_mapping={"base": "base", "max_retries": "maxRetries"},
)
class LogRetentionRetryOptions(_LogRetentionRetryOptions_c6b3d73a):
    def __init__(
        self,
        *,
        base: typing.Optional[_Duration_070aa057] = None,
        max_retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(deprecated) Retry options for all AWS API calls.

        :param base: (experimental) The base duration to use in the exponential backoff for operation retries. Default: Duration.millis(100) (AWS SDK default)
        :param max_retries: (experimental) The maximum amount of retries. Default: 3 (AWS SDK default)

        :deprecated: use ``LogRetentionRetryOptions`` from '

        :stability: deprecated
        :aws-cdk: /aws-logs' instead
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if base is not None:
            self._values["base"] = base
        if max_retries is not None:
            self._values["max_retries"] = max_retries

    @builtins.property
    def base(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The base duration to use in the exponential backoff for operation retries.

        :default: Duration.millis(100) (AWS SDK default)

        :stability: experimental
        """
        result = self._values.get("base")
        return result

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum amount of retries.

        :default: 3 (AWS SDK default)

        :stability: experimental
        """
        result = self._values.get("max_retries")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogRetentionRetryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.Permission",
    jsii_struct_bases=[],
    name_mapping={
        "principal": "principal",
        "action": "action",
        "event_source_token": "eventSourceToken",
        "scope": "scope",
        "source_account": "sourceAccount",
        "source_arn": "sourceArn",
    },
)
class Permission:
    def __init__(
        self,
        *,
        principal: _IPrincipal_93b48231,
        action: typing.Optional[builtins.str] = None,
        event_source_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[_Construct_e78e779f] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Represents a permission statement that can be added to a Lambda's resource policy via the ``addToResourcePolicy`` method.

        :param principal: (experimental) The entity for which you are granting permission to invoke the Lambda function. This entity can be any valid AWS service principal, such as s3.amazonaws.com or sns.amazonaws.com, or, if you are granting cross-account permission, an AWS account ID. For example, you might want to allow a custom application in another AWS account to push events to Lambda by invoking your function. The principal can be either an AccountPrincipal or a ServicePrincipal.
        :param action: (experimental) The Lambda actions that you want to allow in this statement. For example, you can specify lambda:CreateFunction to specify a certain action, or use a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a list of actions, see Actions and Condition Context Keys for AWS Lambda in the IAM User Guide. Default: 'lambda:InvokeFunction'
        :param event_source_token: (experimental) A unique token that must be supplied by the principal invoking the function. Default: The caller would not need to present a token.
        :param scope: (experimental) The scope to which the permission constructs be attached. The default is the Lambda function construct itself, but this would need to be different in cases such as cross-stack references where the Permissions would need to sit closer to the consumer of this permission (i.e., the caller). Default: - The instance of lambda.IFunction
        :param source_account: (experimental) The AWS account ID (without hyphens) of the source owner. For example, if you specify an S3 bucket in the SourceArn property, this value is the bucket owner's account ID. You can use this property to ensure that all source principals are owned by a specific account.
        :param source_arn: (experimental) The ARN of a resource that is invoking your function. When granting Amazon Simple Storage Service (Amazon S3) permission to invoke your function, specify this property with the bucket ARN as its value. This ensures that events generated only from the specified bucket, not just any bucket from any AWS account that creates a mapping to your function, can invoke the function.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "principal": principal,
        }
        if action is not None:
            self._values["action"] = action
        if event_source_token is not None:
            self._values["event_source_token"] = event_source_token
        if scope is not None:
            self._values["scope"] = scope
        if source_account is not None:
            self._values["source_account"] = source_account
        if source_arn is not None:
            self._values["source_arn"] = source_arn

    @builtins.property
    def principal(self) -> _IPrincipal_93b48231:
        """(experimental) The entity for which you are granting permission to invoke the Lambda function.

        This entity can be any valid AWS service principal, such as
        s3.amazonaws.com or sns.amazonaws.com, or, if you are granting
        cross-account permission, an AWS account ID. For example, you might want
        to allow a custom application in another AWS account to push events to
        Lambda by invoking your function.

        The principal can be either an AccountPrincipal or a ServicePrincipal.

        :stability: experimental
        """
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return result

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        """(experimental) The Lambda actions that you want to allow in this statement.

        For example,
        you can specify lambda:CreateFunction to specify a certain action, or use
        a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a
        list of actions, see Actions and Condition Context Keys for AWS Lambda in
        the IAM User Guide.

        :default: 'lambda:InvokeFunction'

        :stability: experimental
        """
        result = self._values.get("action")
        return result

    @builtins.property
    def event_source_token(self) -> typing.Optional[builtins.str]:
        """(experimental) A unique token that must be supplied by the principal invoking the function.

        :default: The caller would not need to present a token.

        :stability: experimental
        """
        result = self._values.get("event_source_token")
        return result

    @builtins.property
    def scope(self) -> typing.Optional[_Construct_e78e779f]:
        """(experimental) The scope to which the permission constructs be attached.

        The default is
        the Lambda function construct itself, but this would need to be different
        in cases such as cross-stack references where the Permissions would need
        to sit closer to the consumer of this permission (i.e., the caller).

        :default: - The instance of lambda.IFunction

        :stability: experimental
        """
        result = self._values.get("scope")
        return result

    @builtins.property
    def source_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID (without hyphens) of the source owner.

        For example, if
        you specify an S3 bucket in the SourceArn property, this value is the
        bucket owner's account ID. You can use this property to ensure that all
        source principals are owned by a specific account.

        :stability: experimental
        """
        result = self._values.get("source_account")
        return result

    @builtins.property
    def source_arn(self) -> typing.Optional[builtins.str]:
        """(experimental) The ARN of a resource that is invoking your function.

        When granting
        Amazon Simple Storage Service (Amazon S3) permission to invoke your
        function, specify this property with the bucket ARN as its value. This
        ensures that events generated only from the specified bucket, not just
        any bucket from any AWS account that creates a mapping to your function,
        can invoke the function.

        :stability: experimental
        """
        result = self._values.get("source_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Permission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.ResourceBindOptions",
    jsii_struct_bases=[],
    name_mapping={"resource_property": "resourceProperty"},
)
class ResourceBindOptions:
    def __init__(
        self,
        *,
        resource_property: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param resource_property: (experimental) The name of the CloudFormation property to annotate with asset metadata. Default: Code

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if resource_property is not None:
            self._values["resource_property"] = resource_property

    @builtins.property
    def resource_property(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the CloudFormation property to annotate with asset metadata.

        :default: Code

        :see: https://github.com/aws/aws-cdk/issues/1432
        :stability: experimental
        """
        result = self._values.get("resource_property")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Runtime(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_lambda.Runtime"):
    """(experimental) Lambda function runtime environment.

    If you need to use a runtime name that doesn't exist as a static member, you
    can instantiate a ``Runtime`` object, e.g: ``new Runtime('nodejs99.99')``.

    :stability: experimental
    """

    def __init__(
        self,
        name: builtins.str,
        family: typing.Optional["RuntimeFamily"] = None,
        *,
        bundling_docker_image: typing.Optional[builtins.str] = None,
        supports_code_guru_profiling: typing.Optional[builtins.bool] = None,
        supports_inline_code: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param name: -
        :param family: -
        :param bundling_docker_image: (experimental) The Docker image name to be used for bundling in this runtime. Default: - the latest docker image "amazon/aws-sam-cli-build-image-" from https://hub.docker.com/u/amazon
        :param supports_code_guru_profiling: (experimental) Whether this runtime is integrated with and supported for profiling using Amazon CodeGuru Profiler. Default: false
        :param supports_inline_code: (experimental) Whether the ``ZipFile`` (aka inline code) property can be used with this runtime. Default: false

        :stability: experimental
        """
        props = LambdaRuntimeProps(
            bundling_docker_image=bundling_docker_image,
            supports_code_guru_profiling=supports_code_guru_profiling,
            supports_inline_code=supports_inline_code,
        )

        jsii.create(Runtime, self, [name, family, props])

    @jsii.member(jsii_name="runtimeEquals")
    def runtime_equals(self, other: "Runtime") -> builtins.bool:
        """
        :param other: -

        :stability: experimental
        """
        return jsii.invoke(self, "runtimeEquals", [other])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """
        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="ALL")
    def ALL(cls) -> typing.List["Runtime"]:
        """(experimental) A list of all known ``Runtime``'s.

        :stability: experimental
        """
        return jsii.sget(cls, "ALL")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="DOTNET_CORE_1")
    def DOTNET_CORE_1(cls) -> "Runtime":
        """(deprecated) The .NET Core 1.0 runtime (dotnetcore1.0).

        :deprecated: Use {@link DOTNET_CORE_2_1}

        :stability: deprecated
        """
        return jsii.sget(cls, "DOTNET_CORE_1")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="DOTNET_CORE_2")
    def DOTNET_CORE_2(cls) -> "Runtime":
        """(deprecated) The .NET Core 2.0 runtime (dotnetcore2.0).

        :deprecated: Use {@link DOTNET_CORE_2_1}

        :stability: deprecated
        """
        return jsii.sget(cls, "DOTNET_CORE_2")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="DOTNET_CORE_2_1")
    def DOTNET_CORE_2_1(cls) -> "Runtime":
        """(experimental) The .NET Core 2.1 runtime (dotnetcore2.1).

        :stability: experimental
        """
        return jsii.sget(cls, "DOTNET_CORE_2_1")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="DOTNET_CORE_3_1")
    def DOTNET_CORE_3_1(cls) -> "Runtime":
        """(experimental) The .NET Core 3.1 runtime (dotnetcore3.1).

        :stability: experimental
        """
        return jsii.sget(cls, "DOTNET_CORE_3_1")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="FROM_IMAGE")
    def FROM_IMAGE(cls) -> "Runtime":
        """(experimental) A special runtime entry to be used when function is using a docker image.

        :stability: experimental
        """
        return jsii.sget(cls, "FROM_IMAGE")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="GO_1_X")
    def GO_1_X(cls) -> "Runtime":
        """(experimental) The Go 1.x runtime (go1.x).

        :stability: experimental
        """
        return jsii.sget(cls, "GO_1_X")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="JAVA_11")
    def JAVA_11(cls) -> "Runtime":
        """(experimental) The Java 11 runtime (java11).

        :stability: experimental
        """
        return jsii.sget(cls, "JAVA_11")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="JAVA_8")
    def JAVA_8(cls) -> "Runtime":
        """(experimental) The Java 8 runtime (java8).

        :stability: experimental
        """
        return jsii.sget(cls, "JAVA_8")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="JAVA_8_CORRETTO")
    def JAVA_8_CORRETTO(cls) -> "Runtime":
        """(experimental) The Java 8 Corretto runtime (java8.al2).

        :stability: experimental
        """
        return jsii.sget(cls, "JAVA_8_CORRETTO")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="NODEJS")
    def NODEJS(cls) -> "Runtime":
        """(deprecated) The NodeJS runtime (nodejs).

        :deprecated: Use {@link NODEJS_12_X}

        :stability: deprecated
        """
        return jsii.sget(cls, "NODEJS")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="NODEJS_10_X")
    def NODEJS_10_X(cls) -> "Runtime":
        """(experimental) The NodeJS 10.x runtime (nodejs10.x).

        :stability: experimental
        """
        return jsii.sget(cls, "NODEJS_10_X")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="NODEJS_12_X")
    def NODEJS_12_X(cls) -> "Runtime":
        """(experimental) The NodeJS 12.x runtime (nodejs12.x).

        :stability: experimental
        """
        return jsii.sget(cls, "NODEJS_12_X")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="NODEJS_4_3")
    def NODEJS_4_3(cls) -> "Runtime":
        """(deprecated) The NodeJS 4.3 runtime (nodejs4.3).

        :deprecated: Use {@link NODEJS_12_X}

        :stability: deprecated
        """
        return jsii.sget(cls, "NODEJS_4_3")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="NODEJS_6_10")
    def NODEJS_6_10(cls) -> "Runtime":
        """(deprecated) The NodeJS 6.10 runtime (nodejs6.10).

        :deprecated: Use {@link NODEJS_12_X}

        :stability: deprecated
        """
        return jsii.sget(cls, "NODEJS_6_10")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="NODEJS_8_10")
    def NODEJS_8_10(cls) -> "Runtime":
        """(deprecated) The NodeJS 8.10 runtime (nodejs8.10).

        :deprecated: Use {@link NODEJS_12_X}

        :stability: deprecated
        """
        return jsii.sget(cls, "NODEJS_8_10")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="PROVIDED")
    def PROVIDED(cls) -> "Runtime":
        """(experimental) The custom provided runtime (provided).

        :stability: experimental
        """
        return jsii.sget(cls, "PROVIDED")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="PROVIDED_AL2")
    def PROVIDED_AL2(cls) -> "Runtime":
        """(experimental) The custom provided runtime (provided).

        :stability: experimental
        """
        return jsii.sget(cls, "PROVIDED_AL2")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="PYTHON_2_7")
    def PYTHON_2_7(cls) -> "Runtime":
        """(experimental) The Python 2.7 runtime (python2.7).

        :stability: experimental
        """
        return jsii.sget(cls, "PYTHON_2_7")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="PYTHON_3_6")
    def PYTHON_3_6(cls) -> "Runtime":
        """(experimental) The Python 3.6 runtime (python3.6).

        :stability: experimental
        """
        return jsii.sget(cls, "PYTHON_3_6")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="PYTHON_3_7")
    def PYTHON_3_7(cls) -> "Runtime":
        """(experimental) The Python 3.7 runtime (python3.7).

        :stability: experimental
        """
        return jsii.sget(cls, "PYTHON_3_7")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="PYTHON_3_8")
    def PYTHON_3_8(cls) -> "Runtime":
        """(experimental) The Python 3.8 runtime (python3.8).

        :stability: experimental
        """
        return jsii.sget(cls, "PYTHON_3_8")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="RUBY_2_5")
    def RUBY_2_5(cls) -> "Runtime":
        """(experimental) The Ruby 2.5 runtime (ruby2.5).

        :stability: experimental
        """
        return jsii.sget(cls, "RUBY_2_5")

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="RUBY_2_7")
    def RUBY_2_7(cls) -> "Runtime":
        """(experimental) The Ruby 2.7 runtime (ruby2.7).

        :stability: experimental
        """
        return jsii.sget(cls, "RUBY_2_7")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="bundlingDockerImage")
    def bundling_docker_image(self) -> _BundlingDockerImage_86dee600:
        """(experimental) The bundling Docker image for this runtime.

        :stability: experimental
        """
        return jsii.get(self, "bundlingDockerImage")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) The name of this runtime, as expected by the Lambda resource.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="supportsCodeGuruProfiling")
    def supports_code_guru_profiling(self) -> builtins.bool:
        """(experimental) Whether this runtime is integrated with and supported for profiling using Amazon CodeGuru Profiler.

        :stability: experimental
        """
        return jsii.get(self, "supportsCodeGuruProfiling")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="supportsInlineCode")
    def supports_inline_code(self) -> builtins.bool:
        """(experimental) Whether the ``ZipFile`` (aka inline code) property can be used with this runtime.

        :stability: experimental
        """
        return jsii.get(self, "supportsInlineCode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="family")
    def family(self) -> typing.Optional["RuntimeFamily"]:
        """(experimental) The runtime family.

        :stability: experimental
        """
        return jsii.get(self, "family")


@jsii.enum(jsii_type="monocdk.aws_lambda.RuntimeFamily")
class RuntimeFamily(enum.Enum):
    """
    :stability: experimental
    """

    NODEJS = "NODEJS"
    """
    :stability: experimental
    """
    JAVA = "JAVA"
    """
    :stability: experimental
    """
    PYTHON = "PYTHON"
    """
    :stability: experimental
    """
    DOTNET_CORE = "DOTNET_CORE"
    """
    :stability: experimental
    """
    GO = "GO"
    """
    :stability: experimental
    """
    RUBY = "RUBY"
    """
    :stability: experimental
    """
    OTHER = "OTHER"
    """
    :stability: experimental
    """


class S3Code(Code, metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_lambda.S3Code"):
    """(experimental) Lambda code from an S3 archive.

    :stability: experimental
    """

    def __init__(
        self,
        bucket: _IBucket_73486e29,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param bucket: -
        :param key: -
        :param object_version: -

        :stability: experimental
        """
        jsii.create(S3Code, self, [bucket, key, object_version])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _Construct_e78e779f) -> CodeConfig:
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _scope: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_scope])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(experimental) Determines whether this Code is inline code or not.

        :stability: experimental
        """
        return jsii.get(self, "isInline")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.SingletonFunctionProps",
    jsii_struct_bases=[FunctionProps],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "code": "code",
        "handler": "handler",
        "runtime": "runtime",
        "uuid": "uuid",
        "lambda_purpose": "lambdaPurpose",
    },
)
class SingletonFunctionProps(FunctionProps):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional["VersionOptions"] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List[IEventSource]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List[ILayerVersion]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional[LogRetentionRetryOptions] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional["Tracing"] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        code: Code,
        handler: builtins.str,
        runtime: Runtime,
        uuid: builtins.str,
        lambda_purpose: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for a newly created singleton Lambda.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param code: (experimental) The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: (experimental) The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: (experimental) The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.
        :param uuid: (experimental) A unique identifier to identify this lambda. The identifier should be unique across all custom resource providers. We recommend generating a UUID per provider.
        :param lambda_purpose: (experimental) A descriptive name for the purpose of this Lambda. If the Lambda does not have a physical name, this string will be reflected its generated name. The combination of lambdaPurpose and uuid must be unique. Default: SingletonLambda

        :stability: experimental
        """
        if isinstance(current_version_options, dict):
            current_version_options = VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {
            "code": code,
            "handler": handler,
            "runtime": runtime,
            "uuid": uuid,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if lambda_purpose is not None:
            self._values["lambda_purpose"] = lambda_purpose

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true

        :stability: experimental
        """
        result = self._values.get("allow_all_outbound")
        return result

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        """(experimental) Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        :stability: experimental
        """
        result = self._values.get("allow_public_subnet")
        return result

    @builtins.property
    def current_version_options(self) -> typing.Optional["VersionOptions"]:
        """(experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``

        :stability: experimental
        """
        result = self._values.get("current_version_options")
        return result

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_45a01ab4]:
        """(experimental) The SQS queue to use if DLQ is enabled.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue")
        return result

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue_enabled")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the function.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.

        :stability: experimental
        """
        result = self._values.get("environment")
        return result

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_IKey_36930160]:
        """(experimental) The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).

        :stability: experimental
        """
        result = self._values.get("environment_encryption")
        return result

    @builtins.property
    def events(self) -> typing.Optional[typing.List[IEventSource]]:
        """(experimental) Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.

        :stability: experimental
        """
        result = self._values.get("events")
        return result

    @builtins.property
    def filesystem(self) -> typing.Optional[FileSystem]:
        """(experimental) The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem

        :stability: experimental
        """
        result = self._values.get("filesystem")
        return result

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.

        :stability: experimental
        """
        result = self._values.get("function_name")
        return result

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[_PolicyStatement_296fe8a3]]:
        """(experimental) Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.

        :stability: experimental
        """
        result = self._values.get("initial_policy")
        return result

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[ILayerVersion]]:
        """(experimental) A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by mulitple functions.

        :default: - No layers.

        :stability: experimental
        """
        result = self._values.get("layers")
        return result

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_6c560d31]:
        """(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE

        :stability: experimental
        """
        result = self._values.get("log_retention")
        return result

    @builtins.property
    def log_retention_retry_options(self) -> typing.Optional[LogRetentionRetryOptions]:
        """(experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.

        :stability: experimental
        """
        result = self._values.get("log_retention_retry_options")
        return result

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.

        :stability: experimental
        """
        result = self._values.get("log_retention_role")
        return result

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """(experimental) The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128

        :stability: experimental
        """
        result = self._values.get("memory_size")
        return result

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling")
        return result

    @builtins.property
    def profiling_group(self) -> typing.Optional[_IProfilingGroup_418eb20c]:
        """(experimental) Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling_group")
        return result

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        :stability: experimental
        """
        result = self._values.get("reserved_concurrent_executions")
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_cdbba9d3]:
        """(deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead.

        Only used if 'vpc' is supplied.

        Use securityGroups property instead.
        Function constructor will throw an error if both are specified.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroups prop, a dedicated security
        group will be created for this function.

        :deprecated: - This property is deprecated, use securityGroups instead

        :stability: deprecated
        """
        result = self._values.get("security_group")
        return result

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]]:
        """(experimental) The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.

        :stability: experimental
        """
        result = self._values.get("security_groups")
        return result

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)

        :stability: experimental
        """
        result = self._values.get("timeout")
        return result

    @builtins.property
    def tracing(self) -> typing.Optional["Tracing"]:
        """(experimental) Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled

        :stability: experimental
        """
        result = self._values.get("tracing")
        return result

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_6d1f76c4]:
        """(experimental) VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.

        :default: - Function is not placed within a VPC.

        :stability: experimental
        """
        result = self._values.get("vpc")
        return result

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        """(experimental) Where to place the network interfaces within the VPC.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified

        :stability: experimental
        """
        result = self._values.get("vpc_subnets")
        return result

    @builtins.property
    def code(self) -> Code:
        """(experimental) The source code of your Lambda function.

        You can point to a file in an
        Amazon Simple Storage Service (Amazon S3) bucket or specify your source
        code as inline text.

        :stability: experimental
        """
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return result

    @builtins.property
    def handler(self) -> builtins.str:
        """(experimental) The name of the method within your code that Lambda calls to execute your function.

        The format includes the file name. It can also include
        namespaces and other qualifiers, depending on the runtime.
        For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel.

        Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image.

        NOTE: If you specify your source code as inline text by specifying the
        ZipFile property within the Code property, specify index.function_name as
        the handler.

        :stability: experimental
        """
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return result

    @builtins.property
    def runtime(self) -> Runtime:
        """(experimental) The runtime environment for the Lambda function that you are uploading.

        For valid values, see the Runtime property in the AWS Lambda Developer
        Guide.

        Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.

        :stability: experimental
        """
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return result

    @builtins.property
    def uuid(self) -> builtins.str:
        """(experimental) A unique identifier to identify this lambda.

        The identifier should be unique across all custom resource providers.
        We recommend generating a UUID per provider.

        :stability: experimental
        """
        result = self._values.get("uuid")
        assert result is not None, "Required property 'uuid' is missing"
        return result

    @builtins.property
    def lambda_purpose(self) -> typing.Optional[builtins.str]:
        """(experimental) A descriptive name for the purpose of this Lambda.

        If the Lambda does not have a physical name, this string will be
        reflected its generated name. The combination of lambdaPurpose
        and uuid must be unique.

        :default: SingletonLambda

        :stability: experimental
        """
        result = self._values.get("lambda_purpose")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SingletonFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_lambda.StartingPosition")
class StartingPosition(enum.Enum):
    """(experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading.

    :stability: experimental
    """

    TRIM_HORIZON = "TRIM_HORIZON"
    """(experimental) Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.

    :stability: experimental
    """
    LATEST = "LATEST"
    """(experimental) Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.

    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk.aws_lambda.Tracing")
class Tracing(enum.Enum):
    """(experimental) X-Ray Tracing Modes (https://docs.aws.amazon.com/lambda/latest/dg/API_TracingConfig.html).

    :stability: experimental
    """

    ACTIVE = "ACTIVE"
    """(experimental) Lambda will respect any tracing header it receives from an upstream service.

    If no tracing header is received, Lambda will call X-Ray for a tracing decision.

    :stability: experimental
    """
    PASS_THROUGH = "PASS_THROUGH"
    """(experimental) Lambda will only trace the request from an upstream service if it contains a tracing header with "sampled=1".

    :stability: experimental
    """
    DISABLED = "DISABLED"
    """(experimental) Lambda will not trace any request.

    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.UtilizationScalingOptions",
    jsii_struct_bases=[_BaseTargetTrackingProps_e4402570],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "utilization_target": "utilizationTarget",
    },
)
class UtilizationScalingOptions(_BaseTargetTrackingProps_e4402570):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
        utilization_target: jsii.Number,
    ) -> None:
        """(experimental) Options for enabling Lambda utilization tracking.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param utilization_target: (experimental) Utilization target for the attribute. For example, .5 indicates that 50 percent of allocated provisioned concurrency is in use.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "utilization_target": utilization_target,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        """(experimental) Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false

        :stability: experimental
        """
        result = self._values.get("disable_scale_in")
        return result

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the scaling policy.

        :default: - Automatically generated name.

        :stability: experimental
        """
        result = self._values.get("policy_name")
        return result

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        """
        result = self._values.get("scale_in_cooldown")
        return result

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        """
        result = self._values.get("scale_out_cooldown")
        return result

    @builtins.property
    def utilization_target(self) -> jsii.Number:
        """(experimental) Utilization target for the attribute.

        For example, .5 indicates that 50 percent of allocated provisioned concurrency is in use.

        :stability: experimental
        """
        result = self._values.get("utilization_target")
        assert result is not None, "Required property 'utilization_target' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UtilizationScalingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.VersionAttributes",
    jsii_struct_bases=[],
    name_mapping={"lambda_": "lambda", "version": "version"},
)
class VersionAttributes:
    def __init__(self, *, lambda_: IFunction, version: builtins.str) -> None:
        """
        :param lambda_: (experimental) The lambda function.
        :param version: (experimental) The version.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "lambda_": lambda_,
            "version": version,
        }

    @builtins.property
    def lambda_(self) -> IFunction:
        """(experimental) The lambda function.

        :stability: experimental
        """
        result = self._values.get("lambda_")
        assert result is not None, "Required property 'lambda_' is missing"
        return result

    @builtins.property
    def version(self) -> builtins.str:
        """(experimental) The version.

        :stability: experimental
        """
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.VersionOptions",
    jsii_struct_bases=[EventInvokeConfigOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "code_sha256": "codeSha256",
        "description": "description",
        "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
        "removal_policy": "removalPolicy",
    },
)
class VersionOptions(EventInvokeConfigOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        code_sha256: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
    ) -> None:
        """(experimental) Options for ``lambda.Version``.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param code_sha256: (experimental) SHA256 of the version of the Lambda source code. Specify to validate that you're deploying the right version. Default: No validation is performed
        :param description: (experimental) Description of the version. Default: Description of the Lambda
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's version. Default: No provisioned concurrency
        :param removal_policy: (experimental) Whether to retain old versions of this function when a new version is created. Default: RemovalPolicy.DESTROY

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if code_sha256 is not None:
            self._values["code_sha256"] = code_sha256
        if description is not None:
            self._values["description"] = description
        if provisioned_concurrent_executions is not None:
            self._values["provisioned_concurrent_executions"] = provisioned_concurrent_executions
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def code_sha256(self) -> typing.Optional[builtins.str]:
        """(experimental) SHA256 of the version of the Lambda source code.

        Specify to validate that you're deploying the right version.

        :default: No validation is performed

        :stability: experimental
        """
        result = self._values.get("code_sha256")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) Description of the version.

        :default: Description of the Lambda

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def provisioned_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) Specifies a provisioned concurrency configuration for a function's version.

        :default: No provisioned concurrency

        :stability: experimental
        """
        result = self._values.get("provisioned_concurrent_executions")
        return result

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        """(experimental) Whether to retain old versions of this function when a new version is created.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        """
        result = self._values.get("removal_policy")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.VersionProps",
    jsii_struct_bases=[VersionOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "code_sha256": "codeSha256",
        "description": "description",
        "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
        "removal_policy": "removalPolicy",
        "lambda_": "lambda",
    },
)
class VersionProps(VersionOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        code_sha256: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        lambda_: IFunction,
    ) -> None:
        """(experimental) Properties for a new Lambda version.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param code_sha256: (experimental) SHA256 of the version of the Lambda source code. Specify to validate that you're deploying the right version. Default: No validation is performed
        :param description: (experimental) Description of the version. Default: Description of the Lambda
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's version. Default: No provisioned concurrency
        :param removal_policy: (experimental) Whether to retain old versions of this function when a new version is created. Default: RemovalPolicy.DESTROY
        :param lambda_: (experimental) Function to get the value of.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "lambda_": lambda_,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if code_sha256 is not None:
            self._values["code_sha256"] = code_sha256
        if description is not None:
            self._values["description"] = description
        if provisioned_concurrent_executions is not None:
            self._values["provisioned_concurrent_executions"] = provisioned_concurrent_executions
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def code_sha256(self) -> typing.Optional[builtins.str]:
        """(experimental) SHA256 of the version of the Lambda source code.

        Specify to validate that you're deploying the right version.

        :default: No validation is performed

        :stability: experimental
        """
        result = self._values.get("code_sha256")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) Description of the version.

        :default: Description of the Lambda

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def provisioned_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) Specifies a provisioned concurrency configuration for a function's version.

        :default: No provisioned concurrency

        :stability: experimental
        """
        result = self._values.get("provisioned_concurrent_executions")
        return result

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        """(experimental) Whether to retain old versions of this function when a new version is created.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        """
        result = self._values.get("removal_policy")
        return result

    @builtins.property
    def lambda_(self) -> IFunction:
        """(experimental) Function to get the value of.

        :stability: experimental
        """
        result = self._values.get("lambda_")
        assert result is not None, "Required property 'lambda_' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.VersionWeight",
    jsii_struct_bases=[],
    name_mapping={"version": "version", "weight": "weight"},
)
class VersionWeight:
    def __init__(self, *, version: IVersion, weight: jsii.Number) -> None:
        """(experimental) A version/weight pair for routing traffic to Lambda functions.

        :param version: (experimental) The version to route traffic to.
        :param weight: (experimental) How much weight to assign to this version (0..1).

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "version": version,
            "weight": weight,
        }

    @builtins.property
    def version(self) -> IVersion:
        """(experimental) The version to route traffic to.

        :stability: experimental
        """
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return result

    @builtins.property
    def weight(self) -> jsii.Number:
        """(experimental) How much weight to assign to this version (0..1).

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
        return "VersionWeight(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.AliasOptions",
    jsii_struct_bases=[EventInvokeConfigOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "additional_versions": "additionalVersions",
        "description": "description",
        "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
    },
)
class AliasOptions(EventInvokeConfigOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        additional_versions: typing.Optional[typing.List[VersionWeight]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Options for ``lambda.Alias``.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param additional_versions: (experimental) Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is Example:: version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: (experimental) Description for the alias. Default: No description
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if additional_versions is not None:
            self._values["additional_versions"] = additional_versions
        if description is not None:
            self._values["description"] = description
        if provisioned_concurrent_executions is not None:
            self._values["provisioned_concurrent_executions"] = provisioned_concurrent_executions

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def additional_versions(self) -> typing.Optional[typing.List[VersionWeight]]:
        """(experimental) Additional versions with individual weights this alias points to.

        Individual additional version weights specified here should add up to
        (less than) one. All remaining weight is routed to the default
        version.

        For example, the config is Example::

           version: "1"
           additionalVersions: [{ version: "2", weight: 0.05 }]

        Then 5% of traffic will be routed to function version 2, while
        the remaining 95% of traffic will be routed to function version 1.

        :default: No additional versions

        :stability: experimental
        """
        result = self._values.get("additional_versions")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) Description for the alias.

        :default: No description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def provisioned_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) Specifies a provisioned concurrency configuration for a function's alias.

        :default: No provisioned concurrency

        :stability: experimental
        """
        result = self._values.get("provisioned_concurrent_executions")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.AliasProps",
    jsii_struct_bases=[AliasOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "additional_versions": "additionalVersions",
        "description": "description",
        "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
        "alias_name": "aliasName",
        "version": "version",
    },
)
class AliasProps(AliasOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        additional_versions: typing.Optional[typing.List[VersionWeight]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        alias_name: builtins.str,
        version: IVersion,
    ) -> None:
        """(experimental) Properties for a new Lambda alias.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param additional_versions: (experimental) Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is Example:: version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: (experimental) Description for the alias. Default: No description
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency
        :param alias_name: (experimental) Name of this alias.
        :param version: (experimental) Function version this alias refers to. Use lambda.addVersion() to obtain a new lambda version to refer to.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "version": version,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if additional_versions is not None:
            self._values["additional_versions"] = additional_versions
        if description is not None:
            self._values["description"] = description
        if provisioned_concurrent_executions is not None:
            self._values["provisioned_concurrent_executions"] = provisioned_concurrent_executions

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def additional_versions(self) -> typing.Optional[typing.List[VersionWeight]]:
        """(experimental) Additional versions with individual weights this alias points to.

        Individual additional version weights specified here should add up to
        (less than) one. All remaining weight is routed to the default
        version.

        For example, the config is Example::

           version: "1"
           additionalVersions: [{ version: "2", weight: 0.05 }]

        Then 5% of traffic will be routed to function version 2, while
        the remaining 95% of traffic will be routed to function version 1.

        :default: No additional versions

        :stability: experimental
        """
        result = self._values.get("additional_versions")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) Description for the alias.

        :default: No description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def provisioned_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) Specifies a provisioned concurrency configuration for a function's alias.

        :default: No provisioned concurrency

        :stability: experimental
        """
        result = self._values.get("provisioned_concurrent_executions")
        return result

    @builtins.property
    def alias_name(self) -> builtins.str:
        """(experimental) Name of this alias.

        :stability: experimental
        """
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return result

    @builtins.property
    def version(self) -> IVersion:
        """(experimental) Function version this alias refers to.

        Use lambda.addVersion() to obtain a new lambda version to refer to.

        :stability: experimental
        """
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AssetCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.AssetCode",
):
    """(experimental) Lambda code from a local directory.

    :stability: experimental
    """

    def __init__(
        self,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.List[_IGrantable_4c5a91d1]] = None,
        source_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.List[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_49193809] = None,
        bundling: typing.Optional[_BundlingOptions_ab115a99] = None,
    ) -> None:
        """
        :param path: The path to the asset file or directory.
        :param readers: (experimental) A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param source_hash: (deprecated) Custom hash to use when identifying the specific version of the asset. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the source hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the source hash, you will need to make sure it is updated every time the source changes, or otherwise it is possible that some deployments will not be invalidated. Default: - automatically calculate source hash based on the contents of the source file or directory.
        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '
        :param asset_hash: (experimental) Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: (experimental) Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: (experimental) Bundle the asset by executing a command in a Docker container. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise

        :stability: experimental
        """
        options = _AssetOptions_bd2996da(
            readers=readers,
            source_hash=source_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
        )

        jsii.create(AssetCode, self, [path, options])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_e78e779f) -> CodeConfig:
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [scope])

    @jsii.member(jsii_name="bindToResource")
    def bind_to_resource(
        self,
        resource: _CfnResource_e0a482dc,
        *,
        resource_property: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Called after the CFN function resource has been created to allow the code class to bind to it.

        Specifically it's required to allow assets to add
        metadata for tooling like SAM CLI to be able to find their origins.

        :param resource: -
        :param resource_property: (experimental) The name of the CloudFormation property to annotate with asset metadata. Default: Code

        :stability: experimental
        """
        options = ResourceBindOptions(resource_property=resource_property)

        return jsii.invoke(self, "bindToResource", [resource, options])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(experimental) Determines whether this Code is inline code or not.

        :stability: experimental
        """
        return jsii.get(self, "isInline")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        """(experimental) The path to the asset file or directory.

        :stability: experimental
        """
        return jsii.get(self, "path")


class AssetImageCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.AssetImageCode",
):
    """(experimental) Represents an ECR image that will be constructed from the specified asset and can be bound as Lambda code.

    :stability: experimental
    """

    def __init__(
        self,
        directory: builtins.str,
        *,
        cmd: typing.Optional[typing.List[builtins.str]] = None,
        entrypoint: typing.Optional[typing.List[builtins.str]] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        repository_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.List[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
    ) -> None:
        """
        :param directory: -
        :param cmd: (experimental) Specify or override the CMD on the specified Docker image or Dockerfile. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the CMD specified in the docker image or Dockerfile.
        :param entrypoint: (experimental) Specify or override the ENTRYPOINT on the specified Docker image or Dockerfile. An ENTRYPOINT allows you to configure a container that will run as an executable. This needs to be in the 'exec form', viz., ``[ 'executable', 'param1', 'param2' ]``. Default: - use the ENTRYPOINT in the docker image or Dockerfile.
        :param build_args: (experimental) Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param file: (experimental) Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - the default ECR repository for CDK assets
        :param target: (experimental) Docker target to build to. Default: - no target
        :param extra_hash: (deprecated) Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '

        :stability: experimental
        """
        props = AssetImageCodeProps(
            cmd=cmd,
            entrypoint=entrypoint,
            build_args=build_args,
            file=file,
            repository_name=repository_name,
            target=target,
            extra_hash=extra_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
        )

        jsii.create(AssetImageCode, self, [directory, props])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_e78e779f) -> CodeConfig:
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [scope])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(experimental) Determines whether this Code is inline code or not.

        :stability: experimental
        """
        return jsii.get(self, "isInline")


class CfnParametersCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.CfnParametersCode",
):
    """(experimental) Lambda code defined using 2 CloudFormation parameters.

    Useful when you don't have access to the code of your Lambda from your CDK code, so you can't use Assets,
    and you want to deploy the Lambda in a CodePipeline, using CloudFormation Actions -
    you can fill the parameters using the {@link #assign} method.

    :stability: experimental
    """

    def __init__(
        self,
        *,
        bucket_name_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
        object_key_param: typing.Optional[_CfnParameter_3e6f99ac] = None,
    ) -> None:
        """
        :param bucket_name_param: (experimental) The CloudFormation parameter that represents the name of the S3 Bucket where the Lambda code will be located in. Must be of type 'String'. Default: a new parameter will be created
        :param object_key_param: (experimental) The CloudFormation parameter that represents the path inside the S3 Bucket where the Lambda code will be located at. Must be of type 'String'. Default: a new parameter will be created

        :stability: experimental
        """
        props = CfnParametersCodeProps(
            bucket_name_param=bucket_name_param, object_key_param=object_key_param
        )

        jsii.create(CfnParametersCode, self, [props])

    @jsii.member(jsii_name="assign")
    def assign(
        self,
        *,
        bucket_name: builtins.str,
        object_key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """(experimental) Create a parameters map from this instance's CloudFormation parameters.

        It returns a map with 2 keys that correspond to the names of the parameters defined in this Lambda code,
        and as values it contains the appropriate expressions pointing at the provided S3 location
        (most likely, obtained from a CodePipeline Artifact by calling the ``artifact.s3Location`` method).
        The result should be provided to the CloudFormation Action
        that is deploying the Stack that the Lambda with this code is part of,
        in the ``parameterOverrides`` property.

        :param bucket_name: (experimental) The name of the S3 Bucket the object is in.
        :param object_key: (experimental) The path inside the Bucket where the object is located at.
        :param object_version: (experimental) The S3 object version.

        :stability: experimental
        """
        location = _Location_cce991ca(
            bucket_name=bucket_name,
            object_key=object_key,
            object_version=object_version,
        )

        return jsii.invoke(self, "assign", [location])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_e78e779f) -> CodeConfig:
        """(experimental) Called when the lambda or layer is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: -

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [scope])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="bucketNameParam")
    def bucket_name_param(self) -> builtins.str:
        """
        :stability: experimental
        """
        return jsii.get(self, "bucketNameParam")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isInline")
    def is_inline(self) -> builtins.bool:
        """(experimental) Determines whether this Code is inline code or not.

        :stability: experimental
        """
        return jsii.get(self, "isInline")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="objectKeyParam")
    def object_key_param(self) -> builtins.str:
        """
        :stability: experimental
        """
        return jsii.get(self, "objectKeyParam")


@jsii.data_type(
    jsii_type="monocdk.aws_lambda.DockerImageFunctionProps",
    jsii_struct_bases=[FunctionOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "code": "code",
    },
)
class DockerImageFunctionProps(FunctionOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional[VersionOptions] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List[IEventSource]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List[ILayerVersion]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional[LogRetentionRetryOptions] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional[Tracing] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        code: DockerImageCode,
    ) -> None:
        """(experimental) Properties to configure a new DockerImageFunction construct.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param code: (experimental) The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.

        :stability: experimental
        """
        if isinstance(current_version_options, dict):
            current_version_options = VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {
            "code": code,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)

        :stability: experimental
        """
        result = self._values.get("max_event_age")
        return result

    @builtins.property
    def on_failure(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for failed invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_failure")
        return result

    @builtins.property
    def on_success(self) -> typing.Optional[IDestination]:
        """(experimental) The destination for successful invocations.

        :default: - no destination

        :stability: experimental
        """
        result = self._values.get("on_success")
        return result

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2

        :stability: experimental
        """
        result = self._values.get("retry_attempts")
        return result

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true

        :stability: experimental
        """
        result = self._values.get("allow_all_outbound")
        return result

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        """(experimental) Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        :stability: experimental
        """
        result = self._values.get("allow_public_subnet")
        return result

    @builtins.property
    def current_version_options(self) -> typing.Optional[VersionOptions]:
        """(experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``

        :stability: experimental
        """
        result = self._values.get("current_version_options")
        return result

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_45a01ab4]:
        """(experimental) The SQS queue to use if DLQ is enabled.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue")
        return result

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.

        :stability: experimental
        """
        result = self._values.get("dead_letter_queue_enabled")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the function.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.

        :stability: experimental
        """
        result = self._values.get("environment")
        return result

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_IKey_36930160]:
        """(experimental) The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).

        :stability: experimental
        """
        result = self._values.get("environment_encryption")
        return result

    @builtins.property
    def events(self) -> typing.Optional[typing.List[IEventSource]]:
        """(experimental) Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.

        :stability: experimental
        """
        result = self._values.get("events")
        return result

    @builtins.property
    def filesystem(self) -> typing.Optional[FileSystem]:
        """(experimental) The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem

        :stability: experimental
        """
        result = self._values.get("filesystem")
        return result

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.

        :stability: experimental
        """
        result = self._values.get("function_name")
        return result

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[_PolicyStatement_296fe8a3]]:
        """(experimental) Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.

        :stability: experimental
        """
        result = self._values.get("initial_policy")
        return result

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[ILayerVersion]]:
        """(experimental) A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by mulitple functions.

        :default: - No layers.

        :stability: experimental
        """
        result = self._values.get("layers")
        return result

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_6c560d31]:
        """(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE

        :stability: experimental
        """
        result = self._values.get("log_retention")
        return result

    @builtins.property
    def log_retention_retry_options(self) -> typing.Optional[LogRetentionRetryOptions]:
        """(experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.

        :stability: experimental
        """
        result = self._values.get("log_retention_retry_options")
        return result

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.

        :stability: experimental
        """
        result = self._values.get("log_retention_role")
        return result

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """(experimental) The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128

        :stability: experimental
        """
        result = self._values.get("memory_size")
        return result

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        """(experimental) Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling")
        return result

    @builtins.property
    def profiling_group(self) -> typing.Optional[_IProfilingGroup_418eb20c]:
        """(experimental) Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        :stability: experimental
        """
        result = self._values.get("profiling_group")
        return result

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """(experimental) The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        :stability: experimental
        """
        result = self._values.get("reserved_concurrent_executions")
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_cdbba9d3]:
        """(deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead.

        Only used if 'vpc' is supplied.

        Use securityGroups property instead.
        Function constructor will throw an error if both are specified.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroups prop, a dedicated security
        group will be created for this function.

        :deprecated: - This property is deprecated, use securityGroups instead

        :stability: deprecated
        """
        result = self._values.get("security_group")
        return result

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]]:
        """(experimental) The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.

        :stability: experimental
        """
        result = self._values.get("security_groups")
        return result

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)

        :stability: experimental
        """
        result = self._values.get("timeout")
        return result

    @builtins.property
    def tracing(self) -> typing.Optional[Tracing]:
        """(experimental) Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled

        :stability: experimental
        """
        result = self._values.get("tracing")
        return result

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_6d1f76c4]:
        """(experimental) VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.

        :default: - Function is not placed within a VPC.

        :stability: experimental
        """
        result = self._values.get("vpc")
        return result

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        """(experimental) Where to place the network interfaces within the VPC.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        :default: - the Vpc default strategy if not specified

        :stability: experimental
        """
        result = self._values.get("vpc_subnets")
        return result

    @builtins.property
    def code(self) -> DockerImageCode:
        """(experimental) The source code of your Lambda function.

        You can point to a file in an
        Amazon Simple Storage Service (Amazon S3) bucket or specify your source
        code as inline text.

        :stability: experimental
        """
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEventSourceMapping)
class EventSourceMapping(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.EventSourceMapping",
):
    """(experimental) Defines a Lambda EventSourceMapping resource.

    Usually, you won't need to define the mapping yourself. This will usually be done by
    event sources. For example, to add an SQS event source to a function::

       import { SqsEventSource } from '@aws-cdk/aws-lambda-event-sources';
       lambda.addEventSource(new SqsEventSource(sqs));

    The ``SqsEventSource`` class will automatically create the mapping, and will also
    modify the Lambda's execution role so it can consume messages from the queue.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        target: IFunction,
        event_source_arn: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_070aa057] = None,
        max_record_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IEventSourceDlq] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        starting_position: typing.Optional[StartingPosition] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param target: (experimental) The target AWS Lambda function.
        :param event_source_arn: (experimental) The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: (experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param bisect_batch_on_error: (experimental) If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: (experimental) Set to false to disable the event source upon creation. Default: true
        :param kafka_topic: (experimental) The name of the Kafka topic. Default: - no topic
        :param max_batching_window: (experimental) The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_record_age: (experimental) The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: (experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: (experimental) The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param starting_position: (experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :stability: experimental
        """
        props = EventSourceMappingProps(
            target=target,
            event_source_arn=event_source_arn,
            batch_size=batch_size,
            bisect_batch_on_error=bisect_batch_on_error,
            enabled=enabled,
            kafka_topic=kafka_topic,
            max_batching_window=max_batching_window,
            max_record_age=max_record_age,
            on_failure=on_failure,
            parallelization_factor=parallelization_factor,
            retry_attempts=retry_attempts,
            starting_position=starting_position,
        )

        jsii.create(EventSourceMapping, self, [scope, id, props])

    @jsii.member(jsii_name="fromEventSourceMappingId")
    @builtins.classmethod
    def from_event_source_mapping_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        event_source_mapping_id: builtins.str,
    ) -> IEventSourceMapping:
        """(experimental) Import an event source into this stack from its event source id.

        :param scope: -
        :param id: -
        :param event_source_mapping_id: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromEventSourceMappingId", [scope, id, event_source_mapping_id])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="eventSourceMappingId")
    def event_source_mapping_id(self) -> builtins.str:
        """(experimental) The identifier for this EventSourceMapping.

        :stability: experimental
        """
        return jsii.get(self, "eventSourceMappingId")


@jsii.implements(IFunction)
class FunctionBase(
    _Resource_abff4495,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_lambda.FunctionBase",
):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _FunctionBaseProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param account: (experimental) The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param physical_name: (experimental) The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: (experimental) The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to

        :stability: experimental
        """
        props = _ResourceProps_9b554c0f(
            account=account, physical_name=physical_name, region=region
        )

        jsii.create(FunctionBase, self, [scope, id, props])

    @jsii.member(jsii_name="addEventSource")
    def add_event_source(self, source: IEventSource) -> None:
        """(experimental) Adds an event source to this function.

        Event sources are implemented in the @aws-cdk/aws-lambda-event-sources module.

        The following example adds an SQS Queue as an event source::

           import { SqsEventSource } from '@aws-cdk/aws-lambda-event-sources';
           myFunction.addEventSource(new SqsEventSource(myQueue));

        :param source: -

        :stability: experimental
        """
        return jsii.invoke(self, "addEventSource", [source])

    @jsii.member(jsii_name="addEventSourceMapping")
    def add_event_source_mapping(
        self,
        id: builtins.str,
        *,
        event_source_arn: builtins.str,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_070aa057] = None,
        max_record_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IEventSourceDlq] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        starting_position: typing.Optional[StartingPosition] = None,
    ) -> EventSourceMapping:
        """(experimental) Adds an event source that maps to this AWS Lambda function.

        :param id: -
        :param event_source_arn: (experimental) The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: (experimental) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param bisect_batch_on_error: (experimental) If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: (experimental) Set to false to disable the event source upon creation. Default: true
        :param kafka_topic: (experimental) The name of the Kafka topic. Default: - no topic
        :param max_batching_window: (experimental) The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_record_age: (experimental) The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: (experimental) An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: (experimental) The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param starting_position: (experimental) The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis, Amazon DynamoDB, and Amazon MSK Streams sources.

        :stability: experimental
        """
        options = EventSourceMappingOptions(
            event_source_arn=event_source_arn,
            batch_size=batch_size,
            bisect_batch_on_error=bisect_batch_on_error,
            enabled=enabled,
            kafka_topic=kafka_topic,
            max_batching_window=max_batching_window,
            max_record_age=max_record_age,
            on_failure=on_failure,
            parallelization_factor=parallelization_factor,
            retry_attempts=retry_attempts,
            starting_position=starting_position,
        )

        return jsii.invoke(self, "addEventSourceMapping", [id, options])

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        principal: _IPrincipal_93b48231,
        action: typing.Optional[builtins.str] = None,
        event_source_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[_Construct_e78e779f] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Adds a permission to the Lambda resource policy.

        :param id: The id ƒor the permission construct.
        :param principal: (experimental) The entity for which you are granting permission to invoke the Lambda function. This entity can be any valid AWS service principal, such as s3.amazonaws.com or sns.amazonaws.com, or, if you are granting cross-account permission, an AWS account ID. For example, you might want to allow a custom application in another AWS account to push events to Lambda by invoking your function. The principal can be either an AccountPrincipal or a ServicePrincipal.
        :param action: (experimental) The Lambda actions that you want to allow in this statement. For example, you can specify lambda:CreateFunction to specify a certain action, or use a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a list of actions, see Actions and Condition Context Keys for AWS Lambda in the IAM User Guide. Default: 'lambda:InvokeFunction'
        :param event_source_token: (experimental) A unique token that must be supplied by the principal invoking the function. Default: The caller would not need to present a token.
        :param scope: (experimental) The scope to which the permission constructs be attached. The default is the Lambda function construct itself, but this would need to be different in cases such as cross-stack references where the Permissions would need to sit closer to the consumer of this permission (i.e., the caller). Default: - The instance of lambda.IFunction
        :param source_account: (experimental) The AWS account ID (without hyphens) of the source owner. For example, if you specify an S3 bucket in the SourceArn property, this value is the bucket owner's account ID. You can use this property to ensure that all source principals are owned by a specific account.
        :param source_arn: (experimental) The ARN of a resource that is invoking your function. When granting Amazon Simple Storage Service (Amazon S3) permission to invoke your function, specify this property with the bucket ARN as its value. This ensures that events generated only from the specified bucket, not just any bucket from any AWS account that creates a mapping to your function, can invoke the function.

        :see: Permission for details.
        :stability: experimental
        """
        permission = Permission(
            principal=principal,
            action=action,
            event_source_token=event_source_token,
            scope=scope,
            source_account=source_account,
            source_arn=source_arn,
        )

        return jsii.invoke(self, "addPermission", [id, permission])

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_296fe8a3) -> None:
        """(experimental) Adds a statement to the IAM role assumed by the instance.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToRolePolicy", [statement])

    @jsii.member(jsii_name="configureAsyncInvoke")
    def configure_async_invoke(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Configures options for asynchronous invocation.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        options = EventInvokeConfigOptions(
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return jsii.invoke(self, "configureAsyncInvoke", [options])

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        """(experimental) Grant the given identity permissions to invoke this Lambda.

        :param grantee: -

        :stability: experimental
        """
        return jsii.invoke(self, "grantInvoke", [grantee])

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Return the given named metric for this Function.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricDuration")
    def metric_duration(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) How long execution of this Lambda takes.

        Average over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricDuration", [props])

    @jsii.member(jsii_name="metricErrors")
    def metric_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) How many invocations of this Lambda fail.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricErrors", [props])

    @jsii.member(jsii_name="metricInvocations")
    def metric_invocations(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) How often this Lambda is invoked.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricInvocations", [props])

    @jsii.member(jsii_name="metricThrottles")
    def metric_throttles(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) How often this Lambda is throttled.

        Sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metricThrottles", [props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="canCreatePermissions")
    @abc.abstractmethod
    def _can_create_permissions(self) -> builtins.bool:
        """(experimental) Whether the addPermission() call adds any permissions.

        True for new Lambdas, false for version $LATEST and imported Lambdas
        from different accounts.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_57ccbda9:
        """(experimental) Access the Connections object.

        Will fail if not a VPC-enabled Lambda Function

        :stability: experimental
        """
        return jsii.get(self, "connections")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    @abc.abstractmethod
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN fo the function.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    @abc.abstractmethod
    def function_name(self) -> builtins.str:
        """(experimental) The name of the function.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    @abc.abstractmethod
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) The principal this Lambda Function is running as.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isBoundToVpc")
    def is_bound_to_vpc(self) -> builtins.bool:
        """(experimental) Whether or not this Lambda function was bound to a VPC.

        If this is is ``false``, trying to access the ``connections`` object will fail.

        :stability: experimental
        """
        return jsii.get(self, "isBoundToVpc")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> IVersion:
        """(experimental) The ``$LATEST`` version of this function.

        Note that this is reference to a non-specific AWS Lambda version, which
        means the function this version refers to can return different results in
        different invocations.

        To obtain a reference to an explicit version which references the current
        function configuration, use ``lambdaFunction.currentVersion`` instead.

        :stability: experimental
        """
        return jsii.get(self, "latestVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    @abc.abstractmethod
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    @abc.abstractmethod
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        Undefined if the function was imported without a role.

        :stability: experimental
        """
        ...


class _FunctionBaseProxy(
    FunctionBase, jsii.proxy_for(_Resource_abff4495) # type: ignore
):
    @builtins.property # type: ignore
    @jsii.member(jsii_name="canCreatePermissions")
    def _can_create_permissions(self) -> builtins.bool:
        """(experimental) Whether the addPermission() call adds any permissions.

        True for new Lambdas, false for version $LATEST and imported Lambdas
        from different accounts.

        :stability: experimental
        """
        return jsii.get(self, "canCreatePermissions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN fo the function.

        :stability: experimental
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) The name of the function.

        :stability: experimental
        """
        return jsii.get(self, "functionName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) The principal this Lambda Function is running as.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        return jsii.get(self, "permissionsNode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        Undefined if the function was imported without a role.

        :stability: experimental
        """
        return jsii.get(self, "role")


@jsii.interface(jsii_type="monocdk.aws_lambda.IAlias")
class IAlias(IFunction, typing_extensions.Protocol):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAliasProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        """(experimental) Name of this alias.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="version")
    def version(self) -> IVersion:
        """(experimental) The underlying Lambda function version.

        :stability: experimental
        """
        ...


class _IAliasProxy(
    jsii.proxy_for(IFunction) # type: ignore
):
    """
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_lambda.IAlias"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        """(experimental) Name of this alias.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "aliasName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="version")
    def version(self) -> IVersion:
        """(experimental) The underlying Lambda function version.

        :stability: experimental
        """
        return jsii.get(self, "version")


class QualifiedFunctionBase(
    FunctionBase,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_lambda.QualifiedFunctionBase",
):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _QualifiedFunctionBaseProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param account: (experimental) The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param physical_name: (experimental) The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: (experimental) The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to

        :stability: experimental
        """
        props = _ResourceProps_9b554c0f(
            account=account, physical_name=physical_name, region=region
        )

        jsii.create(QualifiedFunctionBase, self, [scope, id, props])

    @jsii.member(jsii_name="configureAsyncInvoke")
    def configure_async_invoke(
        self,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Configures options for asynchronous invocation.

        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        options = EventInvokeConfigOptions(
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return jsii.invoke(self, "configureAsyncInvoke", [options])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambda")
    @abc.abstractmethod
    def lambda_(self) -> IFunction:
        """
        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> IVersion:
        """(experimental) The ``$LATEST`` version of this function.

        Note that this is reference to a non-specific AWS Lambda version, which
        means the function this version refers to can return different results in
        different invocations.

        To obtain a reference to an explicit version which references the current
        function configuration, use ``lambdaFunction.currentVersion`` instead.

        :stability: experimental
        """
        return jsii.get(self, "latestVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        return jsii.get(self, "permissionsNode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="qualifier")
    @abc.abstractmethod
    def _qualifier(self) -> builtins.str:
        """(experimental) The qualifier of the version or alias of this function.

        A qualifier is the identifier that's appended to a version or alias ARN.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#API_GetFunctionConfiguration_RequestParameters
        :stability: experimental
        """
        ...


class _QualifiedFunctionBaseProxy(
    QualifiedFunctionBase, jsii.proxy_for(FunctionBase) # type: ignore
):
    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> IFunction:
        """
        :stability: experimental
        """
        return jsii.get(self, "lambda")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="qualifier")
    def _qualifier(self) -> builtins.str:
        """(experimental) The qualifier of the version or alias of this function.

        A qualifier is the identifier that's appended to a version or alias ARN.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#API_GetFunctionConfiguration_RequestParameters
        :stability: experimental
        """
        return jsii.get(self, "qualifier")


class SingletonFunction(
    FunctionBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.SingletonFunction",
):
    """(experimental) A Lambda that will only ever be added to a stack once.

    This construct is a way to guarantee that the lambda function will be guaranteed to be part of the stack,
    once and only once, irrespective of how many times the construct is declared to be part of the stack.
    This is guaranteed as long as the ``uuid`` property and the optional ``lambdaPurpose`` property stay the same
    whenever they're declared into the stack.

    :stability: experimental
    :resource: AWS::Lambda::Function
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        uuid: builtins.str,
        lambda_purpose: typing.Optional[builtins.str] = None,
        code: Code,
        handler: builtins.str,
        runtime: Runtime,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional[VersionOptions] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List[IEventSource]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List[ILayerVersion]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional[LogRetentionRetryOptions] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional[Tracing] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param uuid: (experimental) A unique identifier to identify this lambda. The identifier should be unique across all custom resource providers. We recommend generating a UUID per provider.
        :param lambda_purpose: (experimental) A descriptive name for the purpose of this Lambda. If the Lambda does not have a physical name, this string will be reflected its generated name. The combination of lambdaPurpose and uuid must be unique. Default: SingletonLambda
        :param code: (experimental) The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: (experimental) The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: (experimental) The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        props = SingletonFunctionProps(
            uuid=uuid,
            lambda_purpose=lambda_purpose,
            code=code,
            handler=handler,
            runtime=runtime,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            security_group=security_group,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(SingletonFunction, self, [scope, id, props])

    @jsii.member(jsii_name="addDependency")
    def add_dependency(self, *up: _IDependable_1175c9f7) -> None:
        """(experimental) Using node.addDependency() does not work on this method as the underlying lambda function is modeled as a singleton across the stack. Use this method instead to declare dependencies.

        :param up: -

        :stability: experimental
        """
        return jsii.invoke(self, "addDependency", [*up])

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        name: builtins.str,
        *,
        principal: _IPrincipal_93b48231,
        action: typing.Optional[builtins.str] = None,
        event_source_token: typing.Optional[builtins.str] = None,
        scope: typing.Optional[_Construct_e78e779f] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Adds a permission to the Lambda resource policy.

        :param name: -
        :param principal: (experimental) The entity for which you are granting permission to invoke the Lambda function. This entity can be any valid AWS service principal, such as s3.amazonaws.com or sns.amazonaws.com, or, if you are granting cross-account permission, an AWS account ID. For example, you might want to allow a custom application in another AWS account to push events to Lambda by invoking your function. The principal can be either an AccountPrincipal or a ServicePrincipal.
        :param action: (experimental) The Lambda actions that you want to allow in this statement. For example, you can specify lambda:CreateFunction to specify a certain action, or use a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a list of actions, see Actions and Condition Context Keys for AWS Lambda in the IAM User Guide. Default: 'lambda:InvokeFunction'
        :param event_source_token: (experimental) A unique token that must be supplied by the principal invoking the function. Default: The caller would not need to present a token.
        :param scope: (experimental) The scope to which the permission constructs be attached. The default is the Lambda function construct itself, but this would need to be different in cases such as cross-stack references where the Permissions would need to sit closer to the consumer of this permission (i.e., the caller). Default: - The instance of lambda.IFunction
        :param source_account: (experimental) The AWS account ID (without hyphens) of the source owner. For example, if you specify an S3 bucket in the SourceArn property, this value is the bucket owner's account ID. You can use this property to ensure that all source principals are owned by a specific account.
        :param source_arn: (experimental) The ARN of a resource that is invoking your function. When granting Amazon Simple Storage Service (Amazon S3) permission to invoke your function, specify this property with the bucket ARN as its value. This ensures that events generated only from the specified bucket, not just any bucket from any AWS account that creates a mapping to your function, can invoke the function.

        :stability: experimental
        """
        permission = Permission(
            principal=principal,
            action=action,
            event_source_token=event_source_token,
            scope=scope,
            source_account=source_account,
            source_arn=source_arn,
        )

        return jsii.invoke(self, "addPermission", [name, permission])

    @jsii.member(jsii_name="dependOn")
    def depend_on(self, down: _IConstruct_5a0f9c5e) -> None:
        """(experimental) The SingletonFunction construct cannot be added as a dependency of another construct using node.addDependency(). Use this method instead to declare this as a dependency of another construct.

        :param down: -

        :stability: experimental
        """
        return jsii.invoke(self, "dependOn", [down])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="canCreatePermissions")
    def _can_create_permissions(self) -> builtins.bool:
        """(experimental) Whether the addPermission() call adds any permissions.

        True for new Lambdas, false for version $LATEST and imported Lambdas
        from different accounts.

        :stability: experimental
        """
        return jsii.get(self, "canCreatePermissions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> "Version":
        """(experimental) Returns a ``lambda.Version`` which represents the current version of this singleton Lambda function. A new version will be created every time the function's configuration changes.

        You can specify options for this version using the ``currentVersionOptions``
        prop when initializing the ``lambda.SingletonFunction``.

        :stability: experimental
        """
        return jsii.get(self, "currentVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN fo the function.

        :stability: experimental
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) The name of the function.

        :stability: experimental
        """
        return jsii.get(self, "functionName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) The principal this Lambda Function is running as.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        return jsii.get(self, "permissionsNode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        Undefined if the function was imported without a role.

        :stability: experimental
        """
        return jsii.get(self, "role")


@jsii.implements(IVersion)
class Version(
    QualifiedFunctionBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.Version",
):
    """(experimental) A single newly-deployed version of a Lambda function.

    This object exists to--at deploy time--query the "then-current" version of
    the Lambda function that it refers to. This Version object can then be
    used in ``Alias`` to refer to a particular deployment of a Lambda.

    This means that for every new update you deploy to your Lambda (using the
    CDK and Aliases), you must always create a new Version object. In
    particular, it must have a different name, so that a new resource is
    created.

    If you want to ensure that you're associating the right version with
    the right deployment, specify the ``codeSha256`` property while
    creating the `Version.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        lambda_: IFunction,
        code_sha256: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param lambda_: (experimental) Function to get the value of.
        :param code_sha256: (experimental) SHA256 of the version of the Lambda source code. Specify to validate that you're deploying the right version. Default: No validation is performed
        :param description: (experimental) Description of the version. Default: Description of the Lambda
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's version. Default: No provisioned concurrency
        :param removal_policy: (experimental) Whether to retain old versions of this function when a new version is created. Default: RemovalPolicy.DESTROY
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        props = VersionProps(
            lambda_=lambda_,
            code_sha256=code_sha256,
            description=description,
            provisioned_concurrent_executions=provisioned_concurrent_executions,
            removal_policy=removal_policy,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(Version, self, [scope, id, props])

    @jsii.member(jsii_name="fromVersionArn")
    @builtins.classmethod
    def from_version_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        version_arn: builtins.str,
    ) -> IVersion:
        """(experimental) Construct a Version object from a Version ARN.

        :param scope: The cdk scope creating this resource.
        :param id: The cdk id of this resource.
        :param version_arn: The version ARN to create this version from.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromVersionArn", [scope, id, version_arn])

    @jsii.member(jsii_name="fromVersionAttributes")
    @builtins.classmethod
    def from_version_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        lambda_: IFunction,
        version: builtins.str,
    ) -> IVersion:
        """
        :param scope: -
        :param id: -
        :param lambda_: (experimental) The lambda function.
        :param version: (experimental) The version.

        :stability: experimental
        """
        attrs = VersionAttributes(lambda_=lambda_, version=version)

        return jsii.sinvoke(cls, "fromVersionAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addAlias")
    def add_alias(
        self,
        alias_name: builtins.str,
        *,
        additional_versions: typing.Optional[typing.List[VersionWeight]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> "Alias":
        """(experimental) Defines an alias for this version.

        :param alias_name: The name of the alias (e.g. "live").
        :param additional_versions: (experimental) Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is Example:: version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: (experimental) Description for the alias. Default: No description
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        options = AliasOptions(
            additional_versions=additional_versions,
            description=description,
            provisioned_concurrent_executions=provisioned_concurrent_executions,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return jsii.invoke(self, "addAlias", [alias_name, options])

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Return the given named metric for this Function.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metric", [metric_name, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="canCreatePermissions")
    def _can_create_permissions(self) -> builtins.bool:
        """(experimental) Whether the addPermission() call adds any permissions.

        True for new Lambdas, false for version $LATEST and imported Lambdas
        from different accounts.

        :stability: experimental
        """
        return jsii.get(self, "canCreatePermissions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="edgeArn")
    def edge_arn(self) -> builtins.str:
        """(experimental) The ARN of the version for Lambda@Edge.

        :stability: experimental
        """
        return jsii.get(self, "edgeArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) The ARN fo the function.

        :stability: experimental
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) The name of the function.

        :stability: experimental
        """
        return jsii.get(self, "functionName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) The principal this Lambda Function is running as.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> IFunction:
        """(experimental) The underlying AWS Lambda function.

        :stability: experimental
        """
        return jsii.get(self, "lambda")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="qualifier")
    def _qualifier(self) -> builtins.str:
        """(experimental) The qualifier of the version or alias of this function.

        A qualifier is the identifier that's appended to a version or alias ARN.

        :stability: experimental
        """
        return jsii.get(self, "qualifier")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        """(experimental) The most recently deployed version of this function.

        :stability: experimental
        """
        return jsii.get(self, "version")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        Undefined if the function was imported without a role.

        :stability: experimental
        """
        return jsii.get(self, "role")


@jsii.implements(IAlias)
class Alias(
    QualifiedFunctionBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.Alias",
):
    """(experimental) A new alias to a particular version of a Lambda function.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
        version: IVersion,
        additional_versions: typing.Optional[typing.List[VersionWeight]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param alias_name: (experimental) Name of this alias.
        :param version: (experimental) Function version this alias refers to. Use lambda.addVersion() to obtain a new lambda version to refer to.
        :param additional_versions: (experimental) Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is Example:: version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: (experimental) Description for the alias. Default: No description
        :param provisioned_concurrent_executions: (experimental) Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        props = AliasProps(
            alias_name=alias_name,
            version=version,
            additional_versions=additional_versions,
            description=description,
            provisioned_concurrent_executions=provisioned_concurrent_executions,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(Alias, self, [scope, id, props])

    @jsii.member(jsii_name="fromAliasAttributes")
    @builtins.classmethod
    def from_alias_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
        alias_version: IVersion,
    ) -> IAlias:
        """
        :param scope: -
        :param id: -
        :param alias_name: 
        :param alias_version: 

        :stability: experimental
        """
        attrs = AliasAttributes(alias_name=alias_name, alias_version=alias_version)

        return jsii.sinvoke(cls, "fromAliasAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addAutoScaling")
    def add_auto_scaling(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> IScalableFunctionAttribute:
        """(experimental) Configure provisioned concurrency autoscaling on a function alias.

        Returns a scalable attribute that can call
        ``scaleOnUtilization()`` and ``scaleOnSchedule()``.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1

        :stability: experimental
        """
        options = AutoScalingOptions(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return jsii.invoke(self, "addAutoScaling", [options])

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Return the given named metric for this Function.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.invoke(self, "metric", [metric_name, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        """(experimental) Name of this alias.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "aliasName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="canCreatePermissions")
    def _can_create_permissions(self) -> builtins.bool:
        """(experimental) Whether the addPermission() call adds any permissions.

        True for new Lambdas, false for version $LATEST and imported Lambdas
        from different accounts.

        :stability: experimental
        """
        return jsii.get(self, "canCreatePermissions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) ARN of this alias.

        Used to be able to use Alias in place of a regular Lambda. Lambda accepts
        ARNs everywhere it accepts function names.

        :stability: experimental
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) ARN of this alias.

        Used to be able to use Alias in place of a regular Lambda. Lambda accepts
        ARNs everywhere it accepts function names.

        :stability: experimental
        """
        return jsii.get(self, "functionName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) The principal this Lambda Function is running as.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> IFunction:
        """
        :stability: experimental
        """
        return jsii.get(self, "lambda")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="qualifier")
    def _qualifier(self) -> builtins.str:
        """(experimental) The qualifier of the version or alias of this function.

        A qualifier is the identifier that's appended to a version or alias ARN.

        :stability: experimental
        """
        return jsii.get(self, "qualifier")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="version")
    def version(self) -> IVersion:
        """(experimental) The underlying Lambda function version.

        :stability: experimental
        """
        return jsii.get(self, "version")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM role associated with this function.

        Undefined if the function was imported without a role.

        :stability: experimental
        """
        return jsii.get(self, "role")


class Function(
    FunctionBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.Function",
):
    """(experimental) Deploys a file from from inside the construct library as a function.

    The supplied file is subject to the 4096 bytes limit of being embedded in a
    CloudFormation template.

    The construct includes an associated role with the lambda.

    This construct does not yet reproduce all features from the underlying resource
    library.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        code: Code,
        handler: builtins.str,
        runtime: Runtime,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional[VersionOptions] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List[IEventSource]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List[ILayerVersion]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional[LogRetentionRetryOptions] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional[Tracing] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param code: (experimental) The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: (experimental) The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: (experimental) The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when when defining a function from a Docker image.
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        props = FunctionProps(
            code=code,
            handler=handler,
            runtime=runtime,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            security_group=security_group,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(Function, self, [scope, id, props])

    @jsii.member(jsii_name="fromFunctionArn")
    @builtins.classmethod
    def from_function_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        function_arn: builtins.str,
    ) -> IFunction:
        """
        :param scope: -
        :param id: -
        :param function_arn: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromFunctionArn", [scope, id, function_arn])

    @jsii.member(jsii_name="fromFunctionAttributes")
    @builtins.classmethod
    def from_function_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        function_arn: builtins.str,
        role: typing.Optional[_IRole_59af6f50] = None,
        same_environment: typing.Optional[builtins.bool] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_group_id: typing.Optional[builtins.str] = None,
    ) -> IFunction:
        """(experimental) Creates a Lambda function object which represents a function not defined within this stack.

        :param scope: The parent construct.
        :param id: The name of the lambda construct.
        :param function_arn: (experimental) The ARN of the Lambda function. Format: arn::lambda:::function:
        :param role: (experimental) The IAM execution role associated with this function. If the role is not specified, any role-related operations will no-op.
        :param same_environment: (experimental) Setting this property informs the CDK that the imported function is in the same environment as the stack. This affects certain behaviours such as, whether this function's permission can be modified. When not configured, the CDK attempts to auto-determine this. For environment agnostic stacks, i.e., stacks where the account is not specified with the ``env`` property, this is determined to be false. Set this to property *ONLY IF* the imported function is in the same account as the stack it's imported in. Default: - depends: true, if the Stack is configured with an explicit ``env`` (account and region) and the account is the same as this function. For environment-agnostic stacks this will default to ``false``.
        :param security_group: (experimental) The security group of this Lambda, if in a VPC. This needs to be given in order to support allowing connections to this Lambda.
        :param security_group_id: (deprecated) Id of the security group of this Lambda, if in a VPC. This needs to be given in order to support allowing connections to this Lambda.

        :stability: experimental
        """
        attrs = FunctionAttributes(
            function_arn=function_arn,
            role=role,
            same_environment=same_environment,
            security_group=security_group,
            security_group_id=security_group_id,
        )

        return jsii.sinvoke(cls, "fromFunctionAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="metricAll")
    @builtins.classmethod
    def metric_all(
        cls,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Return the given named metric for this Lambda.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAll", [metric_name, props])

    @jsii.member(jsii_name="metricAllConcurrentExecutions")
    @builtins.classmethod
    def metric_all_concurrent_executions(
        cls,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of concurrent executions across all Lambdas.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: max over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAllConcurrentExecutions", [props])

    @jsii.member(jsii_name="metricAllDuration")
    @builtins.classmethod
    def metric_all_duration(
        cls,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the Duration executing all Lambdas.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAllDuration", [props])

    @jsii.member(jsii_name="metricAllErrors")
    @builtins.classmethod
    def metric_all_errors(
        cls,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of Errors executing all Lambdas.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAllErrors", [props])

    @jsii.member(jsii_name="metricAllInvocations")
    @builtins.classmethod
    def metric_all_invocations(
        cls,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of invocations of all Lambdas.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAllInvocations", [props])

    @jsii.member(jsii_name="metricAllThrottles")
    @builtins.classmethod
    def metric_all_throttles(
        cls,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of throttled invocations of all Lambdas.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAllThrottles", [props])

    @jsii.member(jsii_name="metricAllUnreservedConcurrentExecutions")
    @builtins.classmethod
    def metric_all_unreserved_concurrent_executions(
        cls,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        """(experimental) Metric for the number of unreserved concurrent executions across all Lambdas.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: max over 5 minutes

        :stability: experimental
        """
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return jsii.sinvoke(cls, "metricAllUnreservedConcurrentExecutions", [props])

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(
        self,
        key: builtins.str,
        value: builtins.str,
        *,
        remove_in_edge: typing.Optional[builtins.bool] = None,
    ) -> "Function":
        """(experimental) Adds an environment variable to this Lambda function.

        If this is a ref to a Lambda function, this operation results in a no-op.

        :param key: The environment variable key.
        :param value: The environment variable's value.
        :param remove_in_edge: (experimental) When used in Lambda@Edge via edgeArn() API, these environment variables will be removed. If not set, an error will be thrown. Default: false - using the function in Lambda

        :stability: experimental
        """
        options = EnvironmentOptions(remove_in_edge=remove_in_edge)

        return jsii.invoke(self, "addEnvironment", [key, value, options])

    @jsii.member(jsii_name="addLayers")
    def add_layers(self, *layers: ILayerVersion) -> None:
        """(experimental) Adds one or more Lambda Layers to this Lambda function.

        :param layers: the layers to be added.

        :stability: experimental
        :throws: if there are already 5 layers on this function, or the layer is incompatible with this function's runtime.
        """
        return jsii.invoke(self, "addLayers", [*layers])

    @jsii.member(jsii_name="addVersion")
    def add_version(
        self,
        name: builtins.str,
        code_sha256: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_executions: typing.Optional[jsii.Number] = None,
        *,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> Version:
        """(deprecated) Add a new version for this Lambda.

        If you want to deploy through CloudFormation and use aliases, you need to
        add a new version (with a new name) to your Lambda every time you want to
        deploy an update. An alias can then refer to the newly created Version.

        All versions should have distinct names, and you should not delete versions
        as long as your Alias needs to refer to them.

        :param name: A unique name for this version.
        :param code_sha256: The SHA-256 hash of the most recently deployed Lambda source code, or omit to skip validation.
        :param description: A description for this version.
        :param provisioned_executions: A provisioned concurrency configuration for a function's version.
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :return: A new Version object.

        :deprecated:

        This method will create an AWS::Lambda::Version resource which
        snapshots the AWS Lambda function *at the time of its creation* and it
        won't get updated when the function changes. Instead, use
        ``this.currentVersion`` to obtain a reference to a version resource that gets
        automatically recreated when the function configuration (or code) changes.

        :stability: deprecated
        """
        async_invoke_config = EventInvokeConfigOptions(
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return jsii.invoke(self, "addVersion", [name, code_sha256, description, provisioned_executions, async_invoke_config])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="canCreatePermissions")
    def _can_create_permissions(self) -> builtins.bool:
        """(experimental) Whether the addPermission() call adds any permissions.

        True for new Lambdas, false for version $LATEST and imported Lambdas
        from different accounts.

        :stability: experimental
        """
        return jsii.get(self, "canCreatePermissions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> Version:
        """(experimental) Returns a ``lambda.Version`` which represents the current version of this Lambda function. A new version will be created every time the function's configuration changes.

        You can specify options for this version using the ``currentVersionOptions``
        prop when initializing the ``lambda.Function``.

        :stability: experimental
        """
        return jsii.get(self, "currentVersion")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) ARN of this function.

        :stability: experimental
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) Name of this function.

        :stability: experimental
        """
        return jsii.get(self, "functionName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) The principal this Lambda Function is running as.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> _ILogGroup_846e17a0:
        """(experimental) The LogGroup where the Lambda function's logs are made available.

        If either ``logRetention`` is set or this property is called, a CloudFormation custom resource is added to the stack that
        pre-creates the log group as part of the stack deployment, if it already doesn't exist, and sets the correct log retention
        period (never expire, by default).

        Further, if the log group already exists and the ``logRetention`` is not set, the custom resource will reset the log retention
        to never expire even if it was configured with a different value.

        :stability: experimental
        """
        return jsii.get(self, "logGroup")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _ConstructNode_33e3628c:
        """(experimental) The construct node where permissions are attached.

        :stability: experimental
        """
        return jsii.get(self, "permissionsNode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> Runtime:
        """(experimental) The runtime configured for this lambda.

        :stability: experimental
        """
        return jsii.get(self, "runtime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="deadLetterQueue")
    def dead_letter_queue(self) -> typing.Optional[_IQueue_45a01ab4]:
        """(experimental) The DLQ associated with this Lambda Function (this is an optional attribute).

        :stability: experimental
        """
        return jsii.get(self, "deadLetterQueue")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) Execution role associated with this function.

        :stability: experimental
        """
        return jsii.get(self, "role")


class DockerImageFunction(
    Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lambda.DockerImageFunction",
):
    """(experimental) Create a lambda function where the handler is a docker image.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        code: DockerImageCode,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        current_version_options: typing.Optional[VersionOptions] = None,
        dead_letter_queue: typing.Optional[_IQueue_45a01ab4] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_36930160] = None,
        events: typing.Optional[typing.List[IEventSource]] = None,
        filesystem: typing.Optional[FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.List[_PolicyStatement_296fe8a3]] = None,
        layers: typing.Optional[typing.List[ILayerVersion]] = None,
        log_retention: typing.Optional[_RetentionDays_6c560d31] = None,
        log_retention_retry_options: typing.Optional[LogRetentionRetryOptions] = None,
        log_retention_role: typing.Optional[_IRole_59af6f50] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_418eb20c] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        security_group: typing.Optional[_ISecurityGroup_cdbba9d3] = None,
        security_groups: typing.Optional[typing.List[_ISecurityGroup_cdbba9d3]] = None,
        timeout: typing.Optional[_Duration_070aa057] = None,
        tracing: typing.Optional[Tracing] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        max_event_age: typing.Optional[_Duration_070aa057] = None,
        on_failure: typing.Optional[IDestination] = None,
        on_success: typing.Optional[IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param code: (experimental) The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param allow_all_outbound: (experimental) Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: (experimental) Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param current_version_options: (experimental) Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: (experimental) The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: (experimental) Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: (experimental) A description of the function. Default: - No description.
        :param environment: (experimental) Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: (experimental) The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param events: (experimental) Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: (experimental) The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: (experimental) A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: (experimental) Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: (experimental) A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: (experimental) When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: (experimental) Enable profiling. Default: - No profiling.
        :param profiling_group: (experimental) Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: (experimental) The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: (experimental) Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: (deprecated) What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: (experimental) The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: (experimental) Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: (experimental) VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: (experimental) Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified
        :param max_event_age: (experimental) The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: (experimental) The destination for failed invocations. Default: - no destination
        :param on_success: (experimental) The destination for successful invocations. Default: - no destination
        :param retry_attempts: (experimental) The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        """
        props = DockerImageFunctionProps(
            code=code,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            security_group=security_group,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(DockerImageFunction, self, [scope, id, props])


__all__ = [
    "Alias",
    "AliasAttributes",
    "AliasOptions",
    "AliasProps",
    "AssetCode",
    "AssetImageCode",
    "AssetImageCodeProps",
    "AutoScalingOptions",
    "CfnAlias",
    "CfnAliasProps",
    "CfnCodeSigningConfig",
    "CfnCodeSigningConfigProps",
    "CfnEventInvokeConfig",
    "CfnEventInvokeConfigProps",
    "CfnEventSourceMapping",
    "CfnEventSourceMappingProps",
    "CfnFunction",
    "CfnFunctionProps",
    "CfnLayerVersion",
    "CfnLayerVersionPermission",
    "CfnLayerVersionPermissionProps",
    "CfnLayerVersionProps",
    "CfnParametersCode",
    "CfnParametersCodeProps",
    "CfnPermission",
    "CfnPermissionProps",
    "CfnVersion",
    "CfnVersionProps",
    "Code",
    "CodeConfig",
    "CodeImageConfig",
    "DestinationConfig",
    "DestinationOptions",
    "DestinationType",
    "DlqDestinationConfig",
    "DockerImageCode",
    "DockerImageFunction",
    "DockerImageFunctionProps",
    "EcrImageCode",
    "EcrImageCodeProps",
    "EnvironmentOptions",
    "EventInvokeConfig",
    "EventInvokeConfigOptions",
    "EventInvokeConfigProps",
    "EventSourceMapping",
    "EventSourceMappingOptions",
    "EventSourceMappingProps",
    "FileSystem",
    "FileSystemConfig",
    "Function",
    "FunctionAttributes",
    "FunctionBase",
    "FunctionOptions",
    "FunctionProps",
    "Handler",
    "IAlias",
    "IDestination",
    "IEventSource",
    "IEventSourceDlq",
    "IEventSourceMapping",
    "IFunction",
    "ILayerVersion",
    "IScalableFunctionAttribute",
    "IVersion",
    "InlineCode",
    "LambdaRuntimeProps",
    "LayerVersion",
    "LayerVersionAttributes",
    "LayerVersionOptions",
    "LayerVersionPermission",
    "LayerVersionProps",
    "LogRetention",
    "LogRetentionProps",
    "LogRetentionRetryOptions",
    "Permission",
    "QualifiedFunctionBase",
    "ResourceBindOptions",
    "Runtime",
    "RuntimeFamily",
    "S3Code",
    "SingletonFunction",
    "SingletonFunctionProps",
    "StartingPosition",
    "Tracing",
    "UtilizationScalingOptions",
    "Version",
    "VersionAttributes",
    "VersionOptions",
    "VersionProps",
    "VersionWeight",
]

publication.publish()
