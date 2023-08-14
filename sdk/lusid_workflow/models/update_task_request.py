# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.361
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_workflow.configuration import Configuration


class UpdateTaskRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'correlation_ids': 'list[str]',
        'fields': 'list[TaskInstanceField]'
    }

    attribute_map = {
        'correlation_ids': 'correlationIds',
        'fields': 'fields'
    }

    required_map = {
        'correlation_ids': 'optional',
        'fields': 'optional'
    }

    def __init__(self, correlation_ids=None, fields=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTaskRequest - a model defined in OpenAPI"
        
        :param correlation_ids:  A set of guid identifiers that allow correlation across the application tier
        :type correlation_ids: list[str]
        :param fields:  Defines the fields associated with the update
        :type fields: list[lusid_workflow.TaskInstanceField]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._correlation_ids = None
        self._fields = None
        self.discriminator = None

        self.correlation_ids = correlation_ids
        self.fields = fields

    @property
    def correlation_ids(self):
        """Gets the correlation_ids of this UpdateTaskRequest.  # noqa: E501

        A set of guid identifiers that allow correlation across the application tier  # noqa: E501

        :return: The correlation_ids of this UpdateTaskRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._correlation_ids

    @correlation_ids.setter
    def correlation_ids(self, correlation_ids):
        """Sets the correlation_ids of this UpdateTaskRequest.

        A set of guid identifiers that allow correlation across the application tier  # noqa: E501

        :param correlation_ids: The correlation_ids of this UpdateTaskRequest.  # noqa: E501
        :type correlation_ids: list[str]
        """

        self._correlation_ids = correlation_ids

    @property
    def fields(self):
        """Gets the fields of this UpdateTaskRequest.  # noqa: E501

        Defines the fields associated with the update  # noqa: E501

        :return: The fields of this UpdateTaskRequest.  # noqa: E501
        :rtype: list[lusid_workflow.TaskInstanceField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this UpdateTaskRequest.

        Defines the fields associated with the update  # noqa: E501

        :param fields: The fields of this UpdateTaskRequest.  # noqa: E501
        :type fields: list[lusid_workflow.TaskInstanceField]
        """

        self._fields = fields

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
