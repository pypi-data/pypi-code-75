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
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_cloudwatch import Alarm as _Alarm_a55fe34b, IMetric as _IMetric_5db43d61
from ..aws_iam import (
    IRole as _IRole_59af6f50, PolicyStatement as _PolicyStatement_296fe8a3
)


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.AdjustmentTier",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "lower_bound": "lowerBound",
        "upper_bound": "upperBound",
    },
)
class AdjustmentTier:
    def __init__(
        self,
        *,
        adjustment: jsii.Number,
        lower_bound: typing.Optional[jsii.Number] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) An adjustment.

        :param adjustment: (experimental) What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
        :param lower_bound: (experimental) Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        :param upper_bound: (experimental) Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "adjustment": adjustment,
        }
        if lower_bound is not None:
            self._values["lower_bound"] = lower_bound
        if upper_bound is not None:
            self._values["upper_bound"] = upper_bound

    @builtins.property
    def adjustment(self) -> jsii.Number:
        """(experimental) What number to adjust the capacity with.

        The number is interpeted as an added capacity, a new fixed capacity or an
        added percentage depending on the AdjustmentType value of the
        StepScalingPolicy.

        Can be positive or negative.

        :stability: experimental
        """
        result = self._values.get("adjustment")
        assert result is not None, "Required property 'adjustment' is missing"
        return result

    @builtins.property
    def lower_bound(self) -> typing.Optional[jsii.Number]:
        """(experimental) Lower bound where this scaling tier applies.

        The scaling tier applies if the difference between the metric
        value and its alarm threshold is higher than this value.

        :default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier

        :stability: experimental
        """
        result = self._values.get("lower_bound")
        return result

    @builtins.property
    def upper_bound(self) -> typing.Optional[jsii.Number]:
        """(experimental) Upper bound where this scaling tier applies.

        The scaling tier applies if the difference between the metric
        value and its alarm threshold is lower than this value.

        :default: +Infinity

        :stability: experimental
        """
        result = self._values.get("upper_bound")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdjustmentTier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.AdjustmentType")
class AdjustmentType(enum.Enum):
    """(experimental) How adjustment numbers are interpreted.

    :stability: experimental
    """

    CHANGE_IN_CAPACITY = "CHANGE_IN_CAPACITY"
    """(experimental) Add the adjustment number to the current capacity.

    A positive number increases capacity, a negative number decreases capacity.

    :stability: experimental
    """
    PERCENT_CHANGE_IN_CAPACITY = "PERCENT_CHANGE_IN_CAPACITY"
    """(experimental) Add this percentage of the current capacity to itself.

    The number must be between -100 and 100; a positive number increases
    capacity and a negative number decreases it.

    :stability: experimental
    """
    EXACT_CAPACITY = "EXACT_CAPACITY"
    """(experimental) Make the capacity equal to the exact number given.

    :stability: experimental
    """


class BaseScalableAttribute(
    _Construct_e78e779f,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_applicationautoscaling.BaseScalableAttribute",
):
    """(experimental) Represent an attribute for which autoscaling can be configured.

    This class is basically a light wrapper around ScalableTarget, but with
    all methods protected instead of public so they can be selectively
    exposed and/or more specific versions of them can be exposed by derived
    classes for individual services support autoscaling.

    Typical use cases:

    - Hide away the PredefinedMetric enum for target tracking policies.
    - Don't expose all scaling methods (for example Dynamo tables don't support
      Step Scaling, so the Dynamo subclass won't expose this method).

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _BaseScalableAttributeProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: _IRole_59af6f50,
        service_namespace: "ServiceNamespace",
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param dimension: (experimental) Scalable dimension of the attribute.
        :param resource_id: (experimental) Resource ID of the attribute.
        :param role: (experimental) Role to use for scaling.
        :param service_namespace: (experimental) Service namespace of the scalable attribute.
        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1

        :stability: experimental
        """
        props = BaseScalableAttributeProps(
            dimension=dimension,
            resource_id=resource_id,
            role=role,
            service_namespace=service_namespace,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
        )

        jsii.create(BaseScalableAttribute, self, [scope, id, props])

    @jsii.member(jsii_name="doScaleOnMetric")
    def _do_scale_on_metric(
        self,
        id: builtins.str,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.List["ScalingInterval"],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Scale out or in based on a metric value.

        :param id: -
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        """
        props = BasicStepScalingPolicyProps(
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        return jsii.invoke(self, "doScaleOnMetric", [id, props])

    @jsii.member(jsii_name="doScaleOnSchedule")
    def _do_scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        """(experimental) Scale out or in based on time.

        :param id: -
        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        """
        props = ScalingSchedule(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
        )

        return jsii.invoke(self, "doScaleOnSchedule", [id, props])

    @jsii.member(jsii_name="doScaleToTrackMetric")
    def _do_scale_to_track_metric(
        self,
        id: builtins.str,
        *,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional["PredefinedMetric"] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Scale out or in in order to keep a metric around a target value.

        :param id: -
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Default: - No resource label.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        """
        props = BasicTargetTrackingScalingPolicyProps(
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return jsii.invoke(self, "doScaleToTrackMetric", [id, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="props")
    def _props(self) -> "BaseScalableAttributeProps":
        """
        :stability: experimental
        """
        return jsii.get(self, "props")


class _BaseScalableAttributeProxy(BaseScalableAttribute):
    pass


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BaseTargetTrackingProps",
    jsii_struct_bases=[],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
    },
)
class BaseTargetTrackingProps:
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """(experimental) Base interface for target tracking props.

        Contains the attributes that are common to target tracking policies,
        except the ones relating to the metric and to the scalable target.

        This interface is reused by more specific target tracking props objects
        in other services.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseTargetTrackingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BasicStepScalingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric": "metric",
        "scaling_steps": "scalingSteps",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
    },
)
class BasicStepScalingPolicyProps:
    def __init__(
        self,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.List["ScalingInterval"],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "scaling_steps": scaling_steps,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude

    @builtins.property
    def metric(self) -> _IMetric_5db43d61:
        """(experimental) Metric to scale on.

        :stability: experimental
        """
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return result

    @builtins.property
    def scaling_steps(self) -> typing.List["ScalingInterval"]:
        """(experimental) The intervals for scaling.

        Maps a range of metric values to a particular scaling behavior.

        :stability: experimental
        """
        result = self._values.get("scaling_steps")
        assert result is not None, "Required property 'scaling_steps' is missing"
        return result

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        """(experimental) How the adjustment numbers inside 'intervals' are interpreted.

        :default: ChangeInCapacity

        :stability: experimental
        """
        result = self._values.get("adjustment_type")
        return result

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) Grace period after scaling activity.

        Subsequent scale outs during the cooldown period are squashed so that only
        the biggest scale out happens.

        Subsequent scale ins during the cooldown period are ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        :stability: experimental
        """
        result = self._values.get("cooldown")
        return result

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        """(experimental) Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect

        :stability: experimental
        """
        result = self._values.get("min_adjustment_magnitude")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicStepScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BasicTargetTrackingScalingPolicyProps",
    jsii_struct_bases=[BaseTargetTrackingProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_value": "targetValue",
        "custom_metric": "customMetric",
        "predefined_metric": "predefinedMetric",
        "resource_label": "resourceLabel",
    },
)
class BasicTargetTrackingScalingPolicyProps(BaseTargetTrackingProps):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional["PredefinedMetric"] = None,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for a Target Tracking policy that include the metric but exclude the target.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Default: - No resource label.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if predefined_metric is not None:
            self._values["predefined_metric"] = predefined_metric
        if resource_label is not None:
            self._values["resource_label"] = resource_label

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
    def target_value(self) -> jsii.Number:
        """(experimental) The target value for the metric.

        :stability: experimental
        """
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return result

    @builtins.property
    def custom_metric(self) -> typing.Optional[_IMetric_5db43d61]:
        """(experimental) A custom metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No custom metric.

        :stability: experimental
        """
        result = self._values.get("custom_metric")
        return result

    @builtins.property
    def predefined_metric(self) -> typing.Optional["PredefinedMetric"]:
        """(experimental) A predefined metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No predefined metrics.

        :stability: experimental
        """
        result = self._values.get("predefined_metric")
        return result

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        """(experimental) Identify the resource associated with the metric type.

        Only used for predefined metric ALBRequestCountPerTarget.

        :default: - No resource label.

        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            app / <load-balancer - name > /<load-balancer-id>/targetgroup / <target-group - name > /<target-group-id>
        """
        result = self._values.get("resource_label")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicTargetTrackingScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnScalableTarget(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget",
):
    """A CloudFormation ``AWS::ApplicationAutoScaling::ScalableTarget``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
    :cloudformationResource: AWS::ApplicationAutoScaling::ScalableTarget
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        role_arn: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        scheduled_actions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]] = None,
        suspended_state: typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::ApplicationAutoScaling::ScalableTarget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param max_capacity: ``AWS::ApplicationAutoScaling::ScalableTarget.MaxCapacity``.
        :param min_capacity: ``AWS::ApplicationAutoScaling::ScalableTarget.MinCapacity``.
        :param resource_id: ``AWS::ApplicationAutoScaling::ScalableTarget.ResourceId``.
        :param role_arn: ``AWS::ApplicationAutoScaling::ScalableTarget.RoleARN``.
        :param scalable_dimension: ``AWS::ApplicationAutoScaling::ScalableTarget.ScalableDimension``.
        :param service_namespace: ``AWS::ApplicationAutoScaling::ScalableTarget.ServiceNamespace``.
        :param scheduled_actions: ``AWS::ApplicationAutoScaling::ScalableTarget.ScheduledActions``.
        :param suspended_state: ``AWS::ApplicationAutoScaling::ScalableTarget.SuspendedState``.
        """
        props = CfnScalableTargetProps(
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            resource_id=resource_id,
            role_arn=role_arn,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            scheduled_actions=scheduled_actions,
            suspended_state=suspended_state,
        )

        jsii.create(CfnScalableTarget, self, [scope, id, props])

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
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        """``AWS::ApplicationAutoScaling::ScalableTarget.MaxCapacity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity
        """
        return jsii.get(self, "maxCapacity")

    @max_capacity.setter # type: ignore
    def max_capacity(self, value: jsii.Number) -> None:
        jsii.set(self, "maxCapacity", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        """``AWS::ApplicationAutoScaling::ScalableTarget.MinCapacity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity
        """
        return jsii.get(self, "minCapacity")

    @min_capacity.setter # type: ignore
    def min_capacity(self, value: jsii.Number) -> None:
        jsii.set(self, "minCapacity", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ResourceId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid
        """
        return jsii.get(self, "resourceId")

    @resource_id.setter # type: ignore
    def resource_id(self, value: builtins.str) -> None:
        jsii.set(self, "resourceId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.RoleARN``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter # type: ignore
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ScalableDimension``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension
        """
        return jsii.get(self, "scalableDimension")

    @scalable_dimension.setter # type: ignore
    def scalable_dimension(self, value: builtins.str) -> None:
        jsii.set(self, "scalableDimension", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ServiceNamespace``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace
        """
        return jsii.get(self, "serviceNamespace")

    @service_namespace.setter # type: ignore
    def service_namespace(self, value: builtins.str) -> None:
        jsii.set(self, "serviceNamespace", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scheduledActions")
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ScheduledActions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions
        """
        return jsii.get(self, "scheduledActions")

    @scheduled_actions.setter # type: ignore
    def scheduled_actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "scheduledActions", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="suspendedState")
    def suspended_state(
        self,
    ) -> typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]]:
        """``AWS::ApplicationAutoScaling::ScalableTarget.SuspendedState``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate
        """
        return jsii.get(self, "suspendedState")

    @suspended_state.setter # type: ignore
    def suspended_state(
        self,
        value: typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "suspendedState", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalableTargetActionProperty:
        def __init__(
            self,
            *,
            max_capacity: typing.Optional[jsii.Number] = None,
            min_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param max_capacity: ``CfnScalableTarget.ScalableTargetActionProperty.MaxCapacity``.
            :param min_capacity: ``CfnScalableTarget.ScalableTargetActionProperty.MinCapacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if max_capacity is not None:
                self._values["max_capacity"] = max_capacity
            if min_capacity is not None:
                self._values["min_capacity"] = min_capacity

        @builtins.property
        def max_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnScalableTarget.ScalableTargetActionProperty.MaxCapacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity
            """
            result = self._values.get("max_capacity")
            return result

        @builtins.property
        def min_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnScalableTarget.ScalableTargetActionProperty.MinCapacity``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity
            """
            result = self._values.get("min_capacity")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalableTargetActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget.ScheduledActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule": "schedule",
            "scheduled_action_name": "scheduledActionName",
            "end_time": "endTime",
            "scalable_target_action": "scalableTargetAction",
            "start_time": "startTime",
        },
    )
    class ScheduledActionProperty:
        def __init__(
            self,
            *,
            schedule: builtins.str,
            scheduled_action_name: builtins.str,
            end_time: typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]] = None,
            scalable_target_action: typing.Optional[typing.Union["CfnScalableTarget.ScalableTargetActionProperty", _IResolvable_a771d0ef]] = None,
            start_time: typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]] = None,
        ) -> None:
            """
            :param schedule: ``CfnScalableTarget.ScheduledActionProperty.Schedule``.
            :param scheduled_action_name: ``CfnScalableTarget.ScheduledActionProperty.ScheduledActionName``.
            :param end_time: ``CfnScalableTarget.ScheduledActionProperty.EndTime``.
            :param scalable_target_action: ``CfnScalableTarget.ScheduledActionProperty.ScalableTargetAction``.
            :param start_time: ``CfnScalableTarget.ScheduledActionProperty.StartTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "schedule": schedule,
                "scheduled_action_name": scheduled_action_name,
            }
            if end_time is not None:
                self._values["end_time"] = end_time
            if scalable_target_action is not None:
                self._values["scalable_target_action"] = scalable_target_action
            if start_time is not None:
                self._values["start_time"] = start_time

        @builtins.property
        def schedule(self) -> builtins.str:
            """``CfnScalableTarget.ScheduledActionProperty.Schedule``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-schedule
            """
            result = self._values.get("schedule")
            assert result is not None, "Required property 'schedule' is missing"
            return result

        @builtins.property
        def scheduled_action_name(self) -> builtins.str:
            """``CfnScalableTarget.ScheduledActionProperty.ScheduledActionName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scheduledactionname
            """
            result = self._values.get("scheduled_action_name")
            assert result is not None, "Required property 'scheduled_action_name' is missing"
            return result

        @builtins.property
        def end_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]]:
            """``CfnScalableTarget.ScheduledActionProperty.EndTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-endtime
            """
            result = self._values.get("end_time")
            return result

        @builtins.property
        def scalable_target_action(
            self,
        ) -> typing.Optional[typing.Union["CfnScalableTarget.ScalableTargetActionProperty", _IResolvable_a771d0ef]]:
            """``CfnScalableTarget.ScheduledActionProperty.ScalableTargetAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scalabletargetaction
            """
            result = self._values.get("scalable_target_action")
            return result

        @builtins.property
        def start_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]]:
            """``CfnScalableTarget.ScheduledActionProperty.StartTime``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-starttime
            """
            result = self._values.get("start_time")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget.SuspendedStateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dynamic_scaling_in_suspended": "dynamicScalingInSuspended",
            "dynamic_scaling_out_suspended": "dynamicScalingOutSuspended",
            "scheduled_scaling_suspended": "scheduledScalingSuspended",
        },
    )
    class SuspendedStateProperty:
        def __init__(
            self,
            *,
            dynamic_scaling_in_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            dynamic_scaling_out_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            scheduled_scaling_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param dynamic_scaling_in_suspended: ``CfnScalableTarget.SuspendedStateProperty.DynamicScalingInSuspended``.
            :param dynamic_scaling_out_suspended: ``CfnScalableTarget.SuspendedStateProperty.DynamicScalingOutSuspended``.
            :param scheduled_scaling_suspended: ``CfnScalableTarget.SuspendedStateProperty.ScheduledScalingSuspended``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if dynamic_scaling_in_suspended is not None:
                self._values["dynamic_scaling_in_suspended"] = dynamic_scaling_in_suspended
            if dynamic_scaling_out_suspended is not None:
                self._values["dynamic_scaling_out_suspended"] = dynamic_scaling_out_suspended
            if scheduled_scaling_suspended is not None:
                self._values["scheduled_scaling_suspended"] = scheduled_scaling_suspended

        @builtins.property
        def dynamic_scaling_in_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnScalableTarget.SuspendedStateProperty.DynamicScalingInSuspended``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalinginsuspended
            """
            result = self._values.get("dynamic_scaling_in_suspended")
            return result

        @builtins.property
        def dynamic_scaling_out_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnScalableTarget.SuspendedStateProperty.DynamicScalingOutSuspended``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalingoutsuspended
            """
            result = self._values.get("dynamic_scaling_out_suspended")
            return result

        @builtins.property
        def scheduled_scaling_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnScalableTarget.SuspendedStateProperty.ScheduledScalingSuspended``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-scheduledscalingsuspended
            """
            result = self._values.get("scheduled_scaling_suspended")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuspendedStateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "role_arn": "roleArn",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "scheduled_actions": "scheduledActions",
        "suspended_state": "suspendedState",
    },
)
class CfnScalableTargetProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        role_arn: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        scheduled_actions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnScalableTarget.ScheduledActionProperty, _IResolvable_a771d0ef]]]] = None,
        suspended_state: typing.Optional[typing.Union[CfnScalableTarget.SuspendedStateProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::ApplicationAutoScaling::ScalableTarget``.

        :param max_capacity: ``AWS::ApplicationAutoScaling::ScalableTarget.MaxCapacity``.
        :param min_capacity: ``AWS::ApplicationAutoScaling::ScalableTarget.MinCapacity``.
        :param resource_id: ``AWS::ApplicationAutoScaling::ScalableTarget.ResourceId``.
        :param role_arn: ``AWS::ApplicationAutoScaling::ScalableTarget.RoleARN``.
        :param scalable_dimension: ``AWS::ApplicationAutoScaling::ScalableTarget.ScalableDimension``.
        :param service_namespace: ``AWS::ApplicationAutoScaling::ScalableTarget.ServiceNamespace``.
        :param scheduled_actions: ``AWS::ApplicationAutoScaling::ScalableTarget.ScheduledActions``.
        :param suspended_state: ``AWS::ApplicationAutoScaling::ScalableTarget.SuspendedState``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "role_arn": role_arn,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }
        if scheduled_actions is not None:
            self._values["scheduled_actions"] = scheduled_actions
        if suspended_state is not None:
            self._values["suspended_state"] = suspended_state

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        """``AWS::ApplicationAutoScaling::ScalableTarget.MaxCapacity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity
        """
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return result

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        """``AWS::ApplicationAutoScaling::ScalableTarget.MinCapacity``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity
        """
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return result

    @builtins.property
    def resource_id(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ResourceId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid
        """
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return result

    @builtins.property
    def role_arn(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.RoleARN``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn
        """
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return result

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ScalableDimension``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension
        """
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return result

    @builtins.property
    def service_namespace(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ServiceNamespace``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace
        """
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return result

    @builtins.property
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnScalableTarget.ScheduledActionProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::ApplicationAutoScaling::ScalableTarget.ScheduledActions``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions
        """
        result = self._values.get("scheduled_actions")
        return result

    @builtins.property
    def suspended_state(
        self,
    ) -> typing.Optional[typing.Union[CfnScalableTarget.SuspendedStateProperty, _IResolvable_a771d0ef]]:
        """``AWS::ApplicationAutoScaling::ScalableTarget.SuspendedState``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate
        """
        result = self._values.get("suspended_state")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalableTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnScalingPolicy(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy",
):
    """A CloudFormation ``AWS::ApplicationAutoScaling::ScalingPolicy``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
    :cloudformationResource: AWS::ApplicationAutoScaling::ScalingPolicy
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        policy_type: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        scalable_dimension: typing.Optional[builtins.str] = None,
        scaling_target_id: typing.Optional[builtins.str] = None,
        service_namespace: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::ApplicationAutoScaling::ScalingPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_name: ``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyName``.
        :param policy_type: ``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyType``.
        :param resource_id: ``AWS::ApplicationAutoScaling::ScalingPolicy.ResourceId``.
        :param scalable_dimension: ``AWS::ApplicationAutoScaling::ScalingPolicy.ScalableDimension``.
        :param scaling_target_id: ``AWS::ApplicationAutoScaling::ScalingPolicy.ScalingTargetId``.
        :param service_namespace: ``AWS::ApplicationAutoScaling::ScalingPolicy.ServiceNamespace``.
        :param step_scaling_policy_configuration: ``AWS::ApplicationAutoScaling::ScalingPolicy.StepScalingPolicyConfiguration``.
        :param target_tracking_scaling_policy_configuration: ``AWS::ApplicationAutoScaling::ScalingPolicy.TargetTrackingScalingPolicyConfiguration``.
        """
        props = CfnScalingPolicyProps(
            policy_name=policy_name,
            policy_type=policy_type,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            scaling_target_id=scaling_target_id,
            service_namespace=service_namespace,
            step_scaling_policy_configuration=step_scaling_policy_configuration,
            target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
        )

        jsii.create(CfnScalingPolicy, self, [scope, id, props])

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
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname
        """
        return jsii.get(self, "policyName")

    @policy_name.setter # type: ignore
    def policy_name(self, value: builtins.str) -> None:
        jsii.set(self, "policyName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype
        """
        return jsii.get(self, "policyType")

    @policy_type.setter # type: ignore
    def policy_type(self, value: builtins.str) -> None:
        jsii.set(self, "policyType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ResourceId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid
        """
        return jsii.get(self, "resourceId")

    @resource_id.setter # type: ignore
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ScalableDimension``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension
        """
        return jsii.get(self, "scalableDimension")

    @scalable_dimension.setter # type: ignore
    def scalable_dimension(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scalableDimension", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalingTargetId")
    def scaling_target_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ScalingTargetId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid
        """
        return jsii.get(self, "scalingTargetId")

    @scaling_target_id.setter # type: ignore
    def scaling_target_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scalingTargetId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ServiceNamespace``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace
        """
        return jsii.get(self, "serviceNamespace")

    @service_namespace.setter # type: ignore
    def service_namespace(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceNamespace", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.StepScalingPolicyConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration
        """
        return jsii.get(self, "stepScalingPolicyConfiguration")

    @step_scaling_policy_configuration.setter # type: ignore
    def step_scaling_policy_configuration(
        self,
        value: typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "stepScalingPolicyConfiguration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.TargetTrackingScalingPolicyConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration
        """
        return jsii.get(self, "targetTrackingScalingPolicyConfiguration")

    @target_tracking_scaling_policy_configuration.setter # type: ignore
    def target_tracking_scaling_policy_configuration(
        self,
        value: typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "targetTrackingScalingPolicyConfiguration", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "statistic": "statistic",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class CustomizedMetricSpecificationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            statistic: builtins.str,
            dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.MetricDimensionProperty", _IResolvable_a771d0ef]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param metric_name: ``CfnScalingPolicy.CustomizedMetricSpecificationProperty.MetricName``.
            :param namespace: ``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Namespace``.
            :param statistic: ``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Statistic``.
            :param dimensions: ``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Dimensions``.
            :param unit: ``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Unit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
                "statistic": statistic,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.MetricName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname
            """
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return result

        @builtins.property
        def namespace(self) -> builtins.str:
            """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Namespace``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace
            """
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return result

        @builtins.property
        def statistic(self) -> builtins.str:
            """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Statistic``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic
            """
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return result

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.MetricDimensionProperty", _IResolvable_a771d0ef]]]]:
            """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Dimensions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions
            """
            result = self._values.get("dimensions")
            return result

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Unit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit
            """
            result = self._values.get("unit")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            """
            :param name: ``CfnScalingPolicy.MetricDimensionProperty.Name``.
            :param value: ``CfnScalingPolicy.MetricDimensionProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnScalingPolicy.MetricDimensionProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def value(self) -> builtins.str:
            """``CfnScalingPolicy.MetricDimensionProperty.Value``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value
            """
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_metric_type": "predefinedMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param predefined_metric_type: ``CfnScalingPolicy.PredefinedMetricSpecificationProperty.PredefinedMetricType``.
            :param resource_label: ``CfnScalingPolicy.PredefinedMetricSpecificationProperty.ResourceLabel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "predefined_metric_type": predefined_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_metric_type(self) -> builtins.str:
            """``CfnScalingPolicy.PredefinedMetricSpecificationProperty.PredefinedMetricType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype
            """
            result = self._values.get("predefined_metric_type")
            assert result is not None, "Required property 'predefined_metric_type' is missing"
            return result

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            """``CfnScalingPolicy.PredefinedMetricSpecificationProperty.ResourceLabel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel
            """
            result = self._values.get("resource_label")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "metric_interval_lower_bound": "metricIntervalLowerBound",
            "metric_interval_upper_bound": "metricIntervalUpperBound",
        },
    )
    class StepAdjustmentProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            metric_interval_lower_bound: typing.Optional[jsii.Number] = None,
            metric_interval_upper_bound: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param scaling_adjustment: ``CfnScalingPolicy.StepAdjustmentProperty.ScalingAdjustment``.
            :param metric_interval_lower_bound: ``CfnScalingPolicy.StepAdjustmentProperty.MetricIntervalLowerBound``.
            :param metric_interval_upper_bound: ``CfnScalingPolicy.StepAdjustmentProperty.MetricIntervalUpperBound``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if metric_interval_lower_bound is not None:
                self._values["metric_interval_lower_bound"] = metric_interval_lower_bound
            if metric_interval_upper_bound is not None:
                self._values["metric_interval_upper_bound"] = metric_interval_upper_bound

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            """``CfnScalingPolicy.StepAdjustmentProperty.ScalingAdjustment``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-scalingadjustment
            """
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return result

        @builtins.property
        def metric_interval_lower_bound(self) -> typing.Optional[jsii.Number]:
            """``CfnScalingPolicy.StepAdjustmentProperty.MetricIntervalLowerBound``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervallowerbound
            """
            result = self._values.get("metric_interval_lower_bound")
            return result

        @builtins.property
        def metric_interval_upper_bound(self) -> typing.Optional[jsii.Number]:
            """``CfnScalingPolicy.StepAdjustmentProperty.MetricIntervalUpperBound``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervalupperbound
            """
            result = self._values.get("metric_interval_upper_bound")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepAdjustmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adjustment_type": "adjustmentType",
            "cooldown": "cooldown",
            "metric_aggregation_type": "metricAggregationType",
            "min_adjustment_magnitude": "minAdjustmentMagnitude",
            "step_adjustments": "stepAdjustments",
        },
    )
    class StepScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            adjustment_type: typing.Optional[builtins.str] = None,
            cooldown: typing.Optional[jsii.Number] = None,
            metric_aggregation_type: typing.Optional[builtins.str] = None,
            min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
            step_adjustments: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.StepAdjustmentProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            """
            :param adjustment_type: ``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.AdjustmentType``.
            :param cooldown: ``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.Cooldown``.
            :param metric_aggregation_type: ``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.MetricAggregationType``.
            :param min_adjustment_magnitude: ``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.MinAdjustmentMagnitude``.
            :param step_adjustments: ``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.StepAdjustments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cooldown is not None:
                self._values["cooldown"] = cooldown
            if metric_aggregation_type is not None:
                self._values["metric_aggregation_type"] = metric_aggregation_type
            if min_adjustment_magnitude is not None:
                self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
            if step_adjustments is not None:
                self._values["step_adjustments"] = step_adjustments

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            """``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.AdjustmentType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype
            """
            result = self._values.get("adjustment_type")
            return result

        @builtins.property
        def cooldown(self) -> typing.Optional[jsii.Number]:
            """``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.Cooldown``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown
            """
            result = self._values.get("cooldown")
            return result

        @builtins.property
        def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
            """``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.MetricAggregationType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype
            """
            result = self._values.get("metric_aggregation_type")
            return result

        @builtins.property
        def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
            """``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.MinAdjustmentMagnitude``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude
            """
            result = self._values.get("min_adjustment_magnitude")
            return result

        @builtins.property
        def step_adjustments(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.StepAdjustmentProperty", _IResolvable_a771d0ef]]]]:
            """``CfnScalingPolicy.StepScalingPolicyConfigurationProperty.StepAdjustments``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments
            """
            result = self._values.get("step_adjustments")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_value": "targetValue",
            "customized_metric_specification": "customizedMetricSpecification",
            "disable_scale_in": "disableScaleIn",
            "predefined_metric_specification": "predefinedMetricSpecification",
            "scale_in_cooldown": "scaleInCooldown",
            "scale_out_cooldown": "scaleOutCooldown",
        },
    )
    class TargetTrackingScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            target_value: jsii.Number,
            customized_metric_specification: typing.Optional[typing.Union["CfnScalingPolicy.CustomizedMetricSpecificationProperty", _IResolvable_a771d0ef]] = None,
            disable_scale_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            predefined_metric_specification: typing.Optional[typing.Union["CfnScalingPolicy.PredefinedMetricSpecificationProperty", _IResolvable_a771d0ef]] = None,
            scale_in_cooldown: typing.Optional[jsii.Number] = None,
            scale_out_cooldown: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param target_value: ``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.TargetValue``.
            :param customized_metric_specification: ``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.CustomizedMetricSpecification``.
            :param disable_scale_in: ``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.DisableScaleIn``.
            :param predefined_metric_specification: ``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.PredefinedMetricSpecification``.
            :param scale_in_cooldown: ``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.ScaleInCooldown``.
            :param scale_out_cooldown: ``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.ScaleOutCooldown``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "target_value": target_value,
            }
            if customized_metric_specification is not None:
                self._values["customized_metric_specification"] = customized_metric_specification
            if disable_scale_in is not None:
                self._values["disable_scale_in"] = disable_scale_in
            if predefined_metric_specification is not None:
                self._values["predefined_metric_specification"] = predefined_metric_specification
            if scale_in_cooldown is not None:
                self._values["scale_in_cooldown"] = scale_in_cooldown
            if scale_out_cooldown is not None:
                self._values["scale_out_cooldown"] = scale_out_cooldown

        @builtins.property
        def target_value(self) -> jsii.Number:
            """``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.TargetValue``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue
            """
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return result

        @builtins.property
        def customized_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPolicy.CustomizedMetricSpecificationProperty", _IResolvable_a771d0ef]]:
            """``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.CustomizedMetricSpecification``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification
            """
            result = self._values.get("customized_metric_specification")
            return result

        @builtins.property
        def disable_scale_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.DisableScaleIn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein
            """
            result = self._values.get("disable_scale_in")
            return result

        @builtins.property
        def predefined_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPolicy.PredefinedMetricSpecificationProperty", _IResolvable_a771d0ef]]:
            """``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.PredefinedMetricSpecification``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification
            """
            result = self._values.get("predefined_metric_specification")
            return result

        @builtins.property
        def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
            """``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.ScaleInCooldown``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown
            """
            result = self._values.get("scale_in_cooldown")
            return result

        @builtins.property
        def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
            """``CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty.ScaleOutCooldown``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown
            """
            result = self._values.get("scale_out_cooldown")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_name": "policyName",
        "policy_type": "policyType",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "scaling_target_id": "scalingTargetId",
        "service_namespace": "serviceNamespace",
        "step_scaling_policy_configuration": "stepScalingPolicyConfiguration",
        "target_tracking_scaling_policy_configuration": "targetTrackingScalingPolicyConfiguration",
    },
)
class CfnScalingPolicyProps:
    def __init__(
        self,
        *,
        policy_name: builtins.str,
        policy_type: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        scalable_dimension: typing.Optional[builtins.str] = None,
        scaling_target_id: typing.Optional[builtins.str] = None,
        service_namespace: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::ApplicationAutoScaling::ScalingPolicy``.

        :param policy_name: ``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyName``.
        :param policy_type: ``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyType``.
        :param resource_id: ``AWS::ApplicationAutoScaling::ScalingPolicy.ResourceId``.
        :param scalable_dimension: ``AWS::ApplicationAutoScaling::ScalingPolicy.ScalableDimension``.
        :param scaling_target_id: ``AWS::ApplicationAutoScaling::ScalingPolicy.ScalingTargetId``.
        :param service_namespace: ``AWS::ApplicationAutoScaling::ScalingPolicy.ServiceNamespace``.
        :param step_scaling_policy_configuration: ``AWS::ApplicationAutoScaling::ScalingPolicy.StepScalingPolicyConfiguration``.
        :param target_tracking_scaling_policy_configuration: ``AWS::ApplicationAutoScaling::ScalingPolicy.TargetTrackingScalingPolicyConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "policy_name": policy_name,
            "policy_type": policy_type,
        }
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if scalable_dimension is not None:
            self._values["scalable_dimension"] = scalable_dimension
        if scaling_target_id is not None:
            self._values["scaling_target_id"] = scaling_target_id
        if service_namespace is not None:
            self._values["service_namespace"] = service_namespace
        if step_scaling_policy_configuration is not None:
            self._values["step_scaling_policy_configuration"] = step_scaling_policy_configuration
        if target_tracking_scaling_policy_configuration is not None:
            self._values["target_tracking_scaling_policy_configuration"] = target_tracking_scaling_policy_configuration

    @builtins.property
    def policy_name(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname
        """
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return result

    @builtins.property
    def policy_type(self) -> builtins.str:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.PolicyType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype
        """
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return result

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ResourceId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid
        """
        result = self._values.get("resource_id")
        return result

    @builtins.property
    def scalable_dimension(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ScalableDimension``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension
        """
        result = self._values.get("scalable_dimension")
        return result

    @builtins.property
    def scaling_target_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ScalingTargetId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid
        """
        result = self._values.get("scaling_target_id")
        return result

    @builtins.property
    def service_namespace(self) -> typing.Optional[builtins.str]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.ServiceNamespace``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace
        """
        result = self._values.get("service_namespace")
        return result

    @builtins.property
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.StepScalingPolicyConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration
        """
        result = self._values.get("step_scaling_policy_configuration")
        return result

    @builtins.property
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::ApplicationAutoScaling::ScalingPolicy.TargetTrackingScalingPolicyConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration
        """
        result = self._values.get("target_tracking_scaling_policy_configuration")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.CronOptions",
    jsii_struct_bases=[],
    name_mapping={
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "week_day": "weekDay",
        "year": "year",
    },
)
class CronOptions:
    def __init__(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Options to configure a cron expression.

        All fields are strings so you can use complex expressions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: (experimental) The day of the month to run this rule at. Default: - Every day of the month
        :param hour: (experimental) The hour to run this rule at. Default: - Every hour
        :param minute: (experimental) The minute to run this rule at. Default: - Every minute
        :param month: (experimental) The month to run this rule at. Default: - Every month
        :param week_day: (experimental) The day of the week to run this rule at. Default: - Any day of the week
        :param year: (experimental) The year to run this rule at. Default: - Every year

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if hour is not None:
            self._values["hour"] = hour
        if minute is not None:
            self._values["minute"] = minute
        if month is not None:
            self._values["month"] = month
        if week_day is not None:
            self._values["week_day"] = week_day
        if year is not None:
            self._values["year"] = year

    @builtins.property
    def day(self) -> typing.Optional[builtins.str]:
        """(experimental) The day of the month to run this rule at.

        :default: - Every day of the month

        :stability: experimental
        """
        result = self._values.get("day")
        return result

    @builtins.property
    def hour(self) -> typing.Optional[builtins.str]:
        """(experimental) The hour to run this rule at.

        :default: - Every hour

        :stability: experimental
        """
        result = self._values.get("hour")
        return result

    @builtins.property
    def minute(self) -> typing.Optional[builtins.str]:
        """(experimental) The minute to run this rule at.

        :default: - Every minute

        :stability: experimental
        """
        result = self._values.get("minute")
        return result

    @builtins.property
    def month(self) -> typing.Optional[builtins.str]:
        """(experimental) The month to run this rule at.

        :default: - Every month

        :stability: experimental
        """
        result = self._values.get("month")
        return result

    @builtins.property
    def week_day(self) -> typing.Optional[builtins.str]:
        """(experimental) The day of the week to run this rule at.

        :default: - Any day of the week

        :stability: experimental
        """
        result = self._values.get("week_day")
        return result

    @builtins.property
    def year(self) -> typing.Optional[builtins.str]:
        """(experimental) The year to run this rule at.

        :default: - Every year

        :stability: experimental
        """
        result = self._values.get("year")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.EnableScalingProps",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class EnableScalingProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Properties for enabling DynamoDB capacity scaling.

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
        return "EnableScalingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_applicationautoscaling.IScalableTarget")
class IScalableTarget(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IScalableTargetProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        """
        :stability: experimental
        :attribute: true
        """
        ...


class _IScalableTargetProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """
    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_applicationautoscaling.IScalableTarget"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        """
        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "scalableTargetId")


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.MetricAggregationType")
class MetricAggregationType(enum.Enum):
    """(experimental) How the scaling metric is going to be aggregated.

    :stability: experimental
    """

    AVERAGE = "AVERAGE"
    """(experimental) Average.

    :stability: experimental
    """
    MINIMUM = "MINIMUM"
    """(experimental) Minimum.

    :stability: experimental
    """
    MAXIMUM = "MAXIMUM"
    """(experimental) Maximum.

    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.PredefinedMetric")
class PredefinedMetric(enum.Enum):
    """(experimental) One of the predefined autoscaling metrics.

    :stability: experimental
    """

    DYNAMODB_READ_CAPACITY_UTILIZATION = "DYNAMODB_READ_CAPACITY_UTILIZATION"
    """(experimental) DYNAMODB_READ_CAPACITY_UTILIZATIO.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    DYANMODB_WRITE_CAPACITY_UTILIZATION = "DYANMODB_WRITE_CAPACITY_UTILIZATION"
    """(experimental) DYANMODB_WRITE_CAPACITY_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    ALB_REQUEST_COUNT_PER_TARGET = "ALB_REQUEST_COUNT_PER_TARGET"
    """(experimental) ALB_REQUEST_COUNT_PER_TARGET.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    RDS_READER_AVERAGE_CPU_UTILIZATION = "RDS_READER_AVERAGE_CPU_UTILIZATION"
    """(experimental) RDS_READER_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    RDS_READER_AVERAGE_DATABASE_CONNECTIONS = "RDS_READER_AVERAGE_DATABASE_CONNECTIONS"
    """(experimental) RDS_READER_AVERAGE_DATABASE_CONNECTIONS.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION = "EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION"
    """(experimental) EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN = "EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN"
    """(experimental) EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT = "EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT"
    """(experimental) EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE = "SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE"
    """(experimental) SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    ECS_SERVICE_AVERAGE_CPU_UTILIZATION = "ECS_SERVICE_AVERAGE_CPU_UTILIZATION"
    """(experimental) ECS_SERVICE_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION = "ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION"
    """(experimental) ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """
    LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION = "LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION"
    """(experimental) LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION.

    :see: https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-concurrency
    :stability: experimental
    """
    KAFKA_BROKER_STORAGE_UTILIZATION = "KAFKA_BROKER_STORAGE_UTILIZATION"
    """(experimental) KAFKA_BROKER_STORAGE_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    """


@jsii.implements(IScalableTarget)
class ScalableTarget(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.ScalableTarget",
):
    """(experimental) Define a scalable target.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: "ServiceNamespace",
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param max_capacity: (experimental) The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param min_capacity: (experimental) The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param resource_id: (experimental) The resource identifier to associate with this scalable target. This string consists of the resource type and unique identifier.
        :param scalable_dimension: (experimental) The scalable dimension that's associated with the scalable target. Specify the service namespace, resource type, and scaling property.
        :param service_namespace: (experimental) The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service. For valid AWS service namespace values, see the RegisterScalableTarget action in the Application Auto Scaling API Reference.
        :param role: (experimental) Role that allows Application Auto Scaling to modify your scalable target. Default: A role is automatically created

        :stability: experimental
        """
        props = ScalableTargetProps(
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            role=role,
        )

        jsii.create(ScalableTarget, self, [scope, id, props])

    @jsii.member(jsii_name="fromScalableTargetId")
    @builtins.classmethod
    def from_scalable_target_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        scalable_target_id: builtins.str,
    ) -> IScalableTarget:
        """
        :param scope: -
        :param id: -
        :param scalable_target_id: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromScalableTargetId", [scope, id, scalable_target_id])

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_296fe8a3) -> None:
        """(experimental) Add a policy statement to the role's policy.

        :param statement: -

        :stability: experimental
        """
        return jsii.invoke(self, "addToRolePolicy", [statement])

    @jsii.member(jsii_name="scaleOnMetric")
    def scale_on_metric(
        self,
        id: builtins.str,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.List["ScalingInterval"],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> "StepScalingPolicy":
        """(experimental) Scale out or in, in response to a metric.

        :param id: -
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        """
        props = BasicStepScalingPolicyProps(
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        return jsii.invoke(self, "scaleOnMetric", [id, props])

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        """(experimental) Scale out or in based on time.

        :param id: -
        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        """
        action = ScalingSchedule(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
        )

        return jsii.invoke(self, "scaleOnSchedule", [id, action])

    @jsii.member(jsii_name="scaleToTrackMetric")
    def scale_to_track_metric(
        self,
        id: builtins.str,
        *,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> "TargetTrackingScalingPolicy":
        """(experimental) Scale out or in in order to keep a metric around a target value.

        :param id: -
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Default: - No resource label.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        """
        props = BasicTargetTrackingScalingPolicyProps(
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return jsii.invoke(self, "scaleToTrackMetric", [id, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_59af6f50:
        """(experimental) The role used to give AutoScaling permissions to your resource.

        :stability: experimental
        """
        return jsii.get(self, "role")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        """(experimental) ID of the Scalable Target.

        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            service / ecs_stack - MyECSCluster - AB12CDE3F4GH / ecs_stack - MyECSService - AB12CDE3F4GH | ecsservice:DesiredCount|ecs@attributeundefined
        """
        return jsii.get(self, "scalableTargetId")


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.ScalableTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "role": "role",
    },
)
class ScalableTargetProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: "ServiceNamespace",
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        """(experimental) Properties for a scalable target.

        :param max_capacity: (experimental) The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param min_capacity: (experimental) The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param resource_id: (experimental) The resource identifier to associate with this scalable target. This string consists of the resource type and unique identifier.
        :param scalable_dimension: (experimental) The scalable dimension that's associated with the scalable target. Specify the service namespace, resource type, and scaling property.
        :param service_namespace: (experimental) The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service. For valid AWS service namespace values, see the RegisterScalableTarget action in the Application Auto Scaling API Reference.
        :param role: (experimental) Role that allows Application Auto Scaling to modify your scalable target. Default: A role is automatically created

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        """(experimental) The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.

        :stability: experimental
        """
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return result

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        """(experimental) The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.

        :stability: experimental
        """
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return result

    @builtins.property
    def resource_id(self) -> builtins.str:
        """(experimental) The resource identifier to associate with this scalable target.

        This string consists of the resource type and unique identifier.

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html
        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            service / ecs_stack - MyECSCluster - AB12CDE3F4GH / ecs_stack - MyECSService - AB12CDE3F4GH
        """
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return result

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        """(experimental) The scalable dimension that's associated with the scalable target.

        Specify the service namespace, resource type, and scaling property.

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingPolicy.html
        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            ecs:service:DesiredCount
        """
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return result

    @builtins.property
    def service_namespace(self) -> "ServiceNamespace":
        """(experimental) The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service.

        For valid AWS service namespace values, see the RegisterScalableTarget
        action in the Application Auto Scaling API Reference.

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html
        :stability: experimental
        """
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) Role that allows Application Auto Scaling to modify your scalable target.

        :default: A role is automatically created

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalableTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.ScalingInterval",
    jsii_struct_bases=[],
    name_mapping={"change": "change", "lower": "lower", "upper": "upper"},
)
class ScalingInterval:
    def __init__(
        self,
        *,
        change: jsii.Number,
        lower: typing.Optional[jsii.Number] = None,
        upper: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) A range of metric values in which to apply a certain scaling operation.

        :param change: (experimental) The capacity adjustment to apply in this interval. The number is interpreted differently based on AdjustmentType: - ChangeInCapacity: add the adjustment to the current capacity. The number can be positive or negative. - PercentChangeInCapacity: add or remove the given percentage of the current capacity to itself. The number can be in the range [-100..100]. - ExactCapacity: set the capacity to this number. The number must be positive.
        :param lower: (experimental) The lower bound of the interval. The scaling adjustment will be applied if the metric is higher than this value. Default: Threshold automatically derived from neighbouring intervals
        :param upper: (experimental) The upper bound of the interval. The scaling adjustment will be applied if the metric is lower than this value. Default: Threshold automatically derived from neighbouring intervals

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "change": change,
        }
        if lower is not None:
            self._values["lower"] = lower
        if upper is not None:
            self._values["upper"] = upper

    @builtins.property
    def change(self) -> jsii.Number:
        """(experimental) The capacity adjustment to apply in this interval.

        The number is interpreted differently based on AdjustmentType:

        - ChangeInCapacity: add the adjustment to the current capacity.
          The number can be positive or negative.
        - PercentChangeInCapacity: add or remove the given percentage of the current
          capacity to itself. The number can be in the range [-100..100].
        - ExactCapacity: set the capacity to this number. The number must
          be positive.

        :stability: experimental
        """
        result = self._values.get("change")
        assert result is not None, "Required property 'change' is missing"
        return result

    @builtins.property
    def lower(self) -> typing.Optional[jsii.Number]:
        """(experimental) The lower bound of the interval.

        The scaling adjustment will be applied if the metric is higher than this value.

        :default: Threshold automatically derived from neighbouring intervals

        :stability: experimental
        """
        result = self._values.get("lower")
        return result

    @builtins.property
    def upper(self) -> typing.Optional[jsii.Number]:
        """(experimental) The upper bound of the interval.

        The scaling adjustment will be applied if the metric is lower than this value.

        :default: Threshold automatically derived from neighbouring intervals

        :stability: experimental
        """
        result = self._values.get("upper")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.ScalingSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "schedule": "schedule",
        "end_time": "endTime",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "start_time": "startTime",
    },
)
class ScalingSchedule:
    def __init__(
        self,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        """(experimental) A scheduled scaling action.

        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "schedule": schedule,
        }
        if end_time is not None:
            self._values["end_time"] = end_time
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def schedule(self) -> "Schedule":
        """(experimental) When to perform this action.

        :stability: experimental
        """
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return result

    @builtins.property
    def end_time(self) -> typing.Optional[datetime.datetime]:
        """(experimental) When this scheduled action expires.

        :default: The rule never expires.

        :stability: experimental
        """
        result = self._values.get("end_time")
        return result

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        """(experimental) The new maximum capacity.

        During the scheduled time, the current capacity is above the maximum
        capacity, Application Auto Scaling scales in to the maximum capacity.

        At least one of maxCapacity and minCapacity must be supplied.

        :default: No new maximum capacity

        :stability: experimental
        """
        result = self._values.get("max_capacity")
        return result

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        """(experimental) The new minimum capacity.

        During the scheduled time, if the current capacity is below the minimum
        capacity, Application Auto Scaling scales out to the minimum capacity.

        At least one of maxCapacity and minCapacity must be supplied.

        :default: No new minimum capacity

        :stability: experimental
        """
        result = self._values.get("min_capacity")
        return result

    @builtins.property
    def start_time(self) -> typing.Optional[datetime.datetime]:
        """(experimental) When this scheduled action becomes active.

        :default: The rule is activate immediately

        :stability: experimental
        """
        result = self._values.get("start_time")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Schedule(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_applicationautoscaling.Schedule",
):
    """(experimental) Schedule for scheduled scaling actions.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ScheduleProxy

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(Schedule, self, [])

    @jsii.member(jsii_name="at")
    @builtins.classmethod
    def at(cls, moment: datetime.datetime) -> "Schedule":
        """(experimental) Construct a Schedule from a moment in time.

        :param moment: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "at", [moment])

    @jsii.member(jsii_name="cron")
    @builtins.classmethod
    def cron(
        cls,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> "Schedule":
        """(experimental) Create a schedule from a set of cron fields.

        :param day: (experimental) The day of the month to run this rule at. Default: - Every day of the month
        :param hour: (experimental) The hour to run this rule at. Default: - Every hour
        :param minute: (experimental) The minute to run this rule at. Default: - Every minute
        :param month: (experimental) The month to run this rule at. Default: - Every month
        :param week_day: (experimental) The day of the week to run this rule at. Default: - Any day of the week
        :param year: (experimental) The year to run this rule at. Default: - Every year

        :stability: experimental
        """
        options = CronOptions(
            day=day,
            hour=hour,
            minute=minute,
            month=month,
            week_day=week_day,
            year=year,
        )

        return jsii.sinvoke(cls, "cron", [options])

    @jsii.member(jsii_name="expression")
    @builtins.classmethod
    def expression(cls, expression: builtins.str) -> "Schedule":
        """(experimental) Construct a schedule from a literal schedule expression.

        :param expression: The expression to use. Must be in a format that Application AutoScaling will recognize

        :stability: experimental
        """
        return jsii.sinvoke(cls, "expression", [expression])

    @jsii.member(jsii_name="rate")
    @builtins.classmethod
    def rate(cls, duration: _Duration_070aa057) -> "Schedule":
        """(experimental) Construct a schedule from an interval and a time unit.

        :param duration: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "rate", [duration])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> builtins.str:
        """(experimental) Retrieve the expression for this schedule.

        :stability: experimental
        """
        ...


class _ScheduleProxy(Schedule):
    @builtins.property # type: ignore
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> builtins.str:
        """(experimental) Retrieve the expression for this schedule.

        :stability: experimental
        """
        return jsii.get(self, "expressionString")


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.ServiceNamespace")
class ServiceNamespace(enum.Enum):
    """(experimental) The service that supports Application AutoScaling.

    :stability: experimental
    """

    ECS = "ECS"
    """(experimental) Elastic Container Service.

    :stability: experimental
    """
    ELASTIC_MAP_REDUCE = "ELASTIC_MAP_REDUCE"
    """(experimental) Elastic Map Reduce.

    :stability: experimental
    """
    EC2 = "EC2"
    """(experimental) Elastic Compute Cloud.

    :stability: experimental
    """
    APPSTREAM = "APPSTREAM"
    """(experimental) App Stream.

    :stability: experimental
    """
    DYNAMODB = "DYNAMODB"
    """(experimental) Dynamo DB.

    :stability: experimental
    """
    RDS = "RDS"
    """(experimental) Relational Database Service.

    :stability: experimental
    """
    SAGEMAKER = "SAGEMAKER"
    """(experimental) SageMaker.

    :stability: experimental
    """
    CUSTOM_RESOURCE = "CUSTOM_RESOURCE"
    """(experimental) Custom Resource.

    :stability: experimental
    """
    LAMBDA = "LAMBDA"
    """(experimental) Lambda.

    :stability: experimental
    """
    COMPREHEND = "COMPREHEND"
    """(experimental) Comprehend.

    :stability: experimental
    """
    KAFKA = "KAFKA"
    """(experimental) Kafka.

    :stability: experimental
    """


class StepScalingAction(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingAction",
):
    """(experimental) Define a step scaling action.

    This kind of scaling policy adjusts the target capacity in configurable
    steps. The size of the step is configurable based on the metric's distance
    to its alarm threshold.

    This Action must be used as the target of a CloudWatch alarm to take effect.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param scaling_target: (experimental) The scalable target.
        :param adjustment_type: (experimental) How the adjustment numbers are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. For scale out policies, multiple scale outs during the cooldown period are squashed so that only the biggest scale out happens. For scale in policies, subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param metric_aggregation_type: (experimental) The aggregation type for the CloudWatch metrics. Default: Average
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param policy_name: (experimental) A name for the scaling policy. Default: Automatically generated name

        :stability: experimental
        """
        props = StepScalingActionProps(
            scaling_target=scaling_target,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            policy_name=policy_name,
        )

        jsii.create(StepScalingAction, self, [scope, id, props])

    @jsii.member(jsii_name="addAdjustment")
    def add_adjustment(
        self,
        *,
        adjustment: jsii.Number,
        lower_bound: typing.Optional[jsii.Number] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Add an adjusment interval to the ScalingAction.

        :param adjustment: (experimental) What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
        :param lower_bound: (experimental) Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        :param upper_bound: (experimental) Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity

        :stability: experimental
        """
        adjustment_ = AdjustmentTier(
            adjustment=adjustment, lower_bound=lower_bound, upper_bound=upper_bound
        )

        return jsii.invoke(self, "addAdjustment", [adjustment_])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> builtins.str:
        """(experimental) ARN of the scaling policy.

        :stability: experimental
        """
        return jsii.get(self, "scalingPolicyArn")


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_target": "scalingTarget",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "policy_name": "policyName",
    },
)
class StepScalingActionProps:
    def __init__(
        self,
        *,
        scaling_target: IScalableTarget,
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for a scaling policy.

        :param scaling_target: (experimental) The scalable target.
        :param adjustment_type: (experimental) How the adjustment numbers are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. For scale out policies, multiple scale outs during the cooldown period are squashed so that only the biggest scale out happens. For scale in policies, subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param metric_aggregation_type: (experimental) The aggregation type for the CloudWatch metrics. Default: Average
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param policy_name: (experimental) A name for the scaling policy. Default: Automatically generated name

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "scaling_target": scaling_target,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        """(experimental) The scalable target.

        :stability: experimental
        """
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return result

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        """(experimental) How the adjustment numbers are interpreted.

        :default: ChangeInCapacity

        :stability: experimental
        """
        result = self._values.get("adjustment_type")
        return result

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) Grace period after scaling activity.

        For scale out policies, multiple scale outs during the cooldown period are
        squashed so that only the biggest scale out happens.

        For scale in policies, subsequent scale ins during the cooldown period are
        ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        :stability: experimental
        """
        result = self._values.get("cooldown")
        return result

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[MetricAggregationType]:
        """(experimental) The aggregation type for the CloudWatch metrics.

        :default: Average

        :stability: experimental
        """
        result = self._values.get("metric_aggregation_type")
        return result

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        """(experimental) Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect

        :stability: experimental
        """
        result = self._values.get("min_adjustment_magnitude")
        return result

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        """(experimental) A name for the scaling policy.

        :default: Automatically generated name

        :stability: experimental
        """
        result = self._values.get("policy_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepScalingActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StepScalingPolicy(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingPolicy",
):
    """(experimental) Define a scaling strategy which scales depending on absolute values of some metric.

    You can specify the scaling behavior for various values of the metric.

    Implemented using one or more CloudWatch alarms and Step Scaling Policies.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.List[ScalingInterval],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param scaling_target: (experimental) The scaling target.
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        """
        props = StepScalingPolicyProps(
            scaling_target=scaling_target,
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        jsii.create(StepScalingPolicy, self, [scope, id, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lowerAction")
    def lower_action(self) -> typing.Optional[StepScalingAction]:
        """
        :stability: experimental
        """
        return jsii.get(self, "lowerAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lowerAlarm")
    def lower_alarm(self) -> typing.Optional[_Alarm_a55fe34b]:
        """
        :stability: experimental
        """
        return jsii.get(self, "lowerAlarm")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="upperAction")
    def upper_action(self) -> typing.Optional[StepScalingAction]:
        """
        :stability: experimental
        """
        return jsii.get(self, "upperAction")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="upperAlarm")
    def upper_alarm(self) -> typing.Optional[_Alarm_a55fe34b]:
        """
        :stability: experimental
        """
        return jsii.get(self, "upperAlarm")


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingPolicyProps",
    jsii_struct_bases=[BasicStepScalingPolicyProps],
    name_mapping={
        "metric": "metric",
        "scaling_steps": "scalingSteps",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "scaling_target": "scalingTarget",
    },
)
class StepScalingPolicyProps(BasicStepScalingPolicyProps):
    def __init__(
        self,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.List[ScalingInterval],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        scaling_target: IScalableTarget,
    ) -> None:
        """
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param scaling_target: (experimental) The scaling target.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "scaling_steps": scaling_steps,
            "scaling_target": scaling_target,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude

    @builtins.property
    def metric(self) -> _IMetric_5db43d61:
        """(experimental) Metric to scale on.

        :stability: experimental
        """
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return result

    @builtins.property
    def scaling_steps(self) -> typing.List[ScalingInterval]:
        """(experimental) The intervals for scaling.

        Maps a range of metric values to a particular scaling behavior.

        :stability: experimental
        """
        result = self._values.get("scaling_steps")
        assert result is not None, "Required property 'scaling_steps' is missing"
        return result

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        """(experimental) How the adjustment numbers inside 'intervals' are interpreted.

        :default: ChangeInCapacity

        :stability: experimental
        """
        result = self._values.get("adjustment_type")
        return result

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_070aa057]:
        """(experimental) Grace period after scaling activity.

        Subsequent scale outs during the cooldown period are squashed so that only
        the biggest scale out happens.

        Subsequent scale ins during the cooldown period are ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        :stability: experimental
        """
        result = self._values.get("cooldown")
        return result

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        """(experimental) Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect

        :stability: experimental
        """
        result = self._values.get("min_adjustment_magnitude")
        return result

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        """(experimental) The scaling target.

        :stability: experimental
        """
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TargetTrackingScalingPolicy(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.TargetTrackingScalingPolicy",
):
    """
    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param scaling_target: 
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Default: - No resource label.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        """
        props = TargetTrackingScalingPolicyProps(
            scaling_target=scaling_target,
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        jsii.create(TargetTrackingScalingPolicy, self, [scope, id, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> builtins.str:
        """(experimental) ARN of the scaling policy.

        :stability: experimental
        """
        return jsii.get(self, "scalingPolicyArn")


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.TargetTrackingScalingPolicyProps",
    jsii_struct_bases=[BasicTargetTrackingScalingPolicyProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_value": "targetValue",
        "custom_metric": "customMetric",
        "predefined_metric": "predefinedMetric",
        "resource_label": "resourceLabel",
        "scaling_target": "scalingTarget",
    },
)
class TargetTrackingScalingPolicyProps(BasicTargetTrackingScalingPolicyProps):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        scaling_target: IScalableTarget,
    ) -> None:
        """(experimental) Properties for a concrete TargetTrackingPolicy.

        Adds the scalingTarget.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Default: - No resource label.
        :param scaling_target: 

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
            "scaling_target": scaling_target,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if predefined_metric is not None:
            self._values["predefined_metric"] = predefined_metric
        if resource_label is not None:
            self._values["resource_label"] = resource_label

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
    def target_value(self) -> jsii.Number:
        """(experimental) The target value for the metric.

        :stability: experimental
        """
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return result

    @builtins.property
    def custom_metric(self) -> typing.Optional[_IMetric_5db43d61]:
        """(experimental) A custom metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No custom metric.

        :stability: experimental
        """
        result = self._values.get("custom_metric")
        return result

    @builtins.property
    def predefined_metric(self) -> typing.Optional[PredefinedMetric]:
        """(experimental) A predefined metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No predefined metrics.

        :stability: experimental
        """
        result = self._values.get("predefined_metric")
        return result

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        """(experimental) Identify the resource associated with the metric type.

        Only used for predefined metric ALBRequestCountPerTarget.

        :default: - No resource label.

        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            app / <load-balancer - name > /<load-balancer-id>/targetgroup / <target-group - name > /<target-group-id>
        """
        result = self._values.get("resource_label")
        return result

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        """
        :stability: experimental
        """
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetTrackingScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BaseScalableAttributeProps",
    jsii_struct_bases=[EnableScalingProps],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "dimension": "dimension",
        "resource_id": "resourceId",
        "role": "role",
        "service_namespace": "serviceNamespace",
    },
)
class BaseScalableAttributeProps(EnableScalingProps):
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: _IRole_59af6f50,
        service_namespace: ServiceNamespace,
    ) -> None:
        """(experimental) Properties for a ScalableTableAttribute.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1
        :param dimension: (experimental) Scalable dimension of the attribute.
        :param resource_id: (experimental) Resource ID of the attribute.
        :param role: (experimental) Role to use for scaling.
        :param service_namespace: (experimental) Service namespace of the scalable attribute.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "dimension": dimension,
            "resource_id": resource_id,
            "role": role,
            "service_namespace": service_namespace,
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

    @builtins.property
    def dimension(self) -> builtins.str:
        """(experimental) Scalable dimension of the attribute.

        :stability: experimental
        """
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return result

    @builtins.property
    def resource_id(self) -> builtins.str:
        """(experimental) Resource ID of the attribute.

        :stability: experimental
        """
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return result

    @builtins.property
    def role(self) -> _IRole_59af6f50:
        """(experimental) Role to use for scaling.

        :stability: experimental
        """
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return result

    @builtins.property
    def service_namespace(self) -> ServiceNamespace:
        """(experimental) Service namespace of the scalable attribute.

        :stability: experimental
        """
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseScalableAttributeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AdjustmentTier",
    "AdjustmentType",
    "BaseScalableAttribute",
    "BaseScalableAttributeProps",
    "BaseTargetTrackingProps",
    "BasicStepScalingPolicyProps",
    "BasicTargetTrackingScalingPolicyProps",
    "CfnScalableTarget",
    "CfnScalableTargetProps",
    "CfnScalingPolicy",
    "CfnScalingPolicyProps",
    "CronOptions",
    "EnableScalingProps",
    "IScalableTarget",
    "MetricAggregationType",
    "PredefinedMetric",
    "ScalableTarget",
    "ScalableTargetProps",
    "ScalingInterval",
    "ScalingSchedule",
    "Schedule",
    "ServiceNamespace",
    "StepScalingAction",
    "StepScalingActionProps",
    "StepScalingPolicy",
    "StepScalingPolicyProps",
    "TargetTrackingScalingPolicy",
    "TargetTrackingScalingPolicyProps",
]

publication.publish()
