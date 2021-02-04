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
class CfnAnalysis(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_quicksight.CfnAnalysis",
):
    """A CloudFormation ``AWS::QuickSight::Analysis``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html
    :cloudformationResource: AWS::QuickSight::Analysis
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        errors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.AnalysisErrorProperty", _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union["CfnAnalysis.ParametersProperty", _IResolvable_a771d0ef]] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.ResourcePermissionProperty", _IResolvable_a771d0ef]]]] = None,
        source_entity: typing.Optional[typing.Union["CfnAnalysis.AnalysisSourceEntityProperty", _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::QuickSight::Analysis``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param analysis_id: ``AWS::QuickSight::Analysis.AnalysisId``.
        :param aws_account_id: ``AWS::QuickSight::Analysis.AwsAccountId``.
        :param errors: ``AWS::QuickSight::Analysis.Errors``.
        :param name: ``AWS::QuickSight::Analysis.Name``.
        :param parameters: ``AWS::QuickSight::Analysis.Parameters``.
        :param permissions: ``AWS::QuickSight::Analysis.Permissions``.
        :param source_entity: ``AWS::QuickSight::Analysis.SourceEntity``.
        :param tags: ``AWS::QuickSight::Analysis.Tags``.
        :param theme_arn: ``AWS::QuickSight::Analysis.ThemeArn``.
        """
        props = CfnAnalysisProps(
            analysis_id=analysis_id,
            aws_account_id=aws_account_id,
            errors=errors,
            name=name,
            parameters=parameters,
            permissions=permissions,
            source_entity=source_entity,
            tags=tags,
            theme_arn=theme_arn,
        )

        jsii.create(CfnAnalysis, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreatedTime
        """
        return jsii.get(self, "attrCreatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrDataSetArns")
    def attr_data_set_arns(self) -> typing.List[builtins.str]:
        """
        :cloudformationAttribute: DataSetArns
        """
        return jsii.get(self, "attrDataSetArns")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        """
        :cloudformationAttribute: LastUpdatedTime
        """
        return jsii.get(self, "attrLastUpdatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrSheets")
    def attr_sheets(self) -> _IResolvable_a771d0ef:
        """
        :cloudformationAttribute: Sheets
        """
        return jsii.get(self, "attrSheets")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        """
        :cloudformationAttribute: Status
        """
        return jsii.get(self, "attrStatus")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::QuickSight::Analysis.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="analysisId")
    def analysis_id(self) -> builtins.str:
        """``AWS::QuickSight::Analysis.AnalysisId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-analysisid
        """
        return jsii.get(self, "analysisId")

    @analysis_id.setter # type: ignore
    def analysis_id(self, value: builtins.str) -> None:
        jsii.set(self, "analysisId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Analysis.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-awsaccountid
        """
        return jsii.get(self, "awsAccountId")

    @aws_account_id.setter # type: ignore
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="errors")
    def errors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.AnalysisErrorProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Analysis.Errors``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-errors
        """
        return jsii.get(self, "errors")

    @errors.setter # type: ignore
    def errors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.AnalysisErrorProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "errors", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Analysis.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union["CfnAnalysis.ParametersProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Analysis.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-parameters
        """
        return jsii.get(self, "parameters")

    @parameters.setter # type: ignore
    def parameters(
        self,
        value: typing.Optional[typing.Union["CfnAnalysis.ParametersProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.ResourcePermissionProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Analysis.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-permissions
        """
        return jsii.get(self, "permissions")

    @permissions.setter # type: ignore
    def permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.ResourcePermissionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourceEntity")
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union["CfnAnalysis.AnalysisSourceEntityProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Analysis.SourceEntity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-sourceentity
        """
        return jsii.get(self, "sourceEntity")

    @source_entity.setter # type: ignore
    def source_entity(
        self,
        value: typing.Optional[typing.Union["CfnAnalysis.AnalysisSourceEntityProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "sourceEntity", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="themeArn")
    def theme_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Analysis.ThemeArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-themearn
        """
        return jsii.get(self, "themeArn")

    @theme_arn.setter # type: ignore
    def theme_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "themeArn", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.AnalysisErrorProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "type": "type"},
    )
    class AnalysisErrorProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param message: ``CfnAnalysis.AnalysisErrorProperty.Message``.
            :param type: ``CfnAnalysis.AnalysisErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            """``CfnAnalysis.AnalysisErrorProperty.Message``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-message
            """
            result = self._values.get("message")
            return result

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            """``CfnAnalysis.AnalysisErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-type
            """
            result = self._values.get("type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisErrorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.AnalysisSourceEntityProperty",
        jsii_struct_bases=[],
        name_mapping={"source_template": "sourceTemplate"},
    )
    class AnalysisSourceEntityProperty:
        def __init__(
            self,
            *,
            source_template: typing.Optional[typing.Union["CfnAnalysis.AnalysisSourceTemplateProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param source_template: ``CfnAnalysis.AnalysisSourceEntityProperty.SourceTemplate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if source_template is not None:
                self._values["source_template"] = source_template

        @builtins.property
        def source_template(
            self,
        ) -> typing.Optional[typing.Union["CfnAnalysis.AnalysisSourceTemplateProperty", _IResolvable_a771d0ef]]:
            """``CfnAnalysis.AnalysisSourceEntityProperty.SourceTemplate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html#cfn-quicksight-analysis-analysissourceentity-sourcetemplate
            """
            result = self._values.get("source_template")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSourceEntityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.AnalysisSourceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
    )
    class AnalysisSourceTemplateProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            data_set_references: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.DataSetReferenceProperty", _IResolvable_a771d0ef]]],
        ) -> None:
            """
            :param arn: ``CfnAnalysis.AnalysisSourceTemplateProperty.Arn``.
            :param data_set_references: ``CfnAnalysis.AnalysisSourceTemplateProperty.DataSetReferences``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "data_set_references": data_set_references,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            """``CfnAnalysis.AnalysisSourceTemplateProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-arn
            """
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return result

        @builtins.property
        def data_set_references(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.DataSetReferenceProperty", _IResolvable_a771d0ef]]]:
            """``CfnAnalysis.AnalysisSourceTemplateProperty.DataSetReferences``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-datasetreferences
            """
            result = self._values.get("data_set_references")
            assert result is not None, "Required property 'data_set_references' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSourceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.DataSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_set_arn": "dataSetArn",
            "data_set_placeholder": "dataSetPlaceholder",
        },
    )
    class DataSetReferenceProperty:
        def __init__(
            self,
            *,
            data_set_arn: builtins.str,
            data_set_placeholder: builtins.str,
        ) -> None:
            """
            :param data_set_arn: ``CfnAnalysis.DataSetReferenceProperty.DataSetArn``.
            :param data_set_placeholder: ``CfnAnalysis.DataSetReferenceProperty.DataSetPlaceholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "data_set_arn": data_set_arn,
                "data_set_placeholder": data_set_placeholder,
            }

        @builtins.property
        def data_set_arn(self) -> builtins.str:
            """``CfnAnalysis.DataSetReferenceProperty.DataSetArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetarn
            """
            result = self._values.get("data_set_arn")
            assert result is not None, "Required property 'data_set_arn' is missing"
            return result

        @builtins.property
        def data_set_placeholder(self) -> builtins.str:
            """``CfnAnalysis.DataSetReferenceProperty.DataSetPlaceholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetplaceholder
            """
            result = self._values.get("data_set_placeholder")
            assert result is not None, "Required property 'data_set_placeholder' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.DateTimeParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DateTimeParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.List[builtins.str],
        ) -> None:
            """
            :param name: ``CfnAnalysis.DateTimeParameterProperty.Name``.
            :param values: ``CfnAnalysis.DateTimeParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnAnalysis.DateTimeParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            """``CfnAnalysis.DateTimeParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateTimeParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.DecimalParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DecimalParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]],
        ) -> None:
            """
            :param name: ``CfnAnalysis.DecimalParameterProperty.Name``.
            :param values: ``CfnAnalysis.DecimalParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnAnalysis.DecimalParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]:
            """``CfnAnalysis.DecimalParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecimalParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.IntegerParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class IntegerParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]],
        ) -> None:
            """
            :param name: ``CfnAnalysis.IntegerParameterProperty.Name``.
            :param values: ``CfnAnalysis.IntegerParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnAnalysis.IntegerParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]:
            """``CfnAnalysis.IntegerParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_time_parameters": "dateTimeParameters",
            "decimal_parameters": "decimalParameters",
            "integer_parameters": "integerParameters",
            "string_parameters": "stringParameters",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            date_time_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.DateTimeParameterProperty", _IResolvable_a771d0ef]]]] = None,
            decimal_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.DecimalParameterProperty", _IResolvable_a771d0ef]]]] = None,
            integer_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.IntegerParameterProperty", _IResolvable_a771d0ef]]]] = None,
            string_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.StringParameterProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param date_time_parameters: ``CfnAnalysis.ParametersProperty.DateTimeParameters``.
            :param decimal_parameters: ``CfnAnalysis.ParametersProperty.DecimalParameters``.
            :param integer_parameters: ``CfnAnalysis.ParametersProperty.IntegerParameters``.
            :param string_parameters: ``CfnAnalysis.ParametersProperty.StringParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if date_time_parameters is not None:
                self._values["date_time_parameters"] = date_time_parameters
            if decimal_parameters is not None:
                self._values["decimal_parameters"] = decimal_parameters
            if integer_parameters is not None:
                self._values["integer_parameters"] = integer_parameters
            if string_parameters is not None:
                self._values["string_parameters"] = string_parameters

        @builtins.property
        def date_time_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.DateTimeParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnAnalysis.ParametersProperty.DateTimeParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-datetimeparameters
            """
            result = self._values.get("date_time_parameters")
            return result

        @builtins.property
        def decimal_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.DecimalParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnAnalysis.ParametersProperty.DecimalParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-decimalparameters
            """
            result = self._values.get("decimal_parameters")
            return result

        @builtins.property
        def integer_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.IntegerParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnAnalysis.ParametersProperty.IntegerParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-integerparameters
            """
            result = self._values.get("integer_parameters")
            return result

        @builtins.property
        def string_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnalysis.StringParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnAnalysis.ParametersProperty.StringParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-stringparameters
            """
            result = self._values.get("string_parameters")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.List[builtins.str],
            principal: builtins.str,
        ) -> None:
            """
            :param actions: ``CfnAnalysis.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnAnalysis.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            """``CfnAnalysis.ResourcePermissionProperty.Actions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-actions
            """
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return result

        @builtins.property
        def principal(self) -> builtins.str:
            """``CfnAnalysis.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-principal
            """
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.SheetProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sheet_id": "sheetId"},
    )
    class SheetProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            sheet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param name: ``CfnAnalysis.SheetProperty.Name``.
            :param sheet_id: ``CfnAnalysis.SheetProperty.SheetId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if sheet_id is not None:
                self._values["sheet_id"] = sheet_id

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnAnalysis.SheetProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def sheet_id(self) -> typing.Optional[builtins.str]:
            """``CfnAnalysis.SheetProperty.SheetId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-sheetid
            """
            result = self._values.get("sheet_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnAnalysis.StringParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class StringParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.List[builtins.str],
        ) -> None:
            """
            :param name: ``CfnAnalysis.StringParameterProperty.Name``.
            :param values: ``CfnAnalysis.StringParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnAnalysis.StringParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            """``CfnAnalysis.StringParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_quicksight.CfnAnalysisProps",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
        "errors": "errors",
        "name": "name",
        "parameters": "parameters",
        "permissions": "permissions",
        "source_entity": "sourceEntity",
        "tags": "tags",
        "theme_arn": "themeArn",
    },
)
class CfnAnalysisProps:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        errors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnalysis.AnalysisErrorProperty, _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[CfnAnalysis.ParametersProperty, _IResolvable_a771d0ef]] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnalysis.ResourcePermissionProperty, _IResolvable_a771d0ef]]]] = None,
        source_entity: typing.Optional[typing.Union[CfnAnalysis.AnalysisSourceEntityProperty, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::QuickSight::Analysis``.

        :param analysis_id: ``AWS::QuickSight::Analysis.AnalysisId``.
        :param aws_account_id: ``AWS::QuickSight::Analysis.AwsAccountId``.
        :param errors: ``AWS::QuickSight::Analysis.Errors``.
        :param name: ``AWS::QuickSight::Analysis.Name``.
        :param parameters: ``AWS::QuickSight::Analysis.Parameters``.
        :param permissions: ``AWS::QuickSight::Analysis.Permissions``.
        :param source_entity: ``AWS::QuickSight::Analysis.SourceEntity``.
        :param tags: ``AWS::QuickSight::Analysis.Tags``.
        :param theme_arn: ``AWS::QuickSight::Analysis.ThemeArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }
        if errors is not None:
            self._values["errors"] = errors
        if name is not None:
            self._values["name"] = name
        if parameters is not None:
            self._values["parameters"] = parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if source_entity is not None:
            self._values["source_entity"] = source_entity
        if tags is not None:
            self._values["tags"] = tags
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn

    @builtins.property
    def analysis_id(self) -> builtins.str:
        """``AWS::QuickSight::Analysis.AnalysisId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-analysisid
        """
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return result

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Analysis.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-awsaccountid
        """
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return result

    @builtins.property
    def errors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnalysis.AnalysisErrorProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Analysis.Errors``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-errors
        """
        result = self._values.get("errors")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Analysis.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[CfnAnalysis.ParametersProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Analysis.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-parameters
        """
        result = self._values.get("parameters")
        return result

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnalysis.ResourcePermissionProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Analysis.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-permissions
        """
        result = self._values.get("permissions")
        return result

    @builtins.property
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[CfnAnalysis.AnalysisSourceEntityProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Analysis.SourceEntity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-sourceentity
        """
        result = self._values.get("source_entity")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::QuickSight::Analysis.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Analysis.ThemeArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-themearn
        """
        result = self._values.get("theme_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnalysisProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDashboard(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_quicksight.CfnDashboard",
):
    """A CloudFormation ``AWS::QuickSight::Dashboard``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html
    :cloudformationResource: AWS::QuickSight::Dashboard
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        dashboard_publish_options: typing.Optional[typing.Union["CfnDashboard.DashboardPublishOptionsProperty", _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union["CfnDashboard.ParametersProperty", _IResolvable_a771d0ef]] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.ResourcePermissionProperty", _IResolvable_a771d0ef]]]] = None,
        source_entity: typing.Optional[typing.Union["CfnDashboard.DashboardSourceEntityProperty", _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::QuickSight::Dashboard``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::Dashboard.AwsAccountId``.
        :param dashboard_id: ``AWS::QuickSight::Dashboard.DashboardId``.
        :param dashboard_publish_options: ``AWS::QuickSight::Dashboard.DashboardPublishOptions``.
        :param name: ``AWS::QuickSight::Dashboard.Name``.
        :param parameters: ``AWS::QuickSight::Dashboard.Parameters``.
        :param permissions: ``AWS::QuickSight::Dashboard.Permissions``.
        :param source_entity: ``AWS::QuickSight::Dashboard.SourceEntity``.
        :param tags: ``AWS::QuickSight::Dashboard.Tags``.
        :param theme_arn: ``AWS::QuickSight::Dashboard.ThemeArn``.
        :param version_description: ``AWS::QuickSight::Dashboard.VersionDescription``.
        """
        props = CfnDashboardProps(
            aws_account_id=aws_account_id,
            dashboard_id=dashboard_id,
            dashboard_publish_options=dashboard_publish_options,
            name=name,
            parameters=parameters,
            permissions=permissions,
            source_entity=source_entity,
            tags=tags,
            theme_arn=theme_arn,
            version_description=version_description,
        )

        jsii.create(CfnDashboard, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreatedTime
        """
        return jsii.get(self, "attrCreatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrLastPublishedTime")
    def attr_last_published_time(self) -> builtins.str:
        """
        :cloudformationAttribute: LastPublishedTime
        """
        return jsii.get(self, "attrLastPublishedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        """
        :cloudformationAttribute: LastUpdatedTime
        """
        return jsii.get(self, "attrLastUpdatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::QuickSight::Dashboard.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Dashboard.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-awsaccountid
        """
        return jsii.get(self, "awsAccountId")

    @aws_account_id.setter # type: ignore
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> builtins.str:
        """``AWS::QuickSight::Dashboard.DashboardId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardid
        """
        return jsii.get(self, "dashboardId")

    @dashboard_id.setter # type: ignore
    def dashboard_id(self, value: builtins.str) -> None:
        jsii.set(self, "dashboardId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dashboardPublishOptions")
    def dashboard_publish_options(
        self,
    ) -> typing.Optional[typing.Union["CfnDashboard.DashboardPublishOptionsProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Dashboard.DashboardPublishOptions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardpublishoptions
        """
        return jsii.get(self, "dashboardPublishOptions")

    @dashboard_publish_options.setter # type: ignore
    def dashboard_publish_options(
        self,
        value: typing.Optional[typing.Union["CfnDashboard.DashboardPublishOptionsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "dashboardPublishOptions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Dashboard.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union["CfnDashboard.ParametersProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Dashboard.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-parameters
        """
        return jsii.get(self, "parameters")

    @parameters.setter # type: ignore
    def parameters(
        self,
        value: typing.Optional[typing.Union["CfnDashboard.ParametersProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.ResourcePermissionProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Dashboard.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-permissions
        """
        return jsii.get(self, "permissions")

    @permissions.setter # type: ignore
    def permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.ResourcePermissionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourceEntity")
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union["CfnDashboard.DashboardSourceEntityProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Dashboard.SourceEntity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-sourceentity
        """
        return jsii.get(self, "sourceEntity")

    @source_entity.setter # type: ignore
    def source_entity(
        self,
        value: typing.Optional[typing.Union["CfnDashboard.DashboardSourceEntityProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "sourceEntity", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="themeArn")
    def theme_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Dashboard.ThemeArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-themearn
        """
        return jsii.get(self, "themeArn")

    @theme_arn.setter # type: ignore
    def theme_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "themeArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Dashboard.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-versiondescription
        """
        return jsii.get(self, "versionDescription")

    @version_description.setter # type: ignore
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionDescription", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.AdHocFilteringOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_status": "availabilityStatus"},
    )
    class AdHocFilteringOptionProperty:
        def __init__(
            self,
            *,
            availability_status: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param availability_status: ``CfnDashboard.AdHocFilteringOptionProperty.AvailabilityStatus``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_status is not None:
                self._values["availability_status"] = availability_status

        @builtins.property
        def availability_status(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.AdHocFilteringOptionProperty.AvailabilityStatus``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html#cfn-quicksight-dashboard-adhocfilteringoption-availabilitystatus
            """
            result = self._values.get("availability_status")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdHocFilteringOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DashboardErrorProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "type": "type"},
    )
    class DashboardErrorProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param message: ``CfnDashboard.DashboardErrorProperty.Message``.
            :param type: ``CfnDashboard.DashboardErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboarderror.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardErrorProperty.Message``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboarderror.html#cfn-quicksight-dashboard-dashboarderror-message
            """
            result = self._values.get("message")
            return result

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboarderror.html#cfn-quicksight-dashboard-dashboarderror-type
            """
            result = self._values.get("type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardErrorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DashboardPublishOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_hoc_filtering_option": "adHocFilteringOption",
            "export_to_csv_option": "exportToCsvOption",
            "sheet_controls_option": "sheetControlsOption",
        },
    )
    class DashboardPublishOptionsProperty:
        def __init__(
            self,
            *,
            ad_hoc_filtering_option: typing.Optional[typing.Union["CfnDashboard.AdHocFilteringOptionProperty", _IResolvable_a771d0ef]] = None,
            export_to_csv_option: typing.Optional[typing.Union["CfnDashboard.ExportToCSVOptionProperty", _IResolvable_a771d0ef]] = None,
            sheet_controls_option: typing.Optional[typing.Union["CfnDashboard.SheetControlsOptionProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param ad_hoc_filtering_option: ``CfnDashboard.DashboardPublishOptionsProperty.AdHocFilteringOption``.
            :param export_to_csv_option: ``CfnDashboard.DashboardPublishOptionsProperty.ExportToCSVOption``.
            :param sheet_controls_option: ``CfnDashboard.DashboardPublishOptionsProperty.SheetControlsOption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_hoc_filtering_option is not None:
                self._values["ad_hoc_filtering_option"] = ad_hoc_filtering_option
            if export_to_csv_option is not None:
                self._values["export_to_csv_option"] = export_to_csv_option
            if sheet_controls_option is not None:
                self._values["sheet_controls_option"] = sheet_controls_option

        @builtins.property
        def ad_hoc_filtering_option(
            self,
        ) -> typing.Optional[typing.Union["CfnDashboard.AdHocFilteringOptionProperty", _IResolvable_a771d0ef]]:
            """``CfnDashboard.DashboardPublishOptionsProperty.AdHocFilteringOption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption
            """
            result = self._values.get("ad_hoc_filtering_option")
            return result

        @builtins.property
        def export_to_csv_option(
            self,
        ) -> typing.Optional[typing.Union["CfnDashboard.ExportToCSVOptionProperty", _IResolvable_a771d0ef]]:
            """``CfnDashboard.DashboardPublishOptionsProperty.ExportToCSVOption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption
            """
            result = self._values.get("export_to_csv_option")
            return result

        @builtins.property
        def sheet_controls_option(
            self,
        ) -> typing.Optional[typing.Union["CfnDashboard.SheetControlsOptionProperty", _IResolvable_a771d0ef]]:
            """``CfnDashboard.DashboardPublishOptionsProperty.SheetControlsOption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption
            """
            result = self._values.get("sheet_controls_option")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardPublishOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DashboardSourceEntityProperty",
        jsii_struct_bases=[],
        name_mapping={"source_template": "sourceTemplate"},
    )
    class DashboardSourceEntityProperty:
        def __init__(
            self,
            *,
            source_template: typing.Optional[typing.Union["CfnDashboard.DashboardSourceTemplateProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param source_template: ``CfnDashboard.DashboardSourceEntityProperty.SourceTemplate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if source_template is not None:
                self._values["source_template"] = source_template

        @builtins.property
        def source_template(
            self,
        ) -> typing.Optional[typing.Union["CfnDashboard.DashboardSourceTemplateProperty", _IResolvable_a771d0ef]]:
            """``CfnDashboard.DashboardSourceEntityProperty.SourceTemplate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html#cfn-quicksight-dashboard-dashboardsourceentity-sourcetemplate
            """
            result = self._values.get("source_template")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardSourceEntityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DashboardSourceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
    )
    class DashboardSourceTemplateProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            data_set_references: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DataSetReferenceProperty", _IResolvable_a771d0ef]]],
        ) -> None:
            """
            :param arn: ``CfnDashboard.DashboardSourceTemplateProperty.Arn``.
            :param data_set_references: ``CfnDashboard.DashboardSourceTemplateProperty.DataSetReferences``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "data_set_references": data_set_references,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            """``CfnDashboard.DashboardSourceTemplateProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-arn
            """
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return result

        @builtins.property
        def data_set_references(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DataSetReferenceProperty", _IResolvable_a771d0ef]]]:
            """``CfnDashboard.DashboardSourceTemplateProperty.DataSetReferences``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences
            """
            result = self._values.get("data_set_references")
            assert result is not None, "Required property 'data_set_references' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardSourceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DashboardVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "data_set_arns": "dataSetArns",
            "description": "description",
            "errors": "errors",
            "sheets": "sheets",
            "source_entity_arn": "sourceEntityArn",
            "status": "status",
            "theme_arn": "themeArn",
            "version_number": "versionNumber",
        },
    )
    class DashboardVersionProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            data_set_arns: typing.Optional[typing.List[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            errors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DashboardErrorProperty", _IResolvable_a771d0ef]]]] = None,
            sheets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.SheetProperty", _IResolvable_a771d0ef]]]] = None,
            source_entity_arn: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
            theme_arn: typing.Optional[builtins.str] = None,
            version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param arn: ``CfnDashboard.DashboardVersionProperty.Arn``.
            :param created_time: ``CfnDashboard.DashboardVersionProperty.CreatedTime``.
            :param data_set_arns: ``CfnDashboard.DashboardVersionProperty.DataSetArns``.
            :param description: ``CfnDashboard.DashboardVersionProperty.Description``.
            :param errors: ``CfnDashboard.DashboardVersionProperty.Errors``.
            :param sheets: ``CfnDashboard.DashboardVersionProperty.Sheets``.
            :param source_entity_arn: ``CfnDashboard.DashboardVersionProperty.SourceEntityArn``.
            :param status: ``CfnDashboard.DashboardVersionProperty.Status``.
            :param theme_arn: ``CfnDashboard.DashboardVersionProperty.ThemeArn``.
            :param version_number: ``CfnDashboard.DashboardVersionProperty.VersionNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if data_set_arns is not None:
                self._values["data_set_arns"] = data_set_arns
            if description is not None:
                self._values["description"] = description
            if errors is not None:
                self._values["errors"] = errors
            if sheets is not None:
                self._values["sheets"] = sheets
            if source_entity_arn is not None:
                self._values["source_entity_arn"] = source_entity_arn
            if status is not None:
                self._values["status"] = status
            if theme_arn is not None:
                self._values["theme_arn"] = theme_arn
            if version_number is not None:
                self._values["version_number"] = version_number

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardVersionProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-arn
            """
            result = self._values.get("arn")
            return result

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardVersionProperty.CreatedTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-createdtime
            """
            result = self._values.get("created_time")
            return result

        @builtins.property
        def data_set_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnDashboard.DashboardVersionProperty.DataSetArns``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-datasetarns
            """
            result = self._values.get("data_set_arns")
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardVersionProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def errors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DashboardErrorProperty", _IResolvable_a771d0ef]]]]:
            """``CfnDashboard.DashboardVersionProperty.Errors``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-errors
            """
            result = self._values.get("errors")
            return result

        @builtins.property
        def sheets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.SheetProperty", _IResolvable_a771d0ef]]]]:
            """``CfnDashboard.DashboardVersionProperty.Sheets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-sheets
            """
            result = self._values.get("sheets")
            return result

        @builtins.property
        def source_entity_arn(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardVersionProperty.SourceEntityArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-sourceentityarn
            """
            result = self._values.get("source_entity_arn")
            return result

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardVersionProperty.Status``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-status
            """
            result = self._values.get("status")
            return result

        @builtins.property
        def theme_arn(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.DashboardVersionProperty.ThemeArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-themearn
            """
            result = self._values.get("theme_arn")
            return result

        @builtins.property
        def version_number(self) -> typing.Optional[jsii.Number]:
            """``CfnDashboard.DashboardVersionProperty.VersionNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html#cfn-quicksight-dashboard-dashboardversion-versionnumber
            """
            result = self._values.get("version_number")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DataSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_set_arn": "dataSetArn",
            "data_set_placeholder": "dataSetPlaceholder",
        },
    )
    class DataSetReferenceProperty:
        def __init__(
            self,
            *,
            data_set_arn: builtins.str,
            data_set_placeholder: builtins.str,
        ) -> None:
            """
            :param data_set_arn: ``CfnDashboard.DataSetReferenceProperty.DataSetArn``.
            :param data_set_placeholder: ``CfnDashboard.DataSetReferenceProperty.DataSetPlaceholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "data_set_arn": data_set_arn,
                "data_set_placeholder": data_set_placeholder,
            }

        @builtins.property
        def data_set_arn(self) -> builtins.str:
            """``CfnDashboard.DataSetReferenceProperty.DataSetArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetarn
            """
            result = self._values.get("data_set_arn")
            assert result is not None, "Required property 'data_set_arn' is missing"
            return result

        @builtins.property
        def data_set_placeholder(self) -> builtins.str:
            """``CfnDashboard.DataSetReferenceProperty.DataSetPlaceholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetplaceholder
            """
            result = self._values.get("data_set_placeholder")
            assert result is not None, "Required property 'data_set_placeholder' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DateTimeParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DateTimeParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.List[builtins.str],
        ) -> None:
            """
            :param name: ``CfnDashboard.DateTimeParameterProperty.Name``.
            :param values: ``CfnDashboard.DateTimeParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnDashboard.DateTimeParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            """``CfnDashboard.DateTimeParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateTimeParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.DecimalParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DecimalParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]],
        ) -> None:
            """
            :param name: ``CfnDashboard.DecimalParameterProperty.Name``.
            :param values: ``CfnDashboard.DecimalParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnDashboard.DecimalParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]:
            """``CfnDashboard.DecimalParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecimalParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.ExportToCSVOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_status": "availabilityStatus"},
    )
    class ExportToCSVOptionProperty:
        def __init__(
            self,
            *,
            availability_status: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param availability_status: ``CfnDashboard.ExportToCSVOptionProperty.AvailabilityStatus``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_status is not None:
                self._values["availability_status"] = availability_status

        @builtins.property
        def availability_status(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.ExportToCSVOptionProperty.AvailabilityStatus``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html#cfn-quicksight-dashboard-exporttocsvoption-availabilitystatus
            """
            result = self._values.get("availability_status")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExportToCSVOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.IntegerParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class IntegerParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]],
        ) -> None:
            """
            :param name: ``CfnDashboard.IntegerParameterProperty.Name``.
            :param values: ``CfnDashboard.IntegerParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnDashboard.IntegerParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]:
            """``CfnDashboard.IntegerParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_time_parameters": "dateTimeParameters",
            "decimal_parameters": "decimalParameters",
            "integer_parameters": "integerParameters",
            "string_parameters": "stringParameters",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            date_time_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DateTimeParameterProperty", _IResolvable_a771d0ef]]]] = None,
            decimal_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DecimalParameterProperty", _IResolvable_a771d0ef]]]] = None,
            integer_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.IntegerParameterProperty", _IResolvable_a771d0ef]]]] = None,
            string_parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.StringParameterProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param date_time_parameters: ``CfnDashboard.ParametersProperty.DateTimeParameters``.
            :param decimal_parameters: ``CfnDashboard.ParametersProperty.DecimalParameters``.
            :param integer_parameters: ``CfnDashboard.ParametersProperty.IntegerParameters``.
            :param string_parameters: ``CfnDashboard.ParametersProperty.StringParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if date_time_parameters is not None:
                self._values["date_time_parameters"] = date_time_parameters
            if decimal_parameters is not None:
                self._values["decimal_parameters"] = decimal_parameters
            if integer_parameters is not None:
                self._values["integer_parameters"] = integer_parameters
            if string_parameters is not None:
                self._values["string_parameters"] = string_parameters

        @builtins.property
        def date_time_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DateTimeParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnDashboard.ParametersProperty.DateTimeParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-datetimeparameters
            """
            result = self._values.get("date_time_parameters")
            return result

        @builtins.property
        def decimal_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.DecimalParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnDashboard.ParametersProperty.DecimalParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-decimalparameters
            """
            result = self._values.get("decimal_parameters")
            return result

        @builtins.property
        def integer_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.IntegerParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnDashboard.ParametersProperty.IntegerParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-integerparameters
            """
            result = self._values.get("integer_parameters")
            return result

        @builtins.property
        def string_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnDashboard.StringParameterProperty", _IResolvable_a771d0ef]]]]:
            """``CfnDashboard.ParametersProperty.StringParameters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-stringparameters
            """
            result = self._values.get("string_parameters")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.List[builtins.str],
            principal: builtins.str,
        ) -> None:
            """
            :param actions: ``CfnDashboard.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnDashboard.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            """``CfnDashboard.ResourcePermissionProperty.Actions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-actions
            """
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return result

        @builtins.property
        def principal(self) -> builtins.str:
            """``CfnDashboard.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-principal
            """
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.SheetControlsOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"visibility_state": "visibilityState"},
    )
    class SheetControlsOptionProperty:
        def __init__(
            self,
            *,
            visibility_state: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param visibility_state: ``CfnDashboard.SheetControlsOptionProperty.VisibilityState``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if visibility_state is not None:
                self._values["visibility_state"] = visibility_state

        @builtins.property
        def visibility_state(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.SheetControlsOptionProperty.VisibilityState``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html#cfn-quicksight-dashboard-sheetcontrolsoption-visibilitystate
            """
            result = self._values.get("visibility_state")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetControlsOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.SheetProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sheet_id": "sheetId"},
    )
    class SheetProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            sheet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param name: ``CfnDashboard.SheetProperty.Name``.
            :param sheet_id: ``CfnDashboard.SheetProperty.SheetId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheet.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if sheet_id is not None:
                self._values["sheet_id"] = sheet_id

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.SheetProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheet.html#cfn-quicksight-dashboard-sheet-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def sheet_id(self) -> typing.Optional[builtins.str]:
            """``CfnDashboard.SheetProperty.SheetId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheet.html#cfn-quicksight-dashboard-sheet-sheetid
            """
            result = self._values.get("sheet_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnDashboard.StringParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class StringParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.List[builtins.str],
        ) -> None:
            """
            :param name: ``CfnDashboard.StringParameterProperty.Name``.
            :param values: ``CfnDashboard.StringParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnDashboard.StringParameterProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            """``CfnDashboard.StringParameterProperty.Values``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-values
            """
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_quicksight.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "dashboard_publish_options": "dashboardPublishOptions",
        "name": "name",
        "parameters": "parameters",
        "permissions": "permissions",
        "source_entity": "sourceEntity",
        "tags": "tags",
        "theme_arn": "themeArn",
        "version_description": "versionDescription",
    },
)
class CfnDashboardProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        dashboard_publish_options: typing.Optional[typing.Union[CfnDashboard.DashboardPublishOptionsProperty, _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[CfnDashboard.ParametersProperty, _IResolvable_a771d0ef]] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDashboard.ResourcePermissionProperty, _IResolvable_a771d0ef]]]] = None,
        source_entity: typing.Optional[typing.Union[CfnDashboard.DashboardSourceEntityProperty, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::QuickSight::Dashboard``.

        :param aws_account_id: ``AWS::QuickSight::Dashboard.AwsAccountId``.
        :param dashboard_id: ``AWS::QuickSight::Dashboard.DashboardId``.
        :param dashboard_publish_options: ``AWS::QuickSight::Dashboard.DashboardPublishOptions``.
        :param name: ``AWS::QuickSight::Dashboard.Name``.
        :param parameters: ``AWS::QuickSight::Dashboard.Parameters``.
        :param permissions: ``AWS::QuickSight::Dashboard.Permissions``.
        :param source_entity: ``AWS::QuickSight::Dashboard.SourceEntity``.
        :param tags: ``AWS::QuickSight::Dashboard.Tags``.
        :param theme_arn: ``AWS::QuickSight::Dashboard.ThemeArn``.
        :param version_description: ``AWS::QuickSight::Dashboard.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }
        if dashboard_publish_options is not None:
            self._values["dashboard_publish_options"] = dashboard_publish_options
        if name is not None:
            self._values["name"] = name
        if parameters is not None:
            self._values["parameters"] = parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if source_entity is not None:
            self._values["source_entity"] = source_entity
        if tags is not None:
            self._values["tags"] = tags
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Dashboard.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-awsaccountid
        """
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return result

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        """``AWS::QuickSight::Dashboard.DashboardId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardid
        """
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return result

    @builtins.property
    def dashboard_publish_options(
        self,
    ) -> typing.Optional[typing.Union[CfnDashboard.DashboardPublishOptionsProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Dashboard.DashboardPublishOptions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardpublishoptions
        """
        result = self._values.get("dashboard_publish_options")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Dashboard.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[CfnDashboard.ParametersProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Dashboard.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-parameters
        """
        result = self._values.get("parameters")
        return result

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnDashboard.ResourcePermissionProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Dashboard.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-permissions
        """
        result = self._values.get("permissions")
        return result

    @builtins.property
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[CfnDashboard.DashboardSourceEntityProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Dashboard.SourceEntity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-sourceentity
        """
        result = self._values.get("source_entity")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::QuickSight::Dashboard.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Dashboard.ThemeArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-themearn
        """
        result = self._values.get("theme_arn")
        return result

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Dashboard.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-versiondescription
        """
        result = self._values.get("version_description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnTemplate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_quicksight.CfnTemplate",
):
    """A CloudFormation ``AWS::QuickSight::Template``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html
    :cloudformationResource: AWS::QuickSight::Template
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ResourcePermissionProperty", _IResolvable_a771d0ef]]]] = None,
        source_entity: typing.Optional[typing.Union["CfnTemplate.TemplateSourceEntityProperty", _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::QuickSight::Template``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::Template.AwsAccountId``.
        :param template_id: ``AWS::QuickSight::Template.TemplateId``.
        :param name: ``AWS::QuickSight::Template.Name``.
        :param permissions: ``AWS::QuickSight::Template.Permissions``.
        :param source_entity: ``AWS::QuickSight::Template.SourceEntity``.
        :param tags: ``AWS::QuickSight::Template.Tags``.
        :param version_description: ``AWS::QuickSight::Template.VersionDescription``.
        """
        props = CfnTemplateProps(
            aws_account_id=aws_account_id,
            template_id=template_id,
            name=name,
            permissions=permissions,
            source_entity=source_entity,
            tags=tags,
            version_description=version_description,
        )

        jsii.create(CfnTemplate, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreatedTime
        """
        return jsii.get(self, "attrCreatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        """
        :cloudformationAttribute: LastUpdatedTime
        """
        return jsii.get(self, "attrLastUpdatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::QuickSight::Template.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Template.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-awsaccountid
        """
        return jsii.get(self, "awsAccountId")

    @aws_account_id.setter # type: ignore
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> builtins.str:
        """``AWS::QuickSight::Template.TemplateId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-templateid
        """
        return jsii.get(self, "templateId")

    @template_id.setter # type: ignore
    def template_id(self, value: builtins.str) -> None:
        jsii.set(self, "templateId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Template.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ResourcePermissionProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Template.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-permissions
        """
        return jsii.get(self, "permissions")

    @permissions.setter # type: ignore
    def permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ResourcePermissionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="sourceEntity")
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union["CfnTemplate.TemplateSourceEntityProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Template.SourceEntity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-sourceentity
        """
        return jsii.get(self, "sourceEntity")

    @source_entity.setter # type: ignore
    def source_entity(
        self,
        value: typing.Optional[typing.Union["CfnTemplate.TemplateSourceEntityProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "sourceEntity", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Template.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-versiondescription
        """
        return jsii.get(self, "versionDescription")

    @version_description.setter # type: ignore
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionDescription", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.ColumnGroupColumnSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class ColumnGroupColumnSchemaProperty:
        def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
            """
            :param name: ``CfnTemplate.ColumnGroupColumnSchemaProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupcolumnschema.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.ColumnGroupColumnSchemaProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupcolumnschema.html#cfn-quicksight-template-columngroupcolumnschema-name
            """
            result = self._values.get("name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnGroupColumnSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.ColumnGroupSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_group_column_schema_list": "columnGroupColumnSchemaList",
            "name": "name",
        },
    )
    class ColumnGroupSchemaProperty:
        def __init__(
            self,
            *,
            column_group_column_schema_list: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ColumnGroupColumnSchemaProperty", _IResolvable_a771d0ef]]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param column_group_column_schema_list: ``CfnTemplate.ColumnGroupSchemaProperty.ColumnGroupColumnSchemaList``.
            :param name: ``CfnTemplate.ColumnGroupSchemaProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupschema.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if column_group_column_schema_list is not None:
                self._values["column_group_column_schema_list"] = column_group_column_schema_list
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def column_group_column_schema_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ColumnGroupColumnSchemaProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTemplate.ColumnGroupSchemaProperty.ColumnGroupColumnSchemaList``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupschema.html#cfn-quicksight-template-columngroupschema-columngroupcolumnschemalist
            """
            result = self._values.get("column_group_column_schema_list")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.ColumnGroupSchemaProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupschema.html#cfn-quicksight-template-columngroupschema-name
            """
            result = self._values.get("name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnGroupSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.ColumnSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "geographic_role": "geographicRole",
            "name": "name",
        },
    )
    class ColumnSchemaProperty:
        def __init__(
            self,
            *,
            data_type: typing.Optional[builtins.str] = None,
            geographic_role: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param data_type: ``CfnTemplate.ColumnSchemaProperty.DataType``.
            :param geographic_role: ``CfnTemplate.ColumnSchemaProperty.GeographicRole``.
            :param name: ``CfnTemplate.ColumnSchemaProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columnschema.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if data_type is not None:
                self._values["data_type"] = data_type
            if geographic_role is not None:
                self._values["geographic_role"] = geographic_role
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.ColumnSchemaProperty.DataType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columnschema.html#cfn-quicksight-template-columnschema-datatype
            """
            result = self._values.get("data_type")
            return result

        @builtins.property
        def geographic_role(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.ColumnSchemaProperty.GeographicRole``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columnschema.html#cfn-quicksight-template-columnschema-geographicrole
            """
            result = self._values.get("geographic_role")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.ColumnSchemaProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columnschema.html#cfn-quicksight-template-columnschema-name
            """
            result = self._values.get("name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.DataSetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_group_schema_list": "columnGroupSchemaList",
            "data_set_schema": "dataSetSchema",
            "placeholder": "placeholder",
        },
    )
    class DataSetConfigurationProperty:
        def __init__(
            self,
            *,
            column_group_schema_list: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ColumnGroupSchemaProperty", _IResolvable_a771d0ef]]]] = None,
            data_set_schema: typing.Optional[typing.Union["CfnTemplate.DataSetSchemaProperty", _IResolvable_a771d0ef]] = None,
            placeholder: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param column_group_schema_list: ``CfnTemplate.DataSetConfigurationProperty.ColumnGroupSchemaList``.
            :param data_set_schema: ``CfnTemplate.DataSetConfigurationProperty.DataSetSchema``.
            :param placeholder: ``CfnTemplate.DataSetConfigurationProperty.Placeholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if column_group_schema_list is not None:
                self._values["column_group_schema_list"] = column_group_schema_list
            if data_set_schema is not None:
                self._values["data_set_schema"] = data_set_schema
            if placeholder is not None:
                self._values["placeholder"] = placeholder

        @builtins.property
        def column_group_schema_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ColumnGroupSchemaProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTemplate.DataSetConfigurationProperty.ColumnGroupSchemaList``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetconfiguration.html#cfn-quicksight-template-datasetconfiguration-columngroupschemalist
            """
            result = self._values.get("column_group_schema_list")
            return result

        @builtins.property
        def data_set_schema(
            self,
        ) -> typing.Optional[typing.Union["CfnTemplate.DataSetSchemaProperty", _IResolvable_a771d0ef]]:
            """``CfnTemplate.DataSetConfigurationProperty.DataSetSchema``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetconfiguration.html#cfn-quicksight-template-datasetconfiguration-datasetschema
            """
            result = self._values.get("data_set_schema")
            return result

        @builtins.property
        def placeholder(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.DataSetConfigurationProperty.Placeholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetconfiguration.html#cfn-quicksight-template-datasetconfiguration-placeholder
            """
            result = self._values.get("placeholder")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.DataSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_set_arn": "dataSetArn",
            "data_set_placeholder": "dataSetPlaceholder",
        },
    )
    class DataSetReferenceProperty:
        def __init__(
            self,
            *,
            data_set_arn: builtins.str,
            data_set_placeholder: builtins.str,
        ) -> None:
            """
            :param data_set_arn: ``CfnTemplate.DataSetReferenceProperty.DataSetArn``.
            :param data_set_placeholder: ``CfnTemplate.DataSetReferenceProperty.DataSetPlaceholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "data_set_arn": data_set_arn,
                "data_set_placeholder": data_set_placeholder,
            }

        @builtins.property
        def data_set_arn(self) -> builtins.str:
            """``CfnTemplate.DataSetReferenceProperty.DataSetArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetarn
            """
            result = self._values.get("data_set_arn")
            assert result is not None, "Required property 'data_set_arn' is missing"
            return result

        @builtins.property
        def data_set_placeholder(self) -> builtins.str:
            """``CfnTemplate.DataSetReferenceProperty.DataSetPlaceholder``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetplaceholder
            """
            result = self._values.get("data_set_placeholder")
            assert result is not None, "Required property 'data_set_placeholder' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.DataSetSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"column_schema_list": "columnSchemaList"},
    )
    class DataSetSchemaProperty:
        def __init__(
            self,
            *,
            column_schema_list: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ColumnSchemaProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param column_schema_list: ``CfnTemplate.DataSetSchemaProperty.ColumnSchemaList``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetschema.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if column_schema_list is not None:
                self._values["column_schema_list"] = column_schema_list

        @builtins.property
        def column_schema_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.ColumnSchemaProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTemplate.DataSetSchemaProperty.ColumnSchemaList``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetschema.html#cfn-quicksight-template-datasetschema-columnschemalist
            """
            result = self._values.get("column_schema_list")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.List[builtins.str],
            principal: builtins.str,
        ) -> None:
            """
            :param actions: ``CfnTemplate.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnTemplate.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            """``CfnTemplate.ResourcePermissionProperty.Actions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-actions
            """
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return result

        @builtins.property
        def principal(self) -> builtins.str:
            """``CfnTemplate.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-principal
            """
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.SheetProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sheet_id": "sheetId"},
    )
    class SheetProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            sheet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param name: ``CfnTemplate.SheetProperty.Name``.
            :param sheet_id: ``CfnTemplate.SheetProperty.SheetId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-sheet.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if sheet_id is not None:
                self._values["sheet_id"] = sheet_id

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.SheetProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-sheet.html#cfn-quicksight-template-sheet-name
            """
            result = self._values.get("name")
            return result

        @builtins.property
        def sheet_id(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.SheetProperty.SheetId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-sheet.html#cfn-quicksight-template-sheet-sheetid
            """
            result = self._values.get("sheet_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.TemplateErrorProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "type": "type"},
    )
    class TemplateErrorProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param message: ``CfnTemplate.TemplateErrorProperty.Message``.
            :param type: ``CfnTemplate.TemplateErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateerror.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateErrorProperty.Message``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateerror.html#cfn-quicksight-template-templateerror-message
            """
            result = self._values.get("message")
            return result

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateerror.html#cfn-quicksight-template-templateerror-type
            """
            result = self._values.get("type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateErrorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.TemplateSourceAnalysisProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
    )
    class TemplateSourceAnalysisProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            data_set_references: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.DataSetReferenceProperty", _IResolvable_a771d0ef]]],
        ) -> None:
            """
            :param arn: ``CfnTemplate.TemplateSourceAnalysisProperty.Arn``.
            :param data_set_references: ``CfnTemplate.TemplateSourceAnalysisProperty.DataSetReferences``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "data_set_references": data_set_references,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            """``CfnTemplate.TemplateSourceAnalysisProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-arn
            """
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return result

        @builtins.property
        def data_set_references(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.DataSetReferenceProperty", _IResolvable_a771d0ef]]]:
            """``CfnTemplate.TemplateSourceAnalysisProperty.DataSetReferences``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-datasetreferences
            """
            result = self._values.get("data_set_references")
            assert result is not None, "Required property 'data_set_references' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSourceAnalysisProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.TemplateSourceEntityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_analysis": "sourceAnalysis",
            "source_template": "sourceTemplate",
        },
    )
    class TemplateSourceEntityProperty:
        def __init__(
            self,
            *,
            source_analysis: typing.Optional[typing.Union["CfnTemplate.TemplateSourceAnalysisProperty", _IResolvable_a771d0ef]] = None,
            source_template: typing.Optional[typing.Union["CfnTemplate.TemplateSourceTemplateProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param source_analysis: ``CfnTemplate.TemplateSourceEntityProperty.SourceAnalysis``.
            :param source_template: ``CfnTemplate.TemplateSourceEntityProperty.SourceTemplate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if source_analysis is not None:
                self._values["source_analysis"] = source_analysis
            if source_template is not None:
                self._values["source_template"] = source_template

        @builtins.property
        def source_analysis(
            self,
        ) -> typing.Optional[typing.Union["CfnTemplate.TemplateSourceAnalysisProperty", _IResolvable_a771d0ef]]:
            """``CfnTemplate.TemplateSourceEntityProperty.SourceAnalysis``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourceanalysis
            """
            result = self._values.get("source_analysis")
            return result

        @builtins.property
        def source_template(
            self,
        ) -> typing.Optional[typing.Union["CfnTemplate.TemplateSourceTemplateProperty", _IResolvable_a771d0ef]]:
            """``CfnTemplate.TemplateSourceEntityProperty.SourceTemplate``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourcetemplate
            """
            result = self._values.get("source_template")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSourceEntityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.TemplateSourceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class TemplateSourceTemplateProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            """
            :param arn: ``CfnTemplate.TemplateSourceTemplateProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            """``CfnTemplate.TemplateSourceTemplateProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html#cfn-quicksight-template-templatesourcetemplate-arn
            """
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSourceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTemplate.TemplateVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "created_time": "createdTime",
            "data_set_configurations": "dataSetConfigurations",
            "description": "description",
            "errors": "errors",
            "sheets": "sheets",
            "source_entity_arn": "sourceEntityArn",
            "status": "status",
            "theme_arn": "themeArn",
            "version_number": "versionNumber",
        },
    )
    class TemplateVersionProperty:
        def __init__(
            self,
            *,
            created_time: typing.Optional[builtins.str] = None,
            data_set_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.DataSetConfigurationProperty", _IResolvable_a771d0ef]]]] = None,
            description: typing.Optional[builtins.str] = None,
            errors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.TemplateErrorProperty", _IResolvable_a771d0ef]]]] = None,
            sheets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.SheetProperty", _IResolvable_a771d0ef]]]] = None,
            source_entity_arn: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
            theme_arn: typing.Optional[builtins.str] = None,
            version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param created_time: ``CfnTemplate.TemplateVersionProperty.CreatedTime``.
            :param data_set_configurations: ``CfnTemplate.TemplateVersionProperty.DataSetConfigurations``.
            :param description: ``CfnTemplate.TemplateVersionProperty.Description``.
            :param errors: ``CfnTemplate.TemplateVersionProperty.Errors``.
            :param sheets: ``CfnTemplate.TemplateVersionProperty.Sheets``.
            :param source_entity_arn: ``CfnTemplate.TemplateVersionProperty.SourceEntityArn``.
            :param status: ``CfnTemplate.TemplateVersionProperty.Status``.
            :param theme_arn: ``CfnTemplate.TemplateVersionProperty.ThemeArn``.
            :param version_number: ``CfnTemplate.TemplateVersionProperty.VersionNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if created_time is not None:
                self._values["created_time"] = created_time
            if data_set_configurations is not None:
                self._values["data_set_configurations"] = data_set_configurations
            if description is not None:
                self._values["description"] = description
            if errors is not None:
                self._values["errors"] = errors
            if sheets is not None:
                self._values["sheets"] = sheets
            if source_entity_arn is not None:
                self._values["source_entity_arn"] = source_entity_arn
            if status is not None:
                self._values["status"] = status
            if theme_arn is not None:
                self._values["theme_arn"] = theme_arn
            if version_number is not None:
                self._values["version_number"] = version_number

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateVersionProperty.CreatedTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-createdtime
            """
            result = self._values.get("created_time")
            return result

        @builtins.property
        def data_set_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.DataSetConfigurationProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTemplate.TemplateVersionProperty.DataSetConfigurations``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-datasetconfigurations
            """
            result = self._values.get("data_set_configurations")
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateVersionProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def errors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.TemplateErrorProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTemplate.TemplateVersionProperty.Errors``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-errors
            """
            result = self._values.get("errors")
            return result

        @builtins.property
        def sheets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTemplate.SheetProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTemplate.TemplateVersionProperty.Sheets``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-sheets
            """
            result = self._values.get("sheets")
            return result

        @builtins.property
        def source_entity_arn(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateVersionProperty.SourceEntityArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-sourceentityarn
            """
            result = self._values.get("source_entity_arn")
            return result

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateVersionProperty.Status``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-status
            """
            result = self._values.get("status")
            return result

        @builtins.property
        def theme_arn(self) -> typing.Optional[builtins.str]:
            """``CfnTemplate.TemplateVersionProperty.ThemeArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-themearn
            """
            result = self._values.get("theme_arn")
            return result

        @builtins.property
        def version_number(self) -> typing.Optional[jsii.Number]:
            """``CfnTemplate.TemplateVersionProperty.VersionNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html#cfn-quicksight-template-templateversion-versionnumber
            """
            result = self._values.get("version_number")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_quicksight.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "name": "name",
        "permissions": "permissions",
        "source_entity": "sourceEntity",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTemplate.ResourcePermissionProperty, _IResolvable_a771d0ef]]]] = None,
        source_entity: typing.Optional[typing.Union[CfnTemplate.TemplateSourceEntityProperty, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::QuickSight::Template``.

        :param aws_account_id: ``AWS::QuickSight::Template.AwsAccountId``.
        :param template_id: ``AWS::QuickSight::Template.TemplateId``.
        :param name: ``AWS::QuickSight::Template.Name``.
        :param permissions: ``AWS::QuickSight::Template.Permissions``.
        :param source_entity: ``AWS::QuickSight::Template.SourceEntity``.
        :param tags: ``AWS::QuickSight::Template.Tags``.
        :param version_description: ``AWS::QuickSight::Template.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if source_entity is not None:
            self._values["source_entity"] = source_entity
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Template.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-awsaccountid
        """
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return result

    @builtins.property
    def template_id(self) -> builtins.str:
        """``AWS::QuickSight::Template.TemplateId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-templateid
        """
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Template.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTemplate.ResourcePermissionProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Template.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-permissions
        """
        result = self._values.get("permissions")
        return result

    @builtins.property
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[CfnTemplate.TemplateSourceEntityProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Template.SourceEntity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-sourceentity
        """
        result = self._values.get("source_entity")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::QuickSight::Template.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Template.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-versiondescription
        """
        result = self._values.get("version_description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnTheme(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_quicksight.CfnTheme",
):
    """A CloudFormation ``AWS::QuickSight::Theme``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html
    :cloudformationResource: AWS::QuickSight::Theme
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        base_theme_id: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union["CfnTheme.ThemeConfigurationProperty", _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.ResourcePermissionProperty", _IResolvable_a771d0ef]]]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::QuickSight::Theme``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::Theme.AwsAccountId``.
        :param theme_id: ``AWS::QuickSight::Theme.ThemeId``.
        :param base_theme_id: ``AWS::QuickSight::Theme.BaseThemeId``.
        :param configuration: ``AWS::QuickSight::Theme.Configuration``.
        :param name: ``AWS::QuickSight::Theme.Name``.
        :param permissions: ``AWS::QuickSight::Theme.Permissions``.
        :param tags: ``AWS::QuickSight::Theme.Tags``.
        :param version_description: ``AWS::QuickSight::Theme.VersionDescription``.
        """
        props = CfnThemeProps(
            aws_account_id=aws_account_id,
            theme_id=theme_id,
            base_theme_id=base_theme_id,
            configuration=configuration,
            name=name,
            permissions=permissions,
            tags=tags,
            version_description=version_description,
        )

        jsii.create(CfnTheme, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreatedTime
        """
        return jsii.get(self, "attrCreatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        """
        :cloudformationAttribute: LastUpdatedTime
        """
        return jsii.get(self, "attrLastUpdatedTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        """
        :cloudformationAttribute: Type
        """
        return jsii.get(self, "attrType")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::QuickSight::Theme.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Theme.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-awsaccountid
        """
        return jsii.get(self, "awsAccountId")

    @aws_account_id.setter # type: ignore
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="themeId")
    def theme_id(self) -> builtins.str:
        """``AWS::QuickSight::Theme.ThemeId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-themeid
        """
        return jsii.get(self, "themeId")

    @theme_id.setter # type: ignore
    def theme_id(self, value: builtins.str) -> None:
        jsii.set(self, "themeId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="baseThemeId")
    def base_theme_id(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Theme.BaseThemeId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-basethemeid
        """
        return jsii.get(self, "baseThemeId")

    @base_theme_id.setter # type: ignore
    def base_theme_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "baseThemeId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnTheme.ThemeConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Theme.Configuration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-configuration
        """
        return jsii.get(self, "configuration")

    @configuration.setter # type: ignore
    def configuration(
        self,
        value: typing.Optional[typing.Union["CfnTheme.ThemeConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "configuration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Theme.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.ResourcePermissionProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Theme.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-permissions
        """
        return jsii.get(self, "permissions")

    @permissions.setter # type: ignore
    def permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.ResourcePermissionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Theme.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-versiondescription
        """
        return jsii.get(self, "versionDescription")

    @version_description.setter # type: ignore
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionDescription", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.BorderStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"show": "show"},
    )
    class BorderStyleProperty:
        def __init__(
            self,
            *,
            show: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param show: ``CfnTheme.BorderStyleProperty.Show``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if show is not None:
                self._values["show"] = show

        @builtins.property
        def show(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnTheme.BorderStyleProperty.Show``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html#cfn-quicksight-theme-borderstyle-show
            """
            result = self._values.get("show")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BorderStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.DataColorPaletteProperty",
        jsii_struct_bases=[],
        name_mapping={
            "colors": "colors",
            "empty_fill_color": "emptyFillColor",
            "min_max_gradient": "minMaxGradient",
        },
    )
    class DataColorPaletteProperty:
        def __init__(
            self,
            *,
            colors: typing.Optional[typing.List[builtins.str]] = None,
            empty_fill_color: typing.Optional[builtins.str] = None,
            min_max_gradient: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param colors: ``CfnTheme.DataColorPaletteProperty.Colors``.
            :param empty_fill_color: ``CfnTheme.DataColorPaletteProperty.EmptyFillColor``.
            :param min_max_gradient: ``CfnTheme.DataColorPaletteProperty.MinMaxGradient``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if colors is not None:
                self._values["colors"] = colors
            if empty_fill_color is not None:
                self._values["empty_fill_color"] = empty_fill_color
            if min_max_gradient is not None:
                self._values["min_max_gradient"] = min_max_gradient

        @builtins.property
        def colors(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnTheme.DataColorPaletteProperty.Colors``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-colors
            """
            result = self._values.get("colors")
            return result

        @builtins.property
        def empty_fill_color(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.DataColorPaletteProperty.EmptyFillColor``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-emptyfillcolor
            """
            result = self._values.get("empty_fill_color")
            return result

        @builtins.property
        def min_max_gradient(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnTheme.DataColorPaletteProperty.MinMaxGradient``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-minmaxgradient
            """
            result = self._values.get("min_max_gradient")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataColorPaletteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.FontProperty",
        jsii_struct_bases=[],
        name_mapping={"font_family": "fontFamily"},
    )
    class FontProperty:
        def __init__(
            self,
            *,
            font_family: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param font_family: ``CfnTheme.FontProperty.FontFamily``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if font_family is not None:
                self._values["font_family"] = font_family

        @builtins.property
        def font_family(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.FontProperty.FontFamily``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html#cfn-quicksight-theme-font-fontfamily
            """
            result = self._values.get("font_family")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FontProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.GutterStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"show": "show"},
    )
    class GutterStyleProperty:
        def __init__(
            self,
            *,
            show: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param show: ``CfnTheme.GutterStyleProperty.Show``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if show is not None:
                self._values["show"] = show

        @builtins.property
        def show(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnTheme.GutterStyleProperty.Show``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html#cfn-quicksight-theme-gutterstyle-show
            """
            result = self._values.get("show")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GutterStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.MarginStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"show": "show"},
    )
    class MarginStyleProperty:
        def __init__(
            self,
            *,
            show: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param show: ``CfnTheme.MarginStyleProperty.Show``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if show is not None:
                self._values["show"] = show

        @builtins.property
        def show(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnTheme.MarginStyleProperty.Show``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html#cfn-quicksight-theme-marginstyle-show
            """
            result = self._values.get("show")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarginStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.List[builtins.str],
            principal: builtins.str,
        ) -> None:
            """
            :param actions: ``CfnTheme.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnTheme.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            """``CfnTheme.ResourcePermissionProperty.Actions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-actions
            """
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return result

        @builtins.property
        def principal(self) -> builtins.str:
            """``CfnTheme.ResourcePermissionProperty.Principal``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-principal
            """
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.SheetStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"tile": "tile", "tile_layout": "tileLayout"},
    )
    class SheetStyleProperty:
        def __init__(
            self,
            *,
            tile: typing.Optional[typing.Union["CfnTheme.TileStyleProperty", _IResolvable_a771d0ef]] = None,
            tile_layout: typing.Optional[typing.Union["CfnTheme.TileLayoutStyleProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param tile: ``CfnTheme.SheetStyleProperty.Tile``.
            :param tile_layout: ``CfnTheme.SheetStyleProperty.TileLayout``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if tile is not None:
                self._values["tile"] = tile
            if tile_layout is not None:
                self._values["tile_layout"] = tile_layout

        @builtins.property
        def tile(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.TileStyleProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.SheetStyleProperty.Tile``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tile
            """
            result = self._values.get("tile")
            return result

        @builtins.property
        def tile_layout(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.TileLayoutStyleProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.SheetStyleProperty.TileLayout``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tilelayout
            """
            result = self._values.get("tile_layout")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.ThemeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_color_palette": "dataColorPalette",
            "sheet": "sheet",
            "typography": "typography",
            "ui_color_palette": "uiColorPalette",
        },
    )
    class ThemeConfigurationProperty:
        def __init__(
            self,
            *,
            data_color_palette: typing.Optional[typing.Union["CfnTheme.DataColorPaletteProperty", _IResolvable_a771d0ef]] = None,
            sheet: typing.Optional[typing.Union["CfnTheme.SheetStyleProperty", _IResolvable_a771d0ef]] = None,
            typography: typing.Optional[typing.Union["CfnTheme.TypographyProperty", _IResolvable_a771d0ef]] = None,
            ui_color_palette: typing.Optional[typing.Union["CfnTheme.UIColorPaletteProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param data_color_palette: ``CfnTheme.ThemeConfigurationProperty.DataColorPalette``.
            :param sheet: ``CfnTheme.ThemeConfigurationProperty.Sheet``.
            :param typography: ``CfnTheme.ThemeConfigurationProperty.Typography``.
            :param ui_color_palette: ``CfnTheme.ThemeConfigurationProperty.UIColorPalette``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if data_color_palette is not None:
                self._values["data_color_palette"] = data_color_palette
            if sheet is not None:
                self._values["sheet"] = sheet
            if typography is not None:
                self._values["typography"] = typography
            if ui_color_palette is not None:
                self._values["ui_color_palette"] = ui_color_palette

        @builtins.property
        def data_color_palette(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.DataColorPaletteProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.ThemeConfigurationProperty.DataColorPalette``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-datacolorpalette
            """
            result = self._values.get("data_color_palette")
            return result

        @builtins.property
        def sheet(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.SheetStyleProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.ThemeConfigurationProperty.Sheet``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-sheet
            """
            result = self._values.get("sheet")
            return result

        @builtins.property
        def typography(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.TypographyProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.ThemeConfigurationProperty.Typography``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-typography
            """
            result = self._values.get("typography")
            return result

        @builtins.property
        def ui_color_palette(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.UIColorPaletteProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.ThemeConfigurationProperty.UIColorPalette``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-uicolorpalette
            """
            result = self._values.get("ui_color_palette")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThemeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.ThemeErrorProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "type": "type"},
    )
    class ThemeErrorProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param message: ``CfnTheme.ThemeErrorProperty.Message``.
            :param type: ``CfnTheme.ThemeErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeerror.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeErrorProperty.Message``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeerror.html#cfn-quicksight-theme-themeerror-message
            """
            result = self._values.get("message")
            return result

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeErrorProperty.Type``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeerror.html#cfn-quicksight-theme-themeerror-type
            """
            result = self._values.get("type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThemeErrorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.ThemeVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "base_theme_id": "baseThemeId",
            "configuration": "configuration",
            "created_time": "createdTime",
            "description": "description",
            "errors": "errors",
            "status": "status",
            "version_number": "versionNumber",
        },
    )
    class ThemeVersionProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            base_theme_id: typing.Optional[builtins.str] = None,
            configuration: typing.Optional[typing.Union["CfnTheme.ThemeConfigurationProperty", _IResolvable_a771d0ef]] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            errors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.ThemeErrorProperty", _IResolvable_a771d0ef]]]] = None,
            status: typing.Optional[builtins.str] = None,
            version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param arn: ``CfnTheme.ThemeVersionProperty.Arn``.
            :param base_theme_id: ``CfnTheme.ThemeVersionProperty.BaseThemeId``.
            :param configuration: ``CfnTheme.ThemeVersionProperty.Configuration``.
            :param created_time: ``CfnTheme.ThemeVersionProperty.CreatedTime``.
            :param description: ``CfnTheme.ThemeVersionProperty.Description``.
            :param errors: ``CfnTheme.ThemeVersionProperty.Errors``.
            :param status: ``CfnTheme.ThemeVersionProperty.Status``.
            :param version_number: ``CfnTheme.ThemeVersionProperty.VersionNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if base_theme_id is not None:
                self._values["base_theme_id"] = base_theme_id
            if configuration is not None:
                self._values["configuration"] = configuration
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if errors is not None:
                self._values["errors"] = errors
            if status is not None:
                self._values["status"] = status
            if version_number is not None:
                self._values["version_number"] = version_number

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeVersionProperty.Arn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-arn
            """
            result = self._values.get("arn")
            return result

        @builtins.property
        def base_theme_id(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeVersionProperty.BaseThemeId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-basethemeid
            """
            result = self._values.get("base_theme_id")
            return result

        @builtins.property
        def configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.ThemeConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.ThemeVersionProperty.Configuration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-configuration
            """
            result = self._values.get("configuration")
            return result

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeVersionProperty.CreatedTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-createdtime
            """
            result = self._values.get("created_time")
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeVersionProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def errors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.ThemeErrorProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTheme.ThemeVersionProperty.Errors``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-errors
            """
            result = self._values.get("errors")
            return result

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.ThemeVersionProperty.Status``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-status
            """
            result = self._values.get("status")
            return result

        @builtins.property
        def version_number(self) -> typing.Optional[jsii.Number]:
            """``CfnTheme.ThemeVersionProperty.VersionNumber``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html#cfn-quicksight-theme-themeversion-versionnumber
            """
            result = self._values.get("version_number")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThemeVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.TileLayoutStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"gutter": "gutter", "margin": "margin"},
    )
    class TileLayoutStyleProperty:
        def __init__(
            self,
            *,
            gutter: typing.Optional[typing.Union["CfnTheme.GutterStyleProperty", _IResolvable_a771d0ef]] = None,
            margin: typing.Optional[typing.Union["CfnTheme.MarginStyleProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param gutter: ``CfnTheme.TileLayoutStyleProperty.Gutter``.
            :param margin: ``CfnTheme.TileLayoutStyleProperty.Margin``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if gutter is not None:
                self._values["gutter"] = gutter
            if margin is not None:
                self._values["margin"] = margin

        @builtins.property
        def gutter(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.GutterStyleProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.TileLayoutStyleProperty.Gutter``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-gutter
            """
            result = self._values.get("gutter")
            return result

        @builtins.property
        def margin(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.MarginStyleProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.TileLayoutStyleProperty.Margin``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-margin
            """
            result = self._values.get("margin")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TileLayoutStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.TileStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"border": "border"},
    )
    class TileStyleProperty:
        def __init__(
            self,
            *,
            border: typing.Optional[typing.Union["CfnTheme.BorderStyleProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param border: ``CfnTheme.TileStyleProperty.Border``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if border is not None:
                self._values["border"] = border

        @builtins.property
        def border(
            self,
        ) -> typing.Optional[typing.Union["CfnTheme.BorderStyleProperty", _IResolvable_a771d0ef]]:
            """``CfnTheme.TileStyleProperty.Border``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html#cfn-quicksight-theme-tilestyle-border
            """
            result = self._values.get("border")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TileStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.TypographyProperty",
        jsii_struct_bases=[],
        name_mapping={"font_families": "fontFamilies"},
    )
    class TypographyProperty:
        def __init__(
            self,
            *,
            font_families: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.FontProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param font_families: ``CfnTheme.TypographyProperty.FontFamilies``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if font_families is not None:
                self._values["font_families"] = font_families

        @builtins.property
        def font_families(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTheme.FontProperty", _IResolvable_a771d0ef]]]]:
            """``CfnTheme.TypographyProperty.FontFamilies``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html#cfn-quicksight-theme-typography-fontfamilies
            """
            result = self._values.get("font_families")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TypographyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_quicksight.CfnTheme.UIColorPaletteProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accent": "accent",
            "accent_foreground": "accentForeground",
            "danger": "danger",
            "danger_foreground": "dangerForeground",
            "dimension": "dimension",
            "dimension_foreground": "dimensionForeground",
            "measure": "measure",
            "measure_foreground": "measureForeground",
            "primary_background": "primaryBackground",
            "primary_foreground": "primaryForeground",
            "secondary_background": "secondaryBackground",
            "secondary_foreground": "secondaryForeground",
            "success": "success",
            "success_foreground": "successForeground",
            "warning": "warning",
            "warning_foreground": "warningForeground",
        },
    )
    class UIColorPaletteProperty:
        def __init__(
            self,
            *,
            accent: typing.Optional[builtins.str] = None,
            accent_foreground: typing.Optional[builtins.str] = None,
            danger: typing.Optional[builtins.str] = None,
            danger_foreground: typing.Optional[builtins.str] = None,
            dimension: typing.Optional[builtins.str] = None,
            dimension_foreground: typing.Optional[builtins.str] = None,
            measure: typing.Optional[builtins.str] = None,
            measure_foreground: typing.Optional[builtins.str] = None,
            primary_background: typing.Optional[builtins.str] = None,
            primary_foreground: typing.Optional[builtins.str] = None,
            secondary_background: typing.Optional[builtins.str] = None,
            secondary_foreground: typing.Optional[builtins.str] = None,
            success: typing.Optional[builtins.str] = None,
            success_foreground: typing.Optional[builtins.str] = None,
            warning: typing.Optional[builtins.str] = None,
            warning_foreground: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param accent: ``CfnTheme.UIColorPaletteProperty.Accent``.
            :param accent_foreground: ``CfnTheme.UIColorPaletteProperty.AccentForeground``.
            :param danger: ``CfnTheme.UIColorPaletteProperty.Danger``.
            :param danger_foreground: ``CfnTheme.UIColorPaletteProperty.DangerForeground``.
            :param dimension: ``CfnTheme.UIColorPaletteProperty.Dimension``.
            :param dimension_foreground: ``CfnTheme.UIColorPaletteProperty.DimensionForeground``.
            :param measure: ``CfnTheme.UIColorPaletteProperty.Measure``.
            :param measure_foreground: ``CfnTheme.UIColorPaletteProperty.MeasureForeground``.
            :param primary_background: ``CfnTheme.UIColorPaletteProperty.PrimaryBackground``.
            :param primary_foreground: ``CfnTheme.UIColorPaletteProperty.PrimaryForeground``.
            :param secondary_background: ``CfnTheme.UIColorPaletteProperty.SecondaryBackground``.
            :param secondary_foreground: ``CfnTheme.UIColorPaletteProperty.SecondaryForeground``.
            :param success: ``CfnTheme.UIColorPaletteProperty.Success``.
            :param success_foreground: ``CfnTheme.UIColorPaletteProperty.SuccessForeground``.
            :param warning: ``CfnTheme.UIColorPaletteProperty.Warning``.
            :param warning_foreground: ``CfnTheme.UIColorPaletteProperty.WarningForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if accent is not None:
                self._values["accent"] = accent
            if accent_foreground is not None:
                self._values["accent_foreground"] = accent_foreground
            if danger is not None:
                self._values["danger"] = danger
            if danger_foreground is not None:
                self._values["danger_foreground"] = danger_foreground
            if dimension is not None:
                self._values["dimension"] = dimension
            if dimension_foreground is not None:
                self._values["dimension_foreground"] = dimension_foreground
            if measure is not None:
                self._values["measure"] = measure
            if measure_foreground is not None:
                self._values["measure_foreground"] = measure_foreground
            if primary_background is not None:
                self._values["primary_background"] = primary_background
            if primary_foreground is not None:
                self._values["primary_foreground"] = primary_foreground
            if secondary_background is not None:
                self._values["secondary_background"] = secondary_background
            if secondary_foreground is not None:
                self._values["secondary_foreground"] = secondary_foreground
            if success is not None:
                self._values["success"] = success
            if success_foreground is not None:
                self._values["success_foreground"] = success_foreground
            if warning is not None:
                self._values["warning"] = warning
            if warning_foreground is not None:
                self._values["warning_foreground"] = warning_foreground

        @builtins.property
        def accent(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.Accent``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accent
            """
            result = self._values.get("accent")
            return result

        @builtins.property
        def accent_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.AccentForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accentforeground
            """
            result = self._values.get("accent_foreground")
            return result

        @builtins.property
        def danger(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.Danger``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-danger
            """
            result = self._values.get("danger")
            return result

        @builtins.property
        def danger_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.DangerForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dangerforeground
            """
            result = self._values.get("danger_foreground")
            return result

        @builtins.property
        def dimension(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.Dimension``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimension
            """
            result = self._values.get("dimension")
            return result

        @builtins.property
        def dimension_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.DimensionForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimensionforeground
            """
            result = self._values.get("dimension_foreground")
            return result

        @builtins.property
        def measure(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.Measure``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measure
            """
            result = self._values.get("measure")
            return result

        @builtins.property
        def measure_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.MeasureForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measureforeground
            """
            result = self._values.get("measure_foreground")
            return result

        @builtins.property
        def primary_background(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.PrimaryBackground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primarybackground
            """
            result = self._values.get("primary_background")
            return result

        @builtins.property
        def primary_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.PrimaryForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primaryforeground
            """
            result = self._values.get("primary_foreground")
            return result

        @builtins.property
        def secondary_background(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.SecondaryBackground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondarybackground
            """
            result = self._values.get("secondary_background")
            return result

        @builtins.property
        def secondary_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.SecondaryForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondaryforeground
            """
            result = self._values.get("secondary_foreground")
            return result

        @builtins.property
        def success(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.Success``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-success
            """
            result = self._values.get("success")
            return result

        @builtins.property
        def success_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.SuccessForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-successforeground
            """
            result = self._values.get("success_foreground")
            return result

        @builtins.property
        def warning(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.Warning``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warning
            """
            result = self._values.get("warning")
            return result

        @builtins.property
        def warning_foreground(self) -> typing.Optional[builtins.str]:
            """``CfnTheme.UIColorPaletteProperty.WarningForeground``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warningforeground
            """
            result = self._values.get("warning_foreground")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UIColorPaletteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_quicksight.CfnThemeProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "base_theme_id": "baseThemeId",
        "configuration": "configuration",
        "name": "name",
        "permissions": "permissions",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CfnThemeProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        base_theme_id: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[CfnTheme.ThemeConfigurationProperty, _IResolvable_a771d0ef]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTheme.ResourcePermissionProperty, _IResolvable_a771d0ef]]]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::QuickSight::Theme``.

        :param aws_account_id: ``AWS::QuickSight::Theme.AwsAccountId``.
        :param theme_id: ``AWS::QuickSight::Theme.ThemeId``.
        :param base_theme_id: ``AWS::QuickSight::Theme.BaseThemeId``.
        :param configuration: ``AWS::QuickSight::Theme.Configuration``.
        :param name: ``AWS::QuickSight::Theme.Name``.
        :param permissions: ``AWS::QuickSight::Theme.Permissions``.
        :param tags: ``AWS::QuickSight::Theme.Tags``.
        :param version_description: ``AWS::QuickSight::Theme.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if base_theme_id is not None:
            self._values["base_theme_id"] = base_theme_id
        if configuration is not None:
            self._values["configuration"] = configuration
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        """``AWS::QuickSight::Theme.AwsAccountId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-awsaccountid
        """
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return result

    @builtins.property
    def theme_id(self) -> builtins.str:
        """``AWS::QuickSight::Theme.ThemeId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-themeid
        """
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return result

    @builtins.property
    def base_theme_id(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Theme.BaseThemeId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-basethemeid
        """
        result = self._values.get("base_theme_id")
        return result

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnTheme.ThemeConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::QuickSight::Theme.Configuration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-configuration
        """
        result = self._values.get("configuration")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Theme.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTheme.ResourcePermissionProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::QuickSight::Theme.Permissions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-permissions
        """
        result = self._values.get("permissions")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::QuickSight::Theme.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        """``AWS::QuickSight::Theme.VersionDescription``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-versiondescription
        """
        result = self._values.get("version_description")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThemeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnalysis",
    "CfnAnalysisProps",
    "CfnDashboard",
    "CfnDashboardProps",
    "CfnTemplate",
    "CfnTemplateProps",
    "CfnTheme",
    "CfnThemeProps",
]

publication.publish()
