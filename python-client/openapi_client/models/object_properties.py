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


class ObjectProperties(object):
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
        'name': 'str',
        'size': 'int',
        'ctime': 'str',
        'checksum': 'str',
        'type': 'str',
        'atime': 'str',
        'bucket': 'str',
        'version': 'str',
        'iscached': 'str',
        'target_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'ctime': 'ctime',
        'checksum': 'checksum',
        'type': 'type',
        'atime': 'atime',
        'bucket': 'bucket',
        'version': 'version',
        'iscached': 'iscached',
        'target_url': 'targetURL'
    }

    def __init__(self, name=None, size=None, ctime=None, checksum=None, type=None, atime=None, bucket=None, version=None, iscached=None, target_url=None):  # noqa: E501
        """ObjectProperties - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._size = None
        self._ctime = None
        self._checksum = None
        self._type = None
        self._atime = None
        self._bucket = None
        self._version = None
        self._iscached = None
        self._target_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if ctime is not None:
            self.ctime = ctime
        if checksum is not None:
            self.checksum = checksum
        if type is not None:
            self.type = type
        if atime is not None:
            self.atime = atime
        if bucket is not None:
            self.bucket = bucket
        if version is not None:
            self.version = version
        if iscached is not None:
            self.iscached = iscached
        if target_url is not None:
            self.target_url = target_url

    @property
    def name(self):
        """Gets the name of this ObjectProperties.  # noqa: E501


        :return: The name of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectProperties.


        :param name: The name of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this ObjectProperties.  # noqa: E501


        :return: The size of this ObjectProperties.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ObjectProperties.


        :param size: The size of this ObjectProperties.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def ctime(self):
        """Gets the ctime of this ObjectProperties.  # noqa: E501


        :return: The ctime of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this ObjectProperties.


        :param ctime: The ctime of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._ctime = ctime

    @property
    def checksum(self):
        """Gets the checksum of this ObjectProperties.  # noqa: E501


        :return: The checksum of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this ObjectProperties.


        :param checksum: The checksum of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def type(self):
        """Gets the type of this ObjectProperties.  # noqa: E501


        :return: The type of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ObjectProperties.


        :param type: The type of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def atime(self):
        """Gets the atime of this ObjectProperties.  # noqa: E501


        :return: The atime of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this ObjectProperties.


        :param atime: The atime of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._atime = atime

    @property
    def bucket(self):
        """Gets the bucket of this ObjectProperties.  # noqa: E501


        :return: The bucket of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ObjectProperties.


        :param bucket: The bucket of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def version(self):
        """Gets the version of this ObjectProperties.  # noqa: E501


        :return: The version of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ObjectProperties.


        :param version: The version of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def iscached(self):
        """Gets the iscached of this ObjectProperties.  # noqa: E501


        :return: The iscached of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._iscached

    @iscached.setter
    def iscached(self, iscached):
        """Sets the iscached of this ObjectProperties.


        :param iscached: The iscached of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._iscached = iscached

    @property
    def target_url(self):
        """Gets the target_url of this ObjectProperties.  # noqa: E501


        :return: The target_url of this ObjectProperties.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this ObjectProperties.


        :param target_url: The target_url of this ObjectProperties.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

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
        if not isinstance(other, ObjectProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
