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


class TaskInstance(object):
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
        'task_instance_id': 'str',
        'correlation_id': 'str',
        'states': 'list[State]',
        'transitions': 'list[Transition]',
        'triggers': 'list[Trigger]',
        'active_state': 'str',
        'status': 'Status',
        'terminal_state': 'bool',
        'created': 'str',
        'updated': 'str',
        'last_transition': 'str',
        'fields': 'list[FieldInstance]',
        'receivers': 'list[str]',
        'history': 'list[HistoryEntry]'
    }

    attribute_map = {
        'task_definition_id': 'taskDefinitionId',
        'task_instance_id': 'taskInstanceId',
        'correlation_id': 'correlationId',
        'states': 'states',
        'transitions': 'transitions',
        'triggers': 'triggers',
        'active_state': 'activeState',
        'status': 'status',
        'terminal_state': 'terminalState',
        'created': 'created',
        'updated': 'updated',
        'last_transition': 'lastTransition',
        'fields': 'fields',
        'receivers': 'receivers',
        'history': 'history'
    }

    required_map = {
        'task_definition_id': 'optional',
        'task_instance_id': 'optional',
        'correlation_id': 'optional',
        'states': 'optional',
        'transitions': 'optional',
        'triggers': 'optional',
        'active_state': 'optional',
        'status': 'optional',
        'terminal_state': 'optional',
        'created': 'optional',
        'updated': 'optional',
        'last_transition': 'optional',
        'fields': 'optional',
        'receivers': 'optional',
        'history': 'optional'
    }

    def __init__(self, task_definition_id=None, task_instance_id=None, correlation_id=None, states=None, transitions=None, triggers=None, active_state=None, status=None, terminal_state=None, created=None, updated=None, last_transition=None, fields=None, receivers=None, history=None, local_vars_configuration=None):  # noqa: E501
        """TaskInstance - a model defined in OpenAPI"
        
        :param task_definition_id: 
        :type task_definition_id: lusid_workflow.TaskDefinitionId
        :param task_instance_id:  The unique id for this Task Instance
        :type task_instance_id: str
        :param correlation_id:  User-provided ID used to link entities and tasks
        :type correlation_id: str
        :param states:  States
        :type states: list[lusid_workflow.State]
        :param transitions:  Transitions
        :type transitions: list[lusid_workflow.Transition]
        :param triggers:  Triggers
        :type triggers: list[lusid_workflow.Trigger]
        :param active_state:  Currently Active State
        :type active_state: str
        :param status: 
        :type status: lusid_workflow.Status
        :param terminal_state:  True if no onward transitions are possible
        :type terminal_state: bool
        :param created:  Creation timestamp
        :type created: str
        :param updated:  Last Update timestamp
        :type updated: str
        :param last_transition:  Last Transition timestamp
        :type last_transition: str
        :param fields:  Fields and their latest values - should correspond with the Task Definition field schema
        :type fields: list[lusid_workflow.FieldInstance]
        :param receivers:  A list of downstream Tasks to be invoked on completion
        :type receivers: list[str]
        :param history:  A list of timestamped messages detailing what has occurred to this Task
        :type history: list[lusid_workflow.HistoryEntry]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._task_definition_id = None
        self._task_instance_id = None
        self._correlation_id = None
        self._states = None
        self._transitions = None
        self._triggers = None
        self._active_state = None
        self._status = None
        self._terminal_state = None
        self._created = None
        self._updated = None
        self._last_transition = None
        self._fields = None
        self._receivers = None
        self._history = None
        self.discriminator = None

        if task_definition_id is not None:
            self.task_definition_id = task_definition_id
        if task_instance_id is not None:
            self.task_instance_id = task_instance_id
        self.correlation_id = correlation_id
        self.states = states
        self.transitions = transitions
        self.triggers = triggers
        self.active_state = active_state
        if status is not None:
            self.status = status
        if terminal_state is not None:
            self.terminal_state = terminal_state
        self.created = created
        self.updated = updated
        self.last_transition = last_transition
        self.fields = fields
        self.receivers = receivers
        self.history = history

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this TaskInstance.  # noqa: E501


        :return: The task_definition_id of this TaskInstance.  # noqa: E501
        :rtype: lusid_workflow.TaskDefinitionId
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this TaskInstance.


        :param task_definition_id: The task_definition_id of this TaskInstance.  # noqa: E501
        :type task_definition_id: lusid_workflow.TaskDefinitionId
        """

        self._task_definition_id = task_definition_id

    @property
    def task_instance_id(self):
        """Gets the task_instance_id of this TaskInstance.  # noqa: E501

        The unique id for this Task Instance  # noqa: E501

        :return: The task_instance_id of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, task_instance_id):
        """Sets the task_instance_id of this TaskInstance.

        The unique id for this Task Instance  # noqa: E501

        :param task_instance_id: The task_instance_id of this TaskInstance.  # noqa: E501
        :type task_instance_id: str
        """

        self._task_instance_id = task_instance_id

    @property
    def correlation_id(self):
        """Gets the correlation_id of this TaskInstance.  # noqa: E501

        User-provided ID used to link entities and tasks  # noqa: E501

        :return: The correlation_id of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this TaskInstance.

        User-provided ID used to link entities and tasks  # noqa: E501

        :param correlation_id: The correlation_id of this TaskInstance.  # noqa: E501
        :type correlation_id: str
        """

        self._correlation_id = correlation_id

    @property
    def states(self):
        """Gets the states of this TaskInstance.  # noqa: E501

        States  # noqa: E501

        :return: The states of this TaskInstance.  # noqa: E501
        :rtype: list[lusid_workflow.State]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this TaskInstance.

        States  # noqa: E501

        :param states: The states of this TaskInstance.  # noqa: E501
        :type states: list[lusid_workflow.State]
        """

        self._states = states

    @property
    def transitions(self):
        """Gets the transitions of this TaskInstance.  # noqa: E501

        Transitions  # noqa: E501

        :return: The transitions of this TaskInstance.  # noqa: E501
        :rtype: list[lusid_workflow.Transition]
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        """Sets the transitions of this TaskInstance.

        Transitions  # noqa: E501

        :param transitions: The transitions of this TaskInstance.  # noqa: E501
        :type transitions: list[lusid_workflow.Transition]
        """

        self._transitions = transitions

    @property
    def triggers(self):
        """Gets the triggers of this TaskInstance.  # noqa: E501

        Triggers  # noqa: E501

        :return: The triggers of this TaskInstance.  # noqa: E501
        :rtype: list[lusid_workflow.Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this TaskInstance.

        Triggers  # noqa: E501

        :param triggers: The triggers of this TaskInstance.  # noqa: E501
        :type triggers: list[lusid_workflow.Trigger]
        """

        self._triggers = triggers

    @property
    def active_state(self):
        """Gets the active_state of this TaskInstance.  # noqa: E501

        Currently Active State  # noqa: E501

        :return: The active_state of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._active_state

    @active_state.setter
    def active_state(self, active_state):
        """Sets the active_state of this TaskInstance.

        Currently Active State  # noqa: E501

        :param active_state: The active_state of this TaskInstance.  # noqa: E501
        :type active_state: str
        """

        self._active_state = active_state

    @property
    def status(self):
        """Gets the status of this TaskInstance.  # noqa: E501


        :return: The status of this TaskInstance.  # noqa: E501
        :rtype: lusid_workflow.Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskInstance.


        :param status: The status of this TaskInstance.  # noqa: E501
        :type status: lusid_workflow.Status
        """

        self._status = status

    @property
    def terminal_state(self):
        """Gets the terminal_state of this TaskInstance.  # noqa: E501

        True if no onward transitions are possible  # noqa: E501

        :return: The terminal_state of this TaskInstance.  # noqa: E501
        :rtype: bool
        """
        return self._terminal_state

    @terminal_state.setter
    def terminal_state(self, terminal_state):
        """Sets the terminal_state of this TaskInstance.

        True if no onward transitions are possible  # noqa: E501

        :param terminal_state: The terminal_state of this TaskInstance.  # noqa: E501
        :type terminal_state: bool
        """

        self._terminal_state = terminal_state

    @property
    def created(self):
        """Gets the created of this TaskInstance.  # noqa: E501

        Creation timestamp  # noqa: E501

        :return: The created of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TaskInstance.

        Creation timestamp  # noqa: E501

        :param created: The created of this TaskInstance.  # noqa: E501
        :type created: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this TaskInstance.  # noqa: E501

        Last Update timestamp  # noqa: E501

        :return: The updated of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TaskInstance.

        Last Update timestamp  # noqa: E501

        :param updated: The updated of this TaskInstance.  # noqa: E501
        :type updated: str
        """

        self._updated = updated

    @property
    def last_transition(self):
        """Gets the last_transition of this TaskInstance.  # noqa: E501

        Last Transition timestamp  # noqa: E501

        :return: The last_transition of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_transition

    @last_transition.setter
    def last_transition(self, last_transition):
        """Sets the last_transition of this TaskInstance.

        Last Transition timestamp  # noqa: E501

        :param last_transition: The last_transition of this TaskInstance.  # noqa: E501
        :type last_transition: str
        """

        self._last_transition = last_transition

    @property
    def fields(self):
        """Gets the fields of this TaskInstance.  # noqa: E501

        Fields and their latest values - should correspond with the Task Definition field schema  # noqa: E501

        :return: The fields of this TaskInstance.  # noqa: E501
        :rtype: list[lusid_workflow.FieldInstance]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this TaskInstance.

        Fields and their latest values - should correspond with the Task Definition field schema  # noqa: E501

        :param fields: The fields of this TaskInstance.  # noqa: E501
        :type fields: list[lusid_workflow.FieldInstance]
        """

        self._fields = fields

    @property
    def receivers(self):
        """Gets the receivers of this TaskInstance.  # noqa: E501

        A list of downstream Tasks to be invoked on completion  # noqa: E501

        :return: The receivers of this TaskInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._receivers

    @receivers.setter
    def receivers(self, receivers):
        """Sets the receivers of this TaskInstance.

        A list of downstream Tasks to be invoked on completion  # noqa: E501

        :param receivers: The receivers of this TaskInstance.  # noqa: E501
        :type receivers: list[str]
        """

        self._receivers = receivers

    @property
    def history(self):
        """Gets the history of this TaskInstance.  # noqa: E501

        A list of timestamped messages detailing what has occurred to this Task  # noqa: E501

        :return: The history of this TaskInstance.  # noqa: E501
        :rtype: list[lusid_workflow.HistoryEntry]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this TaskInstance.

        A list of timestamped messages detailing what has occurred to this Task  # noqa: E501

        :param history: The history of this TaskInstance.  # noqa: E501
        :type history: list[lusid_workflow.HistoryEntry]
        """

        self._history = history

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
        if not isinstance(other, TaskInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskInstance):
            return True

        return self.to_dict() != other.to_dict()
