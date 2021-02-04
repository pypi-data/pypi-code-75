"""
# Amazon SageMaker Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sagemaker as sagemaker
```
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

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCodeRepository(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepository",
):
    """A CloudFormation ``AWS::SageMaker::CodeRepository``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
    :cloudformationResource: AWS::SageMaker::CodeRepository
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        git_config: typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable],
        code_repository_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::CodeRepository``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param git_config: ``AWS::SageMaker::CodeRepository.GitConfig``.
        :param code_repository_name: ``AWS::SageMaker::CodeRepository.CodeRepositoryName``.
        """
        props = CfnCodeRepositoryProps(
            git_config=git_config, code_repository_name=code_repository_name
        )

        jsii.create(CfnCodeRepository, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCodeRepositoryName")
    def attr_code_repository_name(self) -> builtins.str:
        """
        :cloudformationAttribute: CodeRepositoryName
        """
        return jsii.get(self, "attrCodeRepositoryName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="gitConfig")
    def git_config(
        self,
    ) -> typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable]:
        """``AWS::SageMaker::CodeRepository.GitConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig
        """
        return jsii.get(self, "gitConfig")

    @git_config.setter # type: ignore
    def git_config(
        self,
        value: typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "gitConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="codeRepositoryName")
    def code_repository_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname
        """
        return jsii.get(self, "codeRepositoryName")

    @code_repository_name.setter # type: ignore
    def code_repository_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "codeRepositoryName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepository.GitConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_url": "repositoryUrl",
            "branch": "branch",
            "secret_arn": "secretArn",
        },
    )
    class GitConfigProperty:
        def __init__(
            self,
            *,
            repository_url: builtins.str,
            branch: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param repository_url: ``CfnCodeRepository.GitConfigProperty.RepositoryUrl``.
            :param branch: ``CfnCodeRepository.GitConfigProperty.Branch``.
            :param secret_arn: ``CfnCodeRepository.GitConfigProperty.SecretArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "repository_url": repository_url,
            }
            if branch is not None:
                self._values["branch"] = branch
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn

        @builtins.property
        def repository_url(self) -> builtins.str:
            """``CfnCodeRepository.GitConfigProperty.RepositoryUrl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-repositoryurl
            """
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return result

        @builtins.property
        def branch(self) -> typing.Optional[builtins.str]:
            """``CfnCodeRepository.GitConfigProperty.Branch``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-branch
            """
            result = self._values.get("branch")
            return result

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            """``CfnCodeRepository.GitConfigProperty.SecretArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-secretarn
            """
            result = self._values.get("secret_arn")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "git_config": "gitConfig",
        "code_repository_name": "codeRepositoryName",
    },
)
class CfnCodeRepositoryProps:
    def __init__(
        self,
        *,
        git_config: typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable],
        code_repository_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::CodeRepository``.

        :param git_config: ``AWS::SageMaker::CodeRepository.GitConfig``.
        :param code_repository_name: ``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "git_config": git_config,
        }
        if code_repository_name is not None:
            self._values["code_repository_name"] = code_repository_name

    @builtins.property
    def git_config(
        self,
    ) -> typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable]:
        """``AWS::SageMaker::CodeRepository.GitConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig
        """
        result = self._values.get("git_config")
        assert result is not None, "Required property 'git_config' is missing"
        return result

    @builtins.property
    def code_repository_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname
        """
        result = self._values.get("code_repository_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataQualityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition",
):
    """A CloudFormation ``AWS::SageMaker::DataQualityJobDefinition``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
    :cloudformationResource: AWS::SageMaker::DataQualityJobDefinition
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"],
        data_quality_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"],
        data_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"],
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"],
        role_arn: builtins.str,
        data_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::DataQualityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_quality_app_specification: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.
        :param data_quality_job_input: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.
        :param data_quality_job_output_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.
        :param job_resources: ``AWS::SageMaker::DataQualityJobDefinition.JobResources``.
        :param role_arn: ``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.
        :param data_quality_baseline_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.
        :param job_definition_name: ``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.
        :param network_config: ``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::DataQualityJobDefinition.Tags``.
        """
        props = CfnDataQualityJobDefinitionProps(
            data_quality_app_specification=data_quality_app_specification,
            data_quality_job_input=data_quality_job_input,
            data_quality_job_output_config=data_quality_job_output_config,
            job_resources=job_resources,
            role_arn=role_arn,
            data_quality_baseline_config=data_quality_baseline_config,
            job_definition_name=job_definition_name,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnDataQualityJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: JobDefinitionArn
        """
        return jsii.get(self, "attrJobDefinitionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataQualityAppSpecification")
    def data_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        """
        return jsii.get(self, "dataQualityAppSpecification")

    @data_quality_app_specification.setter # type: ignore
    def data_quality_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "dataQualityAppSpecification", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataQualityJobInput")
    def data_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        """
        return jsii.get(self, "dataQualityJobInput")

    @data_quality_job_input.setter # type: ignore
    def data_quality_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"],
    ) -> None:
        jsii.set(self, "dataQualityJobInput", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataQualityJobOutputConfig")
    def data_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        """
        return jsii.get(self, "dataQualityJobOutputConfig")

    @data_quality_job_output_config.setter # type: ignore
    def data_quality_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "dataQualityJobOutputConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"]:
        """``AWS::SageMaker::DataQualityJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        """
        return jsii.get(self, "jobResources")

    @job_resources.setter # type: ignore
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataQualityBaselineConfig")
    def data_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        """
        return jsii.get(self, "dataQualityBaselineConfig")

    @data_quality_baseline_config.setter # type: ignore
    def data_quality_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "dataQualityBaselineConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        """
        return jsii.get(self, "jobDefinitionName")

    @job_definition_name.setter # type: ignore
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]]:
        """``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        """
        return jsii.get(self, "networkConfig")

    @network_config.setter # type: ignore
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]]:
        """``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        """
        return jsii.get(self, "stoppingCondition")

    @stopping_condition.setter # type: ignore
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param instance_count: ``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            """``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancecount
            """
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            """``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumesizeingb
            """
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return result

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumekmskeyid
            """
            result = self._values.get("volume_kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnDataQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html#cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "environment": "environment",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class DataQualityAppSpecificationProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            container_arguments: typing.Optional[typing.List[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.List[builtins.str]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EnvironmentProperty"]] = None,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param image_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ImageUri``.
            :param container_arguments: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerEntrypoint``.
            :param environment: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.Environment``.
            :param post_analytics_processor_source_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if environment is not None:
                self._values["environment"] = environment
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def image_uri(self) -> builtins.str:
            """``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ImageUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-imageuri
            """
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return result

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerArguments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerarguments
            """
            result = self._values.get("container_arguments")
            return result

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerEntrypoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerentrypoint
            """
            result = self._values.get("container_entrypoint")
            return result

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EnvironmentProperty"]]:
            """``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-environment
            """
            result = self._values.get("environment")
            return result

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-postanalyticsprocessorsourceuri
            """
            result = self._values.get("post_analytics_processor_source_uri")
            return result

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-recordpreprocessorsourceuri
            """
            result = self._values.get("record_preprocessor_source_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
            "statistics_resource": "statisticsResource",
        },
    )
    class DataQualityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]] = None,
            statistics_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]] = None,
        ) -> None:
            """
            :param baselining_job_name: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.ConstraintsResource``.
            :param statistics_resource: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.StatisticsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource
            if statistics_resource is not None:
                self._values["statistics_resource"] = statistics_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.BaseliningJobName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-baseliningjobname
            """
            result = self._values.get("baselining_job_name")
            return result

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]]:
            """``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-constraintsresource
            """
            result = self._values.get("constraints_resource")
            return result

        @builtins.property
        def statistics_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]]:
            """``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.StatisticsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-statisticsresource
            """
            result = self._values.get("statistics_resource")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class DataQualityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"],
        ) -> None:
            """
            :param endpoint_input: ``CfnDataQualityJobDefinition.DataQualityJobInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"]:
            """``CfnDataQualityJobDefinition.DataQualityJobInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput
            """
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param endpoint_name: ``CfnDataQualityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnDataQualityJobDefinition.EndpointInputProperty.LocalPath``.
            :param s3_data_distribution_type: ``CfnDataQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnDataQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            """``CfnDataQualityJobDefinition.EndpointInputProperty.EndpointName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname
            """
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return result

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnDataQualityJobDefinition.EndpointInputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype
            """
            result = self._values.get("s3_data_distribution_type")
            return result

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode
            """
            result = self._values.get("s3_input_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param monitoring_outputs: ``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]]:
            """``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-monitoringoutputs
            """
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"],
        ) -> None:
            """
            :param s3_output: ``CfnDataQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"]:
            """``CfnDataQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutput-s3output
            """
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            """
            :param cluster_config: ``CfnDataQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"]:
            """``CfnDataQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html#cfn-sagemaker-dataqualityjobdefinition-monitoringresources-clusterconfig
            """
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            """
            :param enable_inter_container_traffic_encryption: ``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnDataQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enableintercontainertrafficencryption
            """
            result = self._values.get("enable_inter_container_traffic_encryption")
            return result

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enablenetworkisolation
            """
            result = self._values.get("enable_network_isolation")
            return result

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]]:
            """``CfnDataQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-vpcconfig
            """
            result = self._values.get("vpc_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param local_path: ``CfnDataQualityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnDataQualityJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnDataQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnDataQualityJobDefinition.S3OutputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnDataQualityJobDefinition.S3OutputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uploadmode
            """
            result = self._values.get("s3_upload_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class StatisticsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnDataQualityJobDefinition.StatisticsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnDataQualityJobDefinition.StatisticsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html#cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            """
            :param max_runtime_in_seconds: ``CfnDataQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            """``CfnDataQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition-maxruntimeinseconds
            """
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnets: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnDataQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnDataQualityJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnDataQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            """``CfnDataQualityJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-subnets
            """
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
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
    jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_quality_app_specification": "dataQualityAppSpecification",
        "data_quality_job_input": "dataQualityJobInput",
        "data_quality_job_output_config": "dataQualityJobOutputConfig",
        "job_resources": "jobResources",
        "role_arn": "roleArn",
        "data_quality_baseline_config": "dataQualityBaselineConfig",
        "job_definition_name": "jobDefinitionName",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnDataQualityJobDefinitionProps:
    def __init__(
        self,
        *,
        data_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty],
        data_quality_job_input: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty],
        data_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty],
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty],
        role_arn: builtins.str,
        data_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::DataQualityJobDefinition``.

        :param data_quality_app_specification: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.
        :param data_quality_job_input: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.
        :param data_quality_job_output_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.
        :param job_resources: ``AWS::SageMaker::DataQualityJobDefinition.JobResources``.
        :param role_arn: ``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.
        :param data_quality_baseline_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.
        :param job_definition_name: ``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.
        :param network_config: ``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "data_quality_app_specification": data_quality_app_specification,
            "data_quality_job_input": data_quality_job_input,
            "data_quality_job_output_config": data_quality_job_output_config,
            "job_resources": job_resources,
            "role_arn": role_arn,
        }
        if data_quality_baseline_config is not None:
            self._values["data_quality_baseline_config"] = data_quality_baseline_config
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        """
        result = self._values.get("data_quality_app_specification")
        assert result is not None, "Required property 'data_quality_app_specification' is missing"
        return result

    @builtins.property
    def data_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        """
        result = self._values.get("data_quality_job_input")
        assert result is not None, "Required property 'data_quality_job_input' is missing"
        return result

    @builtins.property
    def data_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        """
        result = self._values.get("data_quality_job_output_config")
        assert result is not None, "Required property 'data_quality_job_output_config' is missing"
        return result

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty]:
        """``AWS::SageMaker::DataQualityJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        """
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def data_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]]:
        """``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        """
        result = self._values.get("data_quality_baseline_config")
        return result

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        """
        result = self._values.get("job_definition_name")
        return result

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]]:
        """``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        """
        result = self._values.get("network_config")
        return result

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]]:
        """``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        """
        result = self._values.get("stopping_condition")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataQualityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDevice(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDevice",
):
    """A CloudFormation ``AWS::SageMaker::Device``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
    :cloudformationResource: AWS::SageMaker::Device
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        device_fleet_name: builtins.str,
        device: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::Device``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_fleet_name: ``AWS::SageMaker::Device.DeviceFleetName``.
        :param device: ``AWS::SageMaker::Device.Device``.
        :param tags: ``AWS::SageMaker::Device.Tags``.
        """
        props = CfnDeviceProps(
            device_fleet_name=device_fleet_name, device=device, tags=tags
        )

        jsii.create(CfnDevice, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::Device.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="deviceFleetName")
    def device_fleet_name(self) -> builtins.str:
        """``AWS::SageMaker::Device.DeviceFleetName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname
        """
        return jsii.get(self, "deviceFleetName")

    @device_fleet_name.setter # type: ignore
    def device_fleet_name(self, value: builtins.str) -> None:
        jsii.set(self, "deviceFleetName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="device")
    def device(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]]:
        """``AWS::SageMaker::Device.Device``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device
        """
        return jsii.get(self, "device")

    @device.setter # type: ignore
    def device(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]],
    ) -> None:
        jsii.set(self, "device", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDevice.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "description": "description",
            "iot_thing_name": "iotThingName",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            device_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            iot_thing_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param device_name: ``CfnDevice.DeviceProperty.DeviceName``.
            :param description: ``CfnDevice.DeviceProperty.Description``.
            :param iot_thing_name: ``CfnDevice.DeviceProperty.IotThingName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "device_name": device_name,
            }
            if description is not None:
                self._values["description"] = description
            if iot_thing_name is not None:
                self._values["iot_thing_name"] = iot_thing_name

        @builtins.property
        def device_name(self) -> builtins.str:
            """``CfnDevice.DeviceProperty.DeviceName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-devicename
            """
            result = self._values.get("device_name")
            assert result is not None, "Required property 'device_name' is missing"
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnDevice.DeviceProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def iot_thing_name(self) -> typing.Optional[builtins.str]:
            """``CfnDevice.DeviceProperty.IotThingName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-iotthingname
            """
            result = self._values.get("iot_thing_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeviceFleet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleet",
):
    """A CloudFormation ``AWS::SageMaker::DeviceFleet``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
    :cloudformationResource: AWS::SageMaker::DeviceFleet
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        device_fleet_name: builtins.str,
        output_config: typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::DeviceFleet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_fleet_name: ``AWS::SageMaker::DeviceFleet.DeviceFleetName``.
        :param output_config: ``AWS::SageMaker::DeviceFleet.OutputConfig``.
        :param role_arn: ``AWS::SageMaker::DeviceFleet.RoleArn``.
        :param description: ``AWS::SageMaker::DeviceFleet.Description``.
        :param tags: ``AWS::SageMaker::DeviceFleet.Tags``.
        """
        props = CfnDeviceFleetProps(
            device_fleet_name=device_fleet_name,
            output_config=output_config,
            role_arn=role_arn,
            description=description,
            tags=tags,
        )

        jsii.create(CfnDeviceFleet, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::DeviceFleet.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="deviceFleetName")
    def device_fleet_name(self) -> builtins.str:
        """``AWS::SageMaker::DeviceFleet.DeviceFleetName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname
        """
        return jsii.get(self, "deviceFleetName")

    @device_fleet_name.setter # type: ignore
    def device_fleet_name(self, value: builtins.str) -> None:
        jsii.set(self, "deviceFleetName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"]:
        """``AWS::SageMaker::DeviceFleet.OutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig
        """
        return jsii.get(self, "outputConfig")

    @output_config.setter # type: ignore
    def output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "outputConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::DeviceFleet.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::DeviceFleet.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleet.EdgeOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_output_location": "s3OutputLocation",
            "kms_key_id": "kmsKeyId",
        },
    )
    class EdgeOutputConfigProperty:
        def __init__(
            self,
            *,
            s3_output_location: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param s3_output_location: ``CfnDeviceFleet.EdgeOutputConfigProperty.S3OutputLocation``.
            :param kms_key_id: ``CfnDeviceFleet.EdgeOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output_location": s3_output_location,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def s3_output_location(self) -> builtins.str:
            """``CfnDeviceFleet.EdgeOutputConfigProperty.S3OutputLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation
            """
            result = self._values.get("s3_output_location")
            assert result is not None, "Required property 's3_output_location' is missing"
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnDeviceFleet.EdgeOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdgeOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_fleet_name": "deviceFleetName",
        "output_config": "outputConfig",
        "role_arn": "roleArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDeviceFleetProps:
    def __init__(
        self,
        *,
        device_fleet_name: builtins.str,
        output_config: typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::DeviceFleet``.

        :param device_fleet_name: ``AWS::SageMaker::DeviceFleet.DeviceFleetName``.
        :param output_config: ``AWS::SageMaker::DeviceFleet.OutputConfig``.
        :param role_arn: ``AWS::SageMaker::DeviceFleet.RoleArn``.
        :param description: ``AWS::SageMaker::DeviceFleet.Description``.
        :param tags: ``AWS::SageMaker::DeviceFleet.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
            "output_config": output_config,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        """``AWS::SageMaker::DeviceFleet.DeviceFleetName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname
        """
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return result

    @builtins.property
    def output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty]:
        """``AWS::SageMaker::DeviceFleet.OutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig
        """
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::DeviceFleet.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::DeviceFleet.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::DeviceFleet.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_fleet_name": "deviceFleetName",
        "device": "device",
        "tags": "tags",
    },
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        device_fleet_name: builtins.str,
        device: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::Device``.

        :param device_fleet_name: ``AWS::SageMaker::Device.DeviceFleetName``.
        :param device: ``AWS::SageMaker::Device.Device``.
        :param tags: ``AWS::SageMaker::Device.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
        }
        if device is not None:
            self._values["device"] = device
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        """``AWS::SageMaker::Device.DeviceFleetName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname
        """
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return result

    @builtins.property
    def device(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]]:
        """``AWS::SageMaker::Device.Device``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device
        """
        result = self._values.get("device")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::Device.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint",
):
    """A CloudFormation ``AWS::SageMaker::Endpoint``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
    :cloudformationResource: AWS::SageMaker::Endpoint
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        endpoint_config_name: builtins.str,
        deployment_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]] = None,
        endpoint_name: typing.Optional[builtins.str] = None,
        exclude_retained_variant_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]] = None,
        retain_all_variant_properties: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::Endpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_config_name: ``AWS::SageMaker::Endpoint.EndpointConfigName``.
        :param deployment_config: ``AWS::SageMaker::Endpoint.DeploymentConfig``.
        :param endpoint_name: ``AWS::SageMaker::Endpoint.EndpointName``.
        :param exclude_retained_variant_properties: ``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.
        :param retain_all_variant_properties: ``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.
        :param tags: ``AWS::SageMaker::Endpoint.Tags``.
        """
        props = CfnEndpointProps(
            endpoint_config_name=endpoint_config_name,
            deployment_config=deployment_config,
            endpoint_name=endpoint_name,
            exclude_retained_variant_properties=exclude_retained_variant_properties,
            retain_all_variant_properties=retain_all_variant_properties,
            tags=tags,
        )

        jsii.create(CfnEndpoint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrEndpointName")
    def attr_endpoint_name(self) -> builtins.str:
        """
        :cloudformationAttribute: EndpointName
        """
        return jsii.get(self, "attrEndpointName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::Endpoint.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        """``AWS::SageMaker::Endpoint.EndpointConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname
        """
        return jsii.get(self, "endpointConfigName")

    @endpoint_config_name.setter # type: ignore
    def endpoint_config_name(self, value: builtins.str) -> None:
        jsii.set(self, "endpointConfigName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]]:
        """``AWS::SageMaker::Endpoint.DeploymentConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig
        """
        return jsii.get(self, "deploymentConfig")

    @deployment_config.setter # type: ignore
    def deployment_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]],
    ) -> None:
        jsii.set(self, "deploymentConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Endpoint.EndpointName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname
        """
        return jsii.get(self, "endpointName")

    @endpoint_name.setter # type: ignore
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="excludeRetainedVariantProperties")
    def exclude_retained_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]]:
        """``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties
        """
        return jsii.get(self, "excludeRetainedVariantProperties")

    @exclude_retained_variant_properties.setter # type: ignore
    def exclude_retained_variant_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]],
    ) -> None:
        jsii.set(self, "excludeRetainedVariantProperties", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="retainAllVariantProperties")
    def retain_all_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties
        """
        return jsii.get(self, "retainAllVariantProperties")

    @retain_all_variant_properties.setter # type: ignore
    def retain_all_variant_properties(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "retainAllVariantProperties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.AlarmProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_name": "alarmName"},
    )
    class AlarmProperty:
        def __init__(self, *, alarm_name: builtins.str) -> None:
            """
            :param alarm_name: ``CfnEndpoint.AlarmProperty.AlarmName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_name": alarm_name,
            }

        @builtins.property
        def alarm_name(self) -> builtins.str:
            """``CfnEndpoint.AlarmProperty.AlarmName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html#cfn-sagemaker-endpoint-alarm-alarmname
            """
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.AutoRollbackConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"alarms": "alarms"},
    )
    class AutoRollbackConfigProperty:
        def __init__(
            self,
            *,
            alarms: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]],
        ) -> None:
            """
            :param alarms: ``CfnEndpoint.AutoRollbackConfigProperty.Alarms``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "alarms": alarms,
            }

        @builtins.property
        def alarms(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]]:
            """``CfnEndpoint.AutoRollbackConfigProperty.Alarms``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html#cfn-sagemaker-endpoint-autorollbackconfig-alarms
            """
            result = self._values.get("alarms")
            assert result is not None, "Required property 'alarms' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoRollbackConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "traffic_routing_configuration": "trafficRoutingConfiguration",
            "maximum_execution_timeout_in_seconds": "maximumExecutionTimeoutInSeconds",
            "termination_wait_in_seconds": "terminationWaitInSeconds",
        },
    )
    class BlueGreenUpdatePolicyProperty:
        def __init__(
            self,
            *,
            traffic_routing_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"],
            maximum_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            termination_wait_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param traffic_routing_configuration: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.TrafficRoutingConfiguration``.
            :param maximum_execution_timeout_in_seconds: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.MaximumExecutionTimeoutInSeconds``.
            :param termination_wait_in_seconds: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.TerminationWaitInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "traffic_routing_configuration": traffic_routing_configuration,
            }
            if maximum_execution_timeout_in_seconds is not None:
                self._values["maximum_execution_timeout_in_seconds"] = maximum_execution_timeout_in_seconds
            if termination_wait_in_seconds is not None:
                self._values["termination_wait_in_seconds"] = termination_wait_in_seconds

        @builtins.property
        def traffic_routing_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"]:
            """``CfnEndpoint.BlueGreenUpdatePolicyProperty.TrafficRoutingConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-trafficroutingconfiguration
            """
            result = self._values.get("traffic_routing_configuration")
            assert result is not None, "Required property 'traffic_routing_configuration' is missing"
            return result

        @builtins.property
        def maximum_execution_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnEndpoint.BlueGreenUpdatePolicyProperty.MaximumExecutionTimeoutInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-maximumexecutiontimeoutinseconds
            """
            result = self._values.get("maximum_execution_timeout_in_seconds")
            return result

        @builtins.property
        def termination_wait_in_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnEndpoint.BlueGreenUpdatePolicyProperty.TerminationWaitInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-terminationwaitinseconds
            """
            result = self._values.get("termination_wait_in_seconds")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlueGreenUpdatePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.CapacitySizeProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class CapacitySizeProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            """
            :param type: ``CfnEndpoint.CapacitySizeProperty.Type``.
            :param value: ``CfnEndpoint.CapacitySizeProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            """``CfnEndpoint.CapacitySizeProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-type
            """
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return result

        @builtins.property
        def value(self) -> jsii.Number:
            """``CfnEndpoint.CapacitySizeProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-value
            """
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacitySizeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.DeploymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "blue_green_update_policy": "blueGreenUpdatePolicy",
            "auto_rollback_configuration": "autoRollbackConfiguration",
        },
    )
    class DeploymentConfigProperty:
        def __init__(
            self,
            *,
            blue_green_update_policy: typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"],
            auto_rollback_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]] = None,
        ) -> None:
            """
            :param blue_green_update_policy: ``CfnEndpoint.DeploymentConfigProperty.BlueGreenUpdatePolicy``.
            :param auto_rollback_configuration: ``CfnEndpoint.DeploymentConfigProperty.AutoRollbackConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "blue_green_update_policy": blue_green_update_policy,
            }
            if auto_rollback_configuration is not None:
                self._values["auto_rollback_configuration"] = auto_rollback_configuration

        @builtins.property
        def blue_green_update_policy(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"]:
            """``CfnEndpoint.DeploymentConfigProperty.BlueGreenUpdatePolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy
            """
            result = self._values.get("blue_green_update_policy")
            assert result is not None, "Required property 'blue_green_update_policy' is missing"
            return result

        @builtins.property
        def auto_rollback_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]]:
            """``CfnEndpoint.DeploymentConfigProperty.AutoRollbackConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration
            """
            result = self._values.get("auto_rollback_configuration")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.TrafficRoutingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "canary_size": "canarySize",
            "wait_interval_in_seconds": "waitIntervalInSeconds",
        },
    )
    class TrafficRoutingConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            canary_size: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]] = None,
            wait_interval_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param type: ``CfnEndpoint.TrafficRoutingConfigProperty.Type``.
            :param canary_size: ``CfnEndpoint.TrafficRoutingConfigProperty.CanarySize``.
            :param wait_interval_in_seconds: ``CfnEndpoint.TrafficRoutingConfigProperty.WaitIntervalInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if canary_size is not None:
                self._values["canary_size"] = canary_size
            if wait_interval_in_seconds is not None:
                self._values["wait_interval_in_seconds"] = wait_interval_in_seconds

        @builtins.property
        def type(self) -> builtins.str:
            """``CfnEndpoint.TrafficRoutingConfigProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-type
            """
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return result

        @builtins.property
        def canary_size(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]]:
            """``CfnEndpoint.TrafficRoutingConfigProperty.CanarySize``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-canarysize
            """
            result = self._values.get("canary_size")
            return result

        @builtins.property
        def wait_interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnEndpoint.TrafficRoutingConfigProperty.WaitIntervalInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-waitintervalinseconds
            """
            result = self._values.get("wait_interval_in_seconds")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficRoutingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.VariantPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"variant_property_type": "variantPropertyType"},
    )
    class VariantPropertyProperty:
        def __init__(
            self,
            *,
            variant_property_type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param variant_property_type: ``CfnEndpoint.VariantPropertyProperty.VariantPropertyType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if variant_property_type is not None:
                self._values["variant_property_type"] = variant_property_type

        @builtins.property
        def variant_property_type(self) -> typing.Optional[builtins.str]:
            """``CfnEndpoint.VariantPropertyProperty.VariantPropertyType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html#cfn-sagemaker-endpoint-variantproperty-variantpropertytype
            """
            result = self._values.get("variant_property_type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariantPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpointConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig",
):
    """A CloudFormation ``AWS::SageMaker::EndpointConfig``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
    :cloudformationResource: AWS::SageMaker::EndpointConfig
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        production_variants: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]],
        data_capture_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::EndpointConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param production_variants: ``AWS::SageMaker::EndpointConfig.ProductionVariants``.
        :param data_capture_config: ``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::EndpointConfig.EndpointConfigName``.
        :param kms_key_id: ``AWS::SageMaker::EndpointConfig.KmsKeyId``.
        :param tags: ``AWS::SageMaker::EndpointConfig.Tags``.
        """
        props = CfnEndpointConfigProps(
            production_variants=production_variants,
            data_capture_config=data_capture_config,
            endpoint_config_name=endpoint_config_name,
            kms_key_id=kms_key_id,
            tags=tags,
        )

        jsii.create(CfnEndpointConfig, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrEndpointConfigName")
    def attr_endpoint_config_name(self) -> builtins.str:
        """
        :cloudformationAttribute: EndpointConfigName
        """
        return jsii.get(self, "attrEndpointConfigName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::EndpointConfig.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="productionVariants")
    def production_variants(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]]:
        """``AWS::SageMaker::EndpointConfig.ProductionVariants``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants
        """
        return jsii.get(self, "productionVariants")

    @production_variants.setter # type: ignore
    def production_variants(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]],
    ) -> None:
        jsii.set(self, "productionVariants", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataCaptureConfig")
    def data_capture_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]]:
        """``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig
        """
        return jsii.get(self, "dataCaptureConfig")

    @data_capture_config.setter # type: ignore
    def data_capture_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]],
    ) -> None:
        jsii.set(self, "dataCaptureConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::EndpointConfig.EndpointConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname
        """
        return jsii.get(self, "endpointConfigName")

    @endpoint_config_name.setter # type: ignore
    def endpoint_config_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointConfigName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::EndpointConfig.KmsKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid
        """
        return jsii.get(self, "kmsKeyId")

    @kms_key_id.setter # type: ignore
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_content_types": "csvContentTypes",
            "json_content_types": "jsonContentTypes",
        },
    )
    class CaptureContentTypeHeaderProperty:
        def __init__(
            self,
            *,
            csv_content_types: typing.Optional[typing.List[builtins.str]] = None,
            json_content_types: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param csv_content_types: ``CfnEndpointConfig.CaptureContentTypeHeaderProperty.CsvContentTypes``.
            :param json_content_types: ``CfnEndpointConfig.CaptureContentTypeHeaderProperty.JsonContentTypes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if csv_content_types is not None:
                self._values["csv_content_types"] = csv_content_types
            if json_content_types is not None:
                self._values["json_content_types"] = json_content_types

        @builtins.property
        def csv_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnEndpointConfig.CaptureContentTypeHeaderProperty.CsvContentTypes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-csvcontenttypes
            """
            result = self._values.get("csv_content_types")
            return result

        @builtins.property
        def json_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnEndpointConfig.CaptureContentTypeHeaderProperty.JsonContentTypes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-jsoncontenttypes
            """
            result = self._values.get("json_content_types")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptureContentTypeHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.CaptureOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"capture_mode": "captureMode"},
    )
    class CaptureOptionProperty:
        def __init__(self, *, capture_mode: builtins.str) -> None:
            """
            :param capture_mode: ``CfnEndpointConfig.CaptureOptionProperty.CaptureMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "capture_mode": capture_mode,
            }

        @builtins.property
        def capture_mode(self) -> builtins.str:
            """``CfnEndpointConfig.CaptureOptionProperty.CaptureMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html#cfn-sagemaker-endpointconfig-captureoption-capturemode
            """
            result = self._values.get("capture_mode")
            assert result is not None, "Required property 'capture_mode' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptureOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.DataCaptureConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capture_options": "captureOptions",
            "destination_s3_uri": "destinationS3Uri",
            "initial_sampling_percentage": "initialSamplingPercentage",
            "capture_content_type_header": "captureContentTypeHeader",
            "enable_capture": "enableCapture",
            "kms_key_id": "kmsKeyId",
        },
    )
    class DataCaptureConfigProperty:
        def __init__(
            self,
            *,
            capture_options: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]],
            destination_s3_uri: builtins.str,
            initial_sampling_percentage: jsii.Number,
            capture_content_type_header: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]] = None,
            enable_capture: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param capture_options: ``CfnEndpointConfig.DataCaptureConfigProperty.CaptureOptions``.
            :param destination_s3_uri: ``CfnEndpointConfig.DataCaptureConfigProperty.DestinationS3Uri``.
            :param initial_sampling_percentage: ``CfnEndpointConfig.DataCaptureConfigProperty.InitialSamplingPercentage``.
            :param capture_content_type_header: ``CfnEndpointConfig.DataCaptureConfigProperty.CaptureContentTypeHeader``.
            :param enable_capture: ``CfnEndpointConfig.DataCaptureConfigProperty.EnableCapture``.
            :param kms_key_id: ``CfnEndpointConfig.DataCaptureConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "capture_options": capture_options,
                "destination_s3_uri": destination_s3_uri,
                "initial_sampling_percentage": initial_sampling_percentage,
            }
            if capture_content_type_header is not None:
                self._values["capture_content_type_header"] = capture_content_type_header
            if enable_capture is not None:
                self._values["enable_capture"] = enable_capture
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def capture_options(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]]:
            """``CfnEndpointConfig.DataCaptureConfigProperty.CaptureOptions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-captureoptions
            """
            result = self._values.get("capture_options")
            assert result is not None, "Required property 'capture_options' is missing"
            return result

        @builtins.property
        def destination_s3_uri(self) -> builtins.str:
            """``CfnEndpointConfig.DataCaptureConfigProperty.DestinationS3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-destinations3uri
            """
            result = self._values.get("destination_s3_uri")
            assert result is not None, "Required property 'destination_s3_uri' is missing"
            return result

        @builtins.property
        def initial_sampling_percentage(self) -> jsii.Number:
            """``CfnEndpointConfig.DataCaptureConfigProperty.InitialSamplingPercentage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-initialsamplingpercentage
            """
            result = self._values.get("initial_sampling_percentage")
            assert result is not None, "Required property 'initial_sampling_percentage' is missing"
            return result

        @builtins.property
        def capture_content_type_header(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]]:
            """``CfnEndpointConfig.DataCaptureConfigProperty.CaptureContentTypeHeader``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader
            """
            result = self._values.get("capture_content_type_header")
            return result

        @builtins.property
        def enable_capture(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnEndpointConfig.DataCaptureConfigProperty.EnableCapture``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-enablecapture
            """
            result = self._values.get("enable_capture")
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnEndpointConfig.DataCaptureConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCaptureConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.ProductionVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "initial_instance_count": "initialInstanceCount",
            "initial_variant_weight": "initialVariantWeight",
            "instance_type": "instanceType",
            "model_name": "modelName",
            "variant_name": "variantName",
            "accelerator_type": "acceleratorType",
        },
    )
    class ProductionVariantProperty:
        def __init__(
            self,
            *,
            initial_instance_count: jsii.Number,
            initial_variant_weight: jsii.Number,
            instance_type: builtins.str,
            model_name: builtins.str,
            variant_name: builtins.str,
            accelerator_type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param initial_instance_count: ``CfnEndpointConfig.ProductionVariantProperty.InitialInstanceCount``.
            :param initial_variant_weight: ``CfnEndpointConfig.ProductionVariantProperty.InitialVariantWeight``.
            :param instance_type: ``CfnEndpointConfig.ProductionVariantProperty.InstanceType``.
            :param model_name: ``CfnEndpointConfig.ProductionVariantProperty.ModelName``.
            :param variant_name: ``CfnEndpointConfig.ProductionVariantProperty.VariantName``.
            :param accelerator_type: ``CfnEndpointConfig.ProductionVariantProperty.AcceleratorType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "initial_instance_count": initial_instance_count,
                "initial_variant_weight": initial_variant_weight,
                "instance_type": instance_type,
                "model_name": model_name,
                "variant_name": variant_name,
            }
            if accelerator_type is not None:
                self._values["accelerator_type"] = accelerator_type

        @builtins.property
        def initial_instance_count(self) -> jsii.Number:
            """``CfnEndpointConfig.ProductionVariantProperty.InitialInstanceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount
            """
            result = self._values.get("initial_instance_count")
            assert result is not None, "Required property 'initial_instance_count' is missing"
            return result

        @builtins.property
        def initial_variant_weight(self) -> jsii.Number:
            """``CfnEndpointConfig.ProductionVariantProperty.InitialVariantWeight``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight
            """
            result = self._values.get("initial_variant_weight")
            assert result is not None, "Required property 'initial_variant_weight' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnEndpointConfig.ProductionVariantProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        @builtins.property
        def model_name(self) -> builtins.str:
            """``CfnEndpointConfig.ProductionVariantProperty.ModelName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-modelname
            """
            result = self._values.get("model_name")
            assert result is not None, "Required property 'model_name' is missing"
            return result

        @builtins.property
        def variant_name(self) -> builtins.str:
            """``CfnEndpointConfig.ProductionVariantProperty.VariantName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-variantname
            """
            result = self._values.get("variant_name")
            assert result is not None, "Required property 'variant_name' is missing"
            return result

        @builtins.property
        def accelerator_type(self) -> typing.Optional[builtins.str]:
            """``CfnEndpointConfig.ProductionVariantProperty.AcceleratorType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype
            """
            result = self._values.get("accelerator_type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProductionVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "production_variants": "productionVariants",
        "data_capture_config": "dataCaptureConfig",
        "endpoint_config_name": "endpointConfigName",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
    },
)
class CfnEndpointConfigProps:
    def __init__(
        self,
        *,
        production_variants: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]],
        data_capture_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::EndpointConfig``.

        :param production_variants: ``AWS::SageMaker::EndpointConfig.ProductionVariants``.
        :param data_capture_config: ``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::EndpointConfig.EndpointConfigName``.
        :param kms_key_id: ``AWS::SageMaker::EndpointConfig.KmsKeyId``.
        :param tags: ``AWS::SageMaker::EndpointConfig.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "production_variants": production_variants,
        }
        if data_capture_config is not None:
            self._values["data_capture_config"] = data_capture_config
        if endpoint_config_name is not None:
            self._values["endpoint_config_name"] = endpoint_config_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def production_variants(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]]:
        """``AWS::SageMaker::EndpointConfig.ProductionVariants``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants
        """
        result = self._values.get("production_variants")
        assert result is not None, "Required property 'production_variants' is missing"
        return result

    @builtins.property
    def data_capture_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]]:
        """``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig
        """
        result = self._values.get("data_capture_config")
        return result

    @builtins.property
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::EndpointConfig.EndpointConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname
        """
        result = self._values.get("endpoint_config_name")
        return result

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::EndpointConfig.KmsKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid
        """
        result = self._values.get("kms_key_id")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::EndpointConfig.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_config_name": "endpointConfigName",
        "deployment_config": "deploymentConfig",
        "endpoint_name": "endpointName",
        "exclude_retained_variant_properties": "excludeRetainedVariantProperties",
        "retain_all_variant_properties": "retainAllVariantProperties",
        "tags": "tags",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        endpoint_config_name: builtins.str,
        deployment_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]] = None,
        endpoint_name: typing.Optional[builtins.str] = None,
        exclude_retained_variant_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]] = None,
        retain_all_variant_properties: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::Endpoint``.

        :param endpoint_config_name: ``AWS::SageMaker::Endpoint.EndpointConfigName``.
        :param deployment_config: ``AWS::SageMaker::Endpoint.DeploymentConfig``.
        :param endpoint_name: ``AWS::SageMaker::Endpoint.EndpointName``.
        :param exclude_retained_variant_properties: ``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.
        :param retain_all_variant_properties: ``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.
        :param tags: ``AWS::SageMaker::Endpoint.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_config_name": endpoint_config_name,
        }
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if exclude_retained_variant_properties is not None:
            self._values["exclude_retained_variant_properties"] = exclude_retained_variant_properties
        if retain_all_variant_properties is not None:
            self._values["retain_all_variant_properties"] = retain_all_variant_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_config_name(self) -> builtins.str:
        """``AWS::SageMaker::Endpoint.EndpointConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname
        """
        result = self._values.get("endpoint_config_name")
        assert result is not None, "Required property 'endpoint_config_name' is missing"
        return result

    @builtins.property
    def deployment_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]]:
        """``AWS::SageMaker::Endpoint.DeploymentConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig
        """
        result = self._values.get("deployment_config")
        return result

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Endpoint.EndpointName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname
        """
        result = self._values.get("endpoint_name")
        return result

    @builtins.property
    def exclude_retained_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]]:
        """``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties
        """
        result = self._values.get("exclude_retained_variant_properties")
        return result

    @builtins.property
    def retain_all_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties
        """
        result = self._values.get("retain_all_variant_properties")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::Endpoint.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModel",
):
    """A CloudFormation ``AWS::SageMaker::Model``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
    :cloudformationResource: AWS::SageMaker::Model
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        execution_role_arn: builtins.str,
        containers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]] = None,
        enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        model_name: typing.Optional[builtins.str] = None,
        primary_container: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::Model``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param execution_role_arn: ``AWS::SageMaker::Model.ExecutionRoleArn``.
        :param containers: ``AWS::SageMaker::Model.Containers``.
        :param enable_network_isolation: ``AWS::SageMaker::Model.EnableNetworkIsolation``.
        :param model_name: ``AWS::SageMaker::Model.ModelName``.
        :param primary_container: ``AWS::SageMaker::Model.PrimaryContainer``.
        :param tags: ``AWS::SageMaker::Model.Tags``.
        :param vpc_config: ``AWS::SageMaker::Model.VpcConfig``.
        """
        props = CfnModelProps(
            execution_role_arn=execution_role_arn,
            containers=containers,
            enable_network_isolation=enable_network_isolation,
            model_name=model_name,
            primary_container=primary_container,
            tags=tags,
            vpc_config=vpc_config,
        )

        jsii.create(CfnModel, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrModelName")
    def attr_model_name(self) -> builtins.str:
        """
        :cloudformationAttribute: ModelName
        """
        return jsii.get(self, "attrModelName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::Model.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        """``AWS::SageMaker::Model.ExecutionRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn
        """
        return jsii.get(self, "executionRoleArn")

    @execution_role_arn.setter # type: ignore
    def execution_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="containers")
    def containers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]]:
        """``AWS::SageMaker::Model.Containers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers
        """
        return jsii.get(self, "containers")

    @containers.setter # type: ignore
    def containers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]],
    ) -> None:
        jsii.set(self, "containers", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="enableNetworkIsolation")
    def enable_network_isolation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::SageMaker::Model.EnableNetworkIsolation``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation
        """
        return jsii.get(self, "enableNetworkIsolation")

    @enable_network_isolation.setter # type: ignore
    def enable_network_isolation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableNetworkIsolation", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Model.ModelName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname
        """
        return jsii.get(self, "modelName")

    @model_name.setter # type: ignore
    def model_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "modelName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="primaryContainer")
    def primary_container(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]:
        """``AWS::SageMaker::Model.PrimaryContainer``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer
        """
        return jsii.get(self, "primaryContainer")

    @primary_container.setter # type: ignore
    def primary_container(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]],
    ) -> None:
        jsii.set(self, "primaryContainer", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]]:
        """``AWS::SageMaker::Model.VpcConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig
        """
        return jsii.get(self, "vpcConfig")

    @vpc_config.setter # type: ignore
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]],
    ) -> None:
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.ContainerDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_hostname": "containerHostname",
            "environment": "environment",
            "image": "image",
            "image_config": "imageConfig",
            "mode": "mode",
            "model_data_url": "modelDataUrl",
            "model_package_name": "modelPackageName",
            "multi_model_config": "multiModelConfig",
        },
    )
    class ContainerDefinitionProperty:
        def __init__(
            self,
            *,
            container_hostname: typing.Optional[builtins.str] = None,
            environment: typing.Any = None,
            image: typing.Optional[builtins.str] = None,
            image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]] = None,
            mode: typing.Optional[builtins.str] = None,
            model_data_url: typing.Optional[builtins.str] = None,
            model_package_name: typing.Optional[builtins.str] = None,
            multi_model_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]] = None,
        ) -> None:
            """
            :param container_hostname: ``CfnModel.ContainerDefinitionProperty.ContainerHostname``.
            :param environment: ``CfnModel.ContainerDefinitionProperty.Environment``.
            :param image: ``CfnModel.ContainerDefinitionProperty.Image``.
            :param image_config: ``CfnModel.ContainerDefinitionProperty.ImageConfig``.
            :param mode: ``CfnModel.ContainerDefinitionProperty.Mode``.
            :param model_data_url: ``CfnModel.ContainerDefinitionProperty.ModelDataUrl``.
            :param model_package_name: ``CfnModel.ContainerDefinitionProperty.ModelPackageName``.
            :param multi_model_config: ``CfnModel.ContainerDefinitionProperty.MultiModelConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if container_hostname is not None:
                self._values["container_hostname"] = container_hostname
            if environment is not None:
                self._values["environment"] = environment
            if image is not None:
                self._values["image"] = image
            if image_config is not None:
                self._values["image_config"] = image_config
            if mode is not None:
                self._values["mode"] = mode
            if model_data_url is not None:
                self._values["model_data_url"] = model_data_url
            if model_package_name is not None:
                self._values["model_package_name"] = model_package_name
            if multi_model_config is not None:
                self._values["multi_model_config"] = multi_model_config

        @builtins.property
        def container_hostname(self) -> typing.Optional[builtins.str]:
            """``CfnModel.ContainerDefinitionProperty.ContainerHostname``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-containerhostname
            """
            result = self._values.get("container_hostname")
            return result

        @builtins.property
        def environment(self) -> typing.Any:
            """``CfnModel.ContainerDefinitionProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-environment
            """
            result = self._values.get("environment")
            return result

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            """``CfnModel.ContainerDefinitionProperty.Image``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-image
            """
            result = self._values.get("image")
            return result

        @builtins.property
        def image_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]]:
            """``CfnModel.ContainerDefinitionProperty.ImageConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-imageconfig
            """
            result = self._values.get("image_config")
            return result

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            """``CfnModel.ContainerDefinitionProperty.Mode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-mode
            """
            result = self._values.get("mode")
            return result

        @builtins.property
        def model_data_url(self) -> typing.Optional[builtins.str]:
            """``CfnModel.ContainerDefinitionProperty.ModelDataUrl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modeldataurl
            """
            result = self._values.get("model_data_url")
            return result

        @builtins.property
        def model_package_name(self) -> typing.Optional[builtins.str]:
            """``CfnModel.ContainerDefinitionProperty.ModelPackageName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modelpackagename
            """
            result = self._values.get("model_package_name")
            return result

        @builtins.property
        def multi_model_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]]:
            """``CfnModel.ContainerDefinitionProperty.MultiModelConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-multimodelconfig
            """
            result = self._values.get("multi_model_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.ImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_access_mode": "repositoryAccessMode"},
    )
    class ImageConfigProperty:
        def __init__(self, *, repository_access_mode: builtins.str) -> None:
            """
            :param repository_access_mode: ``CfnModel.ImageConfigProperty.RepositoryAccessMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "repository_access_mode": repository_access_mode,
            }

        @builtins.property
        def repository_access_mode(self) -> builtins.str:
            """``CfnModel.ImageConfigProperty.RepositoryAccessMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryaccessmode
            """
            result = self._values.get("repository_access_mode")
            assert result is not None, "Required property 'repository_access_mode' is missing"
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
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.MultiModelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"model_cache_setting": "modelCacheSetting"},
    )
    class MultiModelConfigProperty:
        def __init__(
            self,
            *,
            model_cache_setting: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param model_cache_setting: ``CfnModel.MultiModelConfigProperty.ModelCacheSetting``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if model_cache_setting is not None:
                self._values["model_cache_setting"] = model_cache_setting

        @builtins.property
        def model_cache_setting(self) -> typing.Optional[builtins.str]:
            """``CfnModel.MultiModelConfigProperty.ModelCacheSetting``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html#cfn-sagemaker-model-containerdefinition-multimodelconfig-modelcachesetting
            """
            result = self._values.get("model_cache_setting")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiModelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnets: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnModel.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModel.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnModel.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            """``CfnModel.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-subnets
            """
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelBiasJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition",
):
    """A CloudFormation ``AWS::SageMaker::ModelBiasJobDefinition``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
    :cloudformationResource: AWS::SageMaker::ModelBiasJobDefinition
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"],
        model_bias_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"],
        model_bias_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"],
        model_bias_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_bias_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::ModelBiasJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_resources: ``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.
        :param model_bias_app_specification: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.
        :param model_bias_job_input: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.
        :param model_bias_job_output_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.
        :param model_bias_baseline_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelBiasJobDefinition.Tags``.
        """
        props = CfnModelBiasJobDefinitionProps(
            job_resources=job_resources,
            model_bias_app_specification=model_bias_app_specification,
            model_bias_job_input=model_bias_job_input,
            model_bias_job_output_config=model_bias_job_output_config,
            role_arn=role_arn,
            job_definition_name=job_definition_name,
            model_bias_baseline_config=model_bias_baseline_config,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnModelBiasJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: JobDefinitionArn
        """
        return jsii.get(self, "attrJobDefinitionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"]:
        """``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        """
        return jsii.get(self, "jobResources")

    @job_resources.setter # type: ignore
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelBiasAppSpecification")
    def model_bias_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        """
        return jsii.get(self, "modelBiasAppSpecification")

    @model_bias_app_specification.setter # type: ignore
    def model_bias_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelBiasAppSpecification", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelBiasJobInput")
    def model_bias_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        """
        return jsii.get(self, "modelBiasJobInput")

    @model_bias_job_input.setter # type: ignore
    def model_bias_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelBiasJobInput", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelBiasJobOutputConfig")
    def model_bias_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        """
        return jsii.get(self, "modelBiasJobOutputConfig")

    @model_bias_job_output_config.setter # type: ignore
    def model_bias_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelBiasJobOutputConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        """
        return jsii.get(self, "jobDefinitionName")

    @job_definition_name.setter # type: ignore
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelBiasBaselineConfig")
    def model_bias_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        """
        return jsii.get(self, "modelBiasBaselineConfig")

    @model_bias_baseline_config.setter # type: ignore
    def model_bias_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelBiasBaselineConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        """
        return jsii.get(self, "networkConfig")

    @network_config.setter # type: ignore
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        """
        return jsii.get(self, "stoppingCondition")

    @stopping_condition.setter # type: ignore
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param instance_count: ``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            """``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancecount
            """
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            """``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumesizeingb
            """
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return result

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumekmskeyid
            """
            result = self._values.get("volume_kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnModelBiasJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html#cfn-sagemaker-modelbiasjobdefinition-constraintsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "end_time_offset": "endTimeOffset",
            "features_attribute": "featuresAttribute",
            "inference_attribute": "inferenceAttribute",
            "probability_attribute": "probabilityAttribute",
            "probability_threshold_attribute": "probabilityThresholdAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
            "start_time_offset": "startTimeOffset",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            end_time_offset: typing.Optional[builtins.str] = None,
            features_attribute: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            probability_attribute: typing.Optional[builtins.str] = None,
            probability_threshold_attribute: typing.Optional[jsii.Number] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
            start_time_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param endpoint_name: ``CfnModelBiasJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnModelBiasJobDefinition.EndpointInputProperty.LocalPath``.
            :param end_time_offset: ``CfnModelBiasJobDefinition.EndpointInputProperty.EndTimeOffset``.
            :param features_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.FeaturesAttribute``.
            :param inference_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param probability_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param probability_threshold_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.
            :param s3_data_distribution_type: ``CfnModelBiasJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelBiasJobDefinition.EndpointInputProperty.S3InputMode``.
            :param start_time_offset: ``CfnModelBiasJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if end_time_offset is not None:
                self._values["end_time_offset"] = end_time_offset
            if features_attribute is not None:
                self._values["features_attribute"] = features_attribute
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if probability_threshold_attribute is not None:
                self._values["probability_threshold_attribute"] = probability_threshold_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode
            if start_time_offset is not None:
                self._values["start_time_offset"] = start_time_offset

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.EndpointName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endpointname
            """
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return result

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def end_time_offset(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.EndTimeOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endtimeoffset
            """
            result = self._values.get("end_time_offset")
            return result

        @builtins.property
        def features_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.FeaturesAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-featuresattribute
            """
            result = self._values.get("features_attribute")
            return result

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-inferenceattribute
            """
            result = self._values.get("inference_attribute")
            return result

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilityattribute
            """
            result = self._values.get("probability_attribute")
            return result

        @builtins.property
        def probability_threshold_attribute(self) -> typing.Optional[jsii.Number]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilitythresholdattribute
            """
            result = self._values.get("probability_threshold_attribute")
            return result

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3datadistributiontype
            """
            result = self._values.get("s3_data_distribution_type")
            return result

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3inputmode
            """
            result = self._values.get("s3_input_mode")
            return result

        @builtins.property
        def start_time_offset(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-starttimeoffset
            """
            result = self._values.get("start_time_offset")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "config_uri": "configUri",
            "image_uri": "imageUri",
            "environment": "environment",
        },
    )
    class ModelBiasAppSpecificationProperty:
        def __init__(
            self,
            *,
            config_uri: builtins.str,
            image_uri: builtins.str,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EnvironmentProperty"]] = None,
        ) -> None:
            """
            :param config_uri: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ConfigUri``.
            :param image_uri: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ImageUri``.
            :param environment: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "config_uri": config_uri,
                "image_uri": image_uri,
            }
            if environment is not None:
                self._values["environment"] = environment

        @builtins.property
        def config_uri(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ConfigUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri
            """
            result = self._values.get("config_uri")
            assert result is not None, "Required property 'config_uri' is missing"
            return result

        @builtins.property
        def image_uri(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ImageUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri
            """
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return result

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EnvironmentProperty"]]:
            """``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment
            """
            result = self._values.get("environment")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelBiasBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            """
            :param baselining_job_name: ``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.BaseliningJobName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-baseliningjobname
            """
            result = self._values.get("baselining_job_name")
            return result

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]]:
            """``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-constraintsresource
            """
            result = self._values.get("constraints_resource")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_input": "endpointInput",
            "ground_truth_s3_input": "groundTruthS3Input",
        },
    )
    class ModelBiasJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"],
            ground_truth_s3_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"],
        ) -> None:
            """
            :param endpoint_input: ``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.EndpointInput``.
            :param ground_truth_s3_input: ``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.GroundTruthS3Input``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
                "ground_truth_s3_input": ground_truth_s3_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"]:
            """``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput
            """
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return result

        @builtins.property
        def ground_truth_s3_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"]:
            """``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.GroundTruthS3Input``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input
            """
            result = self._values.get("ground_truth_s3_input")
            assert result is not None, "Required property 'ground_truth_s3_input' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class MonitoringGroundTruthS3InputProperty:
        def __init__(self, *, s3_uri: builtins.str) -> None:
            """
            :param s3_uri: ``CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_uri": s3_uri,
            }

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringGroundTruthS3InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param monitoring_outputs: ``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]]:
            """``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-monitoringoutputs
            """
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"],
        ) -> None:
            """
            :param s3_output: ``CfnModelBiasJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"]:
            """``CfnModelBiasJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutput-s3output
            """
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"],
        ) -> None:
            """
            :param cluster_config: ``CfnModelBiasJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"]:
            """``CfnModelBiasJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html#cfn-sagemaker-modelbiasjobdefinition-monitoringresources-clusterconfig
            """
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            """
            :param enable_inter_container_traffic_encryption: ``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelBiasJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enableintercontainertrafficencryption
            """
            result = self._values.get("enable_inter_container_traffic_encryption")
            return result

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enablenetworkisolation
            """
            result = self._values.get("enable_network_isolation")
            return result

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]]:
            """``CfnModelBiasJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-vpcconfig
            """
            result = self._values.get("vpc_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param local_path: ``CfnModelBiasJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnModelBiasJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnModelBiasJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.S3OutputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnModelBiasJobDefinition.S3OutputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            """``CfnModelBiasJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uploadmode
            """
            result = self._values.get("s3_upload_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            """
            :param max_runtime_in_seconds: ``CfnModelBiasJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            """``CfnModelBiasJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition-maxruntimeinseconds
            """
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnets: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnModelBiasJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelBiasJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnModelBiasJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            """``CfnModelBiasJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets
            """
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
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
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_resources": "jobResources",
        "model_bias_app_specification": "modelBiasAppSpecification",
        "model_bias_job_input": "modelBiasJobInput",
        "model_bias_job_output_config": "modelBiasJobOutputConfig",
        "role_arn": "roleArn",
        "job_definition_name": "jobDefinitionName",
        "model_bias_baseline_config": "modelBiasBaselineConfig",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelBiasJobDefinitionProps:
    def __init__(
        self,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty],
        model_bias_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty],
        model_bias_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty],
        model_bias_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_bias_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::ModelBiasJobDefinition``.

        :param job_resources: ``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.
        :param model_bias_app_specification: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.
        :param model_bias_job_input: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.
        :param model_bias_job_output_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.
        :param model_bias_baseline_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_bias_app_specification": model_bias_app_specification,
            "model_bias_job_input": model_bias_job_input,
            "model_bias_job_output_config": model_bias_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_bias_baseline_config is not None:
            self._values["model_bias_baseline_config"] = model_bias_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty]:
        """``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        """
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return result

    @builtins.property
    def model_bias_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        """
        result = self._values.get("model_bias_app_specification")
        assert result is not None, "Required property 'model_bias_app_specification' is missing"
        return result

    @builtins.property
    def model_bias_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        """
        result = self._values.get("model_bias_job_input")
        assert result is not None, "Required property 'model_bias_job_input' is missing"
        return result

    @builtins.property
    def model_bias_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        """
        result = self._values.get("model_bias_job_output_config")
        assert result is not None, "Required property 'model_bias_job_output_config' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        """
        result = self._values.get("job_definition_name")
        return result

    @builtins.property
    def model_bias_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        """
        result = self._values.get("model_bias_baseline_config")
        return result

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        """
        result = self._values.get("network_config")
        return result

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        """
        result = self._values.get("stopping_condition")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelBiasJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelExplainabilityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition",
):
    """A CloudFormation ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
    :cloudformationResource: AWS::SageMaker::ModelExplainabilityJobDefinition
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"],
        model_explainability_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"],
        model_explainability_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"],
        model_explainability_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_explainability_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_resources: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.
        :param model_explainability_app_specification: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.
        :param model_explainability_job_input: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.
        :param model_explainability_job_output_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.
        :param model_explainability_baseline_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.
        """
        props = CfnModelExplainabilityJobDefinitionProps(
            job_resources=job_resources,
            model_explainability_app_specification=model_explainability_app_specification,
            model_explainability_job_input=model_explainability_job_input,
            model_explainability_job_output_config=model_explainability_job_output_config,
            role_arn=role_arn,
            job_definition_name=job_definition_name,
            model_explainability_baseline_config=model_explainability_baseline_config,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnModelExplainabilityJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: JobDefinitionArn
        """
        return jsii.get(self, "attrJobDefinitionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
        """
        return jsii.get(self, "jobResources")

    @job_resources.setter # type: ignore
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelExplainabilityAppSpecification")
    def model_explainability_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
        """
        return jsii.get(self, "modelExplainabilityAppSpecification")

    @model_explainability_app_specification.setter # type: ignore
    def model_explainability_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityAppSpecification", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelExplainabilityJobInput")
    def model_explainability_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
        """
        return jsii.get(self, "modelExplainabilityJobInput")

    @model_explainability_job_input.setter # type: ignore
    def model_explainability_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityJobInput", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelExplainabilityJobOutputConfig")
    def model_explainability_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
        """
        return jsii.get(self, "modelExplainabilityJobOutputConfig")

    @model_explainability_job_output_config.setter # type: ignore
    def model_explainability_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityJobOutputConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
        """
        return jsii.get(self, "jobDefinitionName")

    @job_definition_name.setter # type: ignore
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelExplainabilityBaselineConfig")
    def model_explainability_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
        """
        return jsii.get(self, "modelExplainabilityBaselineConfig")

    @model_explainability_baseline_config.setter # type: ignore
    def model_explainability_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelExplainabilityBaselineConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
        """
        return jsii.get(self, "networkConfig")

    @network_config.setter # type: ignore
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
        """
        return jsii.get(self, "stoppingCondition")

    @stopping_condition.setter # type: ignore
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param instance_count: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            """``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancecount
            """
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            """``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumesizeingb
            """
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return result

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumekmskeyid
            """
            result = self._values.get("volume_kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html#cfn-sagemaker-modelexplainabilityjobdefinition-constraintsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "features_attribute": "featuresAttribute",
            "inference_attribute": "inferenceAttribute",
            "probability_attribute": "probabilityAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            features_attribute: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            probability_attribute: typing.Optional[builtins.str] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param endpoint_name: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.LocalPath``.
            :param features_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.FeaturesAttribute``.
            :param inference_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param probability_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param s3_data_distribution_type: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if features_attribute is not None:
                self._values["features_attribute"] = features_attribute
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.EndpointName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-endpointname
            """
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return result

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def features_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.FeaturesAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-featuresattribute
            """
            result = self._values.get("features_attribute")
            return result

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-inferenceattribute
            """
            result = self._values.get("inference_attribute")
            return result

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-probabilityattribute
            """
            result = self._values.get("probability_attribute")
            return result

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3datadistributiontype
            """
            result = self._values.get("s3_data_distribution_type")
            return result

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3inputmode
            """
            result = self._values.get("s3_input_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "config_uri": "configUri",
            "image_uri": "imageUri",
            "environment": "environment",
        },
    )
    class ModelExplainabilityAppSpecificationProperty:
        def __init__(
            self,
            *,
            config_uri: builtins.str,
            image_uri: builtins.str,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EnvironmentProperty"]] = None,
        ) -> None:
            """
            :param config_uri: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ConfigUri``.
            :param image_uri: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ImageUri``.
            :param environment: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "config_uri": config_uri,
                "image_uri": image_uri,
            }
            if environment is not None:
                self._values["environment"] = environment

        @builtins.property
        def config_uri(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ConfigUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri
            """
            result = self._values.get("config_uri")
            assert result is not None, "Required property 'config_uri' is missing"
            return result

        @builtins.property
        def image_uri(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ImageUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri
            """
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return result

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EnvironmentProperty"]]:
            """``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment
            """
            result = self._values.get("environment")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelExplainabilityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            """
            :param baselining_job_name: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.BaseliningJobName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-baseliningjobname
            """
            result = self._values.get("baselining_job_name")
            return result

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]]:
            """``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-constraintsresource
            """
            result = self._values.get("constraints_resource")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class ModelExplainabilityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"],
        ) -> None:
            """
            :param endpoint_input: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"]:
            """``CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput
            """
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param monitoring_outputs: ``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]]:
            """``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-monitoringoutputs
            """
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"],
        ) -> None:
            """
            :param s3_output: ``CfnModelExplainabilityJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"]:
            """``CfnModelExplainabilityJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutput-s3output
            """
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            """
            :param cluster_config: ``CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"]:
            """``CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig
            """
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            """
            :param enable_inter_container_traffic_encryption: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enableintercontainertrafficencryption
            """
            result = self._values.get("enable_inter_container_traffic_encryption")
            return result

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enablenetworkisolation
            """
            result = self._values.get("enable_network_isolation")
            return result

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]]:
            """``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-vpcconfig
            """
            result = self._values.get("vpc_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param local_path: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.S3OutputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uploadmode
            """
            result = self._values.get("s3_upload_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            """
            :param max_runtime_in_seconds: ``CfnModelExplainabilityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            """``CfnModelExplainabilityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds
            """
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnets: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnModelExplainabilityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelExplainabilityJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            """``CfnModelExplainabilityJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-subnets
            """
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
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
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_resources": "jobResources",
        "model_explainability_app_specification": "modelExplainabilityAppSpecification",
        "model_explainability_job_input": "modelExplainabilityJobInput",
        "model_explainability_job_output_config": "modelExplainabilityJobOutputConfig",
        "role_arn": "roleArn",
        "job_definition_name": "jobDefinitionName",
        "model_explainability_baseline_config": "modelExplainabilityBaselineConfig",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelExplainabilityJobDefinitionProps:
    def __init__(
        self,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty],
        model_explainability_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty],
        model_explainability_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty],
        model_explainability_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_explainability_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

        :param job_resources: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.
        :param model_explainability_app_specification: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.
        :param model_explainability_job_input: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.
        :param model_explainability_job_output_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.
        :param model_explainability_baseline_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_explainability_app_specification": model_explainability_app_specification,
            "model_explainability_job_input": model_explainability_job_input,
            "model_explainability_job_output_config": model_explainability_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_explainability_baseline_config is not None:
            self._values["model_explainability_baseline_config"] = model_explainability_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
        """
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return result

    @builtins.property
    def model_explainability_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
        """
        result = self._values.get("model_explainability_app_specification")
        assert result is not None, "Required property 'model_explainability_app_specification' is missing"
        return result

    @builtins.property
    def model_explainability_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
        """
        result = self._values.get("model_explainability_job_input")
        assert result is not None, "Required property 'model_explainability_job_input' is missing"
        return result

    @builtins.property
    def model_explainability_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
        """
        result = self._values.get("model_explainability_job_output_config")
        assert result is not None, "Required property 'model_explainability_job_output_config' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
        """
        result = self._values.get("job_definition_name")
        return result

    @builtins.property
    def model_explainability_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
        """
        result = self._values.get("model_explainability_baseline_config")
        return result

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
        """
        result = self._values.get("network_config")
        return result

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
        """
        result = self._values.get("stopping_condition")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelExplainabilityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelPackageGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelPackageGroup",
):
    """A CloudFormation ``AWS::SageMaker::ModelPackageGroup``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
    :cloudformationResource: AWS::SageMaker::ModelPackageGroup
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        model_package_group_name: builtins.str,
        model_package_group_description: typing.Optional[builtins.str] = None,
        model_package_group_policy: typing.Any = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::ModelPackageGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param model_package_group_name: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.
        :param model_package_group_description: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.
        :param model_package_group_policy: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.
        :param tags: ``AWS::SageMaker::ModelPackageGroup.Tags``.
        """
        props = CfnModelPackageGroupProps(
            model_package_group_name=model_package_group_name,
            model_package_group_description=model_package_group_description,
            model_package_group_policy=model_package_group_policy,
            tags=tags,
        )

        jsii.create(CfnModelPackageGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrModelPackageGroupArn")
    def attr_model_package_group_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: ModelPackageGroupArn
        """
        return jsii.get(self, "attrModelPackageGroupArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrModelPackageGroupStatus")
    def attr_model_package_group_status(self) -> builtins.str:
        """
        :cloudformationAttribute: ModelPackageGroupStatus
        """
        return jsii.get(self, "attrModelPackageGroupStatus")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::ModelPackageGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelPackageGroupName")
    def model_package_group_name(self) -> builtins.str:
        """``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        """
        return jsii.get(self, "modelPackageGroupName")

    @model_package_group_name.setter # type: ignore
    def model_package_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "modelPackageGroupName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelPackageGroupPolicy")
    def model_package_group_policy(self) -> typing.Any:
        """``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        """
        return jsii.get(self, "modelPackageGroupPolicy")

    @model_package_group_policy.setter # type: ignore
    def model_package_group_policy(self, value: typing.Any) -> None:
        jsii.set(self, "modelPackageGroupPolicy", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelPackageGroupDescription")
    def model_package_group_description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        """
        return jsii.get(self, "modelPackageGroupDescription")

    @model_package_group_description.setter # type: ignore
    def model_package_group_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "modelPackageGroupDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelPackageGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "model_package_group_name": "modelPackageGroupName",
        "model_package_group_description": "modelPackageGroupDescription",
        "model_package_group_policy": "modelPackageGroupPolicy",
        "tags": "tags",
    },
)
class CfnModelPackageGroupProps:
    def __init__(
        self,
        *,
        model_package_group_name: builtins.str,
        model_package_group_description: typing.Optional[builtins.str] = None,
        model_package_group_policy: typing.Any = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::ModelPackageGroup``.

        :param model_package_group_name: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.
        :param model_package_group_description: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.
        :param model_package_group_policy: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.
        :param tags: ``AWS::SageMaker::ModelPackageGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "model_package_group_name": model_package_group_name,
        }
        if model_package_group_description is not None:
            self._values["model_package_group_description"] = model_package_group_description
        if model_package_group_policy is not None:
            self._values["model_package_group_policy"] = model_package_group_policy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def model_package_group_name(self) -> builtins.str:
        """``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        """
        result = self._values.get("model_package_group_name")
        assert result is not None, "Required property 'model_package_group_name' is missing"
        return result

    @builtins.property
    def model_package_group_description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        """
        result = self._values.get("model_package_group_description")
        return result

    @builtins.property
    def model_package_group_policy(self) -> typing.Any:
        """``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        """
        result = self._values.get("model_package_group_policy")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::ModelPackageGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelPackageGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role_arn": "executionRoleArn",
        "containers": "containers",
        "enable_network_isolation": "enableNetworkIsolation",
        "model_name": "modelName",
        "primary_container": "primaryContainer",
        "tags": "tags",
        "vpc_config": "vpcConfig",
    },
)
class CfnModelProps:
    def __init__(
        self,
        *,
        execution_role_arn: builtins.str,
        containers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]] = None,
        enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        model_name: typing.Optional[builtins.str] = None,
        primary_container: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::Model``.

        :param execution_role_arn: ``AWS::SageMaker::Model.ExecutionRoleArn``.
        :param containers: ``AWS::SageMaker::Model.Containers``.
        :param enable_network_isolation: ``AWS::SageMaker::Model.EnableNetworkIsolation``.
        :param model_name: ``AWS::SageMaker::Model.ModelName``.
        :param primary_container: ``AWS::SageMaker::Model.PrimaryContainer``.
        :param tags: ``AWS::SageMaker::Model.Tags``.
        :param vpc_config: ``AWS::SageMaker::Model.VpcConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "execution_role_arn": execution_role_arn,
        }
        if containers is not None:
            self._values["containers"] = containers
        if enable_network_isolation is not None:
            self._values["enable_network_isolation"] = enable_network_isolation
        if model_name is not None:
            self._values["model_name"] = model_name
        if primary_container is not None:
            self._values["primary_container"] = primary_container
        if tags is not None:
            self._values["tags"] = tags
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        """``AWS::SageMaker::Model.ExecutionRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn
        """
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return result

    @builtins.property
    def containers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]]:
        """``AWS::SageMaker::Model.Containers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers
        """
        result = self._values.get("containers")
        return result

    @builtins.property
    def enable_network_isolation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        """``AWS::SageMaker::Model.EnableNetworkIsolation``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation
        """
        result = self._values.get("enable_network_isolation")
        return result

    @builtins.property
    def model_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Model.ModelName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname
        """
        result = self._values.get("model_name")
        return result

    @builtins.property
    def primary_container(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]:
        """``AWS::SageMaker::Model.PrimaryContainer``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer
        """
        result = self._values.get("primary_container")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::Model.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]]:
        """``AWS::SageMaker::Model.VpcConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig
        """
        result = self._values.get("vpc_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelQualityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition",
):
    """A CloudFormation ``AWS::SageMaker::ModelQualityJobDefinition``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
    :cloudformationResource: AWS::SageMaker::ModelQualityJobDefinition
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"],
        model_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"],
        model_quality_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"],
        model_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::ModelQualityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_resources: ``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.
        :param model_quality_app_specification: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.
        :param model_quality_job_input: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.
        :param model_quality_job_output_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.
        :param model_quality_baseline_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelQualityJobDefinition.Tags``.
        """
        props = CfnModelQualityJobDefinitionProps(
            job_resources=job_resources,
            model_quality_app_specification=model_quality_app_specification,
            model_quality_job_input=model_quality_job_input,
            model_quality_job_output_config=model_quality_job_output_config,
            role_arn=role_arn,
            job_definition_name=job_definition_name,
            model_quality_baseline_config=model_quality_baseline_config,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnModelQualityJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: JobDefinitionArn
        """
        return jsii.get(self, "attrJobDefinitionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"]:
        """``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources
        """
        return jsii.get(self, "jobResources")

    @job_resources.setter # type: ignore
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelQualityAppSpecification")
    def model_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification
        """
        return jsii.get(self, "modelQualityAppSpecification")

    @model_quality_app_specification.setter # type: ignore
    def model_quality_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelQualityAppSpecification", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelQualityJobInput")
    def model_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput
        """
        return jsii.get(self, "modelQualityJobInput")

    @model_quality_job_input.setter # type: ignore
    def model_quality_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelQualityJobInput", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelQualityJobOutputConfig")
    def model_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig
        """
        return jsii.get(self, "modelQualityJobOutputConfig")

    @model_quality_job_output_config.setter # type: ignore
    def model_quality_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelQualityJobOutputConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname
        """
        return jsii.get(self, "jobDefinitionName")

    @job_definition_name.setter # type: ignore
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modelQualityBaselineConfig")
    def model_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig
        """
        return jsii.get(self, "modelQualityBaselineConfig")

    @model_quality_baseline_config.setter # type: ignore
    def model_quality_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelQualityBaselineConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig
        """
        return jsii.get(self, "networkConfig")

    @network_config.setter # type: ignore
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition
        """
        return jsii.get(self, "stoppingCondition")

    @stopping_condition.setter # type: ignore
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param instance_count: ``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            """``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount
            """
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            """``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb
            """
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return result

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid
            """
            result = self._values.get("volume_kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnModelQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html#cfn-sagemaker-modelqualityjobdefinition-constraintsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "end_time_offset": "endTimeOffset",
            "inference_attribute": "inferenceAttribute",
            "probability_attribute": "probabilityAttribute",
            "probability_threshold_attribute": "probabilityThresholdAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
            "start_time_offset": "startTimeOffset",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            end_time_offset: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            probability_attribute: typing.Optional[builtins.str] = None,
            probability_threshold_attribute: typing.Optional[jsii.Number] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
            start_time_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param endpoint_name: ``CfnModelQualityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnModelQualityJobDefinition.EndpointInputProperty.LocalPath``.
            :param end_time_offset: ``CfnModelQualityJobDefinition.EndpointInputProperty.EndTimeOffset``.
            :param inference_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param probability_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param probability_threshold_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.
            :param s3_data_distribution_type: ``CfnModelQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelQualityJobDefinition.EndpointInputProperty.S3InputMode``.
            :param start_time_offset: ``CfnModelQualityJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if end_time_offset is not None:
                self._values["end_time_offset"] = end_time_offset
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if probability_threshold_attribute is not None:
                self._values["probability_threshold_attribute"] = probability_threshold_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode
            if start_time_offset is not None:
                self._values["start_time_offset"] = start_time_offset

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.EndpointName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endpointname
            """
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return result

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def end_time_offset(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.EndTimeOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endtimeoffset
            """
            result = self._values.get("end_time_offset")
            return result

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-inferenceattribute
            """
            result = self._values.get("inference_attribute")
            return result

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilityattribute
            """
            result = self._values.get("probability_attribute")
            return result

        @builtins.property
        def probability_threshold_attribute(self) -> typing.Optional[jsii.Number]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilitythresholdattribute
            """
            result = self._values.get("probability_threshold_attribute")
            return result

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3datadistributiontype
            """
            result = self._values.get("s3_data_distribution_type")
            return result

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3inputmode
            """
            result = self._values.get("s3_input_mode")
            return result

        @builtins.property
        def start_time_offset(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-starttimeoffset
            """
            result = self._values.get("start_time_offset")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "problem_type": "problemType",
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "environment": "environment",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class ModelQualityAppSpecificationProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            problem_type: builtins.str,
            container_arguments: typing.Optional[typing.List[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.List[builtins.str]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EnvironmentProperty"]] = None,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param image_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ImageUri``.
            :param problem_type: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ProblemType``.
            :param container_arguments: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerEntrypoint``.
            :param environment: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.Environment``.
            :param post_analytics_processor_source_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
                "problem_type": problem_type,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if environment is not None:
                self._values["environment"] = environment
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def image_uri(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ImageUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-imageuri
            """
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return result

        @builtins.property
        def problem_type(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ProblemType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-problemtype
            """
            result = self._values.get("problem_type")
            assert result is not None, "Required property 'problem_type' is missing"
            return result

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerArguments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerarguments
            """
            result = self._values.get("container_arguments")
            return result

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerEntrypoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerentrypoint
            """
            result = self._values.get("container_entrypoint")
            return result

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EnvironmentProperty"]]:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-environment
            """
            result = self._values.get("environment")
            return result

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-postanalyticsprocessorsourceuri
            """
            result = self._values.get("post_analytics_processor_source_uri")
            return result

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-recordpreprocessorsourceuri
            """
            result = self._values.get("record_preprocessor_source_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelQualityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            """
            :param baselining_job_name: ``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.BaseliningJobName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname
            """
            result = self._values.get("baselining_job_name")
            return result

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]]:
            """``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource
            """
            result = self._values.get("constraints_resource")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_input": "endpointInput",
            "ground_truth_s3_input": "groundTruthS3Input",
        },
    )
    class ModelQualityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"],
            ground_truth_s3_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"],
        ) -> None:
            """
            :param endpoint_input: ``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.EndpointInput``.
            :param ground_truth_s3_input: ``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.GroundTruthS3Input``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
                "ground_truth_s3_input": ground_truth_s3_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"]:
            """``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput
            """
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return result

        @builtins.property
        def ground_truth_s3_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"]:
            """``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.GroundTruthS3Input``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input
            """
            result = self._values.get("ground_truth_s3_input")
            assert result is not None, "Required property 'ground_truth_s3_input' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class MonitoringGroundTruthS3InputProperty:
        def __init__(self, *, s3_uri: builtins.str) -> None:
            """
            :param s3_uri: ``CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_uri": s3_uri,
            }

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringGroundTruthS3InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param monitoring_outputs: ``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]]:
            """``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-monitoringoutputs
            """
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"],
        ) -> None:
            """
            :param s3_output: ``CfnModelQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"]:
            """``CfnModelQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutput-s3output
            """
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            """
            :param cluster_config: ``CfnModelQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"]:
            """``CfnModelQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html#cfn-sagemaker-modelqualityjobdefinition-monitoringresources-clusterconfig
            """
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            """
            :param enable_inter_container_traffic_encryption: ``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enableintercontainertrafficencryption
            """
            result = self._values.get("enable_inter_container_traffic_encryption")
            return result

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enablenetworkisolation
            """
            result = self._values.get("enable_network_isolation")
            return result

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]]:
            """``CfnModelQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-vpcconfig
            """
            result = self._values.get("vpc_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param local_path: ``CfnModelQualityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnModelQualityJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnModelQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.S3OutputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnModelQualityJobDefinition.S3OutputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            """``CfnModelQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode
            """
            result = self._values.get("s3_upload_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            """
            :param max_runtime_in_seconds: ``CfnModelQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            """``CfnModelQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition-maxruntimeinseconds
            """
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnets: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnModelQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelQualityJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnModelQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            """``CfnModelQualityJobDefinition.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-subnets
            """
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
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
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_resources": "jobResources",
        "model_quality_app_specification": "modelQualityAppSpecification",
        "model_quality_job_input": "modelQualityJobInput",
        "model_quality_job_output_config": "modelQualityJobOutputConfig",
        "role_arn": "roleArn",
        "job_definition_name": "jobDefinitionName",
        "model_quality_baseline_config": "modelQualityBaselineConfig",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelQualityJobDefinitionProps:
    def __init__(
        self,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty],
        model_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty],
        model_quality_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty],
        model_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::ModelQualityJobDefinition``.

        :param job_resources: ``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.
        :param model_quality_app_specification: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.
        :param model_quality_job_input: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.
        :param model_quality_job_output_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.
        :param model_quality_baseline_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_quality_app_specification": model_quality_app_specification,
            "model_quality_job_input": model_quality_job_input,
            "model_quality_job_output_config": model_quality_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_quality_baseline_config is not None:
            self._values["model_quality_baseline_config"] = model_quality_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty]:
        """``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources
        """
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return result

    @builtins.property
    def model_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification
        """
        result = self._values.get("model_quality_app_specification")
        assert result is not None, "Required property 'model_quality_app_specification' is missing"
        return result

    @builtins.property
    def model_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput
        """
        result = self._values.get("model_quality_job_input")
        assert result is not None, "Required property 'model_quality_job_input' is missing"
        return result

    @builtins.property
    def model_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig
        """
        result = self._values.get("model_quality_job_output_config")
        assert result is not None, "Required property 'model_quality_job_output_config' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname
        """
        result = self._values.get("job_definition_name")
        return result

    @builtins.property
    def model_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig
        """
        result = self._values.get("model_quality_baseline_config")
        return result

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig
        """
        result = self._values.get("network_config")
        return result

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition
        """
        result = self._values.get("stopping_condition")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelQualityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMonitoringSchedule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule",
):
    """A CloudFormation ``AWS::SageMaker::MonitoringSchedule``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
    :cloudformationResource: AWS::SageMaker::MonitoringSchedule
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        monitoring_schedule_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"],
        monitoring_schedule_name: builtins.str,
        endpoint_name: typing.Optional[builtins.str] = None,
        failure_reason: typing.Optional[builtins.str] = None,
        last_monitoring_execution_summary: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]] = None,
        monitoring_schedule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::MonitoringSchedule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param monitoring_schedule_config: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.
        :param monitoring_schedule_name: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.
        :param endpoint_name: ``AWS::SageMaker::MonitoringSchedule.EndpointName``.
        :param failure_reason: ``AWS::SageMaker::MonitoringSchedule.FailureReason``.
        :param last_monitoring_execution_summary: ``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.
        :param monitoring_schedule_status: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.
        :param tags: ``AWS::SageMaker::MonitoringSchedule.Tags``.
        """
        props = CfnMonitoringScheduleProps(
            monitoring_schedule_config=monitoring_schedule_config,
            monitoring_schedule_name=monitoring_schedule_name,
            endpoint_name=endpoint_name,
            failure_reason=failure_reason,
            last_monitoring_execution_summary=last_monitoring_execution_summary,
            monitoring_schedule_status=monitoring_schedule_status,
            tags=tags,
        )

        jsii.create(CfnMonitoringSchedule, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        """
        :cloudformationAttribute: LastModifiedTime
        """
        return jsii.get(self, "attrLastModifiedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrMonitoringScheduleArn")
    def attr_monitoring_schedule_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: MonitoringScheduleArn
        """
        return jsii.get(self, "attrMonitoringScheduleArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::MonitoringSchedule.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="monitoringScheduleConfig")
    def monitoring_schedule_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"]:
        """``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig
        """
        return jsii.get(self, "monitoringScheduleConfig")

    @monitoring_schedule_config.setter # type: ignore
    def monitoring_schedule_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"],
    ) -> None:
        jsii.set(self, "monitoringScheduleConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="monitoringScheduleName")
    def monitoring_schedule_name(self) -> builtins.str:
        """``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename
        """
        return jsii.get(self, "monitoringScheduleName")

    @monitoring_schedule_name.setter # type: ignore
    def monitoring_schedule_name(self, value: builtins.str) -> None:
        jsii.set(self, "monitoringScheduleName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::MonitoringSchedule.EndpointName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname
        """
        return jsii.get(self, "endpointName")

    @endpoint_name.setter # type: ignore
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="failureReason")
    def failure_reason(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::MonitoringSchedule.FailureReason``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason
        """
        return jsii.get(self, "failureReason")

    @failure_reason.setter # type: ignore
    def failure_reason(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "failureReason", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lastMonitoringExecutionSummary")
    def last_monitoring_execution_summary(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]]:
        """``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary
        """
        return jsii.get(self, "lastMonitoringExecutionSummary")

    @last_monitoring_execution_summary.setter # type: ignore
    def last_monitoring_execution_summary(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]],
    ) -> None:
        jsii.set(self, "lastMonitoringExecutionSummary", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="monitoringScheduleStatus")
    def monitoring_schedule_status(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus
        """
        return jsii.get(self, "monitoringScheduleStatus")

    @monitoring_schedule_status.setter # type: ignore
    def monitoring_schedule_status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "monitoringScheduleStatus", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.BaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "constraints_resource": "constraintsResource",
            "statistics_resource": "statisticsResource",
        },
    )
    class BaselineConfigProperty:
        def __init__(
            self,
            *,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]] = None,
            statistics_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]] = None,
        ) -> None:
            """
            :param constraints_resource: ``CfnMonitoringSchedule.BaselineConfigProperty.ConstraintsResource``.
            :param statistics_resource: ``CfnMonitoringSchedule.BaselineConfigProperty.StatisticsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource
            if statistics_resource is not None:
                self._values["statistics_resource"] = statistics_resource

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]]:
            """``CfnMonitoringSchedule.BaselineConfigProperty.ConstraintsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource
            """
            result = self._values.get("constraints_resource")
            return result

        @builtins.property
        def statistics_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]]:
            """``CfnMonitoringSchedule.BaselineConfigProperty.StatisticsResource``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource
            """
            result = self._values.get("statistics_resource")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param instance_count: ``CfnMonitoringSchedule.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnMonitoringSchedule.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnMonitoringSchedule.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnMonitoringSchedule.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            """``CfnMonitoringSchedule.ClusterConfigProperty.InstanceCount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancecount
            """
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnMonitoringSchedule.ClusterConfigProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            """``CfnMonitoringSchedule.ClusterConfigProperty.VolumeSizeInGB``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumesizeingb
            """
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return result

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.ClusterConfigProperty.VolumeKmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumekmskeyid
            """
            result = self._values.get("volume_kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnMonitoringSchedule.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.ConstraintsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html#cfn-sagemaker-monitoringschedule-constraintsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param endpoint_name: ``CfnMonitoringSchedule.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnMonitoringSchedule.EndpointInputProperty.LocalPath``.
            :param s3_data_distribution_type: ``CfnMonitoringSchedule.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnMonitoringSchedule.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            """``CfnMonitoringSchedule.EndpointInputProperty.EndpointName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-endpointname
            """
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return result

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnMonitoringSchedule.EndpointInputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.EndpointInputProperty.S3DataDistributionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype
            """
            result = self._values.get("s3_data_distribution_type")
            return result

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.EndpointInputProperty.S3InputMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode
            """
            result = self._values.get("s3_input_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class MonitoringAppSpecificationProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            container_arguments: typing.Optional[typing.List[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.List[builtins.str]] = None,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param image_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ImageUri``.
            :param container_arguments: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerEntrypoint``.
            :param post_analytics_processor_source_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def image_uri(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ImageUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri
            """
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return result

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerArguments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments
            """
            result = self._values.get("container_arguments")
            return result

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerEntrypoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint
            """
            result = self._values.get("container_entrypoint")
            return result

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri
            """
            result = self._values.get("post_analytics_processor_source_uri")
            return result

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri
            """
            result = self._values.get("record_preprocessor_source_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringExecutionSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "creation_time": "creationTime",
            "last_modified_time": "lastModifiedTime",
            "monitoring_execution_status": "monitoringExecutionStatus",
            "monitoring_schedule_name": "monitoringScheduleName",
            "scheduled_time": "scheduledTime",
            "endpoint_name": "endpointName",
            "failure_reason": "failureReason",
            "processing_job_arn": "processingJobArn",
        },
    )
    class MonitoringExecutionSummaryProperty:
        def __init__(
            self,
            *,
            creation_time: builtins.str,
            last_modified_time: builtins.str,
            monitoring_execution_status: builtins.str,
            monitoring_schedule_name: builtins.str,
            scheduled_time: builtins.str,
            endpoint_name: typing.Optional[builtins.str] = None,
            failure_reason: typing.Optional[builtins.str] = None,
            processing_job_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param creation_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.CreationTime``.
            :param last_modified_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.LastModifiedTime``.
            :param monitoring_execution_status: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringExecutionStatus``.
            :param monitoring_schedule_name: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringScheduleName``.
            :param scheduled_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ScheduledTime``.
            :param endpoint_name: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.EndpointName``.
            :param failure_reason: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.FailureReason``.
            :param processing_job_arn: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ProcessingJobArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "creation_time": creation_time,
                "last_modified_time": last_modified_time,
                "monitoring_execution_status": monitoring_execution_status,
                "monitoring_schedule_name": monitoring_schedule_name,
                "scheduled_time": scheduled_time,
            }
            if endpoint_name is not None:
                self._values["endpoint_name"] = endpoint_name
            if failure_reason is not None:
                self._values["failure_reason"] = failure_reason
            if processing_job_arn is not None:
                self._values["processing_job_arn"] = processing_job_arn

        @builtins.property
        def creation_time(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.CreationTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-creationtime
            """
            result = self._values.get("creation_time")
            assert result is not None, "Required property 'creation_time' is missing"
            return result

        @builtins.property
        def last_modified_time(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.LastModifiedTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-lastmodifiedtime
            """
            result = self._values.get("last_modified_time")
            assert result is not None, "Required property 'last_modified_time' is missing"
            return result

        @builtins.property
        def monitoring_execution_status(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringExecutionStatus``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringexecutionstatus
            """
            result = self._values.get("monitoring_execution_status")
            assert result is not None, "Required property 'monitoring_execution_status' is missing"
            return result

        @builtins.property
        def monitoring_schedule_name(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringScheduleName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringschedulename
            """
            result = self._values.get("monitoring_schedule_name")
            assert result is not None, "Required property 'monitoring_schedule_name' is missing"
            return result

        @builtins.property
        def scheduled_time(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ScheduledTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-scheduledtime
            """
            result = self._values.get("scheduled_time")
            assert result is not None, "Required property 'scheduled_time' is missing"
            return result

        @builtins.property
        def endpoint_name(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.EndpointName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-endpointname
            """
            result = self._values.get("endpoint_name")
            return result

        @builtins.property
        def failure_reason(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.FailureReason``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-failurereason
            """
            result = self._values.get("failure_reason")
            return result

        @builtins.property
        def processing_job_arn(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ProcessingJobArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-processingjobarn
            """
            result = self._values.get("processing_job_arn")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringExecutionSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class MonitoringInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"],
        ) -> None:
            """
            :param endpoint_input: ``CfnMonitoringSchedule.MonitoringInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"]:
            """``CfnMonitoringSchedule.MonitoringInputProperty.EndpointInput``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html#cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput
            """
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringInputsProperty",
        jsii_struct_bases=[],
        name_mapping={"monitoring_inputs": "monitoringInputs"},
    )
    class MonitoringInputsProperty:
        def __init__(
            self,
            *,
            monitoring_inputs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]]] = None,
        ) -> None:
            """
            :param monitoring_inputs: ``CfnMonitoringSchedule.MonitoringInputsProperty.MonitoringInputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinputs.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if monitoring_inputs is not None:
                self._values["monitoring_inputs"] = monitoring_inputs

        @builtins.property
        def monitoring_inputs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]]]:
            """``CfnMonitoringSchedule.MonitoringInputsProperty.MonitoringInputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinputs.html#cfn-sagemaker-monitoringschedule-monitoringinputs-monitoringinputs
            """
            result = self._values.get("monitoring_inputs")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringInputsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_app_specification": "monitoringAppSpecification",
            "monitoring_inputs": "monitoringInputs",
            "monitoring_output_config": "monitoringOutputConfig",
            "monitoring_resources": "monitoringResources",
            "role_arn": "roleArn",
            "baseline_config": "baselineConfig",
            "environment": "environment",
            "network_config": "networkConfig",
            "stopping_condition": "stoppingCondition",
        },
    )
    class MonitoringJobDefinitionProperty:
        def __init__(
            self,
            *,
            monitoring_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"],
            monitoring_inputs: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputsProperty"],
            monitoring_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"],
            monitoring_resources: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"],
            role_arn: builtins.str,
            baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EnvironmentProperty"]] = None,
            network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]] = None,
            stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]] = None,
        ) -> None:
            """
            :param monitoring_app_specification: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringAppSpecification``.
            :param monitoring_inputs: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringInputs``.
            :param monitoring_output_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringOutputConfig``.
            :param monitoring_resources: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringResources``.
            :param role_arn: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.RoleArn``.
            :param baseline_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.BaselineConfig``.
            :param environment: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.Environment``.
            :param network_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.NetworkConfig``.
            :param stopping_condition: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.StoppingCondition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_app_specification": monitoring_app_specification,
                "monitoring_inputs": monitoring_inputs,
                "monitoring_output_config": monitoring_output_config,
                "monitoring_resources": monitoring_resources,
                "role_arn": role_arn,
            }
            if baseline_config is not None:
                self._values["baseline_config"] = baseline_config
            if environment is not None:
                self._values["environment"] = environment
            if network_config is not None:
                self._values["network_config"] = network_config
            if stopping_condition is not None:
                self._values["stopping_condition"] = stopping_condition

        @builtins.property
        def monitoring_app_specification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringAppSpecification``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringappspecification
            """
            result = self._values.get("monitoring_app_specification")
            assert result is not None, "Required property 'monitoring_app_specification' is missing"
            return result

        @builtins.property
        def monitoring_inputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputsProperty"]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringInputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringinputs
            """
            result = self._values.get("monitoring_inputs")
            assert result is not None, "Required property 'monitoring_inputs' is missing"
            return result

        @builtins.property
        def monitoring_output_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringOutputConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringoutputconfig
            """
            result = self._values.get("monitoring_output_config")
            assert result is not None, "Required property 'monitoring_output_config' is missing"
            return result

        @builtins.property
        def monitoring_resources(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringResources``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringresources
            """
            result = self._values.get("monitoring_resources")
            assert result is not None, "Required property 'monitoring_resources' is missing"
            return result

        @builtins.property
        def role_arn(self) -> builtins.str:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.RoleArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-rolearn
            """
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return result

        @builtins.property
        def baseline_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.BaselineConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-baselineconfig
            """
            result = self._values.get("baseline_config")
            return result

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EnvironmentProperty"]]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.Environment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-environment
            """
            result = self._values.get("environment")
            return result

        @builtins.property
        def network_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.NetworkConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-networkconfig
            """
            result = self._values.get("network_config")
            return result

        @builtins.property
        def stopping_condition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]]:
            """``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.StoppingCondition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-stoppingcondition
            """
            result = self._values.get("stopping_condition")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringJobDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param monitoring_outputs: ``CfnMonitoringSchedule.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnMonitoringSchedule.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]]:
            """``CfnMonitoringSchedule.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-monitoringoutputs
            """
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return result

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringOutputConfigProperty.KmsKeyId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-kmskeyid
            """
            result = self._values.get("kms_key_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"],
        ) -> None:
            """
            :param s3_output: ``CfnMonitoringSchedule.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"]:
            """``CfnMonitoringSchedule.MonitoringOutputProperty.S3Output``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output
            """
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"],
        ) -> None:
            """
            :param cluster_config: ``CfnMonitoringSchedule.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"]:
            """``CfnMonitoringSchedule.MonitoringResourcesProperty.ClusterConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html#cfn-sagemaker-monitoringschedule-monitoringresources-clusterconfig
            """
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_job_definition": "monitoringJobDefinition",
            "monitoring_job_definition_name": "monitoringJobDefinitionName",
            "monitoring_type": "monitoringType",
            "schedule_config": "scheduleConfig",
        },
    )
    class MonitoringScheduleConfigProperty:
        def __init__(
            self,
            *,
            monitoring_job_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]] = None,
            monitoring_job_definition_name: typing.Optional[builtins.str] = None,
            monitoring_type: typing.Optional[builtins.str] = None,
            schedule_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]] = None,
        ) -> None:
            """
            :param monitoring_job_definition: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinition``.
            :param monitoring_job_definition_name: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinitionName``.
            :param monitoring_type: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringType``.
            :param schedule_config: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.ScheduleConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if monitoring_job_definition is not None:
                self._values["monitoring_job_definition"] = monitoring_job_definition
            if monitoring_job_definition_name is not None:
                self._values["monitoring_job_definition_name"] = monitoring_job_definition_name
            if monitoring_type is not None:
                self._values["monitoring_type"] = monitoring_type
            if schedule_config is not None:
                self._values["schedule_config"] = schedule_config

        @builtins.property
        def monitoring_job_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]]:
            """``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition
            """
            result = self._values.get("monitoring_job_definition")
            return result

        @builtins.property
        def monitoring_job_definition_name(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinitionName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname
            """
            result = self._values.get("monitoring_job_definition_name")
            return result

        @builtins.property
        def monitoring_type(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype
            """
            result = self._values.get("monitoring_type")
            return result

        @builtins.property
        def schedule_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]]:
            """``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.ScheduleConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig
            """
            result = self._values.get("schedule_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]] = None,
        ) -> None:
            """
            :param enable_inter_container_traffic_encryption: ``CfnMonitoringSchedule.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnMonitoringSchedule.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnMonitoringSchedule.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnMonitoringSchedule.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enableintercontainertrafficencryption
            """
            result = self._values.get("enable_inter_container_traffic_encryption")
            return result

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            """``CfnMonitoringSchedule.NetworkConfigProperty.EnableNetworkIsolation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enablenetworkisolation
            """
            result = self._values.get("enable_network_isolation")
            return result

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]]:
            """``CfnMonitoringSchedule.NetworkConfigProperty.VpcConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-vpcconfig
            """
            result = self._values.get("vpc_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param local_path: ``CfnMonitoringSchedule.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnMonitoringSchedule.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnMonitoringSchedule.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            """``CfnMonitoringSchedule.S3OutputProperty.LocalPath``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-localpath
            """
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return result

        @builtins.property
        def s3_uri(self) -> builtins.str:
            """``CfnMonitoringSchedule.S3OutputProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uri
            """
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return result

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.S3OutputProperty.S3UploadMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uploadmode
            """
            result = self._values.get("s3_upload_mode")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleConfigProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            """
            :param schedule_expression: ``CfnMonitoringSchedule.ScheduleConfigProperty.ScheduleExpression``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            """``CfnMonitoringSchedule.ScheduleConfigProperty.ScheduleExpression``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html#cfn-sagemaker-monitoringschedule-scheduleconfig-scheduleexpression
            """
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class StatisticsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            """
            :param s3_uri: ``CfnMonitoringSchedule.StatisticsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            """``CfnMonitoringSchedule.StatisticsResourceProperty.S3Uri``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html#cfn-sagemaker-monitoringschedule-statisticsresource-s3uri
            """
            result = self._values.get("s3_uri")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            """
            :param max_runtime_in_seconds: ``CfnMonitoringSchedule.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            """``CfnMonitoringSchedule.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html#cfn-sagemaker-monitoringschedule-stoppingcondition-maxruntimeinseconds
            """
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.List[builtins.str],
            subnets: typing.List[builtins.str],
        ) -> None:
            """
            :param security_group_ids: ``CfnMonitoringSchedule.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnMonitoringSchedule.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            """``CfnMonitoringSchedule.VpcConfigProperty.SecurityGroupIds``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-securitygroupids
            """
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return result

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            """``CfnMonitoringSchedule.VpcConfigProperty.Subnets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-subnets
            """
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
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
    jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "monitoring_schedule_config": "monitoringScheduleConfig",
        "monitoring_schedule_name": "monitoringScheduleName",
        "endpoint_name": "endpointName",
        "failure_reason": "failureReason",
        "last_monitoring_execution_summary": "lastMonitoringExecutionSummary",
        "monitoring_schedule_status": "monitoringScheduleStatus",
        "tags": "tags",
    },
)
class CfnMonitoringScheduleProps:
    def __init__(
        self,
        *,
        monitoring_schedule_config: typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty],
        monitoring_schedule_name: builtins.str,
        endpoint_name: typing.Optional[builtins.str] = None,
        failure_reason: typing.Optional[builtins.str] = None,
        last_monitoring_execution_summary: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]] = None,
        monitoring_schedule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::MonitoringSchedule``.

        :param monitoring_schedule_config: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.
        :param monitoring_schedule_name: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.
        :param endpoint_name: ``AWS::SageMaker::MonitoringSchedule.EndpointName``.
        :param failure_reason: ``AWS::SageMaker::MonitoringSchedule.FailureReason``.
        :param last_monitoring_execution_summary: ``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.
        :param monitoring_schedule_status: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.
        :param tags: ``AWS::SageMaker::MonitoringSchedule.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "monitoring_schedule_config": monitoring_schedule_config,
            "monitoring_schedule_name": monitoring_schedule_name,
        }
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if failure_reason is not None:
            self._values["failure_reason"] = failure_reason
        if last_monitoring_execution_summary is not None:
            self._values["last_monitoring_execution_summary"] = last_monitoring_execution_summary
        if monitoring_schedule_status is not None:
            self._values["monitoring_schedule_status"] = monitoring_schedule_status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def monitoring_schedule_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty]:
        """``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig
        """
        result = self._values.get("monitoring_schedule_config")
        assert result is not None, "Required property 'monitoring_schedule_config' is missing"
        return result

    @builtins.property
    def monitoring_schedule_name(self) -> builtins.str:
        """``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename
        """
        result = self._values.get("monitoring_schedule_name")
        assert result is not None, "Required property 'monitoring_schedule_name' is missing"
        return result

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::MonitoringSchedule.EndpointName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname
        """
        result = self._values.get("endpoint_name")
        return result

    @builtins.property
    def failure_reason(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::MonitoringSchedule.FailureReason``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason
        """
        result = self._values.get("failure_reason")
        return result

    @builtins.property
    def last_monitoring_execution_summary(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]]:
        """``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary
        """
        result = self._values.get("last_monitoring_execution_summary")
        return result

    @builtins.property
    def monitoring_schedule_status(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus
        """
        result = self._values.get("monitoring_schedule_status")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::MonitoringSchedule.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitoringScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotebookInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstance",
):
    """A CloudFormation ``AWS::SageMaker::NotebookInstance``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
    :cloudformationResource: AWS::SageMaker::NotebookInstance
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        role_arn: builtins.str,
        accelerator_types: typing.Optional[typing.List[builtins.str]] = None,
        additional_code_repositories: typing.Optional[typing.List[builtins.str]] = None,
        default_code_repository: typing.Optional[builtins.str] = None,
        direct_internet_access: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_config_name: typing.Optional[builtins.str] = None,
        notebook_instance_name: typing.Optional[builtins.str] = None,
        root_access: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::NotebookInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_type: ``AWS::SageMaker::NotebookInstance.InstanceType``.
        :param role_arn: ``AWS::SageMaker::NotebookInstance.RoleArn``.
        :param accelerator_types: ``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.
        :param additional_code_repositories: ``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.
        :param default_code_repository: ``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.
        :param direct_internet_access: ``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.
        :param kms_key_id: ``AWS::SageMaker::NotebookInstance.KmsKeyId``.
        :param lifecycle_config_name: ``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.
        :param notebook_instance_name: ``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.
        :param root_access: ``AWS::SageMaker::NotebookInstance.RootAccess``.
        :param security_group_ids: ``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.
        :param subnet_id: ``AWS::SageMaker::NotebookInstance.SubnetId``.
        :param tags: ``AWS::SageMaker::NotebookInstance.Tags``.
        :param volume_size_in_gb: ``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.
        """
        props = CfnNotebookInstanceProps(
            instance_type=instance_type,
            role_arn=role_arn,
            accelerator_types=accelerator_types,
            additional_code_repositories=additional_code_repositories,
            default_code_repository=default_code_repository,
            direct_internet_access=direct_internet_access,
            kms_key_id=kms_key_id,
            lifecycle_config_name=lifecycle_config_name,
            notebook_instance_name=notebook_instance_name,
            root_access=root_access,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
            tags=tags,
            volume_size_in_gb=volume_size_in_gb,
        )

        jsii.create(CfnNotebookInstance, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrNotebookInstanceName")
    def attr_notebook_instance_name(self) -> builtins.str:
        """
        :cloudformationAttribute: NotebookInstanceName
        """
        return jsii.get(self, "attrNotebookInstanceName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::NotebookInstance.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        """``AWS::SageMaker::NotebookInstance.InstanceType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter # type: ignore
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::NotebookInstance.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="acceleratorTypes")
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes
        """
        return jsii.get(self, "acceleratorTypes")

    @accelerator_types.setter # type: ignore
    def accelerator_types(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "acceleratorTypes", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="additionalCodeRepositories")
    def additional_code_repositories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories
        """
        return jsii.get(self, "additionalCodeRepositories")

    @additional_code_repositories.setter # type: ignore
    def additional_code_repositories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "additionalCodeRepositories", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="defaultCodeRepository")
    def default_code_repository(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository
        """
        return jsii.get(self, "defaultCodeRepository")

    @default_code_repository.setter # type: ignore
    def default_code_repository(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultCodeRepository", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="directInternetAccess")
    def direct_internet_access(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess
        """
        return jsii.get(self, "directInternetAccess")

    @direct_internet_access.setter # type: ignore
    def direct_internet_access(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "directInternetAccess", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.KmsKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid
        """
        return jsii.get(self, "kmsKeyId")

    @kms_key_id.setter # type: ignore
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lifecycleConfigName")
    def lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname
        """
        return jsii.get(self, "lifecycleConfigName")

    @lifecycle_config_name.setter # type: ignore
    def lifecycle_config_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "lifecycleConfigName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="notebookInstanceName")
    def notebook_instance_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename
        """
        return jsii.get(self, "notebookInstanceName")

    @notebook_instance_name.setter # type: ignore
    def notebook_instance_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "notebookInstanceName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="rootAccess")
    def root_access(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.RootAccess``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess
        """
        return jsii.get(self, "rootAccess")

    @root_access.setter # type: ignore
    def root_access(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "rootAccess", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids
        """
        return jsii.get(self, "securityGroupIds")

    @security_group_ids.setter # type: ignore
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.SubnetId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter # type: ignore
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subnetId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="volumeSizeInGb")
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        """``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb
        """
        return jsii.get(self, "volumeSizeInGb")

    @volume_size_in_gb.setter # type: ignore
    def volume_size_in_gb(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "volumeSizeInGb", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotebookInstanceLifecycleConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfig",
):
    """A CloudFormation ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
    :cloudformationResource: AWS::SageMaker::NotebookInstanceLifecycleConfig
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        notebook_instance_lifecycle_config_name: typing.Optional[builtins.str] = None,
        on_create: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]] = None,
        on_start: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param notebook_instance_lifecycle_config_name: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.
        :param on_create: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.
        :param on_start: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.
        """
        props = CfnNotebookInstanceLifecycleConfigProps(
            notebook_instance_lifecycle_config_name=notebook_instance_lifecycle_config_name,
            on_create=on_create,
            on_start=on_start,
        )

        jsii.create(CfnNotebookInstanceLifecycleConfig, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrNotebookInstanceLifecycleConfigName")
    def attr_notebook_instance_lifecycle_config_name(self) -> builtins.str:
        """
        :cloudformationAttribute: NotebookInstanceLifecycleConfigName
        """
        return jsii.get(self, "attrNotebookInstanceLifecycleConfigName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="notebookInstanceLifecycleConfigName")
    def notebook_instance_lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname
        """
        return jsii.get(self, "notebookInstanceLifecycleConfigName")

    @notebook_instance_lifecycle_config_name.setter # type: ignore
    def notebook_instance_lifecycle_config_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "notebookInstanceLifecycleConfigName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="onCreate")
    def on_create(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]]:
        """``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate
        """
        return jsii.get(self, "onCreate")

    @on_create.setter # type: ignore
    def on_create(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]],
    ) -> None:
        jsii.set(self, "onCreate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="onStart")
    def on_start(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]]:
        """``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart
        """
        return jsii.get(self, "onStart")

    @on_start.setter # type: ignore
    def on_start(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]],
    ) -> None:
        jsii.set(self, "onStart", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content"},
    )
    class NotebookInstanceLifecycleHookProperty:
        def __init__(self, *, content: typing.Optional[builtins.str] = None) -> None:
            """
            :param content: ``CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty.Content``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            """``CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty.Content``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content
            """
            result = self._values.get("content")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotebookInstanceLifecycleHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_instance_lifecycle_config_name": "notebookInstanceLifecycleConfigName",
        "on_create": "onCreate",
        "on_start": "onStart",
    },
)
class CfnNotebookInstanceLifecycleConfigProps:
    def __init__(
        self,
        *,
        notebook_instance_lifecycle_config_name: typing.Optional[builtins.str] = None,
        on_create: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]] = None,
        on_start: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

        :param notebook_instance_lifecycle_config_name: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.
        :param on_create: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.
        :param on_start: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if notebook_instance_lifecycle_config_name is not None:
            self._values["notebook_instance_lifecycle_config_name"] = notebook_instance_lifecycle_config_name
        if on_create is not None:
            self._values["on_create"] = on_create
        if on_start is not None:
            self._values["on_start"] = on_start

    @builtins.property
    def notebook_instance_lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname
        """
        result = self._values.get("notebook_instance_lifecycle_config_name")
        return result

    @builtins.property
    def on_create(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]]:
        """``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate
        """
        result = self._values.get("on_create")
        return result

    @builtins.property
    def on_start(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]]:
        """``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart
        """
        result = self._values.get("on_start")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotebookInstanceLifecycleConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "role_arn": "roleArn",
        "accelerator_types": "acceleratorTypes",
        "additional_code_repositories": "additionalCodeRepositories",
        "default_code_repository": "defaultCodeRepository",
        "direct_internet_access": "directInternetAccess",
        "kms_key_id": "kmsKeyId",
        "lifecycle_config_name": "lifecycleConfigName",
        "notebook_instance_name": "notebookInstanceName",
        "root_access": "rootAccess",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
        "tags": "tags",
        "volume_size_in_gb": "volumeSizeInGb",
    },
)
class CfnNotebookInstanceProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        role_arn: builtins.str,
        accelerator_types: typing.Optional[typing.List[builtins.str]] = None,
        additional_code_repositories: typing.Optional[typing.List[builtins.str]] = None,
        default_code_repository: typing.Optional[builtins.str] = None,
        direct_internet_access: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_config_name: typing.Optional[builtins.str] = None,
        notebook_instance_name: typing.Optional[builtins.str] = None,
        root_access: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.List[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::NotebookInstance``.

        :param instance_type: ``AWS::SageMaker::NotebookInstance.InstanceType``.
        :param role_arn: ``AWS::SageMaker::NotebookInstance.RoleArn``.
        :param accelerator_types: ``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.
        :param additional_code_repositories: ``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.
        :param default_code_repository: ``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.
        :param direct_internet_access: ``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.
        :param kms_key_id: ``AWS::SageMaker::NotebookInstance.KmsKeyId``.
        :param lifecycle_config_name: ``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.
        :param notebook_instance_name: ``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.
        :param root_access: ``AWS::SageMaker::NotebookInstance.RootAccess``.
        :param security_group_ids: ``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.
        :param subnet_id: ``AWS::SageMaker::NotebookInstance.SubnetId``.
        :param tags: ``AWS::SageMaker::NotebookInstance.Tags``.
        :param volume_size_in_gb: ``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "role_arn": role_arn,
        }
        if accelerator_types is not None:
            self._values["accelerator_types"] = accelerator_types
        if additional_code_repositories is not None:
            self._values["additional_code_repositories"] = additional_code_repositories
        if default_code_repository is not None:
            self._values["default_code_repository"] = default_code_repository
        if direct_internet_access is not None:
            self._values["direct_internet_access"] = direct_internet_access
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if lifecycle_config_name is not None:
            self._values["lifecycle_config_name"] = lifecycle_config_name
        if notebook_instance_name is not None:
            self._values["notebook_instance_name"] = notebook_instance_name
        if root_access is not None:
            self._values["root_access"] = root_access
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if volume_size_in_gb is not None:
            self._values["volume_size_in_gb"] = volume_size_in_gb

    @builtins.property
    def instance_type(self) -> builtins.str:
        """``AWS::SageMaker::NotebookInstance.InstanceType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype
        """
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::NotebookInstance.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes
        """
        result = self._values.get("accelerator_types")
        return result

    @builtins.property
    def additional_code_repositories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories
        """
        result = self._values.get("additional_code_repositories")
        return result

    @builtins.property
    def default_code_repository(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository
        """
        result = self._values.get("default_code_repository")
        return result

    @builtins.property
    def direct_internet_access(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess
        """
        result = self._values.get("direct_internet_access")
        return result

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.KmsKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid
        """
        result = self._values.get("kms_key_id")
        return result

    @builtins.property
    def lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname
        """
        result = self._values.get("lifecycle_config_name")
        return result

    @builtins.property
    def notebook_instance_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename
        """
        result = self._values.get("notebook_instance_name")
        return result

    @builtins.property
    def root_access(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.RootAccess``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess
        """
        result = self._values.get("root_access")
        return result

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids
        """
        result = self._values.get("security_group_ids")
        return result

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::NotebookInstance.SubnetId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid
        """
        result = self._values.get("subnet_id")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::NotebookInstance.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        """``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb
        """
        result = self._values.get("volume_size_in_gb")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotebookInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPipeline(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnPipeline",
):
    """A CloudFormation ``AWS::SageMaker::Pipeline``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
    :cloudformationResource: AWS::SageMaker::Pipeline
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        pipeline_definition: typing.Any,
        pipeline_name: builtins.str,
        role_arn: builtins.str,
        pipeline_description: typing.Optional[builtins.str] = None,
        pipeline_display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::Pipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pipeline_definition: ``AWS::SageMaker::Pipeline.PipelineDefinition``.
        :param pipeline_name: ``AWS::SageMaker::Pipeline.PipelineName``.
        :param role_arn: ``AWS::SageMaker::Pipeline.RoleArn``.
        :param pipeline_description: ``AWS::SageMaker::Pipeline.PipelineDescription``.
        :param pipeline_display_name: ``AWS::SageMaker::Pipeline.PipelineDisplayName``.
        :param tags: ``AWS::SageMaker::Pipeline.Tags``.
        """
        props = CfnPipelineProps(
            pipeline_definition=pipeline_definition,
            pipeline_name=pipeline_name,
            role_arn=role_arn,
            pipeline_description=pipeline_description,
            pipeline_display_name=pipeline_display_name,
            tags=tags,
        )

        jsii.create(CfnPipeline, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::Pipeline.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineDefinition")
    def pipeline_definition(self) -> typing.Any:
        """``AWS::SageMaker::Pipeline.PipelineDefinition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition
        """
        return jsii.get(self, "pipelineDefinition")

    @pipeline_definition.setter # type: ignore
    def pipeline_definition(self, value: typing.Any) -> None:
        jsii.set(self, "pipelineDefinition", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineName")
    def pipeline_name(self) -> builtins.str:
        """``AWS::SageMaker::Pipeline.PipelineName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename
        """
        return jsii.get(self, "pipelineName")

    @pipeline_name.setter # type: ignore
    def pipeline_name(self, value: builtins.str) -> None:
        jsii.set(self, "pipelineName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::Pipeline.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineDescription")
    def pipeline_description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Pipeline.PipelineDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription
        """
        return jsii.get(self, "pipelineDescription")

    @pipeline_description.setter # type: ignore
    def pipeline_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineDescription", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineDisplayName")
    def pipeline_display_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Pipeline.PipelineDisplayName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname
        """
        return jsii.get(self, "pipelineDisplayName")

    @pipeline_display_name.setter # type: ignore
    def pipeline_display_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineDisplayName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline_definition": "pipelineDefinition",
        "pipeline_name": "pipelineName",
        "role_arn": "roleArn",
        "pipeline_description": "pipelineDescription",
        "pipeline_display_name": "pipelineDisplayName",
        "tags": "tags",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        pipeline_definition: typing.Any,
        pipeline_name: builtins.str,
        role_arn: builtins.str,
        pipeline_description: typing.Optional[builtins.str] = None,
        pipeline_display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::Pipeline``.

        :param pipeline_definition: ``AWS::SageMaker::Pipeline.PipelineDefinition``.
        :param pipeline_name: ``AWS::SageMaker::Pipeline.PipelineName``.
        :param role_arn: ``AWS::SageMaker::Pipeline.RoleArn``.
        :param pipeline_description: ``AWS::SageMaker::Pipeline.PipelineDescription``.
        :param pipeline_display_name: ``AWS::SageMaker::Pipeline.PipelineDisplayName``.
        :param tags: ``AWS::SageMaker::Pipeline.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "pipeline_definition": pipeline_definition,
            "pipeline_name": pipeline_name,
            "role_arn": role_arn,
        }
        if pipeline_description is not None:
            self._values["pipeline_description"] = pipeline_description
        if pipeline_display_name is not None:
            self._values["pipeline_display_name"] = pipeline_display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pipeline_definition(self) -> typing.Any:
        """``AWS::SageMaker::Pipeline.PipelineDefinition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition
        """
        result = self._values.get("pipeline_definition")
        assert result is not None, "Required property 'pipeline_definition' is missing"
        return result

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        """``AWS::SageMaker::Pipeline.PipelineName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename
        """
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::SageMaker::Pipeline.RoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def pipeline_description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Pipeline.PipelineDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription
        """
        result = self._values.get("pipeline_description")
        return result

    @builtins.property
    def pipeline_display_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Pipeline.PipelineDisplayName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname
        """
        result = self._values.get("pipeline_display_name")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::Pipeline.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnProject(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnProject",
):
    """A CloudFormation ``AWS::SageMaker::Project``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
    :cloudformationResource: AWS::SageMaker::Project
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        project_name: builtins.str,
        service_catalog_provisioning_details: typing.Any,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_name: ``AWS::SageMaker::Project.ProjectName``.
        :param service_catalog_provisioning_details: ``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.
        :param project_description: ``AWS::SageMaker::Project.ProjectDescription``.
        :param tags: ``AWS::SageMaker::Project.Tags``.
        """
        props = CfnProjectProps(
            project_name=project_name,
            service_catalog_provisioning_details=service_catalog_provisioning_details,
            project_description=project_description,
            tags=tags,
        )

        jsii.create(CfnProject, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProjectArn")
    def attr_project_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: ProjectArn
        """
        return jsii.get(self, "attrProjectArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        """
        :cloudformationAttribute: ProjectId
        """
        return jsii.get(self, "attrProjectId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrProjectStatus")
    def attr_project_status(self) -> builtins.str:
        """
        :cloudformationAttribute: ProjectStatus
        """
        return jsii.get(self, "attrProjectStatus")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrServiceCatalogProvisionedProductDetails")
    def attr_service_catalog_provisioned_product_details(
        self,
    ) -> aws_cdk.core.IResolvable:
        """
        :cloudformationAttribute: ServiceCatalogProvisionedProductDetails
        """
        return jsii.get(self, "attrServiceCatalogProvisionedProductDetails")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::Project.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        """``AWS::SageMaker::Project.ProjectName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname
        """
        return jsii.get(self, "projectName")

    @project_name.setter # type: ignore
    def project_name(self, value: builtins.str) -> None:
        jsii.set(self, "projectName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> typing.Any:
        """``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails
        """
        return jsii.get(self, "serviceCatalogProvisioningDetails")

    @service_catalog_provisioning_details.setter # type: ignore
    def service_catalog_provisioning_details(self, value: typing.Any) -> None:
        jsii.set(self, "serviceCatalogProvisioningDetails", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="projectDescription")
    def project_description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Project.ProjectDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription
        """
        return jsii.get(self, "projectDescription")

    @project_description.setter # type: ignore
    def project_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_name": "projectName",
        "service_catalog_provisioning_details": "serviceCatalogProvisioningDetails",
        "project_description": "projectDescription",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        project_name: builtins.str,
        service_catalog_provisioning_details: typing.Any,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::Project``.

        :param project_name: ``AWS::SageMaker::Project.ProjectName``.
        :param service_catalog_provisioning_details: ``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.
        :param project_description: ``AWS::SageMaker::Project.ProjectDescription``.
        :param tags: ``AWS::SageMaker::Project.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "project_name": project_name,
            "service_catalog_provisioning_details": service_catalog_provisioning_details,
        }
        if project_description is not None:
            self._values["project_description"] = project_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def project_name(self) -> builtins.str:
        """``AWS::SageMaker::Project.ProjectName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname
        """
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return result

    @builtins.property
    def service_catalog_provisioning_details(self) -> typing.Any:
        """``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails
        """
        result = self._values.get("service_catalog_provisioning_details")
        assert result is not None, "Required property 'service_catalog_provisioning_details' is missing"
        return result

    @builtins.property
    def project_description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Project.ProjectDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription
        """
        result = self._values.get("project_description")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::Project.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWorkteam(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam",
):
    """A CloudFormation ``AWS::SageMaker::Workteam``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
    :cloudformationResource: AWS::SageMaker::Workteam
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        member_definitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]] = None,
        notification_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        workteam_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::SageMaker::Workteam``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::SageMaker::Workteam.Description``.
        :param member_definitions: ``AWS::SageMaker::Workteam.MemberDefinitions``.
        :param notification_configuration: ``AWS::SageMaker::Workteam.NotificationConfiguration``.
        :param tags: ``AWS::SageMaker::Workteam.Tags``.
        :param workteam_name: ``AWS::SageMaker::Workteam.WorkteamName``.
        """
        props = CfnWorkteamProps(
            description=description,
            member_definitions=member_definitions,
            notification_configuration=notification_configuration,
            tags=tags,
            workteam_name=workteam_name,
        )

        jsii.create(CfnWorkteam, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrWorkteamName")
    def attr_workteam_name(self) -> builtins.str:
        """
        :cloudformationAttribute: WorkteamName
        """
        return jsii.get(self, "attrWorkteamName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SageMaker::Workteam.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Workteam.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="memberDefinitions")
    def member_definitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]]:
        """``AWS::SageMaker::Workteam.MemberDefinitions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions
        """
        return jsii.get(self, "memberDefinitions")

    @member_definitions.setter # type: ignore
    def member_definitions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]],
    ) -> None:
        jsii.set(self, "memberDefinitions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]]:
        """``AWS::SageMaker::Workteam.NotificationConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration
        """
        return jsii.get(self, "notificationConfiguration")

    @notification_configuration.setter # type: ignore
    def notification_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "notificationConfiguration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="workteamName")
    def workteam_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Workteam.WorkteamName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname
        """
        return jsii.get(self, "workteamName")

    @workteam_name.setter # type: ignore
    def workteam_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workteamName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cognito_client_id": "cognitoClientId",
            "cognito_user_group": "cognitoUserGroup",
            "cognito_user_pool": "cognitoUserPool",
        },
    )
    class CognitoMemberDefinitionProperty:
        def __init__(
            self,
            *,
            cognito_client_id: builtins.str,
            cognito_user_group: builtins.str,
            cognito_user_pool: builtins.str,
        ) -> None:
            """
            :param cognito_client_id: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoClientId``.
            :param cognito_user_group: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserGroup``.
            :param cognito_user_pool: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserPool``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cognito_client_id": cognito_client_id,
                "cognito_user_group": cognito_user_group,
                "cognito_user_pool": cognito_user_pool,
            }

        @builtins.property
        def cognito_client_id(self) -> builtins.str:
            """``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoClientId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitoclientid
            """
            result = self._values.get("cognito_client_id")
            assert result is not None, "Required property 'cognito_client_id' is missing"
            return result

        @builtins.property
        def cognito_user_group(self) -> builtins.str:
            """``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserGroup``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitousergroup
            """
            result = self._values.get("cognito_user_group")
            assert result is not None, "Required property 'cognito_user_group' is missing"
            return result

        @builtins.property
        def cognito_user_pool(self) -> builtins.str:
            """``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserPool``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitouserpool
            """
            result = self._values.get("cognito_user_pool")
            assert result is not None, "Required property 'cognito_user_pool' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoMemberDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.MemberDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"cognito_member_definition": "cognitoMemberDefinition"},
    )
    class MemberDefinitionProperty:
        def __init__(
            self,
            *,
            cognito_member_definition: typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"],
        ) -> None:
            """
            :param cognito_member_definition: ``CfnWorkteam.MemberDefinitionProperty.CognitoMemberDefinition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "cognito_member_definition": cognito_member_definition,
            }

        @builtins.property
        def cognito_member_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"]:
            """``CfnWorkteam.MemberDefinitionProperty.CognitoMemberDefinition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html#cfn-sagemaker-workteam-memberdefinition-cognitomemberdefinition
            """
            result = self._values.get("cognito_member_definition")
            assert result is not None, "Required property 'cognito_member_definition' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.NotificationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"notification_topic_arn": "notificationTopicArn"},
    )
    class NotificationConfigurationProperty:
        def __init__(self, *, notification_topic_arn: builtins.str) -> None:
            """
            :param notification_topic_arn: ``CfnWorkteam.NotificationConfigurationProperty.NotificationTopicArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "notification_topic_arn": notification_topic_arn,
            }

        @builtins.property
        def notification_topic_arn(self) -> builtins.str:
            """``CfnWorkteam.NotificationConfigurationProperty.NotificationTopicArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html#cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn
            """
            result = self._values.get("notification_topic_arn")
            assert result is not None, "Required property 'notification_topic_arn' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteamProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "member_definitions": "memberDefinitions",
        "notification_configuration": "notificationConfiguration",
        "tags": "tags",
        "workteam_name": "workteamName",
    },
)
class CfnWorkteamProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        member_definitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]] = None,
        notification_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        workteam_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::SageMaker::Workteam``.

        :param description: ``AWS::SageMaker::Workteam.Description``.
        :param member_definitions: ``AWS::SageMaker::Workteam.MemberDefinitions``.
        :param notification_configuration: ``AWS::SageMaker::Workteam.NotificationConfiguration``.
        :param tags: ``AWS::SageMaker::Workteam.Tags``.
        :param workteam_name: ``AWS::SageMaker::Workteam.WorkteamName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if member_definitions is not None:
            self._values["member_definitions"] = member_definitions
        if notification_configuration is not None:
            self._values["notification_configuration"] = notification_configuration
        if tags is not None:
            self._values["tags"] = tags
        if workteam_name is not None:
            self._values["workteam_name"] = workteam_name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Workteam.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def member_definitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]]:
        """``AWS::SageMaker::Workteam.MemberDefinitions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions
        """
        result = self._values.get("member_definitions")
        return result

    @builtins.property
    def notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]]:
        """``AWS::SageMaker::Workteam.NotificationConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration
        """
        result = self._values.get("notification_configuration")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SageMaker::Workteam.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def workteam_name(self) -> typing.Optional[builtins.str]:
        """``AWS::SageMaker::Workteam.WorkteamName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname
        """
        result = self._values.get("workteam_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkteamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCodeRepository",
    "CfnCodeRepositoryProps",
    "CfnDataQualityJobDefinition",
    "CfnDataQualityJobDefinitionProps",
    "CfnDevice",
    "CfnDeviceFleet",
    "CfnDeviceFleetProps",
    "CfnDeviceProps",
    "CfnEndpoint",
    "CfnEndpointConfig",
    "CfnEndpointConfigProps",
    "CfnEndpointProps",
    "CfnModel",
    "CfnModelBiasJobDefinition",
    "CfnModelBiasJobDefinitionProps",
    "CfnModelExplainabilityJobDefinition",
    "CfnModelExplainabilityJobDefinitionProps",
    "CfnModelPackageGroup",
    "CfnModelPackageGroupProps",
    "CfnModelProps",
    "CfnModelQualityJobDefinition",
    "CfnModelQualityJobDefinitionProps",
    "CfnMonitoringSchedule",
    "CfnMonitoringScheduleProps",
    "CfnNotebookInstance",
    "CfnNotebookInstanceLifecycleConfig",
    "CfnNotebookInstanceLifecycleConfigProps",
    "CfnNotebookInstanceProps",
    "CfnPipeline",
    "CfnPipelineProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnWorkteam",
    "CfnWorkteamProps",
]

publication.publish()
