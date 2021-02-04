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
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnPipeline(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_datapipeline.CfnPipeline",
):
    """A CloudFormation ``AWS::DataPipeline::Pipeline``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html
    :cloudformationResource: AWS::DataPipeline::Pipeline
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        parameter_objects: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterObjectProperty", _IResolvable_a771d0ef]]],
        activate: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_values: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterValueProperty", _IResolvable_a771d0ef]]]] = None,
        pipeline_objects: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.PipelineObjectProperty", _IResolvable_a771d0ef]]]] = None,
        pipeline_tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.PipelineTagProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::DataPipeline::Pipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::DataPipeline::Pipeline.Name``.
        :param parameter_objects: ``AWS::DataPipeline::Pipeline.ParameterObjects``.
        :param activate: ``AWS::DataPipeline::Pipeline.Activate``.
        :param description: ``AWS::DataPipeline::Pipeline.Description``.
        :param parameter_values: ``AWS::DataPipeline::Pipeline.ParameterValues``.
        :param pipeline_objects: ``AWS::DataPipeline::Pipeline.PipelineObjects``.
        :param pipeline_tags: ``AWS::DataPipeline::Pipeline.PipelineTags``.
        """
        props = CfnPipelineProps(
            name=name,
            parameter_objects=parameter_objects,
            activate=activate,
            description=description,
            parameter_values=parameter_values,
            pipeline_objects=pipeline_objects,
            pipeline_tags=pipeline_tags,
        )

        jsii.create(CfnPipeline, self, [scope, id, props])

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
        """``AWS::DataPipeline::Pipeline.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameterObjects")
    def parameter_objects(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterObjectProperty", _IResolvable_a771d0ef]]]:
        """``AWS::DataPipeline::Pipeline.ParameterObjects``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-parameterobjects
        """
        return jsii.get(self, "parameterObjects")

    @parameter_objects.setter # type: ignore
    def parameter_objects(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterObjectProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "parameterObjects", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="activate")
    def activate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::DataPipeline::Pipeline.Activate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-activate
        """
        return jsii.get(self, "activate")

    @activate.setter # type: ignore
    def activate(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "activate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::DataPipeline::Pipeline.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameterValues")
    def parameter_values(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterValueProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::DataPipeline::Pipeline.ParameterValues``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-parametervalues
        """
        return jsii.get(self, "parameterValues")

    @parameter_values.setter # type: ignore
    def parameter_values(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterValueProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "parameterValues", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineObjects")
    def pipeline_objects(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.PipelineObjectProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::DataPipeline::Pipeline.PipelineObjects``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-pipelineobjects
        """
        return jsii.get(self, "pipelineObjects")

    @pipeline_objects.setter # type: ignore
    def pipeline_objects(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.PipelineObjectProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "pipelineObjects", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineTags")
    def pipeline_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.PipelineTagProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::DataPipeline::Pipeline.PipelineTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-pipelinetags
        """
        return jsii.get(self, "pipelineTags")

    @pipeline_tags.setter # type: ignore
    def pipeline_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.PipelineTagProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "pipelineTags", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_datapipeline.CfnPipeline.FieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key": "key",
            "ref_value": "refValue",
            "string_value": "stringValue",
        },
    )
    class FieldProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            ref_value: typing.Optional[builtins.str] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param key: ``CfnPipeline.FieldProperty.Key``.
            :param ref_value: ``CfnPipeline.FieldProperty.RefValue``.
            :param string_value: ``CfnPipeline.FieldProperty.StringValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects-fields.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
            }
            if ref_value is not None:
                self._values["ref_value"] = ref_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def key(self) -> builtins.str:
            """``CfnPipeline.FieldProperty.Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects-fields.html#cfn-datapipeline-pipeline-pipelineobjects-fields-key
            """
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return result

        @builtins.property
        def ref_value(self) -> typing.Optional[builtins.str]:
            """``CfnPipeline.FieldProperty.RefValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects-fields.html#cfn-datapipeline-pipeline-pipelineobjects-fields-refvalue
            """
            result = self._values.get("ref_value")
            return result

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            """``CfnPipeline.FieldProperty.StringValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects-fields.html#cfn-datapipeline-pipeline-pipelineobjects-fields-stringvalue
            """
            result = self._values.get("string_value")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_datapipeline.CfnPipeline.ParameterAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "string_value": "stringValue"},
    )
    class ParameterAttributeProperty:
        def __init__(self, *, key: builtins.str, string_value: builtins.str) -> None:
            """
            :param key: ``CfnPipeline.ParameterAttributeProperty.Key``.
            :param string_value: ``CfnPipeline.ParameterAttributeProperty.StringValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobjects-attributes.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "string_value": string_value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            """``CfnPipeline.ParameterAttributeProperty.Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobjects-attributes.html#cfn-datapipeline-pipeline-parameterobjects-attribtues-key
            """
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return result

        @builtins.property
        def string_value(self) -> builtins.str:
            """``CfnPipeline.ParameterAttributeProperty.StringValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobjects-attributes.html#cfn-datapipeline-pipeline-parameterobjects-attribtues-stringvalue
            """
            result = self._values.get("string_value")
            assert result is not None, "Required property 'string_value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_datapipeline.CfnPipeline.ParameterObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "id": "id"},
    )
    class ParameterObjectProperty:
        def __init__(
            self,
            *,
            attributes: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterAttributeProperty", _IResolvable_a771d0ef]]],
            id: builtins.str,
        ) -> None:
            """
            :param attributes: ``CfnPipeline.ParameterObjectProperty.Attributes``.
            :param id: ``CfnPipeline.ParameterObjectProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobjects.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "attributes": attributes,
                "id": id,
            }

        @builtins.property
        def attributes(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.ParameterAttributeProperty", _IResolvable_a771d0ef]]]:
            """``CfnPipeline.ParameterObjectProperty.Attributes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobjects.html#cfn-datapipeline-pipeline-parameterobjects-attributes
            """
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return result

        @builtins.property
        def id(self) -> builtins.str:
            """``CfnPipeline.ParameterObjectProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobjects.html#cfn-datapipeline-pipeline-parameterobjects-id
            """
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_datapipeline.CfnPipeline.ParameterValueProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "string_value": "stringValue"},
    )
    class ParameterValueProperty:
        def __init__(self, *, id: builtins.str, string_value: builtins.str) -> None:
            """
            :param id: ``CfnPipeline.ParameterValueProperty.Id``.
            :param string_value: ``CfnPipeline.ParameterValueProperty.StringValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalues.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
                "string_value": string_value,
            }

        @builtins.property
        def id(self) -> builtins.str:
            """``CfnPipeline.ParameterValueProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalues.html#cfn-datapipeline-pipeline-parametervalues-id
            """
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return result

        @builtins.property
        def string_value(self) -> builtins.str:
            """``CfnPipeline.ParameterValueProperty.StringValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalues.html#cfn-datapipeline-pipeline-parametervalues-stringvalue
            """
            result = self._values.get("string_value")
            assert result is not None, "Required property 'string_value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_datapipeline.CfnPipeline.PipelineObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"fields": "fields", "id": "id", "name": "name"},
    )
    class PipelineObjectProperty:
        def __init__(
            self,
            *,
            fields: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.FieldProperty", _IResolvable_a771d0ef]]],
            id: builtins.str,
            name: builtins.str,
        ) -> None:
            """
            :param fields: ``CfnPipeline.PipelineObjectProperty.Fields``.
            :param id: ``CfnPipeline.PipelineObjectProperty.Id``.
            :param name: ``CfnPipeline.PipelineObjectProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "fields": fields,
                "id": id,
                "name": name,
            }

        @builtins.property
        def fields(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnPipeline.FieldProperty", _IResolvable_a771d0ef]]]:
            """``CfnPipeline.PipelineObjectProperty.Fields``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects.html#cfn-datapipeline-pipeline-pipelineobjects-fields
            """
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return result

        @builtins.property
        def id(self) -> builtins.str:
            """``CfnPipeline.PipelineObjectProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects.html#cfn-datapipeline-pipeline-pipelineobjects-id
            """
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return result

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnPipeline.PipelineObjectProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobjects.html#cfn-datapipeline-pipeline-pipelineobjects-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipelineObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_datapipeline.CfnPipeline.PipelineTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class PipelineTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            """
            :param key: ``CfnPipeline.PipelineTagProperty.Key``.
            :param value: ``CfnPipeline.PipelineTagProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetags.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            """``CfnPipeline.PipelineTagProperty.Key``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetags.html#cfn-datapipeline-pipeline-pipelinetags-key
            """
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return result

        @builtins.property
        def value(self) -> builtins.str:
            """``CfnPipeline.PipelineTagProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetags.html#cfn-datapipeline-pipeline-pipelinetags-value
            """
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipelineTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_datapipeline.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "parameter_objects": "parameterObjects",
        "activate": "activate",
        "description": "description",
        "parameter_values": "parameterValues",
        "pipeline_objects": "pipelineObjects",
        "pipeline_tags": "pipelineTags",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        parameter_objects: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.ParameterObjectProperty, _IResolvable_a771d0ef]]],
        activate: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_values: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.ParameterValueProperty, _IResolvable_a771d0ef]]]] = None,
        pipeline_objects: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.PipelineObjectProperty, _IResolvable_a771d0ef]]]] = None,
        pipeline_tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.PipelineTagProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::DataPipeline::Pipeline``.

        :param name: ``AWS::DataPipeline::Pipeline.Name``.
        :param parameter_objects: ``AWS::DataPipeline::Pipeline.ParameterObjects``.
        :param activate: ``AWS::DataPipeline::Pipeline.Activate``.
        :param description: ``AWS::DataPipeline::Pipeline.Description``.
        :param parameter_values: ``AWS::DataPipeline::Pipeline.ParameterValues``.
        :param pipeline_objects: ``AWS::DataPipeline::Pipeline.PipelineObjects``.
        :param pipeline_tags: ``AWS::DataPipeline::Pipeline.PipelineTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "parameter_objects": parameter_objects,
        }
        if activate is not None:
            self._values["activate"] = activate
        if description is not None:
            self._values["description"] = description
        if parameter_values is not None:
            self._values["parameter_values"] = parameter_values
        if pipeline_objects is not None:
            self._values["pipeline_objects"] = pipeline_objects
        if pipeline_tags is not None:
            self._values["pipeline_tags"] = pipeline_tags

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::DataPipeline::Pipeline.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def parameter_objects(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.ParameterObjectProperty, _IResolvable_a771d0ef]]]:
        """``AWS::DataPipeline::Pipeline.ParameterObjects``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-parameterobjects
        """
        result = self._values.get("parameter_objects")
        assert result is not None, "Required property 'parameter_objects' is missing"
        return result

    @builtins.property
    def activate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::DataPipeline::Pipeline.Activate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-activate
        """
        result = self._values.get("activate")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::DataPipeline::Pipeline.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def parameter_values(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.ParameterValueProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::DataPipeline::Pipeline.ParameterValues``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-parametervalues
        """
        result = self._values.get("parameter_values")
        return result

    @builtins.property
    def pipeline_objects(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.PipelineObjectProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::DataPipeline::Pipeline.PipelineObjects``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-pipelineobjects
        """
        result = self._values.get("pipeline_objects")
        return result

    @builtins.property
    def pipeline_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnPipeline.PipelineTagProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::DataPipeline::Pipeline.PipelineTags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-pipelinetags
        """
        result = self._values.get("pipeline_tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPipeline",
    "CfnPipelineProps",
]

publication.publish()
