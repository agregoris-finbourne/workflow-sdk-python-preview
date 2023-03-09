# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.159
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


class UpdateTaskDefinitionRequest(object):
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
        'display_name': 'str',
        'description': 'str',
        'fields': 'list[FieldSchema]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'fields': 'fields'
    }

    required_map = {
        'display_name': 'optional',
        'description': 'optional',
        'fields': 'optional'
    }

    def __init__(self, display_name=None, description=None, fields=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTaskDefinitionRequest - a model defined in OpenAPI"
        
        :param display_name:  Human readable name
        :type display_name: str
        :param description:  Human readable description
        :type description: str
        :param fields:  Defines the fields associated with this Task  todo: add in remaining structure: States, Transitions, Field, Trigger, Guards, etc
        :type fields: list[lusid_workflow.FieldSchema]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._description = None
        self._fields = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.fields = fields

    @property
    def display_name(self):
        """Gets the display_name of this UpdateTaskDefinitionRequest.  # noqa: E501

        Human readable name  # noqa: E501

        :return: The display_name of this UpdateTaskDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateTaskDefinitionRequest.

        Human readable name  # noqa: E501

        :param display_name: The display_name of this UpdateTaskDefinitionRequest.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this UpdateTaskDefinitionRequest.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this UpdateTaskDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTaskDefinitionRequest.

        Human readable description  # noqa: E501

        :param description: The description of this UpdateTaskDefinitionRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def fields(self):
        """Gets the fields of this UpdateTaskDefinitionRequest.  # noqa: E501

        Defines the fields associated with this Task  todo: add in remaining structure: States, Transitions, Field, Trigger, Guards, etc  # noqa: E501

        :return: The fields of this UpdateTaskDefinitionRequest.  # noqa: E501
        :rtype: list[lusid_workflow.FieldSchema]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this UpdateTaskDefinitionRequest.

        Defines the fields associated with this Task  todo: add in remaining structure: States, Transitions, Field, Trigger, Guards, etc  # noqa: E501

        :param fields: The fields of this UpdateTaskDefinitionRequest.  # noqa: E501
        :type fields: list[lusid_workflow.FieldSchema]
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
        if not isinstance(other, UpdateTaskDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTaskDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
