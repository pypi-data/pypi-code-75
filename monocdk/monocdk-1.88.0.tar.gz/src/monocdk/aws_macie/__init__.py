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
class CfnCustomDataIdentifier(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_macie.CfnCustomDataIdentifier",
):
    """A CloudFormation ``AWS::Macie::CustomDataIdentifier``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
    :cloudformationResource: AWS::Macie::CustomDataIdentifier
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.List[builtins.str]] = None,
        keywords: typing.Optional[typing.List[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::Macie::CustomDataIdentifier``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Macie::CustomDataIdentifier.Name``.
        :param regex: ``AWS::Macie::CustomDataIdentifier.Regex``.
        :param description: ``AWS::Macie::CustomDataIdentifier.Description``.
        :param ignore_words: ``AWS::Macie::CustomDataIdentifier.IgnoreWords``.
        :param keywords: ``AWS::Macie::CustomDataIdentifier.Keywords``.
        :param maximum_match_distance: ``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.
        """
        props = CfnCustomDataIdentifierProps(
            name=name,
            regex=regex,
            description=description,
            ignore_words=ignore_words,
            keywords=keywords,
            maximum_match_distance=maximum_match_distance,
        )

        jsii.create(CfnCustomDataIdentifier, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        """
        :cloudformationAttribute: CreatedAt
        """
        return jsii.get(self, "attrCreatedAt")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrDeleted")
    def attr_deleted(self) -> _IResolvable_a771d0ef:
        """
        :cloudformationAttribute: Deleted
        """
        return jsii.get(self, "attrDeleted")

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Macie::CustomDataIdentifier.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        """``AWS::Macie::CustomDataIdentifier.Regex``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        """
        return jsii.get(self, "regex")

    @regex.setter # type: ignore
    def regex(self, value: builtins.str) -> None:
        jsii.set(self, "regex", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::CustomDataIdentifier.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="ignoreWords")
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Macie::CustomDataIdentifier.IgnoreWords``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        """
        return jsii.get(self, "ignoreWords")

    @ignore_words.setter # type: ignore
    def ignore_words(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "ignoreWords", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="keywords")
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Macie::CustomDataIdentifier.Keywords``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        """
        return jsii.get(self, "keywords")

    @keywords.setter # type: ignore
    def keywords(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "keywords", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="maximumMatchDistance")
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        """``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        """
        return jsii.get(self, "maximumMatchDistance")

    @maximum_match_distance.setter # type: ignore
    def maximum_match_distance(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maximumMatchDistance", value)


@jsii.data_type(
    jsii_type="monocdk.aws_macie.CfnCustomDataIdentifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "regex": "regex",
        "description": "description",
        "ignore_words": "ignoreWords",
        "keywords": "keywords",
        "maximum_match_distance": "maximumMatchDistance",
    },
)
class CfnCustomDataIdentifierProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.List[builtins.str]] = None,
        keywords: typing.Optional[typing.List[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::Macie::CustomDataIdentifier``.

        :param name: ``AWS::Macie::CustomDataIdentifier.Name``.
        :param regex: ``AWS::Macie::CustomDataIdentifier.Regex``.
        :param description: ``AWS::Macie::CustomDataIdentifier.Description``.
        :param ignore_words: ``AWS::Macie::CustomDataIdentifier.IgnoreWords``.
        :param keywords: ``AWS::Macie::CustomDataIdentifier.Keywords``.
        :param maximum_match_distance: ``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "regex": regex,
        }
        if description is not None:
            self._values["description"] = description
        if ignore_words is not None:
            self._values["ignore_words"] = ignore_words
        if keywords is not None:
            self._values["keywords"] = keywords
        if maximum_match_distance is not None:
            self._values["maximum_match_distance"] = maximum_match_distance

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Macie::CustomDataIdentifier.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def regex(self) -> builtins.str:
        """``AWS::Macie::CustomDataIdentifier.Regex``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        """
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::CustomDataIdentifier.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Macie::CustomDataIdentifier.IgnoreWords``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        """
        result = self._values.get("ignore_words")
        return result

    @builtins.property
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        """``AWS::Macie::CustomDataIdentifier.Keywords``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        """
        result = self._values.get("keywords")
        return result

    @builtins.property
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        """``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        """
        result = self._values.get("maximum_match_distance")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomDataIdentifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnFindingsFilter(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_macie.CfnFindingsFilter",
):
    """A CloudFormation ``AWS::Macie::FindingsFilter``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
    :cloudformationResource: AWS::Macie::FindingsFilter
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        finding_criteria: typing.Union["CfnFindingsFilter.FindingCriteriaProperty", _IResolvable_a771d0ef],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::Macie::FindingsFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param finding_criteria: ``AWS::Macie::FindingsFilter.FindingCriteria``.
        :param name: ``AWS::Macie::FindingsFilter.Name``.
        :param action: ``AWS::Macie::FindingsFilter.Action``.
        :param description: ``AWS::Macie::FindingsFilter.Description``.
        :param position: ``AWS::Macie::FindingsFilter.Position``.
        """
        props = CfnFindingsFilterProps(
            finding_criteria=finding_criteria,
            name=name,
            action=action,
            description=description,
            position=position,
        )

        jsii.create(CfnFindingsFilter, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrFindingsFilterListItems")
    def attr_findings_filter_list_items(self) -> _IResolvable_a771d0ef:
        """
        :cloudformationAttribute: FindingsFilterListItems
        """
        return jsii.get(self, "attrFindingsFilterListItems")

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
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union["CfnFindingsFilter.FindingCriteriaProperty", _IResolvable_a771d0ef]:
        """``AWS::Macie::FindingsFilter.FindingCriteria``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        """
        return jsii.get(self, "findingCriteria")

    @finding_criteria.setter # type: ignore
    def finding_criteria(
        self,
        value: typing.Union["CfnFindingsFilter.FindingCriteriaProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "findingCriteria", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::Macie::FindingsFilter.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::FindingsFilter.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        """
        return jsii.get(self, "action")

    @action.setter # type: ignore
    def action(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::FindingsFilter.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="position")
    def position(self) -> typing.Optional[jsii.Number]:
        """``AWS::Macie::FindingsFilter.Position``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        """
        return jsii.get(self, "position")

    @position.setter # type: ignore
    def position(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "position", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_macie.CfnFindingsFilter.CriterionProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class CriterionProperty:
        def __init__(self) -> None:
            """
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterion.html
            """
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriterionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_macie.CfnFindingsFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Optional[typing.Union["CfnFindingsFilter.CriterionProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param criterion: ``CfnFindingsFilter.FindingCriteriaProperty.Criterion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion

        @builtins.property
        def criterion(
            self,
        ) -> typing.Optional[typing.Union["CfnFindingsFilter.CriterionProperty", _IResolvable_a771d0ef]]:
            """``CfnFindingsFilter.FindingCriteriaProperty.Criterion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion
            """
            result = self._values.get("criterion")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_macie.CfnFindingsFilter.FindingsFilterListItemProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "name": "name"},
    )
    class FindingsFilterListItemProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param id: ``CfnFindingsFilter.FindingsFilterListItemProperty.Id``.
            :param name: ``CfnFindingsFilter.FindingsFilterListItemProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            """``CfnFindingsFilter.FindingsFilterListItemProperty.Id``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-id
            """
            result = self._values.get("id")
            return result

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            """``CfnFindingsFilter.FindingsFilterListItemProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-name
            """
            result = self._values.get("name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingsFilterListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_macie.CfnFindingsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_criteria": "findingCriteria",
        "name": "name",
        "action": "action",
        "description": "description",
        "position": "position",
    },
)
class CfnFindingsFilterProps:
    def __init__(
        self,
        *,
        finding_criteria: typing.Union[CfnFindingsFilter.FindingCriteriaProperty, _IResolvable_a771d0ef],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::Macie::FindingsFilter``.

        :param finding_criteria: ``AWS::Macie::FindingsFilter.FindingCriteria``.
        :param name: ``AWS::Macie::FindingsFilter.Name``.
        :param action: ``AWS::Macie::FindingsFilter.Action``.
        :param description: ``AWS::Macie::FindingsFilter.Description``.
        :param position: ``AWS::Macie::FindingsFilter.Position``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "finding_criteria": finding_criteria,
            "name": name,
        }
        if action is not None:
            self._values["action"] = action
        if description is not None:
            self._values["description"] = description
        if position is not None:
            self._values["position"] = position

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[CfnFindingsFilter.FindingCriteriaProperty, _IResolvable_a771d0ef]:
        """``AWS::Macie::FindingsFilter.FindingCriteria``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        """
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::Macie::FindingsFilter.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::FindingsFilter.Action``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        """
        result = self._values.get("action")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::FindingsFilter.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def position(self) -> typing.Optional[jsii.Number]:
        """``AWS::Macie::FindingsFilter.Position``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        """
        result = self._values.get("position")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFindingsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnSession(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_macie.CfnSession",
):
    """A CloudFormation ``AWS::Macie::Session``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
    :cloudformationResource: AWS::Macie::Session
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::Macie::Session``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param finding_publishing_frequency: ``AWS::Macie::Session.FindingPublishingFrequency``.
        :param status: ``AWS::Macie::Session.Status``.
        """
        props = CfnSessionProps(
            finding_publishing_frequency=finding_publishing_frequency, status=status
        )

        jsii.create(CfnSession, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        """
        :cloudformationAttribute: AwsAccountId
        """
        return jsii.get(self, "attrAwsAccountId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrServiceRole")
    def attr_service_role(self) -> builtins.str:
        """
        :cloudformationAttribute: ServiceRole
        """
        return jsii.get(self, "attrServiceRole")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::Session.FindingPublishingFrequency``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        """
        return jsii.get(self, "findingPublishingFrequency")

    @finding_publishing_frequency.setter # type: ignore
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "findingPublishingFrequency", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::Session.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        """
        return jsii.get(self, "status")

    @status.setter # type: ignore
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="monocdk.aws_macie.CfnSessionProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_publishing_frequency": "findingPublishingFrequency",
        "status": "status",
    },
)
class CfnSessionProps:
    def __init__(
        self,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::Macie::Session``.

        :param finding_publishing_frequency: ``AWS::Macie::Session.FindingPublishingFrequency``.
        :param status: ``AWS::Macie::Session.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::Session.FindingPublishingFrequency``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        """
        result = self._values.get("finding_publishing_frequency")
        return result

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        """``AWS::Macie::Session.Status``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        """
        result = self._values.get("status")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSessionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCustomDataIdentifier",
    "CfnCustomDataIdentifierProps",
    "CfnFindingsFilter",
    "CfnFindingsFilterProps",
    "CfnSession",
    "CfnSessionProps",
]

publication.publish()
