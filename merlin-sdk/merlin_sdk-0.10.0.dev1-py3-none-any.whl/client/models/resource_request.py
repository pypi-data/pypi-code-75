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


class ResourceRequest(object):
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
        'min_replica': 'int',
        'max_replica': 'int',
        'cpu_request': 'str',
        'memory_request': 'str'
    }

    attribute_map = {
        'min_replica': 'min_replica',
        'max_replica': 'max_replica',
        'cpu_request': 'cpu_request',
        'memory_request': 'memory_request'
    }

    def __init__(self, min_replica=None, max_replica=None, cpu_request=None, memory_request=None):  # noqa: E501
        """ResourceRequest - a model defined in Swagger"""  # noqa: E501

        self._min_replica = None
        self._max_replica = None
        self._cpu_request = None
        self._memory_request = None
        self.discriminator = None

        if min_replica is not None:
            self.min_replica = min_replica
        if max_replica is not None:
            self.max_replica = max_replica
        if cpu_request is not None:
            self.cpu_request = cpu_request
        if memory_request is not None:
            self.memory_request = memory_request

    @property
    def min_replica(self):
        """Gets the min_replica of this ResourceRequest.  # noqa: E501


        :return: The min_replica of this ResourceRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_replica

    @min_replica.setter
    def min_replica(self, min_replica):
        """Sets the min_replica of this ResourceRequest.


        :param min_replica: The min_replica of this ResourceRequest.  # noqa: E501
        :type: int
        """

        self._min_replica = min_replica

    @property
    def max_replica(self):
        """Gets the max_replica of this ResourceRequest.  # noqa: E501


        :return: The max_replica of this ResourceRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_replica

    @max_replica.setter
    def max_replica(self, max_replica):
        """Sets the max_replica of this ResourceRequest.


        :param max_replica: The max_replica of this ResourceRequest.  # noqa: E501
        :type: int
        """

        self._max_replica = max_replica

    @property
    def cpu_request(self):
        """Gets the cpu_request of this ResourceRequest.  # noqa: E501


        :return: The cpu_request of this ResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cpu_request

    @cpu_request.setter
    def cpu_request(self, cpu_request):
        """Sets the cpu_request of this ResourceRequest.


        :param cpu_request: The cpu_request of this ResourceRequest.  # noqa: E501
        :type: str
        """

        self._cpu_request = cpu_request

    @property
    def memory_request(self):
        """Gets the memory_request of this ResourceRequest.  # noqa: E501


        :return: The memory_request of this ResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._memory_request

    @memory_request.setter
    def memory_request(self, memory_request):
        """Sets the memory_request of this ResourceRequest.


        :param memory_request: The memory_request of this ResourceRequest.  # noqa: E501
        :type: str
        """

        self._memory_request = memory_request

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
        if issubclass(ResourceRequest, dict):
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
        if not isinstance(other, ResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
