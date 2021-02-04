# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PredictionJobResourceRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'driver_cpu_request': 'str',
        'driver_memory_request': 'str',
        'executor_cpu_request': 'str',
        'executor_memory_request': 'str',
        'executor_replica': 'int'
    }

    attribute_map = {
        'driver_cpu_request': 'driver_cpu_request',
        'driver_memory_request': 'driver_memory_request',
        'executor_cpu_request': 'executor_cpu_request',
        'executor_memory_request': 'executor_memory_request',
        'executor_replica': 'executor_replica'
    }

    def __init__(self, driver_cpu_request=None, driver_memory_request=None, executor_cpu_request=None, executor_memory_request=None, executor_replica=None):  # noqa: E501
        """PredictionJobResourceRequest - a model defined in Swagger"""  # noqa: E501

        self._driver_cpu_request = None
        self._driver_memory_request = None
        self._executor_cpu_request = None
        self._executor_memory_request = None
        self._executor_replica = None
        self.discriminator = None

        if driver_cpu_request is not None:
            self.driver_cpu_request = driver_cpu_request
        if driver_memory_request is not None:
            self.driver_memory_request = driver_memory_request
        if executor_cpu_request is not None:
            self.executor_cpu_request = executor_cpu_request
        if executor_memory_request is not None:
            self.executor_memory_request = executor_memory_request
        if executor_replica is not None:
            self.executor_replica = executor_replica

    @property
    def driver_cpu_request(self):
        """Gets the driver_cpu_request of this PredictionJobResourceRequest.  # noqa: E501


        :return: The driver_cpu_request of this PredictionJobResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._driver_cpu_request

    @driver_cpu_request.setter
    def driver_cpu_request(self, driver_cpu_request):
        """Sets the driver_cpu_request of this PredictionJobResourceRequest.


        :param driver_cpu_request: The driver_cpu_request of this PredictionJobResourceRequest.  # noqa: E501
        :type: str
        """

        self._driver_cpu_request = driver_cpu_request

    @property
    def driver_memory_request(self):
        """Gets the driver_memory_request of this PredictionJobResourceRequest.  # noqa: E501


        :return: The driver_memory_request of this PredictionJobResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._driver_memory_request

    @driver_memory_request.setter
    def driver_memory_request(self, driver_memory_request):
        """Sets the driver_memory_request of this PredictionJobResourceRequest.


        :param driver_memory_request: The driver_memory_request of this PredictionJobResourceRequest.  # noqa: E501
        :type: str
        """

        self._driver_memory_request = driver_memory_request

    @property
    def executor_cpu_request(self):
        """Gets the executor_cpu_request of this PredictionJobResourceRequest.  # noqa: E501


        :return: The executor_cpu_request of this PredictionJobResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._executor_cpu_request

    @executor_cpu_request.setter
    def executor_cpu_request(self, executor_cpu_request):
        """Sets the executor_cpu_request of this PredictionJobResourceRequest.


        :param executor_cpu_request: The executor_cpu_request of this PredictionJobResourceRequest.  # noqa: E501
        :type: str
        """

        self._executor_cpu_request = executor_cpu_request

    @property
    def executor_memory_request(self):
        """Gets the executor_memory_request of this PredictionJobResourceRequest.  # noqa: E501


        :return: The executor_memory_request of this PredictionJobResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._executor_memory_request

    @executor_memory_request.setter
    def executor_memory_request(self, executor_memory_request):
        """Sets the executor_memory_request of this PredictionJobResourceRequest.


        :param executor_memory_request: The executor_memory_request of this PredictionJobResourceRequest.  # noqa: E501
        :type: str
        """

        self._executor_memory_request = executor_memory_request

    @property
    def executor_replica(self):
        """Gets the executor_replica of this PredictionJobResourceRequest.  # noqa: E501


        :return: The executor_replica of this PredictionJobResourceRequest.  # noqa: E501
        :rtype: int
        """
        return self._executor_replica

    @executor_replica.setter
    def executor_replica(self, executor_replica):
        """Sets the executor_replica of this PredictionJobResourceRequest.


        :param executor_replica: The executor_replica of this PredictionJobResourceRequest.  # noqa: E501
        :type: int
        """

        self._executor_replica = executor_replica

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PredictionJobResourceRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PredictionJobResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
