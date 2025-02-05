# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.363
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


class Worker(object):
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
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'worker_configuration': 'object',
        'version': 'VersionInfo',
        'parameters': 'list[Parameter]',
        'result_fields': 'list[ResultField]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'worker_configuration': 'workerConfiguration',
        'version': 'version',
        'parameters': 'parameters',
        'result_fields': 'resultFields',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'worker_configuration': 'required',
        'version': 'optional',
        'parameters': 'optional',
        'result_fields': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, display_name=None, description=None, worker_configuration=None, version=None, parameters=None, result_fields=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Worker - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid_workflow.ResourceId
        :param display_name:  Human readable name (required)
        :type display_name: str
        :param description:  Human readable description
        :type description: str
        :param worker_configuration:  Information about how the worker should be executed (required)
        :type worker_configuration: object
        :param version: 
        :type version: lusid_workflow.VersionInfo
        :param parameters:  The Parameters this Worker accepts or requires.
        :type parameters: list[lusid_workflow.Parameter]
        :param result_fields:  The Fields that the Worker results will come back with.
        :type result_fields: list[lusid_workflow.ResultField]
        :param links: 
        :type links: list[lusid_workflow.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._worker_configuration = None
        self._version = None
        self._parameters = None
        self._result_fields = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.description = description
        self.worker_configuration = worker_configuration
        if version is not None:
            self.version = version
        self.parameters = parameters
        self.result_fields = result_fields
        self.links = links

    @property
    def id(self):
        """Gets the id of this Worker.  # noqa: E501


        :return: The id of this Worker.  # noqa: E501
        :rtype: lusid_workflow.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Worker.


        :param id: The id of this Worker.  # noqa: E501
        :type id: lusid_workflow.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Worker.  # noqa: E501

        Human readable name  # noqa: E501

        :return: The display_name of this Worker.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Worker.

        Human readable name  # noqa: E501

        :param display_name: The display_name of this Worker.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Worker.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this Worker.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Worker.

        Human readable description  # noqa: E501

        :param description: The description of this Worker.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def worker_configuration(self):
        """Gets the worker_configuration of this Worker.  # noqa: E501

        Information about how the worker should be executed  # noqa: E501

        :return: The worker_configuration of this Worker.  # noqa: E501
        :rtype: object
        """
        return self._worker_configuration

    @worker_configuration.setter
    def worker_configuration(self, worker_configuration):
        """Sets the worker_configuration of this Worker.

        Information about how the worker should be executed  # noqa: E501

        :param worker_configuration: The worker_configuration of this Worker.  # noqa: E501
        :type worker_configuration: object
        """

        self._worker_configuration = worker_configuration

    @property
    def version(self):
        """Gets the version of this Worker.  # noqa: E501


        :return: The version of this Worker.  # noqa: E501
        :rtype: lusid_workflow.VersionInfo
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Worker.


        :param version: The version of this Worker.  # noqa: E501
        :type version: lusid_workflow.VersionInfo
        """

        self._version = version

    @property
    def parameters(self):
        """Gets the parameters of this Worker.  # noqa: E501

        The Parameters this Worker accepts or requires.  # noqa: E501

        :return: The parameters of this Worker.  # noqa: E501
        :rtype: list[lusid_workflow.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Worker.

        The Parameters this Worker accepts or requires.  # noqa: E501

        :param parameters: The parameters of this Worker.  # noqa: E501
        :type parameters: list[lusid_workflow.Parameter]
        """

        self._parameters = parameters

    @property
    def result_fields(self):
        """Gets the result_fields of this Worker.  # noqa: E501

        The Fields that the Worker results will come back with.  # noqa: E501

        :return: The result_fields of this Worker.  # noqa: E501
        :rtype: list[lusid_workflow.ResultField]
        """
        return self._result_fields

    @result_fields.setter
    def result_fields(self, result_fields):
        """Sets the result_fields of this Worker.

        The Fields that the Worker results will come back with.  # noqa: E501

        :param result_fields: The result_fields of this Worker.  # noqa: E501
        :type result_fields: list[lusid_workflow.ResultField]
        """

        self._result_fields = result_fields

    @property
    def links(self):
        """Gets the links of this Worker.  # noqa: E501


        :return: The links of this Worker.  # noqa: E501
        :rtype: list[lusid_workflow.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Worker.


        :param links: The links of this Worker.  # noqa: E501
        :type links: list[lusid_workflow.Link]
        """

        self._links = links

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
        if not isinstance(other, Worker):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Worker):
            return True

        return self.to_dict() != other.to_dict()
