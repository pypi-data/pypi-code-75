# coding: utf-8

"""

    Copyright (c) 2021 Aspose.BarCode for Cloud

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""


import pprint
import re  # noqa: F401

import six


class CodabarParams(object):
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
        "checksum_mode": "CodabarChecksumMode",
        "start_symbol": "CodabarSymbol",
        "stop_symbol": "CodabarSymbol",
    }

    attribute_map = {"checksum_mode": "ChecksumMode", "start_symbol": "StartSymbol", "stop_symbol": "StopSymbol"}

    def __init__(self, checksum_mode=None, start_symbol=None, stop_symbol=None):  # noqa: E501
        """CodabarParams - a model defined in Swagger"""  # noqa: E501

        self._checksum_mode = None
        self._start_symbol = None
        self._stop_symbol = None
        self.discriminator = None

        if checksum_mode is not None:
            self.checksum_mode = checksum_mode
        if start_symbol is not None:
            self.start_symbol = start_symbol
        if stop_symbol is not None:
            self.stop_symbol = stop_symbol

    @property
    def checksum_mode(self):
        """Gets the checksum_mode of this CodabarParams.  # noqa: E501

        Checksum algorithm for Codabar barcodes. Default value: CodabarChecksumMode.Mod16. To enable checksum calculation set value EnableChecksum.Yes to property EnableChecksum.  # noqa: E501

        :return: The checksum_mode of this CodabarParams.  # noqa: E501
        :rtype: CodabarChecksumMode
        """
        return self._checksum_mode

    @checksum_mode.setter
    def checksum_mode(self, checksum_mode):
        """Sets the checksum_mode of this CodabarParams.

        Checksum algorithm for Codabar barcodes. Default value: CodabarChecksumMode.Mod16. To enable checksum calculation set value EnableChecksum.Yes to property EnableChecksum.  # noqa: E501

        :param checksum_mode: The checksum_mode of this CodabarParams.  # noqa: E501
        :type: CodabarChecksumMode
        """

        self._checksum_mode = checksum_mode

    @property
    def start_symbol(self):
        """Gets the start_symbol of this CodabarParams.  # noqa: E501

        Start symbol (character) of Codabar symbology. Default value: CodabarSymbol.A  # noqa: E501

        :return: The start_symbol of this CodabarParams.  # noqa: E501
        :rtype: CodabarSymbol
        """
        return self._start_symbol

    @start_symbol.setter
    def start_symbol(self, start_symbol):
        """Sets the start_symbol of this CodabarParams.

        Start symbol (character) of Codabar symbology. Default value: CodabarSymbol.A  # noqa: E501

        :param start_symbol: The start_symbol of this CodabarParams.  # noqa: E501
        :type: CodabarSymbol
        """

        self._start_symbol = start_symbol

    @property
    def stop_symbol(self):
        """Gets the stop_symbol of this CodabarParams.  # noqa: E501

        Stop symbol (character) of Codabar symbology. Default value: CodabarSymbol.A  # noqa: E501

        :return: The stop_symbol of this CodabarParams.  # noqa: E501
        :rtype: CodabarSymbol
        """
        return self._stop_symbol

    @stop_symbol.setter
    def stop_symbol(self, stop_symbol):
        """Sets the stop_symbol of this CodabarParams.

        Stop symbol (character) of Codabar symbology. Default value: CodabarSymbol.A  # noqa: E501

        :param stop_symbol: The stop_symbol of this CodabarParams.  # noqa: E501
        :type: CodabarSymbol
        """

        self._stop_symbol = stop_symbol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CodabarParams, dict):
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
        if not isinstance(other, CodabarParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
