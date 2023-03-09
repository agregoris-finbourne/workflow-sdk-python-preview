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


class Output(object):
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
        'name': 'str',
        'schema': 'OutputSchema'
    }

    attribute_map = {
        'name': 'name',
        'schema': 'schema'
    }

    required_map = {
        'name': 'required',
        'schema': 'required'
    }

    def __init__(self, name=None, schema=None, local_vars_configuration=None):  # noqa: E501
        """Output - a model defined in OpenAPI"
        
        :param name:  The Name of this Output (required)
        :type name: str
        :param schema:  (required)
        :type schema: lusid_workflow.OutputSchema

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._schema = None
        self.discriminator = None

        self.name = name
        self.schema = schema

    @property
    def name(self):
        """Gets the name of this Output.  # noqa: E501

        The Name of this Output  # noqa: E501

        :return: The name of this Output.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Output.

        The Name of this Output  # noqa: E501

        :param name: The name of this Output.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this Output.  # noqa: E501


        :return: The schema of this Output.  # noqa: E501
        :rtype: lusid_workflow.OutputSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Output.


        :param schema: The schema of this Output.  # noqa: E501
        :type schema: lusid_workflow.OutputSchema
        """
        if self.local_vars_configuration.client_side_validation and schema is None:  # noqa: E501
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

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
        if not isinstance(other, Output):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Output):
            return True

        return self.to_dict() != other.to_dict()
