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
class CfnDataCatalog(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_athena.CfnDataCatalog",
):
    """A CloudFormation ``AWS::Athena::DataCatalog``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
    :cloudformationResource: AWS::Athena::DataCatalog
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Create a new ``AWS::Athena::DataCatalog``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Athena::DataCatalog.Name``.
        :param type: ``AWS::Athena::DataCatalog.Type``.
        :param description: ``AWS::Athena::DataCatalog.Description``.
        :param parameters: ``AWS::Athena::DataCatalog.Parameters``.
        :param tags: ``AWS::Athena::DataCatalog.Tags``.
        """
        props = CfnDataCatalogProps(
            name=name,
            type=type,
            description=description,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(CfnDataCatalog, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::Athena::DataCatalog.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Athena::DataCatalog.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        """``AWS::Athena::DataCatalog.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type
        """
        return jsii.get(self, "type")

    @type.setter # type: ignore
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::DataCatalog.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
        """``AWS::Athena::DataCatalog.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters
        """
        return jsii.get(self, "parameters")

    @parameters.setter # type: ignore
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "parameters", value)


@jsii.data_type(
    jsii_type="monocdk.aws_athena.CfnDataCatalogProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "description": "description",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnDataCatalogProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Athena::DataCatalog``.

        :param name: ``AWS::Athena::DataCatalog.Name``.
        :param type: ``AWS::Athena::DataCatalog.Type``.
        :param description: ``AWS::Athena::DataCatalog.Description``.
        :param parameters: ``AWS::Athena::DataCatalog.Parameters``.
        :param tags: ``AWS::Athena::DataCatalog.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Athena::DataCatalog.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def type(self) -> builtins.str:
        """``AWS::Athena::DataCatalog.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::DataCatalog.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
        """``AWS::Athena::DataCatalog.Parameters``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters
        """
        result = self._values.get("parameters")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::Athena::DataCatalog.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags
        """
        result = self._values.get("tags")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCatalogProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnNamedQuery(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_athena.CfnNamedQuery",
):
    """A CloudFormation ``AWS::Athena::NamedQuery``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
    :cloudformationResource: AWS::Athena::NamedQuery
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        database: builtins.str,
        query_string: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        work_group: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Athena::NamedQuery``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database: ``AWS::Athena::NamedQuery.Database``.
        :param query_string: ``AWS::Athena::NamedQuery.QueryString``.
        :param description: ``AWS::Athena::NamedQuery.Description``.
        :param name: ``AWS::Athena::NamedQuery.Name``.
        :param work_group: ``AWS::Athena::NamedQuery.WorkGroup``.
        """
        props = CfnNamedQueryProps(
            database=database,
            query_string=query_string,
            description=description,
            name=name,
            work_group=work_group,
        )

        jsii.create(CfnNamedQuery, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrNamedQueryId")
    def attr_named_query_id(self) -> builtins.str:
        """
        :cloudformationAttribute: NamedQueryId
        """
        return jsii.get(self, "attrNamedQueryId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        """``AWS::Athena::NamedQuery.Database``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
        """
        return jsii.get(self, "database")

    @database.setter # type: ignore
    def database(self, value: builtins.str) -> None:
        jsii.set(self, "database", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        """``AWS::Athena::NamedQuery.QueryString``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
        """
        return jsii.get(self, "queryString")

    @query_string.setter # type: ignore
    def query_string(self, value: builtins.str) -> None:
        jsii.set(self, "queryString", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::NamedQuery.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::NamedQuery.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="workGroup")
    def work_group(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::NamedQuery.WorkGroup``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup
        """
        return jsii.get(self, "workGroup")

    @work_group.setter # type: ignore
    def work_group(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workGroup", value)


@jsii.data_type(
    jsii_type="monocdk.aws_athena.CfnNamedQueryProps",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "query_string": "queryString",
        "description": "description",
        "name": "name",
        "work_group": "workGroup",
    },
)
class CfnNamedQueryProps:
    def __init__(
        self,
        *,
        database: builtins.str,
        query_string: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        work_group: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Athena::NamedQuery``.

        :param database: ``AWS::Athena::NamedQuery.Database``.
        :param query_string: ``AWS::Athena::NamedQuery.QueryString``.
        :param description: ``AWS::Athena::NamedQuery.Description``.
        :param name: ``AWS::Athena::NamedQuery.Name``.
        :param work_group: ``AWS::Athena::NamedQuery.WorkGroup``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "query_string": query_string,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if work_group is not None:
            self._values["work_group"] = work_group

    @builtins.property
    def database(self) -> builtins.str:
        """``AWS::Athena::NamedQuery.Database``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
        """
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return result

    @builtins.property
    def query_string(self) -> builtins.str:
        """``AWS::Athena::NamedQuery.QueryString``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
        """
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::NamedQuery.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::NamedQuery.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def work_group(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::NamedQuery.WorkGroup``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup
        """
        result = self._values.get("work_group")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamedQueryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnWorkGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_athena.CfnWorkGroup",
):
    """A CloudFormation ``AWS::Athena::WorkGroup``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
    :cloudformationResource: AWS::Athena::WorkGroup
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        recursive_delete_option: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        work_group_configuration: typing.Optional[typing.Union["CfnWorkGroup.WorkGroupConfigurationProperty", _IResolvable_a771d0ef]] = None,
        work_group_configuration_updates: typing.Optional[typing.Union["CfnWorkGroup.WorkGroupConfigurationUpdatesProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::Athena::WorkGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Athena::WorkGroup.Name``.
        :param description: ``AWS::Athena::WorkGroup.Description``.
        :param recursive_delete_option: ``AWS::Athena::WorkGroup.RecursiveDeleteOption``.
        :param state: ``AWS::Athena::WorkGroup.State``.
        :param tags: ``AWS::Athena::WorkGroup.Tags``.
        :param work_group_configuration: ``AWS::Athena::WorkGroup.WorkGroupConfiguration``.
        :param work_group_configuration_updates: ``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.
        """
        props = CfnWorkGroupProps(
            name=name,
            description=description,
            recursive_delete_option=recursive_delete_option,
            state=state,
            tags=tags,
            work_group_configuration=work_group_configuration,
            work_group_configuration_updates=work_group_configuration_updates,
        )

        jsii.create(CfnWorkGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        """
        :cloudformationAttribute: CreationTime
        """
        return jsii.get(self, "attrCreationTime")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::Athena::WorkGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Athena::WorkGroup.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::WorkGroup.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="recursiveDeleteOption")
    def recursive_delete_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Athena::WorkGroup.RecursiveDeleteOption``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        """
        return jsii.get(self, "recursiveDeleteOption")

    @recursive_delete_option.setter # type: ignore
    def recursive_delete_option(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "recursiveDeleteOption", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::WorkGroup.State``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        """
        return jsii.get(self, "state")

    @state.setter # type: ignore
    def state(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "state", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="workGroupConfiguration")
    def work_group_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnWorkGroup.WorkGroupConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::Athena::WorkGroup.WorkGroupConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        """
        return jsii.get(self, "workGroupConfiguration")

    @work_group_configuration.setter # type: ignore
    def work_group_configuration(
        self,
        value: typing.Optional[typing.Union["CfnWorkGroup.WorkGroupConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "workGroupConfiguration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union["CfnWorkGroup.WorkGroupConfigurationUpdatesProperty", _IResolvable_a771d0ef]]:
        """``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        """
        return jsii.get(self, "workGroupConfigurationUpdates")

    @work_group_configuration_updates.setter # type: ignore
    def work_group_configuration_updates(
        self,
        value: typing.Optional[typing.Union["CfnWorkGroup.WorkGroupConfigurationUpdatesProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "workGroupConfigurationUpdates", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_athena.CfnWorkGroup.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_option": "encryptionOption", "kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_option: builtins.str,
            kms_key: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param encryption_option: ``CfnWorkGroup.EncryptionConfigurationProperty.EncryptionOption``.
            :param kms_key: ``CfnWorkGroup.EncryptionConfigurationProperty.KmsKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "encryption_option": encryption_option,
            }
            if kms_key is not None:
                self._values["kms_key"] = kms_key

        @builtins.property
        def encryption_option(self) -> builtins.str:
            """``CfnWorkGroup.EncryptionConfigurationProperty.EncryptionOption``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-encryptionoption
            """
            result = self._values.get("encryption_option")
            assert result is not None, "Required property 'encryption_option' is missing"
            return result

        @builtins.property
        def kms_key(self) -> typing.Optional[builtins.str]:
            """``CfnWorkGroup.EncryptionConfigurationProperty.KmsKey``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-kmskey
            """
            result = self._values.get("kms_key")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_athena.CfnWorkGroup.ResultConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration": "encryptionConfiguration",
            "output_location": "outputLocation",
        },
    )
    class ResultConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_configuration: typing.Optional[typing.Union["CfnWorkGroup.EncryptionConfigurationProperty", _IResolvable_a771d0ef]] = None,
            output_location: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param encryption_configuration: ``CfnWorkGroup.ResultConfigurationProperty.EncryptionConfiguration``.
            :param output_location: ``CfnWorkGroup.ResultConfigurationProperty.OutputLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if output_location is not None:
                self._values["output_location"] = output_location

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnWorkGroup.EncryptionConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.ResultConfigurationProperty.EncryptionConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-encryptionconfiguration
            """
            result = self._values.get("encryption_configuration")
            return result

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            """``CfnWorkGroup.ResultConfigurationProperty.OutputLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation
            """
            result = self._values.get("output_location")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResultConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_athena.CfnWorkGroup.ResultConfigurationUpdatesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration": "encryptionConfiguration",
            "output_location": "outputLocation",
            "remove_encryption_configuration": "removeEncryptionConfiguration",
            "remove_output_location": "removeOutputLocation",
        },
    )
    class ResultConfigurationUpdatesProperty:
        def __init__(
            self,
            *,
            encryption_configuration: typing.Optional[typing.Union["CfnWorkGroup.EncryptionConfigurationProperty", _IResolvable_a771d0ef]] = None,
            output_location: typing.Optional[builtins.str] = None,
            remove_encryption_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            remove_output_location: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param encryption_configuration: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.EncryptionConfiguration``.
            :param output_location: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.OutputLocation``.
            :param remove_encryption_configuration: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveEncryptionConfiguration``.
            :param remove_output_location: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveOutputLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if output_location is not None:
                self._values["output_location"] = output_location
            if remove_encryption_configuration is not None:
                self._values["remove_encryption_configuration"] = remove_encryption_configuration
            if remove_output_location is not None:
                self._values["remove_output_location"] = remove_output_location

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnWorkGroup.EncryptionConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.ResultConfigurationUpdatesProperty.EncryptionConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration
            """
            result = self._values.get("encryption_configuration")
            return result

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            """``CfnWorkGroup.ResultConfigurationUpdatesProperty.OutputLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-outputlocation
            """
            result = self._values.get("output_location")
            return result

        @builtins.property
        def remove_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveEncryptionConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration
            """
            result = self._values.get("remove_encryption_configuration")
            return result

        @builtins.property
        def remove_output_location(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveOutputLocation``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation
            """
            result = self._values.get("remove_output_location")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResultConfigurationUpdatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_athena.CfnWorkGroup.WorkGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bytes_scanned_cutoff_per_query": "bytesScannedCutoffPerQuery",
            "enforce_work_group_configuration": "enforceWorkGroupConfiguration",
            "publish_cloud_watch_metrics_enabled": "publishCloudWatchMetricsEnabled",
            "requester_pays_enabled": "requesterPaysEnabled",
            "result_configuration": "resultConfiguration",
        },
    )
    class WorkGroupConfigurationProperty:
        def __init__(
            self,
            *,
            bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
            enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            result_configuration: typing.Optional[typing.Union["CfnWorkGroup.ResultConfigurationProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param bytes_scanned_cutoff_per_query: ``CfnWorkGroup.WorkGroupConfigurationProperty.BytesScannedCutoffPerQuery``.
            :param enforce_work_group_configuration: ``CfnWorkGroup.WorkGroupConfigurationProperty.EnforceWorkGroupConfiguration``.
            :param publish_cloud_watch_metrics_enabled: ``CfnWorkGroup.WorkGroupConfigurationProperty.PublishCloudWatchMetricsEnabled``.
            :param requester_pays_enabled: ``CfnWorkGroup.WorkGroupConfigurationProperty.RequesterPaysEnabled``.
            :param result_configuration: ``CfnWorkGroup.WorkGroupConfigurationProperty.ResultConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if bytes_scanned_cutoff_per_query is not None:
                self._values["bytes_scanned_cutoff_per_query"] = bytes_scanned_cutoff_per_query
            if enforce_work_group_configuration is not None:
                self._values["enforce_work_group_configuration"] = enforce_work_group_configuration
            if publish_cloud_watch_metrics_enabled is not None:
                self._values["publish_cloud_watch_metrics_enabled"] = publish_cloud_watch_metrics_enabled
            if requester_pays_enabled is not None:
                self._values["requester_pays_enabled"] = requester_pays_enabled
            if result_configuration is not None:
                self._values["result_configuration"] = result_configuration

        @builtins.property
        def bytes_scanned_cutoff_per_query(self) -> typing.Optional[jsii.Number]:
            """``CfnWorkGroup.WorkGroupConfigurationProperty.BytesScannedCutoffPerQuery``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-bytesscannedcutoffperquery
            """
            result = self._values.get("bytes_scanned_cutoff_per_query")
            return result

        @builtins.property
        def enforce_work_group_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationProperty.EnforceWorkGroupConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration
            """
            result = self._values.get("enforce_work_group_configuration")
            return result

        @builtins.property
        def publish_cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationProperty.PublishCloudWatchMetricsEnabled``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-publishcloudwatchmetricsenabled
            """
            result = self._values.get("publish_cloud_watch_metrics_enabled")
            return result

        @builtins.property
        def requester_pays_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationProperty.RequesterPaysEnabled``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-requesterpaysenabled
            """
            result = self._values.get("requester_pays_enabled")
            return result

        @builtins.property
        def result_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnWorkGroup.ResultConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationProperty.ResultConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-resultconfiguration
            """
            result = self._values.get("result_configuration")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_athena.CfnWorkGroup.WorkGroupConfigurationUpdatesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bytes_scanned_cutoff_per_query": "bytesScannedCutoffPerQuery",
            "enforce_work_group_configuration": "enforceWorkGroupConfiguration",
            "publish_cloud_watch_metrics_enabled": "publishCloudWatchMetricsEnabled",
            "remove_bytes_scanned_cutoff_per_query": "removeBytesScannedCutoffPerQuery",
            "requester_pays_enabled": "requesterPaysEnabled",
            "result_configuration_updates": "resultConfigurationUpdates",
        },
    )
    class WorkGroupConfigurationUpdatesProperty:
        def __init__(
            self,
            *,
            bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
            enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            remove_bytes_scanned_cutoff_per_query: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            result_configuration_updates: typing.Optional[typing.Union["CfnWorkGroup.ResultConfigurationUpdatesProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param bytes_scanned_cutoff_per_query: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.BytesScannedCutoffPerQuery``.
            :param enforce_work_group_configuration: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.EnforceWorkGroupConfiguration``.
            :param publish_cloud_watch_metrics_enabled: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.PublishCloudWatchMetricsEnabled``.
            :param remove_bytes_scanned_cutoff_per_query: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RemoveBytesScannedCutoffPerQuery``.
            :param requester_pays_enabled: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RequesterPaysEnabled``.
            :param result_configuration_updates: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.ResultConfigurationUpdates``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if bytes_scanned_cutoff_per_query is not None:
                self._values["bytes_scanned_cutoff_per_query"] = bytes_scanned_cutoff_per_query
            if enforce_work_group_configuration is not None:
                self._values["enforce_work_group_configuration"] = enforce_work_group_configuration
            if publish_cloud_watch_metrics_enabled is not None:
                self._values["publish_cloud_watch_metrics_enabled"] = publish_cloud_watch_metrics_enabled
            if remove_bytes_scanned_cutoff_per_query is not None:
                self._values["remove_bytes_scanned_cutoff_per_query"] = remove_bytes_scanned_cutoff_per_query
            if requester_pays_enabled is not None:
                self._values["requester_pays_enabled"] = requester_pays_enabled
            if result_configuration_updates is not None:
                self._values["result_configuration_updates"] = result_configuration_updates

        @builtins.property
        def bytes_scanned_cutoff_per_query(self) -> typing.Optional[jsii.Number]:
            """``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.BytesScannedCutoffPerQuery``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-bytesscannedcutoffperquery
            """
            result = self._values.get("bytes_scanned_cutoff_per_query")
            return result

        @builtins.property
        def enforce_work_group_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.EnforceWorkGroupConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-enforceworkgroupconfiguration
            """
            result = self._values.get("enforce_work_group_configuration")
            return result

        @builtins.property
        def publish_cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.PublishCloudWatchMetricsEnabled``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-publishcloudwatchmetricsenabled
            """
            result = self._values.get("publish_cloud_watch_metrics_enabled")
            return result

        @builtins.property
        def remove_bytes_scanned_cutoff_per_query(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RemoveBytesScannedCutoffPerQuery``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-removebytesscannedcutoffperquery
            """
            result = self._values.get("remove_bytes_scanned_cutoff_per_query")
            return result

        @builtins.property
        def requester_pays_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RequesterPaysEnabled``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-requesterpaysenabled
            """
            result = self._values.get("requester_pays_enabled")
            return result

        @builtins.property
        def result_configuration_updates(
            self,
        ) -> typing.Optional[typing.Union["CfnWorkGroup.ResultConfigurationUpdatesProperty", _IResolvable_a771d0ef]]:
            """``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.ResultConfigurationUpdates``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-resultconfigurationupdates
            """
            result = self._values.get("result_configuration_updates")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkGroupConfigurationUpdatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_athena.CfnWorkGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "recursive_delete_option": "recursiveDeleteOption",
        "state": "state",
        "tags": "tags",
        "work_group_configuration": "workGroupConfiguration",
        "work_group_configuration_updates": "workGroupConfigurationUpdates",
    },
)
class CfnWorkGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        recursive_delete_option: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.List[_CfnTag_95fbdc29]] = None,
        work_group_configuration: typing.Optional[typing.Union[CfnWorkGroup.WorkGroupConfigurationProperty, _IResolvable_a771d0ef]] = None,
        work_group_configuration_updates: typing.Optional[typing.Union[CfnWorkGroup.WorkGroupConfigurationUpdatesProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Athena::WorkGroup``.

        :param name: ``AWS::Athena::WorkGroup.Name``.
        :param description: ``AWS::Athena::WorkGroup.Description``.
        :param recursive_delete_option: ``AWS::Athena::WorkGroup.RecursiveDeleteOption``.
        :param state: ``AWS::Athena::WorkGroup.State``.
        :param tags: ``AWS::Athena::WorkGroup.Tags``.
        :param work_group_configuration: ``AWS::Athena::WorkGroup.WorkGroupConfiguration``.
        :param work_group_configuration_updates: ``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if recursive_delete_option is not None:
            self._values["recursive_delete_option"] = recursive_delete_option
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if work_group_configuration is not None:
            self._values["work_group_configuration"] = work_group_configuration
        if work_group_configuration_updates is not None:
            self._values["work_group_configuration_updates"] = work_group_configuration_updates

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Athena::WorkGroup.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::WorkGroup.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def recursive_delete_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::Athena::WorkGroup.RecursiveDeleteOption``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        """
        result = self._values.get("recursive_delete_option")
        return result

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        """``AWS::Athena::WorkGroup.State``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        """
        result = self._values.get("state")
        return result

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        """``AWS::Athena::WorkGroup.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def work_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnWorkGroup.WorkGroupConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::Athena::WorkGroup.WorkGroupConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        """
        result = self._values.get("work_group_configuration")
        return result

    @builtins.property
    def work_group_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[CfnWorkGroup.WorkGroupConfigurationUpdatesProperty, _IResolvable_a771d0ef]]:
        """``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        """
        result = self._values.get("work_group_configuration_updates")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataCatalog",
    "CfnDataCatalogProps",
    "CfnNamedQuery",
    "CfnNamedQueryProps",
    "CfnWorkGroup",
    "CfnWorkGroupProps",
]

publication.publish()
