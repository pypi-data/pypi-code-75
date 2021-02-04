import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnServer(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_opsworkscm.CfnServer",
):
    """A CloudFormation ``AWS::OpsWorksCM::Server``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html
    :cloudformationResource: AWS::OpsWorksCM::Server
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        instance_profile_arn: builtins.str,
        instance_type: builtins.str,
        service_role_arn: builtins.str,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        backup_id: typing.Optional[builtins.str] = None,
        backup_retention_count: typing.Optional[jsii.Number] = None,
        custom_certificate: typing.Optional[builtins.str] = None,
        custom_domain: typing.Optional[builtins.str] = None,
        custom_private_key: typing.Optional[builtins.str] = None,
        disable_automated_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_attributes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnServer.EngineAttributeProperty", _IResolvable_a771d0ef]]]] = None,
        engine_model: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
        server_name: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.List[builtins.str]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::OpsWorksCM::Server``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_profile_arn: ``AWS::OpsWorksCM::Server.InstanceProfileArn``.
        :param instance_type: ``AWS::OpsWorksCM::Server.InstanceType``.
        :param service_role_arn: ``AWS::OpsWorksCM::Server.ServiceRoleArn``.
        :param associate_public_ip_address: ``AWS::OpsWorksCM::Server.AssociatePublicIpAddress``.
        :param backup_id: ``AWS::OpsWorksCM::Server.BackupId``.
        :param backup_retention_count: ``AWS::OpsWorksCM::Server.BackupRetentionCount``.
        :param custom_certificate: ``AWS::OpsWorksCM::Server.CustomCertificate``.
        :param custom_domain: ``AWS::OpsWorksCM::Server.CustomDomain``.
        :param custom_private_key: ``AWS::OpsWorksCM::Server.CustomPrivateKey``.
        :param disable_automated_backup: ``AWS::OpsWorksCM::Server.DisableAutomatedBackup``.
        :param engine: ``AWS::OpsWorksCM::Server.Engine``.
        :param engine_attributes: ``AWS::OpsWorksCM::Server.EngineAttributes``.
        :param engine_model: ``AWS::OpsWorksCM::Server.EngineModel``.
        :param engine_version: ``AWS::OpsWorksCM::Server.EngineVersion``.
        :param key_pair: ``AWS::OpsWorksCM::Server.KeyPair``.
        :param preferred_backup_window: ``AWS::OpsWorksCM::Server.PreferredBackupWindow``.
        :param preferred_maintenance_window: ``AWS::OpsWorksCM::Server.PreferredMaintenanceWindow``.
        :param security_group_ids: ``AWS::OpsWorksCM::Server.SecurityGroupIds``.
        :param server_name: ``AWS::OpsWorksCM::Server.ServerName``.
        :param subnet_ids: ``AWS::OpsWorksCM::Server.SubnetIds``.
        :param tags: ``AWS::OpsWorksCM::Server.Tags``.
        """
        props = CfnServerProps(
            instance_profile_arn=instance_profile_arn,
            instance_type=instance_type,
            service_role_arn=service_role_arn,
            associate_public_ip_address=associate_public_ip_address,
            backup_id=backup_id,
            backup_retention_count=backup_retention_count,
            custom_certificate=custom_certificate,
            custom_domain=custom_domain,
            custom_private_key=custom_private_key,
            disable_automated_backup=disable_automated_backup,
            engine=engine,
            engine_attributes=engine_attributes,
            engine_model=engine_model,
            engine_version=engine_version,
            key_pair=key_pair,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            security_group_ids=security_group_ids,
            server_name=server_name,
            subnet_ids=subnet_ids,
            tags=tags,
        )

        jsii.create(CfnServer, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        """
        :cloudformationAttribute: Endpoint
        """
        return jsii.get(self, "attrEndpoint")

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::OpsWorksCM::Server.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        """``AWS::OpsWorksCM::Server.InstanceProfileArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-instanceprofilearn
        """
        return jsii.get(self, "instanceProfileArn")

    @instance_profile_arn.setter # type: ignore
    def instance_profile_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        """``AWS::OpsWorksCM::Server.InstanceType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-instancetype
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter # type: ignore
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        """``AWS::OpsWorksCM::Server.ServiceRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-servicerolearn
        """
        return jsii.get(self, "serviceRoleArn")

    @service_role_arn.setter # type: ignore
    def service_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::OpsWorksCM::Server.AssociatePublicIpAddress``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-associatepublicipaddress
        """
        return jsii.get(self, "associatePublicIpAddress")

    @associate_public_ip_address.setter # type: ignore
    def associate_public_ip_address(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="backupId")
    def backup_id(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.BackupId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-backupid
        """
        return jsii.get(self, "backupId")

    @backup_id.setter # type: ignore
    def backup_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "backupId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="backupRetentionCount")
    def backup_retention_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::OpsWorksCM::Server.BackupRetentionCount``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-backupretentioncount
        """
        return jsii.get(self, "backupRetentionCount")

    @backup_retention_count.setter # type: ignore
    def backup_retention_count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "backupRetentionCount", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="customCertificate")
    def custom_certificate(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.CustomCertificate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customcertificate
        """
        return jsii.get(self, "customCertificate")

    @custom_certificate.setter # type: ignore
    def custom_certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customCertificate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="customDomain")
    def custom_domain(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.CustomDomain``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customdomain
        """
        return jsii.get(self, "customDomain")

    @custom_domain.setter # type: ignore
    def custom_domain(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customDomain", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="customPrivateKey")
    def custom_private_key(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.CustomPrivateKey``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customprivatekey
        """
        return jsii.get(self, "customPrivateKey")

    @custom_private_key.setter # type: ignore
    def custom_private_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customPrivateKey", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="disableAutomatedBackup")
    def disable_automated_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::OpsWorksCM::Server.DisableAutomatedBackup``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-disableautomatedbackup
        """
        return jsii.get(self, "disableAutomatedBackup")

    @disable_automated_backup.setter # type: ignore
    def disable_automated_backup(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "disableAutomatedBackup", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.Engine``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engine
        """
        return jsii.get(self, "engine")

    @engine.setter # type: ignore
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engine", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="engineAttributes")
    def engine_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnServer.EngineAttributeProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::OpsWorksCM::Server.EngineAttributes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engineattributes
        """
        return jsii.get(self, "engineAttributes")

    @engine_attributes.setter # type: ignore
    def engine_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnServer.EngineAttributeProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "engineAttributes", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="engineModel")
    def engine_model(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.EngineModel``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-enginemodel
        """
        return jsii.get(self, "engineModel")

    @engine_model.setter # type: ignore
    def engine_model(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engineModel", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.EngineVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engineversion
        """
        return jsii.get(self, "engineVersion")

    @engine_version.setter # type: ignore
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engineVersion", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.KeyPair``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-keypair
        """
        return jsii.get(self, "keyPair")

    @key_pair.setter # type: ignore
    def key_pair(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "keyPair", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.PreferredBackupWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-preferredbackupwindow
        """
        return jsii.get(self, "preferredBackupWindow")

    @preferred_backup_window.setter # type: ignore
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.PreferredMaintenanceWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-preferredmaintenancewindow
        """
        return jsii.get(self, "preferredMaintenanceWindow")

    @preferred_maintenance_window.setter # type: ignore
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::OpsWorksCM::Server.SecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-securitygroupids
        """
        return jsii.get(self, "securityGroupIds")

    @security_group_ids.setter # type: ignore
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.ServerName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-servername
        """
        return jsii.get(self, "serverName")

    @server_name.setter # type: ignore
    def server_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serverName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::OpsWorksCM::Server.SubnetIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-subnetids
        """
        return jsii.get(self, "subnetIds")

    @subnet_ids.setter # type: ignore
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "subnetIds", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_opsworkscm.CfnServer.EngineAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EngineAttributeProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param name: ``CfnServer.EngineAttributeProperty.Name``.
            :param value: ``CfnServer.EngineAttributeProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnServer.EngineAttributeProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html#cfn-opsworkscm-server-engineattribute-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            """``CfnServer.EngineAttributeProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html#cfn-opsworkscm-server-engineattribute-value
            """
            result = self._values.get("value")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EngineAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_opsworkscm.CfnServerProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_arn": "instanceProfileArn",
        "instance_type": "instanceType",
        "service_role_arn": "serviceRoleArn",
        "associate_public_ip_address": "associatePublicIpAddress",
        "backup_id": "backupId",
        "backup_retention_count": "backupRetentionCount",
        "custom_certificate": "customCertificate",
        "custom_domain": "customDomain",
        "custom_private_key": "customPrivateKey",
        "disable_automated_backup": "disableAutomatedBackup",
        "engine": "engine",
        "engine_attributes": "engineAttributes",
        "engine_model": "engineModel",
        "engine_version": "engineVersion",
        "key_pair": "keyPair",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "security_group_ids": "securityGroupIds",
        "server_name": "serverName",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnServerProps:
    def __init__(
        self,
        *,
        instance_profile_arn: builtins.str,
        instance_type: builtins.str,
        service_role_arn: builtins.str,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        backup_id: typing.Optional[builtins.str] = None,
        backup_retention_count: typing.Optional[jsii.Number] = None,
        custom_certificate: typing.Optional[builtins.str] = None,
        custom_domain: typing.Optional[builtins.str] = None,
        custom_private_key: typing.Optional[builtins.str] = None,
        disable_automated_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_attributes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnServer.EngineAttributeProperty, _IResolvable_a771d0ef]]]] = None,
        engine_model: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
        server_name: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.List[builtins.str]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::OpsWorksCM::Server``.

        :param instance_profile_arn: ``AWS::OpsWorksCM::Server.InstanceProfileArn``.
        :param instance_type: ``AWS::OpsWorksCM::Server.InstanceType``.
        :param service_role_arn: ``AWS::OpsWorksCM::Server.ServiceRoleArn``.
        :param associate_public_ip_address: ``AWS::OpsWorksCM::Server.AssociatePublicIpAddress``.
        :param backup_id: ``AWS::OpsWorksCM::Server.BackupId``.
        :param backup_retention_count: ``AWS::OpsWorksCM::Server.BackupRetentionCount``.
        :param custom_certificate: ``AWS::OpsWorksCM::Server.CustomCertificate``.
        :param custom_domain: ``AWS::OpsWorksCM::Server.CustomDomain``.
        :param custom_private_key: ``AWS::OpsWorksCM::Server.CustomPrivateKey``.
        :param disable_automated_backup: ``AWS::OpsWorksCM::Server.DisableAutomatedBackup``.
        :param engine: ``AWS::OpsWorksCM::Server.Engine``.
        :param engine_attributes: ``AWS::OpsWorksCM::Server.EngineAttributes``.
        :param engine_model: ``AWS::OpsWorksCM::Server.EngineModel``.
        :param engine_version: ``AWS::OpsWorksCM::Server.EngineVersion``.
        :param key_pair: ``AWS::OpsWorksCM::Server.KeyPair``.
        :param preferred_backup_window: ``AWS::OpsWorksCM::Server.PreferredBackupWindow``.
        :param preferred_maintenance_window: ``AWS::OpsWorksCM::Server.PreferredMaintenanceWindow``.
        :param security_group_ids: ``AWS::OpsWorksCM::Server.SecurityGroupIds``.
        :param server_name: ``AWS::OpsWorksCM::Server.ServerName``.
        :param subnet_ids: ``AWS::OpsWorksCM::Server.SubnetIds``.
        :param tags: ``AWS::OpsWorksCM::Server.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "instance_profile_arn": instance_profile_arn,
            "instance_type": instance_type,
            "service_role_arn": service_role_arn,
        }
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if backup_retention_count is not None:
            self._values["backup_retention_count"] = backup_retention_count
        if custom_certificate is not None:
            self._values["custom_certificate"] = custom_certificate
        if custom_domain is not None:
            self._values["custom_domain"] = custom_domain
        if custom_private_key is not None:
            self._values["custom_private_key"] = custom_private_key
        if disable_automated_backup is not None:
            self._values["disable_automated_backup"] = disable_automated_backup
        if engine is not None:
            self._values["engine"] = engine
        if engine_attributes is not None:
            self._values["engine_attributes"] = engine_attributes
        if engine_model is not None:
            self._values["engine_model"] = engine_model
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if server_name is not None:
            self._values["server_name"] = server_name
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_profile_arn(self) -> builtins.str:
        """``AWS::OpsWorksCM::Server.InstanceProfileArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-instanceprofilearn
        """
        result = self._values.get("instance_profile_arn")
        assert result is not None, "Required property 'instance_profile_arn' is missing"
        return result

    @builtins.property
    def instance_type(self) -> builtins.str:
        """``AWS::OpsWorksCM::Server.InstanceType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-instancetype
        """
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return result

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        """``AWS::OpsWorksCM::Server.ServiceRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-servicerolearn
        """
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return result

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::OpsWorksCM::Server.AssociatePublicIpAddress``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-associatepublicipaddress
        """
        result = self._values.get("associate_public_ip_address")
        return result

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.BackupId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-backupid
        """
        result = self._values.get("backup_id")
        return result

    @builtins.property
    def backup_retention_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::OpsWorksCM::Server.BackupRetentionCount``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-backupretentioncount
        """
        result = self._values.get("backup_retention_count")
        return result

    @builtins.property
    def custom_certificate(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.CustomCertificate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customcertificate
        """
        result = self._values.get("custom_certificate")
        return result

    @builtins.property
    def custom_domain(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.CustomDomain``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customdomain
        """
        result = self._values.get("custom_domain")
        return result

    @builtins.property
    def custom_private_key(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.CustomPrivateKey``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customprivatekey
        """
        result = self._values.get("custom_private_key")
        return result

    @builtins.property
    def disable_automated_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::OpsWorksCM::Server.DisableAutomatedBackup``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-disableautomatedbackup
        """
        result = self._values.get("disable_automated_backup")
        return result

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.Engine``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engine
        """
        result = self._values.get("engine")
        return result

    @builtins.property
    def engine_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnServer.EngineAttributeProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::OpsWorksCM::Server.EngineAttributes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engineattributes
        """
        result = self._values.get("engine_attributes")
        return result

    @builtins.property
    def engine_model(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.EngineModel``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-enginemodel
        """
        result = self._values.get("engine_model")
        return result

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.EngineVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engineversion
        """
        result = self._values.get("engine_version")
        return result

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.KeyPair``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-keypair
        """
        result = self._values.get("key_pair")
        return result

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.PreferredBackupWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-preferredbackupwindow
        """
        result = self._values.get("preferred_backup_window")
        return result

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.PreferredMaintenanceWindow``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-preferredmaintenancewindow
        """
        result = self._values.get("preferred_maintenance_window")
        return result

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::OpsWorksCM::Server.SecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-securitygroupids
        """
        result = self._values.get("security_group_ids")
        return result

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        """``AWS::OpsWorksCM::Server.ServerName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-servername
        """
        result = self._values.get("server_name")
        return result

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::OpsWorksCM::Server.SubnetIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-subnetids
        """
        result = self._values.get("subnet_ids")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::OpsWorksCM::Server.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServer",
    "CfnServerProps",
]

publication.publish()
