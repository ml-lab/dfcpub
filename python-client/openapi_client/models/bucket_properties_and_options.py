# coding: utf-8

"""
    DFC

    DFC is a scalable object-storage based caching system with Amazon and Google Cloud backends.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: dfc-jenkins@nvidia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BucketPropertiesAndOptions(object):
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
        'props': 'str',
        'time_format': 'TimeFormat',
        'prefix': 'str',
        'pagemarker': 'str',
        'pagesize': 'str'
    }

    attribute_map = {
        'props': 'props',
        'time_format': 'time_format',
        'prefix': 'prefix',
        'pagemarker': 'pagemarker',
        'pagesize': 'pagesize'
    }

    def __init__(self, props=None, time_format=None, prefix=None, pagemarker=None, pagesize=None):  # noqa: E501
        """BucketPropertiesAndOptions - a model defined in OpenAPI"""  # noqa: E501

        self._props = None
        self._time_format = None
        self._prefix = None
        self._pagemarker = None
        self._pagesize = None
        self.discriminator = None

        if props is not None:
            self.props = props
        if time_format is not None:
            self.time_format = time_format
        if prefix is not None:
            self.prefix = prefix
        if pagemarker is not None:
            self.pagemarker = pagemarker
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def props(self):
        """Gets the props of this BucketPropertiesAndOptions.  # noqa: E501


        :return: The props of this BucketPropertiesAndOptions.  # noqa: E501
        :rtype: str
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this BucketPropertiesAndOptions.


        :param props: The props of this BucketPropertiesAndOptions.  # noqa: E501
        :type: str
        """

        self._props = props

    @property
    def time_format(self):
        """Gets the time_format of this BucketPropertiesAndOptions.  # noqa: E501


        :return: The time_format of this BucketPropertiesAndOptions.  # noqa: E501
        :rtype: TimeFormat
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this BucketPropertiesAndOptions.


        :param time_format: The time_format of this BucketPropertiesAndOptions.  # noqa: E501
        :type: TimeFormat
        """

        self._time_format = time_format

    @property
    def prefix(self):
        """Gets the prefix of this BucketPropertiesAndOptions.  # noqa: E501


        :return: The prefix of this BucketPropertiesAndOptions.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this BucketPropertiesAndOptions.


        :param prefix: The prefix of this BucketPropertiesAndOptions.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def pagemarker(self):
        """Gets the pagemarker of this BucketPropertiesAndOptions.  # noqa: E501


        :return: The pagemarker of this BucketPropertiesAndOptions.  # noqa: E501
        :rtype: str
        """
        return self._pagemarker

    @pagemarker.setter
    def pagemarker(self, pagemarker):
        """Sets the pagemarker of this BucketPropertiesAndOptions.


        :param pagemarker: The pagemarker of this BucketPropertiesAndOptions.  # noqa: E501
        :type: str
        """

        self._pagemarker = pagemarker

    @property
    def pagesize(self):
        """Gets the pagesize of this BucketPropertiesAndOptions.  # noqa: E501


        :return: The pagesize of this BucketPropertiesAndOptions.  # noqa: E501
        :rtype: str
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this BucketPropertiesAndOptions.


        :param pagesize: The pagesize of this BucketPropertiesAndOptions.  # noqa: E501
        :type: str
        """

        self._pagesize = pagesize

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
        if not isinstance(other, BucketPropertiesAndOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other