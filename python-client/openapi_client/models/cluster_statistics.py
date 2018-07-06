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


class ClusterStatistics(object):
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
        'proxy': 'DaemonCoreStatistics',
        'target': 'TargetStatistics'
    }

    attribute_map = {
        'proxy': 'proxy',
        'target': 'target'
    }

    def __init__(self, proxy=None, target=None):  # noqa: E501
        """ClusterStatistics - a model defined in OpenAPI"""  # noqa: E501

        self._proxy = None
        self._target = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if target is not None:
            self.target = target

    @property
    def proxy(self):
        """Gets the proxy of this ClusterStatistics.  # noqa: E501


        :return: The proxy of this ClusterStatistics.  # noqa: E501
        :rtype: DaemonCoreStatistics
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ClusterStatistics.


        :param proxy: The proxy of this ClusterStatistics.  # noqa: E501
        :type: DaemonCoreStatistics
        """

        self._proxy = proxy

    @property
    def target(self):
        """Gets the target of this ClusterStatistics.  # noqa: E501


        :return: The target of this ClusterStatistics.  # noqa: E501
        :rtype: TargetStatistics
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ClusterStatistics.


        :param target: The target of this ClusterStatistics.  # noqa: E501
        :type: TargetStatistics
        """

        self._target = target

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
        if not isinstance(other, ClusterStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
