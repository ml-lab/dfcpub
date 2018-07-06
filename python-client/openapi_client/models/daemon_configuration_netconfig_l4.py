# coding: utf-8

"""
    DFC

    DFC is a scalable object-storage based caching system with Amazon and Google Cloud backends.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: dfcdev@exchange.nvidia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DaemonConfigurationNetconfigL4(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'proto': 'str',
        'port': 'str'
    }

    attribute_map = {
        'proto': 'proto',
        'port': 'port'
    }

    def __init__(self, proto=None, port=None):  # noqa: E501
        """DaemonConfigurationNetconfigL4 - a model defined in OpenAPI"""  # noqa: E501

        self._proto = None
        self._port = None
        self.discriminator = None

        if proto is not None:
            self.proto = proto
        if port is not None:
            self.port = port

    @property
    def proto(self):
        """Gets the proto of this DaemonConfigurationNetconfigL4.  # noqa: E501


        :return: The proto of this DaemonConfigurationNetconfigL4.  # noqa: E501
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this DaemonConfigurationNetconfigL4.


        :param proto: The proto of this DaemonConfigurationNetconfigL4.  # noqa: E501
        :type: str
        """

        self._proto = proto

    @property
    def port(self):
        """Gets the port of this DaemonConfigurationNetconfigL4.  # noqa: E501


        :return: The port of this DaemonConfigurationNetconfigL4.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DaemonConfigurationNetconfigL4.


        :param port: The port of this DaemonConfigurationNetconfigL4.  # noqa: E501
        :type: str
        """

        self._port = port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DaemonConfigurationNetconfigL4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
