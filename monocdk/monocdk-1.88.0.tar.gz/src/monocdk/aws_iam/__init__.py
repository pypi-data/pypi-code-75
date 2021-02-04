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
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    IConstruct as _IConstruct_5a0f9c5e,
    IDependable as _IDependable_1175c9f7,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResolveContext as _IResolveContext_e363e2cb,
    IResource as _IResource_8c1dbbbd,
    Resource as _Resource_abff4495,
    SecretValue as _SecretValue_c18506ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.AddToPrincipalPolicyResult",
    jsii_struct_bases=[],
    name_mapping={
        "statement_added": "statementAdded",
        "policy_dependable": "policyDependable",
    },
)
class AddToPrincipalPolicyResult:
    def __init__(
        self,
        *,
        statement_added: builtins.bool,
        policy_dependable: typing.Optional[_IDependable_1175c9f7] = None,
    ) -> None:
        """(experimental) Result of calling ``addToPrincipalPolicy``.

        :param statement_added: (experimental) Whether the statement was added to the identity's policies.
        :param policy_dependable: (experimental) Dependable which allows depending on the policy change being applied. Default: - Required if ``statementAdded`` is true.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "statement_added": statement_added,
        }
        if policy_dependable is not None:
            self._values["policy_dependable"] = policy_dependable

    @builtins.property
    def statement_added(self) -> builtins.bool:
        """(experimental) Whether the statement was added to the identity's policies.

        :stability: experimental
        """
        result = self._values.get("statement_added")
        assert result is not None, "Required property 'statement_added' is missing"
        return result

    @builtins.property
    def policy_dependable(self) -> typing.Optional[_IDependable_1175c9f7]:
        """(experimental) Dependable which allows depending on the policy change being applied.

        :default: - Required if ``statementAdded`` is true.

        :stability: experimental
        """
        result = self._values.get("policy_dependable")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddToPrincipalPolicyResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.AddToResourcePolicyResult",
    jsii_struct_bases=[],
    name_mapping={
        "statement_added": "statementAdded",
        "policy_dependable": "policyDependable",
    },
)
class AddToResourcePolicyResult:
    def __init__(
        self,
        *,
        statement_added: builtins.bool,
        policy_dependable: typing.Optional[_IDependable_1175c9f7] = None,
    ) -> None:
        """(experimental) Result of calling addToResourcePolicy.

        :param statement_added: (experimental) Whether the statement was added.
        :param policy_dependable: (experimental) Dependable which allows depending on the policy change being applied. Default: - If ``statementAdded`` is true, the resource object itself. Otherwise, no dependable.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "statement_added": statement_added,
        }
        if policy_dependable is not None:
            self._values["policy_dependable"] = policy_dependable

    @builtins.property
    def statement_added(self) -> builtins.bool:
        """(experimental) Whether the statement was added.

        :stability: experimental
        """
        result = self._values.get("statement_added")
        assert result is not None, "Required property 'statement_added' is missing"
        return result

    @builtins.property
    def policy_dependable(self) -> typing.Optional[_IDependable_1175c9f7]:
        """(experimental) Dependable which allows depending on the policy change being applied.

        :default:

        - If ``statementAdded`` is true, the resource object itself.
        Otherwise, no dependable.

        :stability: experimental
        """
        result = self._values.get("policy_dependable")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddToResourcePolicyResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAccessKey(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnAccessKey",
):
    """A CloudFormation ``AWS::IAM::AccessKey``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html
    :cloudformationResource: AWS::IAM::AccessKey
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        user_name: builtins.str,
        serial: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::IAM::AccessKey``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param user_name: ``AWS::IAM::AccessKey.UserName``.
        :param serial: ``AWS::IAM::AccessKey.Serial``.
        :param status: ``AWS::IAM::AccessKey.Status``.
        """
        props = CfnAccessKeyProps(user_name=user_name, serial=serial, status=status)

        jsii.create(CfnAccessKey, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrSecretAccessKey")
    def attr_secret_access_key(self) -> builtins.str:
        """
        :cloudformationAttribute: SecretAccessKey
        """
        return jsii.get(self, "attrSecretAccessKey")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        """``AWS::IAM::AccessKey.UserName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-username
        """
        return jsii.get(self, "userName")

    @user_name.setter # type: ignore
    def user_name(self, value: builtins.str) -> None:
        jsii.set(self, "userName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serial")
    def serial(self) -> typing.Optional[jsii.Number]:
        """``AWS::IAM::AccessKey.Serial``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-serial
        """
        return jsii.get(self, "serial")

    @serial.setter # type: ignore
    def serial(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "serial", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::AccessKey.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-status
        """
        return jsii.get(self, "status")

    @status.setter # type: ignore
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnAccessKeyProps",
    jsii_struct_bases=[],
    name_mapping={"user_name": "userName", "serial": "serial", "status": "status"},
)
class CfnAccessKeyProps:
    def __init__(
        self,
        *,
        user_name: builtins.str,
        serial: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::AccessKey``.

        :param user_name: ``AWS::IAM::AccessKey.UserName``.
        :param serial: ``AWS::IAM::AccessKey.Serial``.
        :param status: ``AWS::IAM::AccessKey.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "user_name": user_name,
        }
        if serial is not None:
            self._values["serial"] = serial
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def user_name(self) -> builtins.str:
        """``AWS::IAM::AccessKey.UserName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-username
        """
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return result

    @builtins.property
    def serial(self) -> typing.Optional[jsii.Number]:
        """``AWS::IAM::AccessKey.Serial``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-serial
        """
        result = self._values.get("serial")
        return result

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::AccessKey.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-status
        """
        result = self._values.get("status")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnGroup",
):
    """A CloudFormation ``AWS::IAM::Group``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html
    :cloudformationResource: AWS::IAM::Group
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.List[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGroup.PolicyProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::IAM::Group``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param group_name: ``AWS::IAM::Group.GroupName``.
        :param managed_policy_arns: ``AWS::IAM::Group.ManagedPolicyArns``.
        :param path: ``AWS::IAM::Group.Path``.
        :param policies: ``AWS::IAM::Group.Policies``.
        """
        props = CfnGroupProps(
            group_name=group_name,
            managed_policy_arns=managed_policy_arns,
            path=path,
            policies=policies,
        )

        jsii.create(CfnGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Group.GroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-groupname
        """
        return jsii.get(self, "groupName")

    @group_name.setter # type: ignore
    def group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "groupName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Group.ManagedPolicyArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-managepolicyarns
        """
        return jsii.get(self, "managedPolicyArns")

    @managed_policy_arns.setter # type: ignore
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Group.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-path
        """
        return jsii.get(self, "path")

    @path.setter # type: ignore
    def path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "path", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGroup.PolicyProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::IAM::Group.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-policies
        """
        return jsii.get(self, "policies")

    @policies.setter # type: ignore
    def policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGroup.PolicyProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "policies", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iam.CfnGroup.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_document": "policyDocument",
            "policy_name": "policyName",
        },
    )
    class PolicyProperty:
        def __init__(
            self,
            *,
            policy_document: typing.Any,
            policy_name: builtins.str,
        ) -> None:
            """
            :param policy_document: ``CfnGroup.PolicyProperty.PolicyDocument``.
            :param policy_name: ``CfnGroup.PolicyProperty.PolicyName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "policy_document": policy_document,
                "policy_name": policy_name,
            }

        @builtins.property
        def policy_document(self) -> typing.Any:
            """``CfnGroup.PolicyProperty.PolicyDocument``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html#cfn-iam-policies-policydocument
            """
            result = self._values.get("policy_document")
            assert result is not None, "Required property 'policy_document' is missing"
            return result

        @builtins.property
        def policy_name(self) -> builtins.str:
            """``CfnGroup.PolicyProperty.PolicyName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html#cfn-iam-policies-policyname
            """
            result = self._values.get("policy_name")
            assert result is not None, "Required property 'policy_name' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "managed_policy_arns": "managedPolicyArns",
        "path": "path",
        "policies": "policies",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.List[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGroup.PolicyProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::Group``.

        :param group_name: ``AWS::IAM::Group.GroupName``.
        :param managed_policy_arns: ``AWS::IAM::Group.ManagedPolicyArns``.
        :param path: ``AWS::IAM::Group.Path``.
        :param policies: ``AWS::IAM::Group.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if group_name is not None:
            self._values["group_name"] = group_name
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if path is not None:
            self._values["path"] = path
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Group.GroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-groupname
        """
        result = self._values.get("group_name")
        return result

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Group.ManagedPolicyArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-managepolicyarns
        """
        result = self._values.get("managed_policy_arns")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Group.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGroup.PolicyProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::IAM::Group.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html#cfn-iam-group-policies
        """
        result = self._values.get("policies")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnInstanceProfile(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnInstanceProfile",
):
    """A CloudFormation ``AWS::IAM::InstanceProfile``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html
    :cloudformationResource: AWS::IAM::InstanceProfile
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        roles: typing.List[builtins.str],
        instance_profile_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::IAM::InstanceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param roles: ``AWS::IAM::InstanceProfile.Roles``.
        :param instance_profile_name: ``AWS::IAM::InstanceProfile.InstanceProfileName``.
        :param path: ``AWS::IAM::InstanceProfile.Path``.
        """
        props = CfnInstanceProfileProps(
            roles=roles, instance_profile_name=instance_profile_name, path=path
        )

        jsii.create(CfnInstanceProfile, self, [scope, id, props])

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
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        """``AWS::IAM::InstanceProfile.Roles``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-roles
        """
        return jsii.get(self, "roles")

    @roles.setter # type: ignore
    def roles(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "roles", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::InstanceProfile.InstanceProfileName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-instanceprofilename
        """
        return jsii.get(self, "instanceProfileName")

    @instance_profile_name.setter # type: ignore
    def instance_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "instanceProfileName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::InstanceProfile.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-path
        """
        return jsii.get(self, "path")

    @path.setter # type: ignore
    def path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "path", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnInstanceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "roles": "roles",
        "instance_profile_name": "instanceProfileName",
        "path": "path",
    },
)
class CfnInstanceProfileProps:
    def __init__(
        self,
        *,
        roles: typing.List[builtins.str],
        instance_profile_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::InstanceProfile``.

        :param roles: ``AWS::IAM::InstanceProfile.Roles``.
        :param instance_profile_name: ``AWS::IAM::InstanceProfile.InstanceProfileName``.
        :param path: ``AWS::IAM::InstanceProfile.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "roles": roles,
        }
        if instance_profile_name is not None:
            self._values["instance_profile_name"] = instance_profile_name
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        """``AWS::IAM::InstanceProfile.Roles``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-roles
        """
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return result

    @builtins.property
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::InstanceProfile.InstanceProfileName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-instanceprofilename
        """
        result = self._values.get("instance_profile_name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::InstanceProfile.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-path
        """
        result = self._values.get("path")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnManagedPolicy(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnManagedPolicy",
):
    """A CloudFormation ``AWS::IAM::ManagedPolicy``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html
    :cloudformationResource: AWS::IAM::ManagedPolicy
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.List[builtins.str]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.List[builtins.str]] = None,
        users: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Create a new ``AWS::IAM::ManagedPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_document: ``AWS::IAM::ManagedPolicy.PolicyDocument``.
        :param description: ``AWS::IAM::ManagedPolicy.Description``.
        :param groups: ``AWS::IAM::ManagedPolicy.Groups``.
        :param managed_policy_name: ``AWS::IAM::ManagedPolicy.ManagedPolicyName``.
        :param path: ``AWS::IAM::ManagedPolicy.Path``.
        :param roles: ``AWS::IAM::ManagedPolicy.Roles``.
        :param users: ``AWS::IAM::ManagedPolicy.Users``.
        """
        props = CfnManagedPolicyProps(
            policy_document=policy_document,
            description=description,
            groups=groups,
            managed_policy_name=managed_policy_name,
            path=path,
            roles=roles,
            users=users,
        )

        jsii.create(CfnManagedPolicy, self, [scope, id, props])

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
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        """``AWS::IAM::ManagedPolicy.PolicyDocument``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-policydocument
        """
        return jsii.get(self, "policyDocument")

    @policy_document.setter # type: ignore
    def policy_document(self, value: typing.Any) -> None:
        jsii.set(self, "policyDocument", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ManagedPolicy.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::ManagedPolicy.Groups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-groups
        """
        return jsii.get(self, "groups")

    @groups.setter # type: ignore
    def groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "groups", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyName")
    def managed_policy_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ManagedPolicy.ManagedPolicyName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-managedpolicyname
        """
        return jsii.get(self, "managedPolicyName")

    @managed_policy_name.setter # type: ignore
    def managed_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "managedPolicyName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ManagedPolicy.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-ec2-dhcpoptions-path
        """
        return jsii.get(self, "path")

    @path.setter # type: ignore
    def path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "path", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::ManagedPolicy.Roles``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-roles
        """
        return jsii.get(self, "roles")

    @roles.setter # type: ignore
    def roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "roles", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="users")
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::ManagedPolicy.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-users
        """
        return jsii.get(self, "users")

    @users.setter # type: ignore
    def users(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "users", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnManagedPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "description": "description",
        "groups": "groups",
        "managed_policy_name": "managedPolicyName",
        "path": "path",
        "roles": "roles",
        "users": "users",
    },
)
class CfnManagedPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.List[builtins.str]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.List[builtins.str]] = None,
        users: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::ManagedPolicy``.

        :param policy_document: ``AWS::IAM::ManagedPolicy.PolicyDocument``.
        :param description: ``AWS::IAM::ManagedPolicy.Description``.
        :param groups: ``AWS::IAM::ManagedPolicy.Groups``.
        :param managed_policy_name: ``AWS::IAM::ManagedPolicy.ManagedPolicyName``.
        :param path: ``AWS::IAM::ManagedPolicy.Path``.
        :param roles: ``AWS::IAM::ManagedPolicy.Roles``.
        :param users: ``AWS::IAM::ManagedPolicy.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "policy_document": policy_document,
        }
        if description is not None:
            self._values["description"] = description
        if groups is not None:
            self._values["groups"] = groups
        if managed_policy_name is not None:
            self._values["managed_policy_name"] = managed_policy_name
        if path is not None:
            self._values["path"] = path
        if roles is not None:
            self._values["roles"] = roles
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def policy_document(self) -> typing.Any:
        """``AWS::IAM::ManagedPolicy.PolicyDocument``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-policydocument
        """
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ManagedPolicy.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::ManagedPolicy.Groups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-groups
        """
        result = self._values.get("groups")
        return result

    @builtins.property
    def managed_policy_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ManagedPolicy.ManagedPolicyName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-managedpolicyname
        """
        result = self._values.get("managed_policy_name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ManagedPolicy.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-ec2-dhcpoptions-path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::ManagedPolicy.Roles``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-roles
        """
        result = self._values.get("roles")
        return result

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::ManagedPolicy.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-users
        """
        result = self._values.get("users")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnManagedPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnPolicy(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnPolicy",
):
    """A CloudFormation ``AWS::IAM::Policy``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html
    :cloudformationResource: AWS::IAM::Policy
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        policy_name: builtins.str,
        groups: typing.Optional[typing.List[builtins.str]] = None,
        roles: typing.Optional[typing.List[builtins.str]] = None,
        users: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Create a new ``AWS::IAM::Policy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_document: ``AWS::IAM::Policy.PolicyDocument``.
        :param policy_name: ``AWS::IAM::Policy.PolicyName``.
        :param groups: ``AWS::IAM::Policy.Groups``.
        :param roles: ``AWS::IAM::Policy.Roles``.
        :param users: ``AWS::IAM::Policy.Users``.
        """
        props = CfnPolicyProps(
            policy_document=policy_document,
            policy_name=policy_name,
            groups=groups,
            roles=roles,
            users=users,
        )

        jsii.create(CfnPolicy, self, [scope, id, props])

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
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        """``AWS::IAM::Policy.PolicyDocument``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument
        """
        return jsii.get(self, "policyDocument")

    @policy_document.setter # type: ignore
    def policy_document(self, value: typing.Any) -> None:
        jsii.set(self, "policyDocument", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        """``AWS::IAM::Policy.PolicyName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policyname
        """
        return jsii.get(self, "policyName")

    @policy_name.setter # type: ignore
    def policy_name(self, value: builtins.str) -> None:
        jsii.set(self, "policyName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Policy.Groups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-groups
        """
        return jsii.get(self, "groups")

    @groups.setter # type: ignore
    def groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "groups", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Policy.Roles``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-roles
        """
        return jsii.get(self, "roles")

    @roles.setter # type: ignore
    def roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "roles", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="users")
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Policy.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-users
        """
        return jsii.get(self, "users")

    @users.setter # type: ignore
    def users(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "users", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "policy_name": "policyName",
        "groups": "groups",
        "roles": "roles",
        "users": "users",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        policy_name: builtins.str,
        groups: typing.Optional[typing.List[builtins.str]] = None,
        roles: typing.Optional[typing.List[builtins.str]] = None,
        users: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::Policy``.

        :param policy_document: ``AWS::IAM::Policy.PolicyDocument``.
        :param policy_name: ``AWS::IAM::Policy.PolicyName``.
        :param groups: ``AWS::IAM::Policy.Groups``.
        :param roles: ``AWS::IAM::Policy.Roles``.
        :param users: ``AWS::IAM::Policy.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
        }
        if groups is not None:
            self._values["groups"] = groups
        if roles is not None:
            self._values["roles"] = roles
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def policy_document(self) -> typing.Any:
        """``AWS::IAM::Policy.PolicyDocument``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument
        """
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return result

    @builtins.property
    def policy_name(self) -> builtins.str:
        """``AWS::IAM::Policy.PolicyName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policyname
        """
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return result

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Policy.Groups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-groups
        """
        result = self._values.get("groups")
        return result

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Policy.Roles``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-roles
        """
        result = self._values.get("roles")
        return result

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Policy.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-users
        """
        result = self._values.get("users")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnRole(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnRole",
):
    """A CloudFormation ``AWS::IAM::Role``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html
    :cloudformationResource: AWS::IAM::Role
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        assume_role_policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.List[builtins.str]] = None,
        max_session_duration: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnRole.PolicyProperty", _IResolvable_a771d0ef]]]] = None,
        role_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::IAM::Role``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param assume_role_policy_document: ``AWS::IAM::Role.AssumeRolePolicyDocument``.
        :param description: ``AWS::IAM::Role.Description``.
        :param managed_policy_arns: ``AWS::IAM::Role.ManagedPolicyArns``.
        :param max_session_duration: ``AWS::IAM::Role.MaxSessionDuration``.
        :param path: ``AWS::IAM::Role.Path``.
        :param permissions_boundary: ``AWS::IAM::Role.PermissionsBoundary``.
        :param policies: ``AWS::IAM::Role.Policies``.
        :param role_name: ``AWS::IAM::Role.RoleName``.
        :param tags: ``AWS::IAM::Role.Tags``.
        """
        props = CfnRoleProps(
            assume_role_policy_document=assume_role_policy_document,
            description=description,
            managed_policy_arns=managed_policy_arns,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            policies=policies,
            role_name=role_name,
            tags=tags,
        )

        jsii.create(CfnRole, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrRoleId")
    def attr_role_id(self) -> builtins.str:
        """
        :cloudformationAttribute: RoleId
        """
        return jsii.get(self, "attrRoleId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::IAM::Role.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRolePolicyDocument")
    def assume_role_policy_document(self) -> typing.Any:
        """``AWS::IAM::Role.AssumeRolePolicyDocument``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument
        """
        return jsii.get(self, "assumeRolePolicyDocument")

    @assume_role_policy_document.setter # type: ignore
    def assume_role_policy_document(self, value: typing.Any) -> None:
        jsii.set(self, "assumeRolePolicyDocument", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Role.ManagedPolicyArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-managepolicyarns
        """
        return jsii.get(self, "managedPolicyArns")

    @managed_policy_arns.setter # type: ignore
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maxSessionDuration")
    def max_session_duration(self) -> typing.Optional[jsii.Number]:
        """``AWS::IAM::Role.MaxSessionDuration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-maxsessionduration
        """
        return jsii.get(self, "maxSessionDuration")

    @max_session_duration.setter # type: ignore
    def max_session_duration(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxSessionDuration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-path
        """
        return jsii.get(self, "path")

    @path.setter # type: ignore
    def path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "path", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.PermissionsBoundary``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-permissionsboundary
        """
        return jsii.get(self, "permissionsBoundary")

    @permissions_boundary.setter # type: ignore
    def permissions_boundary(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnRole.PolicyProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::IAM::Role.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-policies
        """
        return jsii.get(self, "policies")

    @policies.setter # type: ignore
    def policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnRole.PolicyProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "policies", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.RoleName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-rolename
        """
        return jsii.get(self, "roleName")

    @role_name.setter # type: ignore
    def role_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iam.CfnRole.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_document": "policyDocument",
            "policy_name": "policyName",
        },
    )
    class PolicyProperty:
        def __init__(
            self,
            *,
            policy_document: typing.Any,
            policy_name: builtins.str,
        ) -> None:
            """
            :param policy_document: ``CfnRole.PolicyProperty.PolicyDocument``.
            :param policy_name: ``CfnRole.PolicyProperty.PolicyName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "policy_document": policy_document,
                "policy_name": policy_name,
            }

        @builtins.property
        def policy_document(self) -> typing.Any:
            """``CfnRole.PolicyProperty.PolicyDocument``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html#cfn-iam-policies-policydocument
            """
            result = self._values.get("policy_document")
            assert result is not None, "Required property 'policy_document' is missing"
            return result

        @builtins.property
        def policy_name(self) -> builtins.str:
            """``CfnRole.PolicyProperty.PolicyName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html#cfn-iam-policies-policyname
            """
            result = self._values.get("policy_name")
            assert result is not None, "Required property 'policy_name' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnRoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "assume_role_policy_document": "assumeRolePolicyDocument",
        "description": "description",
        "managed_policy_arns": "managedPolicyArns",
        "max_session_duration": "maxSessionDuration",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "policies": "policies",
        "role_name": "roleName",
        "tags": "tags",
    },
)
class CfnRoleProps:
    def __init__(
        self,
        *,
        assume_role_policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.List[builtins.str]] = None,
        max_session_duration: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnRole.PolicyProperty, _IResolvable_a771d0ef]]]] = None,
        role_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::Role``.

        :param assume_role_policy_document: ``AWS::IAM::Role.AssumeRolePolicyDocument``.
        :param description: ``AWS::IAM::Role.Description``.
        :param managed_policy_arns: ``AWS::IAM::Role.ManagedPolicyArns``.
        :param max_session_duration: ``AWS::IAM::Role.MaxSessionDuration``.
        :param path: ``AWS::IAM::Role.Path``.
        :param permissions_boundary: ``AWS::IAM::Role.PermissionsBoundary``.
        :param policies: ``AWS::IAM::Role.Policies``.
        :param role_name: ``AWS::IAM::Role.RoleName``.
        :param tags: ``AWS::IAM::Role.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "assume_role_policy_document": assume_role_policy_document,
        }
        if description is not None:
            self._values["description"] = description
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if max_session_duration is not None:
            self._values["max_session_duration"] = max_session_duration
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if policies is not None:
            self._values["policies"] = policies
        if role_name is not None:
            self._values["role_name"] = role_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assume_role_policy_document(self) -> typing.Any:
        """``AWS::IAM::Role.AssumeRolePolicyDocument``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument
        """
        result = self._values.get("assume_role_policy_document")
        assert result is not None, "Required property 'assume_role_policy_document' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::Role.ManagedPolicyArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-managepolicyarns
        """
        result = self._values.get("managed_policy_arns")
        return result

    @builtins.property
    def max_session_duration(self) -> typing.Optional[jsii.Number]:
        """``AWS::IAM::Role.MaxSessionDuration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-maxsessionduration
        """
        result = self._values.get("max_session_duration")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.PermissionsBoundary``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-permissionsboundary
        """
        result = self._values.get("permissions_boundary")
        return result

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnRole.PolicyProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::IAM::Role.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-policies
        """
        result = self._values.get("policies")
        return result

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::Role.RoleName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-rolename
        """
        result = self._values.get("role_name")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IAM::Role.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnServiceLinkedRole(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnServiceLinkedRole",
):
    """A CloudFormation ``AWS::IAM::ServiceLinkedRole``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html
    :cloudformationResource: AWS::IAM::ServiceLinkedRole
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        aws_service_name: builtins.str,
        custom_suffix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::IAM::ServiceLinkedRole``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_service_name: ``AWS::IAM::ServiceLinkedRole.AWSServiceName``.
        :param custom_suffix: ``AWS::IAM::ServiceLinkedRole.CustomSuffix``.
        :param description: ``AWS::IAM::ServiceLinkedRole.Description``.
        """
        props = CfnServiceLinkedRoleProps(
            aws_service_name=aws_service_name,
            custom_suffix=custom_suffix,
            description=description,
        )

        jsii.create(CfnServiceLinkedRole, self, [scope, id, props])

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
    @jsii.member(jsii_name="awsServiceName")
    def aws_service_name(self) -> builtins.str:
        """``AWS::IAM::ServiceLinkedRole.AWSServiceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-awsservicename
        """
        return jsii.get(self, "awsServiceName")

    @aws_service_name.setter # type: ignore
    def aws_service_name(self, value: builtins.str) -> None:
        jsii.set(self, "awsServiceName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="customSuffix")
    def custom_suffix(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ServiceLinkedRole.CustomSuffix``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-customsuffix
        """
        return jsii.get(self, "customSuffix")

    @custom_suffix.setter # type: ignore
    def custom_suffix(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customSuffix", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ServiceLinkedRole.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnServiceLinkedRoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_service_name": "awsServiceName",
        "custom_suffix": "customSuffix",
        "description": "description",
    },
)
class CfnServiceLinkedRoleProps:
    def __init__(
        self,
        *,
        aws_service_name: builtins.str,
        custom_suffix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::ServiceLinkedRole``.

        :param aws_service_name: ``AWS::IAM::ServiceLinkedRole.AWSServiceName``.
        :param custom_suffix: ``AWS::IAM::ServiceLinkedRole.CustomSuffix``.
        :param description: ``AWS::IAM::ServiceLinkedRole.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "aws_service_name": aws_service_name,
        }
        if custom_suffix is not None:
            self._values["custom_suffix"] = custom_suffix
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def aws_service_name(self) -> builtins.str:
        """``AWS::IAM::ServiceLinkedRole.AWSServiceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-awsservicename
        """
        result = self._values.get("aws_service_name")
        assert result is not None, "Required property 'aws_service_name' is missing"
        return result

    @builtins.property
    def custom_suffix(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ServiceLinkedRole.CustomSuffix``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-customsuffix
        """
        result = self._values.get("custom_suffix")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::ServiceLinkedRole.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-description
        """
        result = self._values.get("description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceLinkedRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnUser(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnUser",
):
    """A CloudFormation ``AWS::IAM::User``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html
    :cloudformationResource: AWS::IAM::User
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        groups: typing.Optional[typing.List[builtins.str]] = None,
        login_profile: typing.Optional[typing.Union["CfnUser.LoginProfileProperty", _IResolvable_a771d0ef]] = None,
        managed_policy_arns: typing.Optional[typing.List[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnUser.PolicyProperty", _IResolvable_a771d0ef]]]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::IAM::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param groups: ``AWS::IAM::User.Groups``.
        :param login_profile: ``AWS::IAM::User.LoginProfile``.
        :param managed_policy_arns: ``AWS::IAM::User.ManagedPolicyArns``.
        :param path: ``AWS::IAM::User.Path``.
        :param permissions_boundary: ``AWS::IAM::User.PermissionsBoundary``.
        :param policies: ``AWS::IAM::User.Policies``.
        :param tags: ``AWS::IAM::User.Tags``.
        :param user_name: ``AWS::IAM::User.UserName``.
        """
        props = CfnUserProps(
            groups=groups,
            login_profile=login_profile,
            managed_policy_arns=managed_policy_arns,
            path=path,
            permissions_boundary=permissions_boundary,
            policies=policies,
            tags=tags,
            user_name=user_name,
        )

        jsii.create(CfnUser, self, [scope, id, props])

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
        """``AWS::IAM::User.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::User.Groups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-groups
        """
        return jsii.get(self, "groups")

    @groups.setter # type: ignore
    def groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "groups", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="loginProfile")
    def login_profile(
        self,
    ) -> typing.Optional[typing.Union["CfnUser.LoginProfileProperty", _IResolvable_a771d0ef]]:
        """``AWS::IAM::User.LoginProfile``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-loginprofile
        """
        return jsii.get(self, "loginProfile")

    @login_profile.setter # type: ignore
    def login_profile(
        self,
        value: typing.Optional[typing.Union["CfnUser.LoginProfileProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "loginProfile", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::User.ManagedPolicyArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-managepolicyarns
        """
        return jsii.get(self, "managedPolicyArns")

    @managed_policy_arns.setter # type: ignore
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::User.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-path
        """
        return jsii.get(self, "path")

    @path.setter # type: ignore
    def path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "path", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::User.PermissionsBoundary``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-permissionsboundary
        """
        return jsii.get(self, "permissionsBoundary")

    @permissions_boundary.setter # type: ignore
    def permissions_boundary(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnUser.PolicyProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::IAM::User.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-policies
        """
        return jsii.get(self, "policies")

    @policies.setter # type: ignore
    def policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnUser.PolicyProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "policies", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userName")
    def user_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::User.UserName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-username
        """
        return jsii.get(self, "userName")

    @user_name.setter # type: ignore
    def user_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "userName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iam.CfnUser.LoginProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "password_reset_required": "passwordResetRequired",
        },
    )
    class LoginProfileProperty:
        def __init__(
            self,
            *,
            password: builtins.str,
            password_reset_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param password: ``CfnUser.LoginProfileProperty.Password``.
            :param password_reset_required: ``CfnUser.LoginProfileProperty.PasswordResetRequired``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "password": password,
            }
            if password_reset_required is not None:
                self._values["password_reset_required"] = password_reset_required

        @builtins.property
        def password(self) -> builtins.str:
            """``CfnUser.LoginProfileProperty.Password``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html#cfn-iam-user-loginprofile-password
            """
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return result

        @builtins.property
        def password_reset_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnUser.LoginProfileProperty.PasswordResetRequired``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html#cfn-iam-user-loginprofile-passwordresetrequired
            """
            result = self._values.get("password_reset_required")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoginProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iam.CfnUser.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_document": "policyDocument",
            "policy_name": "policyName",
        },
    )
    class PolicyProperty:
        def __init__(
            self,
            *,
            policy_document: typing.Any,
            policy_name: builtins.str,
        ) -> None:
            """
            :param policy_document: ``CfnUser.PolicyProperty.PolicyDocument``.
            :param policy_name: ``CfnUser.PolicyProperty.PolicyName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "policy_document": policy_document,
                "policy_name": policy_name,
            }

        @builtins.property
        def policy_document(self) -> typing.Any:
            """``CfnUser.PolicyProperty.PolicyDocument``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html#cfn-iam-policies-policydocument
            """
            result = self._values.get("policy_document")
            assert result is not None, "Required property 'policy_document' is missing"
            return result

        @builtins.property
        def policy_name(self) -> builtins.str:
            """``CfnUser.PolicyProperty.PolicyName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html#cfn-iam-policies-policyname
            """
            result = self._values.get("policy_name")
            assert result is not None, "Required property 'policy_name' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "groups": "groups",
        "login_profile": "loginProfile",
        "managed_policy_arns": "managedPolicyArns",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "policies": "policies",
        "tags": "tags",
        "user_name": "userName",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        groups: typing.Optional[typing.List[builtins.str]] = None,
        login_profile: typing.Optional[typing.Union[CfnUser.LoginProfileProperty, _IResolvable_a771d0ef]] = None,
        managed_policy_arns: typing.Optional[typing.List[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnUser.PolicyProperty, _IResolvable_a771d0ef]]]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::IAM::User``.

        :param groups: ``AWS::IAM::User.Groups``.
        :param login_profile: ``AWS::IAM::User.LoginProfile``.
        :param managed_policy_arns: ``AWS::IAM::User.ManagedPolicyArns``.
        :param path: ``AWS::IAM::User.Path``.
        :param permissions_boundary: ``AWS::IAM::User.PermissionsBoundary``.
        :param policies: ``AWS::IAM::User.Policies``.
        :param tags: ``AWS::IAM::User.Tags``.
        :param user_name: ``AWS::IAM::User.UserName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if groups is not None:
            self._values["groups"] = groups
        if login_profile is not None:
            self._values["login_profile"] = login_profile
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if policies is not None:
            self._values["policies"] = policies
        if tags is not None:
            self._values["tags"] = tags
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::User.Groups``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-groups
        """
        result = self._values.get("groups")
        return result

    @builtins.property
    def login_profile(
        self,
    ) -> typing.Optional[typing.Union[CfnUser.LoginProfileProperty, _IResolvable_a771d0ef]]:
        """``AWS::IAM::User.LoginProfile``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-loginprofile
        """
        result = self._values.get("login_profile")
        return result

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::IAM::User.ManagedPolicyArns``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-managepolicyarns
        """
        result = self._values.get("managed_policy_arns")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::User.Path``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::User.PermissionsBoundary``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-permissionsboundary
        """
        result = self._values.get("permissions_boundary")
        return result

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnUser.PolicyProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::IAM::User.Policies``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-policies
        """
        result = self._values.get("policies")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::IAM::User.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        """``AWS::IAM::User.UserName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html#cfn-iam-user-username
        """
        result = self._values.get("user_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnUserToGroupAddition(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CfnUserToGroupAddition",
):
    """A CloudFormation ``AWS::IAM::UserToGroupAddition``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html
    :cloudformationResource: AWS::IAM::UserToGroupAddition
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        group_name: builtins.str,
        users: typing.List[builtins.str],
    ) -> None:
        """Create a new ``AWS::IAM::UserToGroupAddition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param group_name: ``AWS::IAM::UserToGroupAddition.GroupName``.
        :param users: ``AWS::IAM::UserToGroupAddition.Users``.
        """
        props = CfnUserToGroupAdditionProps(group_name=group_name, users=users)

        jsii.create(CfnUserToGroupAddition, self, [scope, id, props])

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
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        """``AWS::IAM::UserToGroupAddition.GroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html#cfn-iam-addusertogroup-groupname
        """
        return jsii.get(self, "groupName")

    @group_name.setter # type: ignore
    def group_name(self, value: builtins.str) -> None:
        jsii.set(self, "groupName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        """``AWS::IAM::UserToGroupAddition.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html#cfn-iam-addusertogroup-users
        """
        return jsii.get(self, "users")

    @users.setter # type: ignore
    def users(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "users", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CfnUserToGroupAdditionProps",
    jsii_struct_bases=[],
    name_mapping={"group_name": "groupName", "users": "users"},
)
class CfnUserToGroupAdditionProps:
    def __init__(
        self,
        *,
        group_name: builtins.str,
        users: typing.List[builtins.str],
    ) -> None:
        """Properties for defining a ``AWS::IAM::UserToGroupAddition``.

        :param group_name: ``AWS::IAM::UserToGroupAddition.GroupName``.
        :param users: ``AWS::IAM::UserToGroupAddition.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "group_name": group_name,
            "users": users,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        """``AWS::IAM::UserToGroupAddition.GroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html#cfn-iam-addusertogroup-groupname
        """
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return result

    @builtins.property
    def users(self) -> typing.List[builtins.str]:
        """``AWS::IAM::UserToGroupAddition.Users``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html#cfn-iam-addusertogroup-users
        """
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserToGroupAdditionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.CommonGrantOptions",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
    },
)
class CommonGrantOptions:
    def __init__(
        self,
        *,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
    ) -> None:
        """(experimental) Basic options for a grant operation.

        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
        }

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        """(experimental) The actions to grant.

        :stability: experimental
        """
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return result

    @builtins.property
    def grantee(self) -> "IGrantable":
        """(experimental) The principal to grant to.

        :default: if principal is undefined, no work is done.

        :stability: experimental
        """
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return result

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        """(experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonGrantOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IDependable_1175c9f7)
class CompositeDependable(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CompositeDependable",
):
    """(experimental) Composite dependable.

    Not as simple as eagerly getting the dependency roots from the
    inner dependables, as they may be mutable so we need to defer
    the query.

    :stability: experimental
    """

    def __init__(self, *dependables: _IDependable_1175c9f7) -> None:
        """
        :param dependables: -

        :stability: experimental
        """
        jsii.create(CompositeDependable, self, [*dependables])


@jsii.enum(jsii_type="monocdk.aws_iam.Effect")
class Effect(enum.Enum):
    """(experimental) The Effect element of an IAM policy.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html
    :stability: experimental
    """

    ALLOW = "ALLOW"
    """(experimental) Allows access to a resource in an IAM policy statement.

    By default, access to resources are denied.

    :stability: experimental
    """
    DENY = "DENY"
    """(experimental) Explicitly deny access to a resource.

    By default, all requests are denied implicitly.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk.aws_iam.FromRoleArnOptions",
    jsii_struct_bases=[],
    name_mapping={"mutable": "mutable"},
)
class FromRoleArnOptions:
    def __init__(self, *, mutable: typing.Optional[builtins.bool] = None) -> None:
        """(experimental) Options allowing customizing the behavior of {@link Role.fromRoleArn}.

        :param mutable: (experimental) Whether the imported role can be modified by attaching policy resources to it. Default: true

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if mutable is not None:
            self._values["mutable"] = mutable

    @builtins.property
    def mutable(self) -> typing.Optional[builtins.bool]:
        """(experimental) Whether the imported role can be modified by attaching policy resources to it.

        :default: true

        :stability: experimental
        """
        result = self._values.get("mutable")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FromRoleArnOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IDependable_1175c9f7)
class Grant(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_iam.Grant"):
    """(experimental) Result of a grant() operation.

    This class is not instantiable by consumers on purpose, so that they will be
    required to call the Grant factory functions.

    :stability: experimental
    """

    @jsii.member(jsii_name="addToPrincipal")
    @builtins.classmethod
    def add_to_principal(
        cls,
        *,
        scope: typing.Optional[_IConstruct_5a0f9c5e] = None,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
    ) -> "Grant":
        """(experimental) Try to grant the given permissions to the given principal.

        Absence of a principal leads to a warning, but failing to add
        the permissions to a present principal is not an error.

        :param scope: (experimental) Construct to report warnings on in case grant could not be registered. Default: - the construct in which this construct is defined
        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        options = GrantOnPrincipalOptions(
            scope=scope, actions=actions, grantee=grantee, resource_arns=resource_arns
        )

        return jsii.sinvoke(cls, "addToPrincipal", [options])

    @jsii.member(jsii_name="addToPrincipalAndResource")
    @builtins.classmethod
    def add_to_principal_and_resource(
        cls,
        *,
        resource: "IResourceWithPolicy",
        resource_policy_principal: typing.Optional["IPrincipal"] = None,
        resource_self_arns: typing.Optional[typing.List[builtins.str]] = None,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
    ) -> "Grant":
        """(experimental) Add a grant both on the principal and on the resource.

        As long as any principal is given, granting on the principal may fail (in
        case of a non-identity principal), but granting on the resource will
        never fail.

        Statement will be the resource statement.

        :param resource: (experimental) The resource with a resource policy. The statement will always be added to the resource policy.
        :param resource_policy_principal: (experimental) The principal to use in the statement for the resource policy. Default: - the principal of the grantee will be used
        :param resource_self_arns: (experimental) When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs
        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        options = GrantOnPrincipalAndResourceOptions(
            resource=resource,
            resource_policy_principal=resource_policy_principal,
            resource_self_arns=resource_self_arns,
            actions=actions,
            grantee=grantee,
            resource_arns=resource_arns,
        )

        return jsii.sinvoke(cls, "addToPrincipalAndResource", [options])

    @jsii.member(jsii_name="addToPrincipalOrResource")
    @builtins.classmethod
    def add_to_principal_or_resource(
        cls,
        *,
        resource: "IResourceWithPolicy",
        resource_self_arns: typing.Optional[typing.List[builtins.str]] = None,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
    ) -> "Grant":
        """(experimental) Grant the given permissions to the principal.

        The permissions will be added to the principal policy primarily, falling
        back to the resource policy if necessary. The permissions must be granted
        somewhere.

        - Trying to grant permissions to a principal that does not admit adding to
          the principal policy while not providing a resource with a resource policy
          is an error.
        - Trying to grant permissions to an absent principal (possible in the
          case of imported resources) leads to a warning being added to the
          resource construct.

        :param resource: (experimental) The resource with a resource policy. The statement will be added to the resource policy if it couldn't be added to the principal policy.
        :param resource_self_arns: (experimental) When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs
        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        options = GrantWithResourceOptions(
            resource=resource,
            resource_self_arns=resource_self_arns,
            actions=actions,
            grantee=grantee,
            resource_arns=resource_arns,
        )

        return jsii.sinvoke(cls, "addToPrincipalOrResource", [options])

    @jsii.member(jsii_name="drop")
    @builtins.classmethod
    def drop(cls, grantee: "IGrantable", _intent: builtins.str) -> "Grant":
        """(experimental) Returns a "no-op" ``Grant`` object which represents a "dropped grant".

        This can be used for e.g. imported resources where you may not be able to modify
        the resource's policy or some underlying policy which you don't know about.

        :param grantee: The intended grantee.
        :param _intent: The user's intent (will be ignored at the moment).

        :stability: experimental
        """
        return jsii.sinvoke(cls, "drop", [grantee, _intent])

    @jsii.member(jsii_name="applyBefore")
    def apply_before(self, *constructs: _IConstruct_5a0f9c5e) -> None:
        """(experimental) Make sure this grant is applied before the given constructs are deployed.

        The same as construct.node.addDependency(grant), but slightly nicer to read.

        :param constructs: -

        :stability: experimental
        """
        return jsii.invoke(self, "applyBefore", [*constructs])

    @jsii.member(jsii_name="assertSuccess")
    def assert_success(self) -> None:
        """(experimental) Throw an error if this grant wasn't successful.

        :stability: experimental
        """
        return jsii.invoke(self, "assertSuccess", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="success")
    def success(self) -> builtins.bool:
        """(experimental) Whether the grant operation was successful.

        :stability: experimental
        """
        return jsii.get(self, "success")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalStatement")
    def principal_statement(self) -> typing.Optional["PolicyStatement"]:
        """(experimental) The statement that was added to the principal's policy.

        Can be accessed to (e.g.) add additional conditions to the statement.

        :stability: experimental
        """
        return jsii.get(self, "principalStatement")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resourceStatement")
    def resource_statement(self) -> typing.Optional["PolicyStatement"]:
        """(experimental) The statement that was added to the resource policy.

        Can be accessed to (e.g.) add additional conditions to the statement.

        :stability: experimental
        """
        return jsii.get(self, "resourceStatement")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.GrantOnPrincipalAndResourceOptions",
    jsii_struct_bases=[CommonGrantOptions],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "resource": "resource",
        "resource_policy_principal": "resourcePolicyPrincipal",
        "resource_self_arns": "resourceSelfArns",
    },
)
class GrantOnPrincipalAndResourceOptions(CommonGrantOptions):
    def __init__(
        self,
        *,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
        resource: "IResourceWithPolicy",
        resource_policy_principal: typing.Optional["IPrincipal"] = None,
        resource_self_arns: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """(experimental) Options for a grant operation to both identity and resource.

        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.
        :param resource: (experimental) The resource with a resource policy. The statement will always be added to the resource policy.
        :param resource_policy_principal: (experimental) The principal to use in the statement for the resource policy. Default: - the principal of the grantee will be used
        :param resource_self_arns: (experimental) When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
            "resource": resource,
        }
        if resource_policy_principal is not None:
            self._values["resource_policy_principal"] = resource_policy_principal
        if resource_self_arns is not None:
            self._values["resource_self_arns"] = resource_self_arns

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        """(experimental) The actions to grant.

        :stability: experimental
        """
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return result

    @builtins.property
    def grantee(self) -> "IGrantable":
        """(experimental) The principal to grant to.

        :default: if principal is undefined, no work is done.

        :stability: experimental
        """
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return result

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        """(experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return result

    @builtins.property
    def resource(self) -> "IResourceWithPolicy":
        """(experimental) The resource with a resource policy.

        The statement will always be added to the resource policy.

        :stability: experimental
        """
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return result

    @builtins.property
    def resource_policy_principal(self) -> typing.Optional["IPrincipal"]:
        """(experimental) The principal to use in the statement for the resource policy.

        :default: - the principal of the grantee will be used

        :stability: experimental
        """
        result = self._values.get("resource_policy_principal")
        return result

    @builtins.property
    def resource_self_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) When referring to the resource in a resource policy, use this as ARN.

        (Depending on the resource type, this needs to be '*' in a resource policy).

        :default: Same as regular resource ARNs

        :stability: experimental
        """
        result = self._values.get("resource_self_arns")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantOnPrincipalAndResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.GrantOnPrincipalOptions",
    jsii_struct_bases=[CommonGrantOptions],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "scope": "scope",
    },
)
class GrantOnPrincipalOptions(CommonGrantOptions):
    def __init__(
        self,
        *,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
        scope: typing.Optional[_IConstruct_5a0f9c5e] = None,
    ) -> None:
        """(experimental) Options for a grant operation that only applies to principals.

        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.
        :param scope: (experimental) Construct to report warnings on in case grant could not be registered. Default: - the construct in which this construct is defined

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
        }
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        """(experimental) The actions to grant.

        :stability: experimental
        """
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return result

    @builtins.property
    def grantee(self) -> "IGrantable":
        """(experimental) The principal to grant to.

        :default: if principal is undefined, no work is done.

        :stability: experimental
        """
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return result

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        """(experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return result

    @builtins.property
    def scope(self) -> typing.Optional[_IConstruct_5a0f9c5e]:
        """(experimental) Construct to report warnings on in case grant could not be registered.

        :default: - the construct in which this construct is defined

        :stability: experimental
        """
        result = self._values.get("scope")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantOnPrincipalOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.GrantWithResourceOptions",
    jsii_struct_bases=[CommonGrantOptions],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "resource": "resource",
        "resource_self_arns": "resourceSelfArns",
    },
)
class GrantWithResourceOptions(CommonGrantOptions):
    def __init__(
        self,
        *,
        actions: typing.List[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.List[builtins.str],
        resource: "IResourceWithPolicy",
        resource_self_arns: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """(experimental) Options for a grant operation.

        :param actions: (experimental) The actions to grant.
        :param grantee: (experimental) The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: (experimental) The resource ARNs to grant to.
        :param resource: (experimental) The resource with a resource policy. The statement will be added to the resource policy if it couldn't be added to the principal policy.
        :param resource_self_arns: (experimental) When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
            "resource": resource,
        }
        if resource_self_arns is not None:
            self._values["resource_self_arns"] = resource_self_arns

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        """(experimental) The actions to grant.

        :stability: experimental
        """
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return result

    @builtins.property
    def grantee(self) -> "IGrantable":
        """(experimental) The principal to grant to.

        :default: if principal is undefined, no work is done.

        :stability: experimental
        """
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return result

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        """(experimental) The resource ARNs to grant to.

        :stability: experimental
        """
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return result

    @builtins.property
    def resource(self) -> "IResourceWithPolicy":
        """(experimental) The resource with a resource policy.

        The statement will be added to the resource policy if it couldn't be
        added to the principal policy.

        :stability: experimental
        """
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return result

    @builtins.property
    def resource_self_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) When referring to the resource in a resource policy, use this as ARN.

        (Depending on the resource type, this needs to be '*' in a resource policy).

        :default: Same as regular resource ARNs

        :stability: experimental
        """
        result = self._values.get("resource_self_arns")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantWithResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.GroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "managed_policies": "managedPolicies",
        "path": "path",
    },
)
class GroupProps:
    def __init__(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policies: typing.Optional[typing.List["IManagedPolicy"]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for defining an IAM group.

        :param group_name: (experimental) A name for the IAM group. For valid values, see the GroupName parameter for the CreateGroup action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: Generated by CloudFormation (recommended)
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param path: (experimental) The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`_ in the IAM User Guide. Default: /

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if group_name is not None:
            self._values["group_name"] = group_name
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the IAM group.

        For valid values, see the GroupName parameter
        for the CreateGroup action in the IAM API Reference. If you don't specify
        a name, AWS CloudFormation generates a unique physical ID and uses that
        ID for the group name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default: Generated by CloudFormation (recommended)

        :stability: experimental
        """
        result = self._values.get("group_name")
        return result

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List["IManagedPolicy"]]:
        """(experimental) A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.

        :stability: experimental
        """
        result = self._values.get("managed_policies")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """(experimental) The path to the group.

        For more information about paths, see `IAM
        Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`_
        in the IAM User Guide.

        :default: /

        :stability: experimental
        """
        result = self._values.get("path")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_iam.IGrantable")
class IGrantable(typing_extensions.Protocol):
    """(experimental) Any object that has an associated principal that a permission can be granted to.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IGrantableProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> "IPrincipal":
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        ...


class _IGrantableProxy:
    """(experimental) Any object that has an associated principal that a permission can be granted to.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IGrantable"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> "IPrincipal":
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")


@jsii.interface(jsii_type="monocdk.aws_iam.IManagedPolicy")
class IManagedPolicy(typing_extensions.Protocol):
    """(experimental) A managed policy.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IManagedPolicyProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        """(experimental) The ARN of the managed policy.

        :stability: experimental
        :attribute: true
        """
        ...


class _IManagedPolicyProxy:
    """(experimental) A managed policy.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IManagedPolicy"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        """(experimental) The ARN of the managed policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "managedPolicyArn")


@jsii.interface(jsii_type="monocdk.aws_iam.IOpenIdConnectProvider")
class IOpenIdConnectProvider(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) Represents an IAM OpenID Connect provider.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IOpenIdConnectProviderProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectProviderArn")
    def open_id_connect_provider_arn(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the IAM OpenID Connect provider.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectProviderIssuer")
    def open_id_connect_provider_issuer(self) -> builtins.str:
        """(experimental) The issuer for OIDC Provider.

        :stability: experimental
        """
        ...


class _IOpenIdConnectProviderProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) Represents an IAM OpenID Connect provider.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IOpenIdConnectProvider"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectProviderArn")
    def open_id_connect_provider_arn(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the IAM OpenID Connect provider.

        :stability: experimental
        """
        return jsii.get(self, "openIdConnectProviderArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectProviderIssuer")
    def open_id_connect_provider_issuer(self) -> builtins.str:
        """(experimental) The issuer for OIDC Provider.

        :stability: experimental
        """
        return jsii.get(self, "openIdConnectProviderIssuer")


@jsii.interface(jsii_type="monocdk.aws_iam.IPolicy")
class IPolicy(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) Represents an IAM Policy.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IPolicyProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        """(experimental) The name of this policy.

        :stability: experimental
        :attribute: true
        """
        ...


class _IPolicyProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) Represents an IAM Policy.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IPolicy"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        """(experimental) The name of this policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "policyName")


@jsii.interface(jsii_type="monocdk.aws_iam.IPrincipal")
class IPrincipal(IGrantable, typing_extensions.Protocol):
    """(experimental) Represents a logical IAM principal.

    An IPrincipal describes a logical entity that can perform AWS API calls
    against sets of resources, optionally under certain conditions.

    Examples of simple principals are IAM objects that you create, such
    as Users or Roles.

    An example of a more complex principals is a ``ServicePrincipal`` (such as
    ``new ServicePrincipal("sns.amazonaws.com")``, which represents the Simple
    Notifications Service).

    A single logical Principal may also map to a set of physical principals.
    For example, ``new OrganizationPrincipal('o-1234')`` represents all
    identities that are part of the given AWS Organization.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IPrincipalProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> "PrincipalPolicyFragment":
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: "PolicyStatement") -> builtins.bool:
        """(deprecated) Add to the policy of this principal.

        :param statement: -

        :return:

        true if the statement was added, false if the principal in
        question does not have a policy document to add the statement to.

        :deprecated: Use ``addToPrincipalPolicy`` instead.

        :stability: deprecated
        """
        ...

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        ...


class _IPrincipalProxy(
    jsii.proxy_for(IGrantable) # type: ignore
):
    """(experimental) Represents a logical IAM principal.

    An IPrincipal describes a logical entity that can perform AWS API calls
    against sets of resources, optionally under certain conditions.

    Examples of simple principals are IAM objects that you create, such
    as Users or Roles.

    An example of a more complex principals is a ``ServicePrincipal`` (such as
    ``new ServicePrincipal("sns.amazonaws.com")``, which represents the Simple
    Notifications Service).

    A single logical Principal may also map to a set of physical principals.
    For example, ``new OrganizationPrincipal('o-1234')`` represents all
    identities that are part of the given AWS Organization.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IPrincipal"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> "PrincipalPolicyFragment":
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        return jsii.get(self, "principalAccount")

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: "PolicyStatement") -> builtins.bool:
        """(deprecated) Add to the policy of this principal.

        :param statement: -

        :return:

        true if the statement was added, false if the principal in
        question does not have a policy document to add the statement to.

        :deprecated: Use ``addToPrincipalPolicy`` instead.

        :stability: deprecated
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])


@jsii.interface(jsii_type="monocdk.aws_iam.IResourceWithPolicy")
class IResourceWithPolicy(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) A resource with a resource policy that can be added to.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IResourceWithPolicyProxy

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToResourcePolicyResult:
        """(experimental) Add a statement to the resource's resource policy.

        :param statement: -

        :stability: experimental
        """
        ...


class _IResourceWithPolicyProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) A resource with a resource policy that can be added to.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IResourceWithPolicy"

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToResourcePolicyResult:
        """(experimental) Add a statement to the resource's resource policy.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement])


@jsii.implements(IManagedPolicy)
class ManagedPolicy(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.ManagedPolicy",
):
    """(experimental) Managed policy.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        document: typing.Optional["PolicyDocument"] = None,
        groups: typing.Optional[typing.List["IGroup"]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.List["IRole"]] = None,
        statements: typing.Optional[typing.List["PolicyStatement"]] = None,
        users: typing.Optional[typing.List["IUser"]] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param description: (experimental) A description of the managed policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed. Default: - empty
        :param document: (experimental) Initial PolicyDocument to use for this ManagedPolicy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param groups: (experimental) Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param managed_policy_name: (experimental) The name of the managed policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - A name is automatically generated.
        :param path: (experimental) The path for the policy. This parameter allows (through its regex pattern) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation characters, digits, and upper and lowercased letters. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: - "/"
        :param roles: (experimental) Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: (experimental) Initial set of permissions to add to this policy document. You can also use ``addPermission(statement)`` to add permissions later. Default: - No statements.
        :param users: (experimental) Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.

        :stability: experimental
        """
        props = ManagedPolicyProps(
            description=description,
            document=document,
            groups=groups,
            managed_policy_name=managed_policy_name,
            path=path,
            roles=roles,
            statements=statements,
            users=users,
        )

        jsii.create(ManagedPolicy, self, [scope, id, props])

    @jsii.member(jsii_name="fromAwsManagedPolicyName")
    @builtins.classmethod
    def from_aws_managed_policy_name(
        cls,
        managed_policy_name: builtins.str,
    ) -> IManagedPolicy:
        """(experimental) Import a managed policy from one of the policies that AWS manages.

        For this managed policy, you only need to know the name to be able to use it.

        Some managed policy names start with "service-role/", some start with
        "job-function/", and some don't start with anything. Do include the
        prefix when constructing this object.

        :param managed_policy_name: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromAwsManagedPolicyName", [managed_policy_name])

    @jsii.member(jsii_name="fromManagedPolicyArn")
    @builtins.classmethod
    def from_managed_policy_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        managed_policy_arn: builtins.str,
    ) -> IManagedPolicy:
        """(experimental) Import an external managed policy by ARN.

        For this managed policy, you only need to know the ARN to be able to use it.
        This can be useful if you got the ARN from a CloudFormation Export.

        If the imported Managed Policy ARN is a Token (such as a
        ``CfnParameter.valueAsString`` or a ``Fn.importValue()``) *and* the referenced
        managed policy has a ``path`` (like ``arn:...:policy/AdminPolicy/AdminAllow``), the
        ``managedPolicyName`` property will not resolve to the correct value. Instead it
        will resolve to the first path component. We unfortunately cannot express
        the correct calculation of the full path name as a CloudFormation
        expression. In this scenario the Managed Policy ARN should be supplied without the
        ``path`` in order to resolve the correct managed policy resource.

        :param scope: construct scope.
        :param id: construct id.
        :param managed_policy_arn: the ARN of the managed policy to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromManagedPolicyArn", [scope, id, managed_policy_arn])

    @jsii.member(jsii_name="fromManagedPolicyName")
    @builtins.classmethod
    def from_managed_policy_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        managed_policy_name: builtins.str,
    ) -> IManagedPolicy:
        """(experimental) Import a customer managed policy from the managedPolicyName.

        For this managed policy, you only need to know the name to be able to use it.

        :param scope: -
        :param id: -
        :param managed_policy_name: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromManagedPolicyName", [scope, id, managed_policy_name])

    @jsii.member(jsii_name="addStatements")
    def add_statements(self, *statement: "PolicyStatement") -> None:
        """(experimental) Adds a statement to the policy document.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addStatements", [*statement])

    @jsii.member(jsii_name="attachToGroup")
    def attach_to_group(self, group: "IGroup") -> None:
        """(experimental) Attaches this policy to a group.

        :param group: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachToGroup", [group])

    @jsii.member(jsii_name="attachToRole")
    def attach_to_role(self, role: "IRole") -> None:
        """(experimental) Attaches this policy to a role.

        :param role: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachToRole", [role])

    @jsii.member(jsii_name="attachToUser")
    def attach_to_user(self, user: "IUser") -> None:
        """(experimental) Attaches this policy to a user.

        :param user: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachToUser", [user])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        """(experimental) Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :stability: experimental
        """
        return jsii.invoke(self, "validate", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        """(experimental) The description of this policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "description")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="document")
    def document(self) -> "PolicyDocument":
        """(experimental) The policy document.

        :stability: experimental
        """
        return jsii.get(self, "document")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        """(experimental) Returns the ARN of this managed policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "managedPolicyArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="managedPolicyName")
    def managed_policy_name(self) -> builtins.str:
        """(experimental) The name of this policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "managedPolicyName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        """(experimental) The path of this policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "path")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.ManagedPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "document": "document",
        "groups": "groups",
        "managed_policy_name": "managedPolicyName",
        "path": "path",
        "roles": "roles",
        "statements": "statements",
        "users": "users",
    },
)
class ManagedPolicyProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        document: typing.Optional["PolicyDocument"] = None,
        groups: typing.Optional[typing.List["IGroup"]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.List["IRole"]] = None,
        statements: typing.Optional[typing.List["PolicyStatement"]] = None,
        users: typing.Optional[typing.List["IUser"]] = None,
    ) -> None:
        """(experimental) Properties for defining an IAM managed policy.

        :param description: (experimental) A description of the managed policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed. Default: - empty
        :param document: (experimental) Initial PolicyDocument to use for this ManagedPolicy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param groups: (experimental) Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param managed_policy_name: (experimental) The name of the managed policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - A name is automatically generated.
        :param path: (experimental) The path for the policy. This parameter allows (through its regex pattern) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation characters, digits, and upper and lowercased letters. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: - "/"
        :param roles: (experimental) Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: (experimental) Initial set of permissions to add to this policy document. You can also use ``addPermission(statement)`` to add permissions later. Default: - No statements.
        :param users: (experimental) Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if document is not None:
            self._values["document"] = document
        if groups is not None:
            self._values["groups"] = groups
        if managed_policy_name is not None:
            self._values["managed_policy_name"] = managed_policy_name
        if path is not None:
            self._values["path"] = path
        if roles is not None:
            self._values["roles"] = roles
        if statements is not None:
            self._values["statements"] = statements
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the managed policy.

        Typically used to store information about the
        permissions defined in the policy. For example, "Grants access to production DynamoDB tables."
        The policy description is immutable. After a value is assigned, it cannot be changed.

        :default: - empty

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def document(self) -> typing.Optional["PolicyDocument"]:
        """(experimental) Initial PolicyDocument to use for this ManagedPolicy.

        If omited, any
        ``PolicyStatement`` provided in the ``statements`` property will be applied
        against the empty default ``PolicyDocument``.

        :default: - An empty policy.

        :stability: experimental
        """
        result = self._values.get("document")
        return result

    @builtins.property
    def groups(self) -> typing.Optional[typing.List["IGroup"]]:
        """(experimental) Groups to attach this policy to.

        You can also use ``attachToGroup(group)`` to attach this policy to a group.

        :default: - No groups.

        :stability: experimental
        """
        result = self._values.get("groups")
        return result

    @builtins.property
    def managed_policy_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the managed policy.

        If you specify multiple policies for an entity,
        specify unique names. For example, if you specify a list of policies for
        an IAM role, each policy must have a unique name.

        :default: - A name is automatically generated.

        :stability: experimental
        """
        result = self._values.get("managed_policy_name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """(experimental) The path for the policy.

        This parameter allows (through its regex pattern) a string of characters
        consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes.
        In addition, it can contain any ASCII character from the ! (\\u0021) through the DEL character (\\u007F),
        including most punctuation characters, digits, and upper and lowercased letters.

        For more information about paths, see IAM Identifiers in the IAM User Guide.

        :default: - "/"

        :stability: experimental
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["IRole"]]:
        """(experimental) Roles to attach this policy to.

        You can also use ``attachToRole(role)`` to attach this policy to a role.

        :default: - No roles.

        :stability: experimental
        """
        result = self._values.get("roles")
        return result

    @builtins.property
    def statements(self) -> typing.Optional[typing.List["PolicyStatement"]]:
        """(experimental) Initial set of permissions to add to this policy document.

        You can also use ``addPermission(statement)`` to add permissions later.

        :default: - No statements.

        :stability: experimental
        """
        result = self._values.get("statements")
        return result

    @builtins.property
    def users(self) -> typing.Optional[typing.List["IUser"]]:
        """(experimental) Users to attach this policy to.

        You can also use ``attachToUser(user)`` to attach this policy to a user.

        :default: - No users.

        :stability: experimental
        """
        result = self._values.get("users")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IOpenIdConnectProvider)
class OpenIdConnectProvider(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.OpenIdConnectProvider",
):
    """(experimental) IAM OIDC identity providers are entities in IAM that describe an external identity provider (IdP) service that supports the OpenID Connect (OIDC) standard, such as Google or Salesforce.

    You use an IAM OIDC identity provider
    when you want to establish trust between an OIDC-compatible IdP and your AWS
    account. This is useful when creating a mobile app or web application that
    requires access to AWS resources, but you don't want to create custom sign-in
    code or manage your own user identities.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html
    :stability: experimental
    :resource: AWS::CloudFormation::CustomResource
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        url: builtins.str,
        client_ids: typing.Optional[typing.List[builtins.str]] = None,
        thumbprints: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """(experimental) Defines an OpenID Connect provider.

        :param scope: The definition scope.
        :param id: Construct ID.
        :param url: (experimental) The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
        :param client_ids: (experimental) A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.) You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider. Client IDs are up to 255 characters long. Default: - no clients are allowed
        :param thumbprints: (experimental) A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates. The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string. You must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com. Default: - If no thumbprints are specified (an empty array or ``undefined``), the thumbprint of the root certificate authority will be obtained from the provider's server as described in https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html

        :stability: experimental
        """
        props = OpenIdConnectProviderProps(
            url=url, client_ids=client_ids, thumbprints=thumbprints
        )

        jsii.create(OpenIdConnectProvider, self, [scope, id, props])

    @jsii.member(jsii_name="fromOpenIdConnectProviderArn")
    @builtins.classmethod
    def from_open_id_connect_provider_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        open_id_connect_provider_arn: builtins.str,
    ) -> IOpenIdConnectProvider:
        """(experimental) Imports an Open ID connect provider from an ARN.

        :param scope: The definition scope.
        :param id: ID of the construct.
        :param open_id_connect_provider_arn: the ARN to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromOpenIdConnectProviderArn", [scope, id, open_id_connect_provider_arn])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectProviderArn")
    def open_id_connect_provider_arn(self) -> builtins.str:
        """(experimental) The Amazon Resource Name (ARN) of the IAM OpenID Connect provider.

        :stability: experimental
        """
        return jsii.get(self, "openIdConnectProviderArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectProviderIssuer")
    def open_id_connect_provider_issuer(self) -> builtins.str:
        """(experimental) The issuer for OIDC Provider.

        :stability: experimental
        """
        return jsii.get(self, "openIdConnectProviderIssuer")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.OpenIdConnectProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "client_ids": "clientIds",
        "thumbprints": "thumbprints",
    },
)
class OpenIdConnectProviderProps:
    def __init__(
        self,
        *,
        url: builtins.str,
        client_ids: typing.Optional[typing.List[builtins.str]] = None,
        thumbprints: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """(experimental) Initialization properties for ``OpenIdConnectProvider``.

        :param url: (experimental) The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
        :param client_ids: (experimental) A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.) You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider. Client IDs are up to 255 characters long. Default: - no clients are allowed
        :param thumbprints: (experimental) A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates. The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string. You must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com. Default: - If no thumbprints are specified (an empty array or ``undefined``), the thumbprint of the root certificate authority will be obtained from the provider's server as described in https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if client_ids is not None:
            self._values["client_ids"] = client_ids
        if thumbprints is not None:
            self._values["thumbprints"] = thumbprints

    @builtins.property
    def url(self) -> builtins.str:
        """(experimental) The URL of the identity provider.

        The URL must begin with https:// and
        should correspond to the iss claim in the provider's OpenID Connect ID
        tokens. Per the OIDC standard, path components are allowed but query
        parameters are not. Typically the URL consists of only a hostname, like
        https://server.example.org or https://example.com.

        You cannot register the same provider multiple times in a single AWS
        account. If you try to submit a URL that has already been used for an
        OpenID Connect provider in the AWS account, you will get an error.

        :stability: experimental
        """
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return result

    @builtins.property
    def client_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) A list of client IDs (also known as audiences).

        When a mobile or web app
        registers with an OpenID Connect provider, they establish a value that
        identifies the application. (This is the value that's sent as the client_id
        parameter on OAuth requests.)

        You can register multiple client IDs with the same provider. For example,
        you might have multiple applications that use the same OIDC provider. You
        cannot register more than 100 client IDs with a single IAM OIDC provider.

        Client IDs are up to 255 characters long.

        :default: - no clients are allowed

        :stability: experimental
        """
        result = self._values.get("client_ids")
        return result

    @builtins.property
    def thumbprints(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates.

        Typically this list includes only one entry. However, IAM lets you have up
        to five thumbprints for an OIDC provider. This lets you maintain multiple
        thumbprints if the identity provider is rotating certificates.

        The server certificate thumbprint is the hex-encoded SHA-1 hash value of
        the X.509 certificate used by the domain where the OpenID Connect provider
        makes its keys available. It is always a 40-character string.

        You must provide at least one thumbprint when creating an IAM OIDC
        provider. For example, assume that the OIDC provider is server.example.com
        and the provider stores its keys at
        https://keys.server.example.com/openid-connect. In that case, the
        thumbprint string would be the hex-encoded SHA-1 hash value of the
        certificate used by https://keys.server.example.com.

        :default:

        - If no thumbprints are specified (an empty array or ``undefined``),
        the thumbprint of the root certificate authority will be obtained from the
        provider's server as described in https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html

        :stability: experimental
        """
        result = self._values.get("thumbprints")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PermissionsBoundary(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.PermissionsBoundary",
):
    """(experimental) Modify the Permissions Boundaries of Users and Roles in a construct tree.

    :stability: experimental

    Example::

        # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
        policy = ManagedPolicy.from_aws_managed_policy_name("ReadOnlyAccess")
        PermissionsBoundary.of(stack).apply(policy)
    """

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, scope: constructs.IConstruct) -> "PermissionsBoundary":
        """(experimental) Access the Permissions Boundaries of a construct tree.

        :param scope: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "of", [scope])

    @jsii.member(jsii_name="apply")
    def apply(self, boundary_policy: IManagedPolicy) -> None:
        """(experimental) Apply the given policy as Permissions Boundary to all Roles in the scope.

        Will override any Permissions Boundaries configured previously; in case
        a Permission Boundary is applied in multiple scopes, the Boundary applied
        closest to the Role wins.

        :param boundary_policy: -

        :stability: experimental
        """
        return jsii.invoke(self, "apply", [boundary_policy])

    @jsii.member(jsii_name="clear")
    def clear(self) -> None:
        """(experimental) Remove previously applied Permissions Boundaries.

        :stability: experimental
        """
        return jsii.invoke(self, "clear", [])


@jsii.implements(IPolicy)
class Policy(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.Policy",
):
    """(experimental) The AWS::IAM::Policy resource associates an IAM policy with IAM users, roles, or groups.

    For more information about IAM policies, see `Overview of IAM
    Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html>`_
    in the IAM User Guide guide.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        document: typing.Optional["PolicyDocument"] = None,
        force: typing.Optional[builtins.bool] = None,
        groups: typing.Optional[typing.List["IGroup"]] = None,
        policy_name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.List["IRole"]] = None,
        statements: typing.Optional[typing.List["PolicyStatement"]] = None,
        users: typing.Optional[typing.List["IUser"]] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param document: (experimental) Initial PolicyDocument to use for this Policy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param force: (experimental) Force creation of an ``AWS::IAM::Policy``. Unless set to ``true``, this ``Policy`` construct will not materialize to an ``AWS::IAM::Policy`` CloudFormation resource in case it would have no effect (for example, if it remains unattached to an IAM identity or if it has no statements). This is generally desired behavior, since it prevents creating invalid--and hence undeployable--CloudFormation templates. In cases where you know the policy must be created and it is actually an error if no statements have been added to it, you can set this to ``true``. Default: false
        :param groups: (experimental) Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param policy_name: (experimental) The name of the policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - Uses the logical ID of the policy resource, which is ensured to be unique within the stack.
        :param roles: (experimental) Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: (experimental) Initial set of permissions to add to this policy document. You can also use ``addStatements(...statement)`` to add permissions later. Default: - No statements.
        :param users: (experimental) Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.

        :stability: experimental
        """
        props = PolicyProps(
            document=document,
            force=force,
            groups=groups,
            policy_name=policy_name,
            roles=roles,
            statements=statements,
            users=users,
        )

        jsii.create(Policy, self, [scope, id, props])

    @jsii.member(jsii_name="fromPolicyName")
    @builtins.classmethod
    def from_policy_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        policy_name: builtins.str,
    ) -> IPolicy:
        """(experimental) Import a policy in this app based on its name.

        :param scope: -
        :param id: -
        :param policy_name: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromPolicyName", [scope, id, policy_name])

    @jsii.member(jsii_name="addStatements")
    def add_statements(self, *statement: "PolicyStatement") -> None:
        """(experimental) Adds a statement to the policy document.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addStatements", [*statement])

    @jsii.member(jsii_name="attachToGroup")
    def attach_to_group(self, group: "IGroup") -> None:
        """(experimental) Attaches this policy to a group.

        :param group: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachToGroup", [group])

    @jsii.member(jsii_name="attachToRole")
    def attach_to_role(self, role: "IRole") -> None:
        """(experimental) Attaches this policy to a role.

        :param role: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachToRole", [role])

    @jsii.member(jsii_name="attachToUser")
    def attach_to_user(self, user: "IUser") -> None:
        """(experimental) Attaches this policy to a user.

        :param user: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachToUser", [user])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        """(experimental) Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :stability: experimental
        """
        return jsii.invoke(self, "validate", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="document")
    def document(self) -> "PolicyDocument":
        """(experimental) The policy document.

        :stability: experimental
        """
        return jsii.get(self, "document")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        """(experimental) The name of this policy.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "policyName")


@jsii.implements(_IResolvable_a771d0ef)
class PolicyDocument(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.PolicyDocument",
):
    """(experimental) A PolicyDocument is a collection of statements.

    :stability: experimental
    """

    def __init__(
        self,
        *,
        assign_sids: typing.Optional[builtins.bool] = None,
        statements: typing.Optional[typing.List["PolicyStatement"]] = None,
    ) -> None:
        """
        :param assign_sids: (experimental) Automatically assign Statement Ids to all statements. Default: false
        :param statements: (experimental) Initial statements to add to the policy document. Default: - No statements

        :stability: experimental
        """
        props = PolicyDocumentProps(assign_sids=assign_sids, statements=statements)

        jsii.create(PolicyDocument, self, [props])

    @jsii.member(jsii_name="fromJson")
    @builtins.classmethod
    def from_json(cls, obj: typing.Any) -> "PolicyDocument":
        """(experimental) Creates a new PolicyDocument based on the object provided.

        This will accept an object created from the ``.toJSON()`` call

        :param obj: the PolicyDocument in object form.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromJson", [obj])

    @jsii.member(jsii_name="addStatements")
    def add_statements(self, *statement: "PolicyStatement") -> None:
        """(experimental) Adds a statement to the policy document.

        :param statement: the statement to add.

        :stability: experimental
        """
        return jsii.invoke(self, "addStatements", [*statement])

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: _IResolveContext_e363e2cb) -> typing.Any:
        """(experimental) Produce the Token's value at resolution time.

        :param context: -

        :stability: experimental
        """
        return jsii.invoke(self, "resolve", [context])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        """(experimental) JSON-ify the document.

        Used when JSON.stringify() is called

        :stability: experimental
        """
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Encode the policy document as a string.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @jsii.member(jsii_name="validateForAnyPolicy")
    def validate_for_any_policy(self) -> typing.List[builtins.str]:
        """(experimental) Validate that all policy statements in the policy document satisfies the requirements for any policy.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
        :stability: experimental
        """
        return jsii.invoke(self, "validateForAnyPolicy", [])

    @jsii.member(jsii_name="validateForIdentityPolicy")
    def validate_for_identity_policy(self) -> typing.List[builtins.str]:
        """(experimental) Validate that all policy statements in the policy document satisfies the requirements for an identity-based policy.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
        :stability: experimental
        """
        return jsii.invoke(self, "validateForIdentityPolicy", [])

    @jsii.member(jsii_name="validateForResourcePolicy")
    def validate_for_resource_policy(self) -> typing.List[builtins.str]:
        """(experimental) Validate that all policy statements in the policy document satisfies the requirements for a resource-based policy.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
        :stability: experimental
        """
        return jsii.invoke(self, "validateForResourcePolicy", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        """(experimental) The creation stack of this resolvable which will be appended to errors thrown during resolution.

        This may return an array with a single informational element indicating how
        to get this property populated, if it was skipped for performance reasons.

        :stability: experimental
        """
        return jsii.get(self, "creationStack")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isEmpty")
    def is_empty(self) -> builtins.bool:
        """(experimental) Whether the policy document contains any statements.

        :stability: experimental
        """
        return jsii.get(self, "isEmpty")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="statementCount")
    def statement_count(self) -> jsii.Number:
        """(experimental) The number of statements already added to this policy.

        Can be used, for example, to generate unique "sid"s within the policy.

        :stability: experimental
        """
        return jsii.get(self, "statementCount")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.PolicyDocumentProps",
    jsii_struct_bases=[],
    name_mapping={"assign_sids": "assignSids", "statements": "statements"},
)
class PolicyDocumentProps:
    def __init__(
        self,
        *,
        assign_sids: typing.Optional[builtins.bool] = None,
        statements: typing.Optional[typing.List["PolicyStatement"]] = None,
    ) -> None:
        """(experimental) Properties for a new PolicyDocument.

        :param assign_sids: (experimental) Automatically assign Statement Ids to all statements. Default: false
        :param statements: (experimental) Initial statements to add to the policy document. Default: - No statements

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if assign_sids is not None:
            self._values["assign_sids"] = assign_sids
        if statements is not None:
            self._values["statements"] = statements

    @builtins.property
    def assign_sids(self) -> typing.Optional[builtins.bool]:
        """(experimental) Automatically assign Statement Ids to all statements.

        :default: false

        :stability: experimental
        """
        result = self._values.get("assign_sids")
        return result

    @builtins.property
    def statements(self) -> typing.Optional[typing.List["PolicyStatement"]]:
        """(experimental) Initial statements to add to the policy document.

        :default: - No statements

        :stability: experimental
        """
        result = self._values.get("statements")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyDocumentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.PolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "document": "document",
        "force": "force",
        "groups": "groups",
        "policy_name": "policyName",
        "roles": "roles",
        "statements": "statements",
        "users": "users",
    },
)
class PolicyProps:
    def __init__(
        self,
        *,
        document: typing.Optional[PolicyDocument] = None,
        force: typing.Optional[builtins.bool] = None,
        groups: typing.Optional[typing.List["IGroup"]] = None,
        policy_name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.List["IRole"]] = None,
        statements: typing.Optional[typing.List["PolicyStatement"]] = None,
        users: typing.Optional[typing.List["IUser"]] = None,
    ) -> None:
        """(experimental) Properties for defining an IAM inline policy document.

        :param document: (experimental) Initial PolicyDocument to use for this Policy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param force: (experimental) Force creation of an ``AWS::IAM::Policy``. Unless set to ``true``, this ``Policy`` construct will not materialize to an ``AWS::IAM::Policy`` CloudFormation resource in case it would have no effect (for example, if it remains unattached to an IAM identity or if it has no statements). This is generally desired behavior, since it prevents creating invalid--and hence undeployable--CloudFormation templates. In cases where you know the policy must be created and it is actually an error if no statements have been added to it, you can set this to ``true``. Default: false
        :param groups: (experimental) Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param policy_name: (experimental) The name of the policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - Uses the logical ID of the policy resource, which is ensured to be unique within the stack.
        :param roles: (experimental) Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: (experimental) Initial set of permissions to add to this policy document. You can also use ``addStatements(...statement)`` to add permissions later. Default: - No statements.
        :param users: (experimental) Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if document is not None:
            self._values["document"] = document
        if force is not None:
            self._values["force"] = force
        if groups is not None:
            self._values["groups"] = groups
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if roles is not None:
            self._values["roles"] = roles
        if statements is not None:
            self._values["statements"] = statements
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def document(self) -> typing.Optional[PolicyDocument]:
        """(experimental) Initial PolicyDocument to use for this Policy.

        If omited, any
        ``PolicyStatement`` provided in the ``statements`` property will be applied
        against the empty default ``PolicyDocument``.

        :default: - An empty policy.

        :stability: experimental
        """
        result = self._values.get("document")
        return result

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        """(experimental) Force creation of an ``AWS::IAM::Policy``.

        Unless set to ``true``, this ``Policy`` construct will not materialize to an
        ``AWS::IAM::Policy`` CloudFormation resource in case it would have no effect
        (for example, if it remains unattached to an IAM identity or if it has no
        statements). This is generally desired behavior, since it prevents
        creating invalid--and hence undeployable--CloudFormation templates.

        In cases where you know the policy must be created and it is actually
        an error if no statements have been added to it, you can set this to ``true``.

        :default: false

        :stability: experimental
        """
        result = self._values.get("force")
        return result

    @builtins.property
    def groups(self) -> typing.Optional[typing.List["IGroup"]]:
        """(experimental) Groups to attach this policy to.

        You can also use ``attachToGroup(group)`` to attach this policy to a group.

        :default: - No groups.

        :stability: experimental
        """
        result = self._values.get("groups")
        return result

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the policy.

        If you specify multiple policies for an entity,
        specify unique names. For example, if you specify a list of policies for
        an IAM role, each policy must have a unique name.

        :default:

        - Uses the logical ID of the policy resource, which is ensured
        to be unique within the stack.

        :stability: experimental
        """
        result = self._values.get("policy_name")
        return result

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["IRole"]]:
        """(experimental) Roles to attach this policy to.

        You can also use ``attachToRole(role)`` to attach this policy to a role.

        :default: - No roles.

        :stability: experimental
        """
        result = self._values.get("roles")
        return result

    @builtins.property
    def statements(self) -> typing.Optional[typing.List["PolicyStatement"]]:
        """(experimental) Initial set of permissions to add to this policy document.

        You can also use ``addStatements(...statement)`` to add permissions later.

        :default: - No statements.

        :stability: experimental
        """
        result = self._values.get("statements")
        return result

    @builtins.property
    def users(self) -> typing.Optional[typing.List["IUser"]]:
        """(experimental) Users to attach this policy to.

        You can also use ``attachToUser(user)`` to attach this policy to a user.

        :default: - No users.

        :stability: experimental
        """
        result = self._values.get("users")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PolicyStatement(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.PolicyStatement",
):
    """(experimental) Represents a statement in an IAM policy document.

    :stability: experimental
    """

    def __init__(
        self,
        *,
        actions: typing.Optional[typing.List[builtins.str]] = None,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        effect: typing.Optional[Effect] = None,
        not_actions: typing.Optional[typing.List[builtins.str]] = None,
        not_principals: typing.Optional[typing.List[IPrincipal]] = None,
        not_resources: typing.Optional[typing.List[builtins.str]] = None,
        principals: typing.Optional[typing.List[IPrincipal]] = None,
        resources: typing.Optional[typing.List[builtins.str]] = None,
        sid: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param actions: (experimental) List of actions to add to the statement. Default: - no actions
        :param conditions: (experimental) Conditions to add to the statement. Default: - no condition
        :param effect: (experimental) Whether to allow or deny the actions in this statement. Default: Effect.ALLOW
        :param not_actions: (experimental) List of not actions to add to the statement. Default: - no not-actions
        :param not_principals: (experimental) List of not principals to add to the statement. Default: - no not principals
        :param not_resources: (experimental) NotResource ARNs to add to the statement. Default: - no not-resources
        :param principals: (experimental) List of principals to add to the statement. Default: - no principals
        :param resources: (experimental) Resource ARNs to add to the statement. Default: - no resources
        :param sid: (experimental) The Sid (statement ID) is an optional identifier that you provide for the policy statement. You can assign a Sid value to each statement in a statement array. In services that let you specify an ID element, such as SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In IAM, the Sid value must be unique within a JSON policy. Default: - no sid

        :stability: experimental
        """
        props = PolicyStatementProps(
            actions=actions,
            conditions=conditions,
            effect=effect,
            not_actions=not_actions,
            not_principals=not_principals,
            not_resources=not_resources,
            principals=principals,
            resources=resources,
            sid=sid,
        )

        jsii.create(PolicyStatement, self, [props])

    @jsii.member(jsii_name="fromJson")
    @builtins.classmethod
    def from_json(cls, obj: typing.Any) -> "PolicyStatement":
        """(experimental) Creates a new PolicyStatement based on the object provided.

        This will accept an object created from the ``.toJSON()`` call

        :param obj: the PolicyStatement in object form.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromJson", [obj])

    @jsii.member(jsii_name="addAccountCondition")
    def add_account_condition(self, account_id: builtins.str) -> None:
        """(experimental) Add a condition that limits to a given account.

        :param account_id: -

        :stability: experimental
        """
        return jsii.invoke(self, "addAccountCondition", [account_id])

    @jsii.member(jsii_name="addAccountRootPrincipal")
    def add_account_root_principal(self) -> None:
        """(experimental) Adds an AWS account root user principal to this policy statement.

        :stability: experimental
        """
        return jsii.invoke(self, "addAccountRootPrincipal", [])

    @jsii.member(jsii_name="addActions")
    def add_actions(self, *actions: builtins.str) -> None:
        """(experimental) Specify allowed actions into the "Action" section of the policy statement.

        :param actions: actions that will be allowed.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html
        :stability: experimental
        """
        return jsii.invoke(self, "addActions", [*actions])

    @jsii.member(jsii_name="addAllResources")
    def add_all_resources(self) -> None:
        """(experimental) Adds a ``"*"`` resource to this statement.

        :stability: experimental
        """
        return jsii.invoke(self, "addAllResources", [])

    @jsii.member(jsii_name="addAnyPrincipal")
    def add_any_principal(self) -> None:
        """(experimental) Adds all identities in all accounts ("*") to this policy statement.

        :stability: experimental
        """
        return jsii.invoke(self, "addAnyPrincipal", [])

    @jsii.member(jsii_name="addArnPrincipal")
    def add_arn_principal(self, arn: builtins.str) -> None:
        """(experimental) Specify a principal using the ARN  identifier of the principal.

        You cannot specify IAM groups and instance profiles as principals.

        :param arn: ARN identifier of AWS account, IAM user, or IAM role (i.e. arn:aws:iam::123456789012:user/user-name).

        :stability: experimental
        """
        return jsii.invoke(self, "addArnPrincipal", [arn])

    @jsii.member(jsii_name="addAwsAccountPrincipal")
    def add_aws_account_principal(self, account_id: builtins.str) -> None:
        """(experimental) Specify AWS account ID as the principal entity to the "Principal" section of a policy statement.

        :param account_id: -

        :stability: experimental
        """
        return jsii.invoke(self, "addAwsAccountPrincipal", [account_id])

    @jsii.member(jsii_name="addCanonicalUserPrincipal")
    def add_canonical_user_principal(self, canonical_user_id: builtins.str) -> None:
        """(experimental) Adds a canonical user ID principal to this policy document.

        :param canonical_user_id: unique identifier assigned by AWS for every account.

        :stability: experimental
        """
        return jsii.invoke(self, "addCanonicalUserPrincipal", [canonical_user_id])

    @jsii.member(jsii_name="addCondition")
    def add_condition(self, key: builtins.str, value: typing.Any) -> None:
        """(experimental) Add a condition to the Policy.

        :param key: -
        :param value: -

        :stability: experimental
        """
        return jsii.invoke(self, "addCondition", [key, value])

    @jsii.member(jsii_name="addConditions")
    def add_conditions(
        self,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        """(experimental) Add multiple conditions to the Policy.

        :param conditions: -

        :stability: experimental
        """
        return jsii.invoke(self, "addConditions", [conditions])

    @jsii.member(jsii_name="addFederatedPrincipal")
    def add_federated_principal(
        self,
        federated: typing.Any,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        """(experimental) Adds a federated identity provider such as Amazon Cognito to this policy statement.

        :param federated: federated identity provider (i.e. 'cognito-identity.amazonaws.com').
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.

        :stability: experimental
        """
        return jsii.invoke(self, "addFederatedPrincipal", [federated, conditions])

    @jsii.member(jsii_name="addNotActions")
    def add_not_actions(self, *not_actions: builtins.str) -> None:
        """(experimental) Explicitly allow all actions except the specified list of actions into the "NotAction" section of the policy document.

        :param not_actions: actions that will be denied. All other actions will be permitted.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html
        :stability: experimental
        """
        return jsii.invoke(self, "addNotActions", [*not_actions])

    @jsii.member(jsii_name="addNotPrincipals")
    def add_not_principals(self, *not_principals: IPrincipal) -> None:
        """(experimental) Specify principals that is not allowed or denied access to the "NotPrincipal" section of a policy statement.

        :param not_principals: IAM principals that will be denied access.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notprincipal.html
        :stability: experimental
        """
        return jsii.invoke(self, "addNotPrincipals", [*not_principals])

    @jsii.member(jsii_name="addNotResources")
    def add_not_resources(self, *arns: builtins.str) -> None:
        """(experimental) Specify resources that this policy statement will not apply to in the "NotResource" section of this policy statement.

        All resources except the specified list will be matched.

        :param arns: Amazon Resource Names (ARNs) of the resources that this policy statement does not apply to.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html
        :stability: experimental
        """
        return jsii.invoke(self, "addNotResources", [*arns])

    @jsii.member(jsii_name="addPrincipals")
    def add_principals(self, *principals: IPrincipal) -> None:
        """(experimental) Adds principals to the "Principal" section of a policy statement.

        :param principals: IAM principals that will be added.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html
        :stability: experimental
        """
        return jsii.invoke(self, "addPrincipals", [*principals])

    @jsii.member(jsii_name="addResources")
    def add_resources(self, *arns: builtins.str) -> None:
        """(experimental) Specify resources that this policy statement applies into the "Resource" section of this policy statement.

        :param arns: Amazon Resource Names (ARNs) of the resources that this policy statement applies to.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html
        :stability: experimental
        """
        return jsii.invoke(self, "addResources", [*arns])

    @jsii.member(jsii_name="addServicePrincipal")
    def add_service_principal(
        self,
        service: builtins.str,
        *,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Adds a service principal to this policy statement.

        :param service: the service name for which a service principal is requested (e.g: ``s3.amazonaws.com``).
        :param conditions: (experimental) Additional conditions to add to the Service Principal. Default: - No conditions
        :param region: (experimental) The region in which the service is operating. Default: the current Stack's region.

        :stability: experimental
        """
        opts = ServicePrincipalOpts(conditions=conditions, region=region)

        return jsii.invoke(self, "addServicePrincipal", [service, opts])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        """(experimental) JSON-ify the statement.

        Used when JSON.stringify() is called

        :stability: experimental
        """
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toStatementJson")
    def to_statement_json(self) -> typing.Any:
        """(experimental) JSON-ify the policy statement.

        Used when JSON.stringify() is called

        :stability: experimental
        """
        return jsii.invoke(self, "toStatementJson", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) String representation of this policy statement.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @jsii.member(jsii_name="validateForAnyPolicy")
    def validate_for_any_policy(self) -> typing.List[builtins.str]:
        """(experimental) Validate that the policy statement satisfies base requirements for a policy.

        :stability: experimental
        """
        return jsii.invoke(self, "validateForAnyPolicy", [])

    @jsii.member(jsii_name="validateForIdentityPolicy")
    def validate_for_identity_policy(self) -> typing.List[builtins.str]:
        """(experimental) Validate that the policy statement satisfies all requirements for an identity-based policy.

        :stability: experimental
        """
        return jsii.invoke(self, "validateForIdentityPolicy", [])

    @jsii.member(jsii_name="validateForResourcePolicy")
    def validate_for_resource_policy(self) -> typing.List[builtins.str]:
        """(experimental) Validate that the policy statement satisfies all requirements for a resource-based policy.

        :stability: experimental
        """
        return jsii.invoke(self, "validateForResourcePolicy", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hasPrincipal")
    def has_principal(self) -> builtins.bool:
        """(experimental) Indicates if this permission has a "Principal" section.

        :stability: experimental
        """
        return jsii.get(self, "hasPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="hasResource")
    def has_resource(self) -> builtins.bool:
        """(experimental) Indicates if this permission as at least one resource associated with it.

        :stability: experimental
        """
        return jsii.get(self, "hasResource")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="effect")
    def effect(self) -> Effect:
        """(experimental) Whether to allow or deny the actions in this statement.

        :stability: experimental
        """
        return jsii.get(self, "effect")

    @effect.setter # type: ignore
    def effect(self, value: Effect) -> None:
        jsii.set(self, "effect", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sid")
    def sid(self) -> typing.Optional[builtins.str]:
        """(experimental) Statement ID for this statement.

        :stability: experimental
        """
        return jsii.get(self, "sid")

    @sid.setter # type: ignore
    def sid(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sid", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iam.PolicyStatementProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "conditions": "conditions",
        "effect": "effect",
        "not_actions": "notActions",
        "not_principals": "notPrincipals",
        "not_resources": "notResources",
        "principals": "principals",
        "resources": "resources",
        "sid": "sid",
    },
)
class PolicyStatementProps:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.List[builtins.str]] = None,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        effect: typing.Optional[Effect] = None,
        not_actions: typing.Optional[typing.List[builtins.str]] = None,
        not_principals: typing.Optional[typing.List[IPrincipal]] = None,
        not_resources: typing.Optional[typing.List[builtins.str]] = None,
        principals: typing.Optional[typing.List[IPrincipal]] = None,
        resources: typing.Optional[typing.List[builtins.str]] = None,
        sid: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Interface for creating a policy statement.

        :param actions: (experimental) List of actions to add to the statement. Default: - no actions
        :param conditions: (experimental) Conditions to add to the statement. Default: - no condition
        :param effect: (experimental) Whether to allow or deny the actions in this statement. Default: Effect.ALLOW
        :param not_actions: (experimental) List of not actions to add to the statement. Default: - no not-actions
        :param not_principals: (experimental) List of not principals to add to the statement. Default: - no not principals
        :param not_resources: (experimental) NotResource ARNs to add to the statement. Default: - no not-resources
        :param principals: (experimental) List of principals to add to the statement. Default: - no principals
        :param resources: (experimental) Resource ARNs to add to the statement. Default: - no resources
        :param sid: (experimental) The Sid (statement ID) is an optional identifier that you provide for the policy statement. You can assign a Sid value to each statement in a statement array. In services that let you specify an ID element, such as SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In IAM, the Sid value must be unique within a JSON policy. Default: - no sid

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if conditions is not None:
            self._values["conditions"] = conditions
        if effect is not None:
            self._values["effect"] = effect
        if not_actions is not None:
            self._values["not_actions"] = not_actions
        if not_principals is not None:
            self._values["not_principals"] = not_principals
        if not_resources is not None:
            self._values["not_resources"] = not_resources
        if principals is not None:
            self._values["principals"] = principals
        if resources is not None:
            self._values["resources"] = resources
        if sid is not None:
            self._values["sid"] = sid

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) List of actions to add to the statement.

        :default: - no actions

        :stability: experimental
        """
        result = self._values.get("actions")
        return result

    @builtins.property
    def conditions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        """(experimental) Conditions to add to the statement.

        :default: - no condition

        :stability: experimental
        """
        result = self._values.get("conditions")
        return result

    @builtins.property
    def effect(self) -> typing.Optional[Effect]:
        """(experimental) Whether to allow or deny the actions in this statement.

        :default: Effect.ALLOW

        :stability: experimental
        """
        result = self._values.get("effect")
        return result

    @builtins.property
    def not_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) List of not actions to add to the statement.

        :default: - no not-actions

        :stability: experimental
        """
        result = self._values.get("not_actions")
        return result

    @builtins.property
    def not_principals(self) -> typing.Optional[typing.List[IPrincipal]]:
        """(experimental) List of not principals to add to the statement.

        :default: - no not principals

        :stability: experimental
        """
        result = self._values.get("not_principals")
        return result

    @builtins.property
    def not_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) NotResource ARNs to add to the statement.

        :default: - no not-resources

        :stability: experimental
        """
        result = self._values.get("not_resources")
        return result

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[IPrincipal]]:
        """(experimental) List of principals to add to the statement.

        :default: - no principals

        :stability: experimental
        """
        result = self._values.get("principals")
        return result

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Resource ARNs to add to the statement.

        :default: - no resources

        :stability: experimental
        """
        result = self._values.get("resources")
        return result

    @builtins.property
    def sid(self) -> typing.Optional[builtins.str]:
        """(experimental) The Sid (statement ID) is an optional identifier that you provide for the policy statement.

        You can assign a Sid value to each statement in a
        statement array. In services that let you specify an ID element, such as
        SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In
        IAM, the Sid value must be unique within a JSON policy.

        :default: - no sid

        :stability: experimental
        """
        result = self._values.get("sid")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyStatementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPrincipal)
class PrincipalBase(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_iam.PrincipalBase",
):
    """(experimental) Base class for policy principals.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _PrincipalBaseProxy

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(PrincipalBase, self, [])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        _statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Add to the policy of this principal.

        :param _statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [_statement])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        """(experimental) JSON-ify the principal.

        Used when JSON.stringify() is called

        :stability: experimental
        """
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @jsii.member(jsii_name="withConditions")
    def with_conditions(
        self,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> IPrincipal:
        """(experimental) Returns a new PrincipalWithConditions using this principal as the base, with the passed conditions added.

        When there is a value for the same operator and key in both the principal and the
        conditions parameter, the value from the conditions parameter will be used.

        :param conditions: -

        :return: a new PrincipalWithConditions object.

        :stability: experimental
        """
        return jsii.invoke(self, "withConditions", [conditions])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    @abc.abstractmethod
    def policy_fragment(self) -> "PrincipalPolicyFragment":
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        return jsii.get(self, "principalAccount")


class _PrincipalBaseProxy(PrincipalBase):
    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> "PrincipalPolicyFragment":
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


class PrincipalPolicyFragment(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.PrincipalPolicyFragment",
):
    """(experimental) A collection of the fields in a PolicyStatement that can be used to identify a principal.

    This consists of the JSON used in the "Principal" field, and optionally a
    set of "Condition"s that need to be applied to the policy.

    :stability: experimental
    """

    def __init__(
        self,
        principal_json: typing.Mapping[builtins.str, typing.List[builtins.str]],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        """
        :param principal_json: JSON of the "Principal" section in a policy statement.
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_. conditions that need to be applied to this policy

        :stability: experimental
        """
        jsii.create(PrincipalPolicyFragment, self, [principal_json, conditions])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Mapping[builtins.str, typing.Any]:
        """(experimental) The conditions under which the policy is in effect.

        See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        conditions that need to be applied to this policy

        :stability: experimental
        """
        return jsii.get(self, "conditions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalJson")
    def principal_json(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        """(experimental) JSON of the "Principal" section in a policy statement.

        :stability: experimental
        """
        return jsii.get(self, "principalJson")


@jsii.implements(IPrincipal)
class PrincipalWithConditions(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.PrincipalWithConditions",
):
    """(experimental) An IAM principal with additional conditions specifying when the policy is in effect.

    For more information about conditions, see:
    https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html

    :stability: experimental
    """

    def __init__(
        self,
        principal: IPrincipal,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        """
        :param principal: -
        :param conditions: -

        :stability: experimental
        """
        jsii.create(PrincipalWithConditions, self, [principal, conditions])

    @jsii.member(jsii_name="addCondition")
    def add_condition(self, key: builtins.str, value: typing.Any) -> None:
        """(experimental) Add a condition to the principal.

        :param key: -
        :param value: -

        :stability: experimental
        """
        return jsii.invoke(self, "addCondition", [key, value])

    @jsii.member(jsii_name="addConditions")
    def add_conditions(
        self,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        """(experimental) Adds multiple conditions to the principal.

        Values from the conditions parameter will overwrite existing values with the same operator
        and key.

        :param conditions: -

        :stability: experimental
        """
        return jsii.invoke(self, "addConditions", [conditions])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        """(experimental) JSON-ify the principal.

        Used when JSON.stringify() is called

        :stability: experimental
        """
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Mapping[builtins.str, typing.Any]:
        """(experimental) The conditions under which the policy is in effect.

        See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.

        :stability: experimental
        """
        return jsii.get(self, "conditions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.RoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "assumed_by": "assumedBy",
        "description": "description",
        "external_id": "externalId",
        "external_ids": "externalIds",
        "inline_policies": "inlinePolicies",
        "managed_policies": "managedPolicies",
        "max_session_duration": "maxSessionDuration",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "role_name": "roleName",
    },
)
class RoleProps:
    def __init__(
        self,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.List[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_070aa057] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for defining an IAM Role.

        :param assumed_by: (experimental) The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: (experimental) A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_id: (deprecated) ID that the role assumer needs to provide when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param external_ids: (experimental) List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: (experimental) A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: (experimental) The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: (experimental) The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: (experimental) AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: (experimental) A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "assumed_by": assumed_by,
        }
        if description is not None:
            self._values["description"] = description
        if external_id is not None:
            self._values["external_id"] = external_id
        if external_ids is not None:
            self._values["external_ids"] = external_ids
        if inline_policies is not None:
            self._values["inline_policies"] = inline_policies
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if max_session_duration is not None:
            self._values["max_session_duration"] = max_session_duration
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def assumed_by(self) -> IPrincipal:
        """(experimental) The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role.

        You can later modify the assume role policy document by accessing it via
        the ``assumeRolePolicy`` property.

        :stability: experimental
        """
        result = self._values.get("assumed_by")
        assert result is not None, "Required property 'assumed_by' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the role.

        It can be up to 1000 characters long.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        """(deprecated) ID that the role assumer needs to provide when assuming this role.

        If the configured and provided external IDs do not match, the
        AssumeRole operation will fail.

        :default: No external ID required

        :deprecated: see {@link externalIds}

        :stability: deprecated
        """
        result = self._values.get("external_id")
        return result

    @builtins.property
    def external_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) List of IDs that the role assumer needs to provide one of when assuming this role.

        If the configured and provided external IDs do not match, the
        AssumeRole operation will fail.

        :default: No external ID required

        :stability: experimental
        """
        result = self._values.get("external_ids")
        return result

    @builtins.property
    def inline_policies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, PolicyDocument]]:
        """(experimental) A list of named policies to inline into this role.

        These policies will be
        created with the role, whereas those added by ``addToPolicy`` are added
        using a separate CloudFormation resource (allowing a way around circular
        dependencies that could otherwise be introduced).

        :default: - No policy is inlined in the Role resource.

        :stability: experimental
        """
        result = self._values.get("inline_policies")
        return result

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[IManagedPolicy]]:
        """(experimental) A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.

        :stability: experimental
        """
        result = self._values.get("managed_policies")
        return result

    @builtins.property
    def max_session_duration(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum session duration that you want to set for the specified role.

        This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours.

        Anyone who assumes the role from the AWS CLI or API can use the
        DurationSeconds API parameter or the duration-seconds CLI parameter to
        request a longer session. The MaxSessionDuration setting determines the
        maximum duration that can be requested using the DurationSeconds
        parameter.

        If users don't specify a value for the DurationSeconds parameter, their
        security credentials are valid for one hour by default. This applies when
        you use the AssumeRole* API operations or the assume-role* CLI operations
        but does not apply when you use those operations to create a console URL.

        :default: Duration.hours(1)

        :stability: experimental
        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
        """
        result = self._values.get("max_session_duration")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """(experimental) The path associated with this role.

        For information about IAM paths, see
        Friendly Names and Paths in IAM User Guide.

        :default: /

        :stability: experimental
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        """(experimental) AWS supports permissions boundaries for IAM entities (users or roles).

        A permissions boundary is an advanced feature for using a managed policy
        to set the maximum permissions that an identity-based policy can grant to
        an IAM entity. An entity's permissions boundary allows it to perform only
        the actions that are allowed by both its identity-based policies and its
        permissions boundaries.

        :default: - No permissions boundary.

        :stability: experimental
        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
        """
        result = self._values.get("permissions_boundary")
        return result

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the IAM role.

        For valid values, see the RoleName parameter for
        the CreateRole action in the IAM API Reference.

        IMPORTANT: If you specify a name, you cannot perform updates that require
        replacement of this resource. You can perform updates that require no or
        some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID
        for the role name.

        :stability: experimental
        """
        result = self._values.get("role_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicePrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.ServicePrincipal",
):
    """(experimental) An IAM principal that represents an AWS service (i.e. sqs.amazonaws.com).

    :stability: experimental
    """

    def __init__(
        self,
        service: builtins.str,
        *,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param service: AWS service (i.e. sqs.amazonaws.com).
        :param conditions: (experimental) Additional conditions to add to the Service Principal. Default: - No conditions
        :param region: (experimental) The region in which the service is operating. Default: the current Stack's region.

        :stability: experimental
        """
        opts = ServicePrincipalOpts(conditions=conditions, region=region)

        jsii.create(ServicePrincipal, self, [service, opts])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        """(experimental) AWS service (i.e. sqs.amazonaws.com).

        :stability: experimental
        """
        return jsii.get(self, "service")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.ServicePrincipalOpts",
    jsii_struct_bases=[],
    name_mapping={"conditions": "conditions", "region": "region"},
)
class ServicePrincipalOpts:
    def __init__(
        self,
        *,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Options for a service principal.

        :param conditions: (experimental) Additional conditions to add to the Service Principal. Default: - No conditions
        :param region: (experimental) The region in which the service is operating. Default: the current Stack's region.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if conditions is not None:
            self._values["conditions"] = conditions
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def conditions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        """(experimental) Additional conditions to add to the Service Principal.

        :default: - No conditions

        :stability: experimental
        """
        result = self._values.get("conditions")
        return result

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        """(experimental) The region in which the service is operating.

        :default: the current Stack's region.

        :stability: experimental
        """
        result = self._values.get("region")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalOpts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPrincipal)
class UnknownPrincipal(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.UnknownPrincipal",
):
    """(experimental) A principal for use in resources that need to have a role but it's unknown.

    Some resources have roles associated with them which they assume, such as
    Lambda Functions, CodeBuild projects, StepFunctions machines, etc.

    When those resources are imported, their actual roles are not always
    imported with them. When that happens, we use an instance of this class
    instead, which will add user warnings when statements are attempted to be
    added to it.

    :stability: experimental
    """

    def __init__(self, *, resource: constructs.IConstruct) -> None:
        """
        :param resource: (experimental) The resource the role proxy is for.

        :stability: experimental
        """
        props = UnknownPrincipalProps(resource=resource)

        jsii.create(UnknownPrincipal, self, [props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.UnknownPrincipalProps",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource"},
)
class UnknownPrincipalProps:
    def __init__(self, *, resource: constructs.IConstruct) -> None:
        """(experimental) Properties for an UnknownPrincipal.

        :param resource: (experimental) The resource the role proxy is for.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "resource": resource,
        }

    @builtins.property
    def resource(self) -> constructs.IConstruct:
        """(experimental) The resource the role proxy is for.

        :stability: experimental
        """
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UnknownPrincipalProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.UserAttributes",
    jsii_struct_bases=[],
    name_mapping={"user_arn": "userArn"},
)
class UserAttributes:
    def __init__(self, *, user_arn: builtins.str) -> None:
        """(experimental) Represents a user defined outside of this stack.

        :param user_arn: (experimental) The ARN of the user. Format: arn::iam:::user/

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "user_arn": user_arn,
        }

    @builtins.property
    def user_arn(self) -> builtins.str:
        """(experimental) The ARN of the user.

        Format: arn::iam:::user/

        :stability: experimental
        """
        result = self._values.get("user_arn")
        assert result is not None, "Required property 'user_arn' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iam.UserProps",
    jsii_struct_bases=[],
    name_mapping={
        "groups": "groups",
        "managed_policies": "managedPolicies",
        "password": "password",
        "password_reset_required": "passwordResetRequired",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "user_name": "userName",
    },
)
class UserProps:
    def __init__(
        self,
        *,
        groups: typing.Optional[typing.List["IGroup"]] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        password: typing.Optional[_SecretValue_c18506ef] = None,
        password_reset_required: typing.Optional[builtins.bool] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for defining an IAM user.

        :param groups: (experimental) Groups to add this user to. You can also use ``addToGroup`` to add this user to a group. Default: - No groups.
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param password: (experimental) The password for the user. This is required so the user can access the AWS Management Console. You can use ``SecretValue.plainText`` to specify a password in plain text or use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in Secrets Manager. Default: - User won't be able to access the management console without a password.
        :param password_reset_required: (experimental) Specifies whether the user is required to set a new password the next time the user logs in to the AWS Management Console. If this is set to 'true', you must also specify "initialPassword". Default: false
        :param path: (experimental) The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: /
        :param permissions_boundary: (experimental) AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param user_name: (experimental) A name for the IAM user. For valid values, see the UserName parameter for the CreateUser action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name. If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - Generated by CloudFormation (recommended)

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if groups is not None:
            self._values["groups"] = groups
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if password is not None:
            self._values["password"] = password
        if password_reset_required is not None:
            self._values["password_reset_required"] = password_reset_required
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def groups(self) -> typing.Optional[typing.List["IGroup"]]:
        """(experimental) Groups to add this user to.

        You can also use ``addToGroup`` to add this
        user to a group.

        :default: - No groups.

        :stability: experimental
        """
        result = self._values.get("groups")
        return result

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[IManagedPolicy]]:
        """(experimental) A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.

        :stability: experimental
        """
        result = self._values.get("managed_policies")
        return result

    @builtins.property
    def password(self) -> typing.Optional[_SecretValue_c18506ef]:
        """(experimental) The password for the user. This is required so the user can access the AWS Management Console.

        You can use ``SecretValue.plainText`` to specify a password in plain text or
        use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in
        Secrets Manager.

        :default: - User won't be able to access the management console without a password.

        :stability: experimental
        """
        result = self._values.get("password")
        return result

    @builtins.property
    def password_reset_required(self) -> typing.Optional[builtins.bool]:
        """(experimental) Specifies whether the user is required to set a new password the next time the user logs in to the AWS Management Console.

        If this is set to 'true', you must also specify "initialPassword".

        :default: false

        :stability: experimental
        """
        result = self._values.get("password_reset_required")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """(experimental) The path for the user name.

        For more information about paths, see IAM
        Identifiers in the IAM User Guide.

        :default: /

        :stability: experimental
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        """(experimental) AWS supports permissions boundaries for IAM entities (users or roles).

        A permissions boundary is an advanced feature for using a managed policy
        to set the maximum permissions that an identity-based policy can grant to
        an IAM entity. An entity's permissions boundary allows it to perform only
        the actions that are allowed by both its identity-based policies and its
        permissions boundaries.

        :default: - No permissions boundary.

        :stability: experimental
        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
        """
        result = self._values.get("permissions_boundary")
        return result

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the IAM user.

        For valid values, see the UserName parameter for
        the CreateUser action in the IAM API Reference. If you don't specify a
        name, AWS CloudFormation generates a unique physical ID and uses that ID
        for the user name.

        If you specify a name, you cannot perform updates that require
        replacement of this resource. You can perform updates that require no or
        some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default: - Generated by CloudFormation (recommended)

        :stability: experimental
        """
        result = self._values.get("user_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ArnPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.ArnPrincipal",
):
    """(experimental) Specify a principal by the Amazon Resource Name (ARN).

    You can specify AWS accounts, IAM users, Federated SAML users, IAM roles, and specific assumed-role sessions.
    You cannot specify IAM groups or instance profiles as principals

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html
    :stability: experimental
    """

    def __init__(self, arn: builtins.str) -> None:
        """
        :param arn: Amazon Resource Name (ARN) of the principal entity (i.e. arn:aws:iam::123456789012:user/user-name).

        :stability: experimental
        """
        jsii.create(ArnPrincipal, self, [arn])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        """(experimental) Amazon Resource Name (ARN) of the principal entity (i.e. arn:aws:iam::123456789012:user/user-name).

        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


class CanonicalUserPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CanonicalUserPrincipal",
):
    """(experimental) A policy principal for canonicalUserIds - useful for S3 bucket policies that use Origin Access identities.

    See https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html

    and

    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html

    for more details.

    :stability: experimental
    """

    def __init__(self, canonical_user_id: builtins.str) -> None:
        """
        :param canonical_user_id: unique identifier assigned by AWS for every account. root user and IAM users for an account all see the same ID. (i.e. 79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be)

        :stability: experimental
        """
        jsii.create(CanonicalUserPrincipal, self, [canonical_user_id])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="canonicalUserId")
    def canonical_user_id(self) -> builtins.str:
        """(experimental) unique identifier assigned by AWS for every account.

        root user and IAM users for an account all see the same ID.
        (i.e. 79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be)

        :stability: experimental
        """
        return jsii.get(self, "canonicalUserId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


class CompositePrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.CompositePrincipal",
):
    """(experimental) Represents a principal that has multiple types of principals.

    A composite principal cannot
    have conditions. i.e. multiple ServicePrincipals that form a composite principal

    :stability: experimental
    """

    def __init__(self, *principals: PrincipalBase) -> None:
        """
        :param principals: -

        :stability: experimental
        """
        jsii.create(CompositePrincipal, self, [*principals])

    @jsii.member(jsii_name="addPrincipals")
    def add_principals(self, *principals: PrincipalBase) -> "CompositePrincipal":
        """(experimental) Adds IAM principals to the composite principal.

        Composite principals cannot have
        conditions.

        :param principals: IAM principals that will be added to the composite principal.

        :stability: experimental
        """
        return jsii.invoke(self, "addPrincipals", [*principals])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


class FederatedPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.FederatedPrincipal",
):
    """(experimental) Principal entity that represents a federated identity provider such as Amazon Cognito, that can be used to provide temporary security credentials to users who have been authenticated.

    Additional condition keys are available when the temporary security credentials are used to make a request.
    You can use these keys to write policies that limit the access of federated users.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif
    :stability: experimental
    """

    def __init__(
        self,
        federated: builtins.str,
        conditions: typing.Mapping[builtins.str, typing.Any],
        assume_role_action: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param federated: federated identity provider (i.e. 'cognito-identity.amazonaws.com' for users authenticated through Cognito).
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        :param assume_role_action: -

        :stability: experimental
        """
        jsii.create(FederatedPrincipal, self, [federated, conditions, assume_role_action])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Mapping[builtins.str, typing.Any]:
        """(experimental) The conditions under which the policy is in effect.

        See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.

        :stability: experimental
        """
        return jsii.get(self, "conditions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="federated")
    def federated(self) -> builtins.str:
        """(experimental) federated identity provider (i.e. 'cognito-identity.amazonaws.com' for users authenticated through Cognito).

        :stability: experimental
        """
        return jsii.get(self, "federated")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


@jsii.interface(jsii_type="monocdk.aws_iam.IIdentity")
class IIdentity(IPrincipal, _IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) A construct that represents an IAM principal, such as a user, group or role.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IIdentityProxy

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        """(experimental) Attaches a managed policy to this principal.

        :param policy: The managed policy.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        """(experimental) Attaches an inline policy to this principal.

        This is the same as calling ``policy.addToXxx(principal)``.

        :param policy: The policy resource to attach to this principal [disable-awslint:ref-via-interface].

        :stability: experimental
        """
        ...


class _IIdentityProxy(
    jsii.proxy_for(IPrincipal), # type: ignore
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore
):
    """(experimental) A construct that represents an IAM principal, such as a user, group or role.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IIdentity"

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        """(experimental) Attaches a managed policy to this principal.

        :param policy: The managed policy.

        :stability: experimental
        """
        return jsii.invoke(self, "addManagedPolicy", [policy])

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        """(experimental) Attaches an inline policy to this principal.

        This is the same as calling ``policy.addToXxx(principal)``.

        :param policy: The policy resource to attach to this principal [disable-awslint:ref-via-interface].

        :stability: experimental
        """
        return jsii.invoke(self, "attachInlinePolicy", [policy])


@jsii.interface(jsii_type="monocdk.aws_iam.IRole")
class IRole(IIdentity, typing_extensions.Protocol):
    """(experimental) A Role object.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IRoleProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """(experimental) Returns the ARN of this role.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        """(experimental) Returns the name of this role.

        :stability: experimental
        :attribute: true
        """
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: IPrincipal, *actions: builtins.str) -> Grant:
        """(experimental) Grant the actions defined in actions to the identity Principal on this resource.

        :param grantee: -
        :param actions: -

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, grantee: IPrincipal) -> Grant:
        """(experimental) Grant permissions to the given principal to pass this role.

        :param grantee: -

        :stability: experimental
        """
        ...


class _IRoleProxy(
    jsii.proxy_for(IIdentity) # type: ignore
):
    """(experimental) A Role object.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IRole"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """(experimental) Returns the ARN of this role.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "roleArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        """(experimental) Returns the name of this role.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "roleName")

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: IPrincipal, *actions: builtins.str) -> Grant:
        """(experimental) Grant the actions defined in actions to the identity Principal on this resource.

        :param grantee: -
        :param actions: -

        :stability: experimental
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, grantee: IPrincipal) -> Grant:
        """(experimental) Grant permissions to the given principal to pass this role.

        :param grantee: -

        :stability: experimental
        """
        return jsii.invoke(self, "grantPassRole", [grantee])


@jsii.interface(jsii_type="monocdk.aws_iam.IUser")
class IUser(IIdentity, typing_extensions.Protocol):
    """(experimental) Represents an IAM user.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IUserProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userArn")
    def user_arn(self) -> builtins.str:
        """(experimental) The user's ARN.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        """(experimental) The user's name.

        :stability: experimental
        :attribute: true
        """
        ...

    @jsii.member(jsii_name="addToGroup")
    def add_to_group(self, group: "IGroup") -> None:
        """(experimental) Adds this user to a group.

        :param group: -

        :stability: experimental
        """
        ...


class _IUserProxy(
    jsii.proxy_for(IIdentity) # type: ignore
):
    """(experimental) Represents an IAM user.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IUser"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userArn")
    def user_arn(self) -> builtins.str:
        """(experimental) The user's ARN.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "userArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        """(experimental) The user's name.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "userName")

    @jsii.member(jsii_name="addToGroup")
    def add_to_group(self, group: "IGroup") -> None:
        """(experimental) Adds this user to a group.

        :param group: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToGroup", [group])


@jsii.implements(IRole)
class LazyRole(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.LazyRole",
):
    """(experimental) An IAM role that only gets attached to the construct tree once it gets used, not before.

    This construct can be used to simplify logic in other constructs
    which need to create a role but only if certain configurations occur
    (such as when AutoScaling is configured). The role can be configured in one
    place, but if it never gets used it doesn't get instantiated and will
    not be synthesized or deployed.

    :stability: experimental
    :resource: AWS::IAM::Role
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.List[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_070aa057] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param assumed_by: (experimental) The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: (experimental) A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_id: (deprecated) ID that the role assumer needs to provide when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param external_ids: (experimental) List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: (experimental) A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: (experimental) The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: (experimental) The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: (experimental) AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: (experimental) A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        :stability: experimental
        """
        props = LazyRoleProps(
            assumed_by=assumed_by,
            description=description,
            external_id=external_id,
            external_ids=external_ids,
            inline_policies=inline_policies,
            managed_policies=managed_policies,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            role_name=role_name,
        )

        jsii.create(LazyRole, self, [scope, id, props])

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        """(experimental) Attaches a managed policy to this role.

        :param policy: The managed policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "addManagedPolicy", [policy])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Adds a permission to the role's default policy document.

        If there is no default policy attached to this role, it will be created.

        :param statement: The permission statement to add to the policy document.

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        """(experimental) Attaches a policy to this role.

        :param policy: The policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "attachInlinePolicy", [policy])

    @jsii.member(jsii_name="grant")
    def grant(self, identity: IPrincipal, *actions: builtins.str) -> Grant:
        """(experimental) Grant the actions defined in actions to the identity Principal on this resource.

        :param identity: -
        :param actions: -

        :stability: experimental
        """
        return jsii.invoke(self, "grant", [identity, *actions])

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, identity: IPrincipal) -> Grant:
        """(experimental) Grant permissions to the given principal to pass this role.

        :param identity: -

        :stability: experimental
        """
        return jsii.invoke(self, "grantPassRole", [identity])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """(experimental) Returns the ARN of this role.

        :stability: experimental
        """
        return jsii.get(self, "roleArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        """(experimental) Returns the stable and unique string identifying the role (i.e. AIDAJQABLZS4A3QDU576Q).

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "roleId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        """(experimental) Returns the name of this role.

        :stability: experimental
        """
        return jsii.get(self, "roleName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        return jsii.get(self, "principalAccount")


@jsii.data_type(
    jsii_type="monocdk.aws_iam.LazyRoleProps",
    jsii_struct_bases=[RoleProps],
    name_mapping={
        "assumed_by": "assumedBy",
        "description": "description",
        "external_id": "externalId",
        "external_ids": "externalIds",
        "inline_policies": "inlinePolicies",
        "managed_policies": "managedPolicies",
        "max_session_duration": "maxSessionDuration",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "role_name": "roleName",
    },
)
class LazyRoleProps(RoleProps):
    def __init__(
        self,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.List[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_070aa057] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for defining a LazyRole.

        :param assumed_by: (experimental) The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: (experimental) A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_id: (deprecated) ID that the role assumer needs to provide when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param external_ids: (experimental) List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: (experimental) A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: (experimental) The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: (experimental) The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: (experimental) AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: (experimental) A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "assumed_by": assumed_by,
        }
        if description is not None:
            self._values["description"] = description
        if external_id is not None:
            self._values["external_id"] = external_id
        if external_ids is not None:
            self._values["external_ids"] = external_ids
        if inline_policies is not None:
            self._values["inline_policies"] = inline_policies
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if max_session_duration is not None:
            self._values["max_session_duration"] = max_session_duration
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def assumed_by(self) -> IPrincipal:
        """(experimental) The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role.

        You can later modify the assume role policy document by accessing it via
        the ``assumeRolePolicy`` property.

        :stability: experimental
        """
        result = self._values.get("assumed_by")
        assert result is not None, "Required property 'assumed_by' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) A description of the role.

        It can be up to 1000 characters long.

        :default: - No description.

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        """(deprecated) ID that the role assumer needs to provide when assuming this role.

        If the configured and provided external IDs do not match, the
        AssumeRole operation will fail.

        :default: No external ID required

        :deprecated: see {@link externalIds}

        :stability: deprecated
        """
        result = self._values.get("external_id")
        return result

    @builtins.property
    def external_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) List of IDs that the role assumer needs to provide one of when assuming this role.

        If the configured and provided external IDs do not match, the
        AssumeRole operation will fail.

        :default: No external ID required

        :stability: experimental
        """
        result = self._values.get("external_ids")
        return result

    @builtins.property
    def inline_policies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, PolicyDocument]]:
        """(experimental) A list of named policies to inline into this role.

        These policies will be
        created with the role, whereas those added by ``addToPolicy`` are added
        using a separate CloudFormation resource (allowing a way around circular
        dependencies that could otherwise be introduced).

        :default: - No policy is inlined in the Role resource.

        :stability: experimental
        """
        result = self._values.get("inline_policies")
        return result

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[IManagedPolicy]]:
        """(experimental) A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.

        :stability: experimental
        """
        result = self._values.get("managed_policies")
        return result

    @builtins.property
    def max_session_duration(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) The maximum session duration that you want to set for the specified role.

        This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours.

        Anyone who assumes the role from the AWS CLI or API can use the
        DurationSeconds API parameter or the duration-seconds CLI parameter to
        request a longer session. The MaxSessionDuration setting determines the
        maximum duration that can be requested using the DurationSeconds
        parameter.

        If users don't specify a value for the DurationSeconds parameter, their
        security credentials are valid for one hour by default. This applies when
        you use the AssumeRole* API operations or the assume-role* CLI operations
        but does not apply when you use those operations to create a console URL.

        :default: Duration.hours(1)

        :stability: experimental
        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
        """
        result = self._values.get("max_session_duration")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """(experimental) The path associated with this role.

        For information about IAM paths, see
        Friendly Names and Paths in IAM User Guide.

        :default: /

        :stability: experimental
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        """(experimental) AWS supports permissions boundaries for IAM entities (users or roles).

        A permissions boundary is an advanced feature for using a managed policy
        to set the maximum permissions that an identity-based policy can grant to
        an IAM entity. An entity's permissions boundary allows it to perform only
        the actions that are allowed by both its identity-based policies and its
        permissions boundaries.

        :default: - No permissions boundary.

        :stability: experimental
        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
        """
        result = self._values.get("permissions_boundary")
        return result

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the IAM role.

        For valid values, see the RoleName parameter for
        the CreateRole action in the IAM API Reference.

        IMPORTANT: If you specify a name, you cannot perform updates that require
        replacement of this resource. You can perform updates that require no or
        some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID
        for the role name.

        :stability: experimental
        """
        result = self._values.get("role_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OrganizationPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.OrganizationPrincipal",
):
    """(experimental) A principal that represents an AWS Organization.

    :stability: experimental
    """

    def __init__(self, organization_id: builtins.str) -> None:
        """
        :param organization_id: The unique identifier (ID) of an organization (i.e. o-12345abcde).

        :stability: experimental
        """
        jsii.create(OrganizationPrincipal, self, [organization_id])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        """(experimental) The unique identifier (ID) of an organization (i.e. o-12345abcde).

        :stability: experimental
        """
        return jsii.get(self, "organizationId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


@jsii.implements(IRole)
class Role(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.Role",
):
    """(experimental) IAM Role.

    Defines an IAM role. The role is created with an assume policy document associated with
    the specified AWS service principal defined in ``serviceAssumeRole``.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.List[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_070aa057] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param assumed_by: (experimental) The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: (experimental) A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_id: (deprecated) ID that the role assumer needs to provide when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param external_ids: (experimental) List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: (experimental) A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: (experimental) The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: (experimental) The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: (experimental) AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: (experimental) A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        :stability: experimental
        """
        props = RoleProps(
            assumed_by=assumed_by,
            description=description,
            external_id=external_id,
            external_ids=external_ids,
            inline_policies=inline_policies,
            managed_policies=managed_policies,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            role_name=role_name,
        )

        jsii.create(Role, self, [scope, id, props])

    @jsii.member(jsii_name="fromRoleArn")
    @builtins.classmethod
    def from_role_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        role_arn: builtins.str,
        *,
        mutable: typing.Optional[builtins.bool] = None,
    ) -> IRole:
        """(experimental) Import an external role by ARN.

        If the imported Role ARN is a Token (such as a
        ``CfnParameter.valueAsString`` or a ``Fn.importValue()``) *and* the referenced
        role has a ``path`` (like ``arn:...:role/AdminRoles/Alice``), the
        ``roleName`` property will not resolve to the correct value. Instead it
        will resolve to the first path component. We unfortunately cannot express
        the correct calculation of the full path name as a CloudFormation
        expression. In this scenario the Role ARN should be supplied without the
        ``path`` in order to resolve the correct role resource.

        :param scope: construct scope.
        :param id: construct id.
        :param role_arn: the ARN of the role to import.
        :param mutable: (experimental) Whether the imported role can be modified by attaching policy resources to it. Default: true

        :stability: experimental
        """
        options = FromRoleArnOptions(mutable=mutable)

        return jsii.sinvoke(cls, "fromRoleArn", [scope, id, role_arn, options])

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        """(experimental) Attaches a managed policy to this role.

        :param policy: The the managed policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "addManagedPolicy", [policy])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Adds a permission to the role's default policy document.

        If there is no default policy attached to this role, it will be created.

        :param statement: The permission statement to add to the policy document.

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        """(experimental) Attaches a policy to this role.

        :param policy: The policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "attachInlinePolicy", [policy])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: IPrincipal, *actions: builtins.str) -> Grant:
        """(experimental) Grant the actions defined in actions to the identity Principal on this resource.

        :param grantee: -
        :param actions: -

        :stability: experimental
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, identity: IPrincipal) -> Grant:
        """(experimental) Grant permissions to the given principal to pass this role.

        :param identity: -

        :stability: experimental
        """
        return jsii.invoke(self, "grantPassRole", [identity])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        """(experimental) Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :stability: experimental
        """
        return jsii.invoke(self, "validate", [])

    @jsii.member(jsii_name="withoutPolicyUpdates")
    def without_policy_updates(self) -> IRole:
        """(experimental) Return a copy of this Role object whose Policies will not be updated.

        Use the object returned by this method if you want this Role to be used by
        a construct without it automatically updating the Role's Policies.

        If you do, you are responsible for adding the correct statements to the
        Role's policies yourself.

        :stability: experimental
        """
        return jsii.invoke(self, "withoutPolicyUpdates", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Returns the role.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """(experimental) Returns the ARN of this role.

        :stability: experimental
        """
        return jsii.get(self, "roleArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        """(experimental) Returns the stable and unique string identifying the role.

        For example,
        AIDAJQABLZS4A3QDU576Q.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "roleId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        """(experimental) Returns the name of the role.

        :stability: experimental
        """
        return jsii.get(self, "roleName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRolePolicy")
    def assume_role_policy(self) -> typing.Optional[PolicyDocument]:
        """(experimental) The assume role policy document associated with this role.

        :stability: experimental
        """
        return jsii.get(self, "assumeRolePolicy")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        """(experimental) Returns the permissions boundary attached to this role.

        :stability: experimental
        """
        return jsii.get(self, "permissionsBoundary")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        return jsii.get(self, "principalAccount")


@jsii.implements(IIdentity, IUser)
class User(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.User",
):
    """(experimental) Define a new IAM user.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        groups: typing.Optional[typing.List["IGroup"]] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        password: typing.Optional[_SecretValue_c18506ef] = None,
        password_reset_required: typing.Optional[builtins.bool] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param groups: (experimental) Groups to add this user to. You can also use ``addToGroup`` to add this user to a group. Default: - No groups.
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param password: (experimental) The password for the user. This is required so the user can access the AWS Management Console. You can use ``SecretValue.plainText`` to specify a password in plain text or use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in Secrets Manager. Default: - User won't be able to access the management console without a password.
        :param password_reset_required: (experimental) Specifies whether the user is required to set a new password the next time the user logs in to the AWS Management Console. If this is set to 'true', you must also specify "initialPassword". Default: false
        :param path: (experimental) The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: /
        :param permissions_boundary: (experimental) AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param user_name: (experimental) A name for the IAM user. For valid values, see the UserName parameter for the CreateUser action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name. If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - Generated by CloudFormation (recommended)

        :stability: experimental
        """
        props = UserProps(
            groups=groups,
            managed_policies=managed_policies,
            password=password,
            password_reset_required=password_reset_required,
            path=path,
            permissions_boundary=permissions_boundary,
            user_name=user_name,
        )

        jsii.create(User, self, [scope, id, props])

    @jsii.member(jsii_name="fromUserArn")
    @builtins.classmethod
    def from_user_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        user_arn: builtins.str,
    ) -> IUser:
        """(experimental) Import an existing user given a user ARN.

        :param scope: construct scope.
        :param id: construct id.
        :param user_arn: the ARN of an existing user to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromUserArn", [scope, id, user_arn])

    @jsii.member(jsii_name="fromUserAttributes")
    @builtins.classmethod
    def from_user_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        user_arn: builtins.str,
    ) -> IUser:
        """(experimental) Import an existing user given user attributes.

        :param scope: construct scope.
        :param id: construct id.
        :param user_arn: (experimental) The ARN of the user. Format: arn::iam:::user/

        :stability: experimental
        """
        attrs = UserAttributes(user_arn=user_arn)

        return jsii.sinvoke(cls, "fromUserAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="fromUserName")
    @builtins.classmethod
    def from_user_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        user_name: builtins.str,
    ) -> IUser:
        """(experimental) Import an existing user given a username.

        :param scope: construct scope.
        :param id: construct id.
        :param user_name: the username of the existing user to import.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromUserName", [scope, id, user_name])

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        """(experimental) Attaches a managed policy to the user.

        :param policy: The managed policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "addManagedPolicy", [policy])

    @jsii.member(jsii_name="addToGroup")
    def add_to_group(self, group: "IGroup") -> None:
        """(experimental) Adds this user to a group.

        :param group: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToGroup", [group])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Adds an IAM statement to the default policy.

        :param statement: -

        :return: true

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        """(experimental) Attaches a policy to this user.

        :param policy: -

        :stability: experimental
        """
        return jsii.invoke(self, "attachInlinePolicy", [policy])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userArn")
    def user_arn(self) -> builtins.str:
        """(experimental) An attribute that represents the user's ARN.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "userArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        """(experimental) An attribute that represents the user name.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "userName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        """(experimental) Returns the permissions boundary attached to this user.

        :stability: experimental
        """
        return jsii.get(self, "permissionsBoundary")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        return jsii.get(self, "principalAccount")


class WebIdentityPrincipal(
    FederatedPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.WebIdentityPrincipal",
):
    """(experimental) A principal that represents a federated identity provider as Web Identity such as Cognito, Amazon, Facebook, Google, etc.

    :stability: experimental
    """

    def __init__(
        self,
        identity_provider: builtins.str,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        """
        :param identity_provider: identity provider (i.e. 'cognito-identity.amazonaws.com' for users authenticated through Cognito).
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.

        :stability: experimental
        """
        jsii.create(WebIdentityPrincipal, self, [identity_provider, conditions])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


class AccountPrincipal(
    ArnPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.AccountPrincipal",
):
    """(experimental) Specify AWS account ID as the principal entity in a policy to delegate authority to the account.

    :stability: experimental
    """

    def __init__(self, account_id: typing.Any) -> None:
        """
        :param account_id: AWS account ID (i.e. 123456789012).

        :stability: experimental
        """
        jsii.create(AccountPrincipal, self, [account_id])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Any:
        """(experimental) AWS account ID (i.e. 123456789012).

        :stability: experimental
        """
        return jsii.get(self, "accountId")


class AccountRootPrincipal(
    AccountPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.AccountRootPrincipal",
):
    """(experimental) Use the AWS account into which a stack is deployed as the principal entity in a policy.

    :stability: experimental
    """

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(AccountRootPrincipal, self, [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])


class AnyPrincipal(
    ArnPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.AnyPrincipal",
):
    """(experimental) A principal representing all identities in all accounts.

    :stability: experimental
    """

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(AnyPrincipal, self, [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])


class Anyone(AnyPrincipal, metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_iam.Anyone"):
    """(deprecated) A principal representing all identities in all accounts.

    :deprecated: use ``AnyPrincipal``

    :stability: deprecated
    """

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(Anyone, self, [])


@jsii.interface(jsii_type="monocdk.aws_iam.IGroup")
class IGroup(IIdentity, typing_extensions.Protocol):
    """(experimental) Represents an IAM Group.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IGroupProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groupArn")
    def group_arn(self) -> builtins.str:
        """(experimental) Returns the IAM Group ARN.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        """(experimental) Returns the IAM Group Name.

        :stability: experimental
        :attribute: true
        """
        ...


class _IGroupProxy(
    jsii.proxy_for(IIdentity) # type: ignore
):
    """(experimental) Represents an IAM Group.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iam.IGroup"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groupArn")
    def group_arn(self) -> builtins.str:
        """(experimental) Returns the IAM Group ARN.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "groupArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        """(experimental) Returns the IAM Group Name.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "groupName")


class OpenIdConnectPrincipal(
    WebIdentityPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.OpenIdConnectPrincipal",
):
    """(experimental) A principal that represents a federated identity provider as from a OpenID Connect provider.

    :stability: experimental
    """

    def __init__(
        self,
        open_id_connect_provider: IOpenIdConnectProvider,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        """
        :param open_id_connect_provider: OpenID Connect provider.
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.

        :stability: experimental
        """
        jsii.create(OpenIdConnectPrincipal, self, [open_id_connect_provider, conditions])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Returns a string representation of an object.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")


@jsii.implements(IGroup)
class Group(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iam.Group",
):
    """(experimental) An IAM Group (collection of IAM users) lets you specify permissions for multiple users, which can make it easier to manage permissions for those users.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policies: typing.Optional[typing.List[IManagedPolicy]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param group_name: (experimental) A name for the IAM group. For valid values, see the GroupName parameter for the CreateGroup action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: Generated by CloudFormation (recommended)
        :param managed_policies: (experimental) A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param path: (experimental) The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`_ in the IAM User Guide. Default: /

        :stability: experimental
        """
        props = GroupProps(
            group_name=group_name, managed_policies=managed_policies, path=path
        )

        jsii.create(Group, self, [scope, id, props])

    @jsii.member(jsii_name="fromGroupArn")
    @builtins.classmethod
    def from_group_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        group_arn: builtins.str,
    ) -> IGroup:
        """(experimental) Import an external group by ARN.

        If the imported Group ARN is a Token (such as a
        ``CfnParameter.valueAsString`` or a ``Fn.importValue()``) *and* the referenced
        group has a ``path`` (like ``arn:...:group/AdminGroup/NetworkAdmin``), the
        ``groupName`` property will not resolve to the correct value. Instead it
        will resolve to the first path component. We unfortunately cannot express
        the correct calculation of the full path name as a CloudFormation
        expression. In this scenario the Group ARN should be supplied without the
        ``path`` in order to resolve the correct group resource.

        :param scope: construct scope.
        :param id: construct id.
        :param group_arn: the ARN of the group to import (e.g. ``arn:aws:iam::account-id:group/group-name``).

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromGroupArn", [scope, id, group_arn])

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        """(experimental) Attaches a managed policy to this group.

        :param policy: The managed policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "addManagedPolicy", [policy])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        """(experimental) Add to the policy of this principal.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        """(experimental) Adds an IAM statement to the default policy.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToPrincipalPolicy", [statement])

    @jsii.member(jsii_name="addUser")
    def add_user(self, user: IUser) -> None:
        """(experimental) Adds a user to this group.

        :param user: -

        :stability: experimental
        """
        return jsii.invoke(self, "addUser", [user])

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        """(experimental) Attaches a policy to this group.

        :param policy: The policy to attach.

        :stability: experimental
        """
        return jsii.invoke(self, "attachInlinePolicy", [policy])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        """(experimental) When this Principal is used in an AssumeRole policy, the action to use.

        :stability: experimental
        """
        return jsii.get(self, "assumeRoleAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        """(experimental) The principal to grant permissions to.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groupArn")
    def group_arn(self) -> builtins.str:
        """(experimental) Returns the IAM Group ARN.

        :stability: experimental
        """
        return jsii.get(self, "groupArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        """(experimental) Returns the IAM Group Name.

        :stability: experimental
        """
        return jsii.get(self, "groupName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        """(experimental) Return the policy fragment that identifies this principal in a Policy.

        :stability: experimental
        """
        return jsii.get(self, "policyFragment")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        """(experimental) The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.

        :stability: experimental
        """
        return jsii.get(self, "principalAccount")


__all__ = [
    "AccountPrincipal",
    "AccountRootPrincipal",
    "AddToPrincipalPolicyResult",
    "AddToResourcePolicyResult",
    "AnyPrincipal",
    "Anyone",
    "ArnPrincipal",
    "CanonicalUserPrincipal",
    "CfnAccessKey",
    "CfnAccessKeyProps",
    "CfnGroup",
    "CfnGroupProps",
    "CfnInstanceProfile",
    "CfnInstanceProfileProps",
    "CfnManagedPolicy",
    "CfnManagedPolicyProps",
    "CfnPolicy",
    "CfnPolicyProps",
    "CfnRole",
    "CfnRoleProps",
    "CfnServiceLinkedRole",
    "CfnServiceLinkedRoleProps",
    "CfnUser",
    "CfnUserProps",
    "CfnUserToGroupAddition",
    "CfnUserToGroupAdditionProps",
    "CommonGrantOptions",
    "CompositeDependable",
    "CompositePrincipal",
    "Effect",
    "FederatedPrincipal",
    "FromRoleArnOptions",
    "Grant",
    "GrantOnPrincipalAndResourceOptions",
    "GrantOnPrincipalOptions",
    "GrantWithResourceOptions",
    "Group",
    "GroupProps",
    "IGrantable",
    "IGroup",
    "IIdentity",
    "IManagedPolicy",
    "IOpenIdConnectProvider",
    "IPolicy",
    "IPrincipal",
    "IResourceWithPolicy",
    "IRole",
    "IUser",
    "LazyRole",
    "LazyRoleProps",
    "ManagedPolicy",
    "ManagedPolicyProps",
    "OpenIdConnectPrincipal",
    "OpenIdConnectProvider",
    "OpenIdConnectProviderProps",
    "OrganizationPrincipal",
    "PermissionsBoundary",
    "Policy",
    "PolicyDocument",
    "PolicyDocumentProps",
    "PolicyProps",
    "PolicyStatement",
    "PolicyStatementProps",
    "PrincipalBase",
    "PrincipalPolicyFragment",
    "PrincipalWithConditions",
    "Role",
    "RoleProps",
    "ServicePrincipal",
    "ServicePrincipalOpts",
    "UnknownPrincipal",
    "UnknownPrincipalProps",
    "User",
    "UserAttributes",
    "UserProps",
    "WebIdentityPrincipal",
]

publication.publish()
