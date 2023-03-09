# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.161
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


class TaskDefinition(object):
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
        'task_definition_id': 'TaskDefinitionId',
        'display_name': 'str',
        'description': 'str',
        'states': 'list[State]',
        'fields_schema': 'list[FieldSchema]',
        'initial_state': 'InitialState',
        'triggers': 'list[Trigger]',
        'outputs': 'list[Output]',
        'transitions': 'list[Transition]',
        'instances': 'list[str]'
    }

    attribute_map = {
        'task_definition_id': 'taskDefinitionId',
        'display_name': 'displayName',
        'description': 'description',
        'states': 'states',
        'fields_schema': 'fieldsSchema',
        'initial_state': 'initialState',
        'triggers': 'triggers',
        'outputs': 'outputs',
        'transitions': 'transitions',
        'instances': 'instances'
    }

    required_map = {
        'task_definition_id': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'states': 'optional',
        'fields_schema': 'optional',
        'initial_state': 'optional',
        'triggers': 'optional',
        'outputs': 'optional',
        'transitions': 'optional',
        'instances': 'optional'
    }

    def __init__(self, task_definition_id=None, display_name=None, description=None, states=None, fields_schema=None, initial_state=None, triggers=None, outputs=None, transitions=None, instances=None, local_vars_configuration=None):  # noqa: E501
        """TaskDefinition - a model defined in OpenAPI"
        
        :param task_definition_id: 
        :type task_definition_id: lusid_workflow.TaskDefinitionId
        :param display_name:  Human readable name
        :type display_name: str
        :param description:  Human readable description
        :type description: str
        :param states:  The states this Task Definition operates over
        :type states: list[lusid_workflow.State]
        :param fields_schema:  The Fields that this Task Definition operates on
        :type fields_schema: list[lusid_workflow.FieldSchema]
        :param initial_state: 
        :type initial_state: lusid_workflow.InitialState
        :param triggers:  The Triggers for State transition
        :type triggers: list[lusid_workflow.Trigger]
        :param outputs:  The Outputs of this Task
        :type outputs: list[lusid_workflow.Output]
        :param transitions:  The Transitions between States
        :type transitions: list[lusid_workflow.Transition]
        :param instances:  Each Definition will have a number of instances associated with it
        :type instances: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._task_definition_id = None
        self._display_name = None
        self._description = None
        self._states = None
        self._fields_schema = None
        self._initial_state = None
        self._triggers = None
        self._outputs = None
        self._transitions = None
        self._instances = None
        self.discriminator = None

        if task_definition_id is not None:
            self.task_definition_id = task_definition_id
        self.display_name = display_name
        self.description = description
        self.states = states
        self.fields_schema = fields_schema
        if initial_state is not None:
            self.initial_state = initial_state
        self.triggers = triggers
        self.outputs = outputs
        self.transitions = transitions
        self.instances = instances

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this TaskDefinition.  # noqa: E501


        :return: The task_definition_id of this TaskDefinition.  # noqa: E501
        :rtype: lusid_workflow.TaskDefinitionId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this TaskDefinition.


        :param task_definition_id: The task_definition_id of this TaskDefinition.  # noqa: E501
        :type task_definition_id: lusid_workflow.TaskDefinitionId
        """

        self._task_definition_id = task_definition_id

    @property
    def display_name(self):
        """Gets the display_name of this TaskDefinition.  # noqa: E501

        Human readable name  # noqa: E501

        :return: The display_name of this TaskDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TaskDefinition.

        Human readable name  # noqa: E501

        :param display_name: The display_name of this TaskDefinition.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this TaskDefinition.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this TaskDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDefinition.

        Human readable description  # noqa: E501

        :param description: The description of this TaskDefinition.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def states(self):
        """Gets the states of this TaskDefinition.  # noqa: E501

        The states this Task Definition operates over  # noqa: E501

        :return: The states of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.State]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this TaskDefinition.

        The states this Task Definition operates over  # noqa: E501

        :param states: The states of this TaskDefinition.  # noqa: E501
        :type states: list[lusid_workflow.State]
        """

        self._states = states

    @property
    def fields_schema(self):
        """Gets the fields_schema of this TaskDefinition.  # noqa: E501

        The Fields that this Task Definition operates on  # noqa: E501

        :return: The fields_schema of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.FieldSchema]
        """
        return self._fields_schema

    @fields_schema.setter
    def fields_schema(self, fields_schema):
        """Sets the fields_schema of this TaskDefinition.

        The Fields that this Task Definition operates on  # noqa: E501

        :param fields_schema: The fields_schema of this TaskDefinition.  # noqa: E501
        :type fields_schema: list[lusid_workflow.FieldSchema]
        """

        self._fields_schema = fields_schema

    @property
    def initial_state(self):
        """Gets the initial_state of this TaskDefinition.  # noqa: E501


        :return: The initial_state of this TaskDefinition.  # noqa: E501
        :rtype: lusid_workflow.InitialState
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state):
        """Sets the initial_state of this TaskDefinition.


        :param initial_state: The initial_state of this TaskDefinition.  # noqa: E501
        :type initial_state: lusid_workflow.InitialState
        """

        self._initial_state = initial_state

    @property
    def triggers(self):
        """Gets the triggers of this TaskDefinition.  # noqa: E501

        The Triggers for State transition  # noqa: E501

        :return: The triggers of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this TaskDefinition.

        The Triggers for State transition  # noqa: E501

        :param triggers: The triggers of this TaskDefinition.  # noqa: E501
        :type triggers: list[lusid_workflow.Trigger]
        """

        self._triggers = triggers

    @property
    def outputs(self):
        """Gets the outputs of this TaskDefinition.  # noqa: E501

        The Outputs of this Task  # noqa: E501

        :return: The outputs of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.Output]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TaskDefinition.

        The Outputs of this Task  # noqa: E501

        :param outputs: The outputs of this TaskDefinition.  # noqa: E501
        :type outputs: list[lusid_workflow.Output]
        """

        self._outputs = outputs

    @property
    def transitions(self):
        """Gets the transitions of this TaskDefinition.  # noqa: E501

        The Transitions between States  # noqa: E501

        :return: The transitions of this TaskDefinition.  # noqa: E501
        :rtype: list[lusid_workflow.Transition]
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        """Sets the transitions of this TaskDefinition.

        The Transitions between States  # noqa: E501

        :param transitions: The transitions of this TaskDefinition.  # noqa: E501
        :type transitions: list[lusid_workflow.Transition]
        """

        self._transitions = transitions

    @property
    def instances(self):
        """Gets the instances of this TaskDefinition.  # noqa: E501

        Each Definition will have a number of instances associated with it  # noqa: E501

        :return: The instances of this TaskDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this TaskDefinition.

        Each Definition will have a number of instances associated with it  # noqa: E501

        :param instances: The instances of this TaskDefinition.  # noqa: E501
        :type instances: list[str]
        """

        self._instances = instances

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
        if not isinstance(other, TaskDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDefinition):
            return True

        return self.to_dict() != other.to_dict()
