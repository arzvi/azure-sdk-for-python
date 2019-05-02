# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .action_rule_properties import ActionRuleProperties


class ActionGroup(ActionRuleProperties):
    """Action Group based Action Rule.

    Action rule with action group configuration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param scope: scope on which action rule will apply
    :type scope: ~azure.mgmt.alertsmanagement.models.Scope
    :param conditions: conditions on which alerts will be filtered
    :type conditions: ~azure.mgmt.alertsmanagement.models.Conditions
    :param description: Description of action rule
    :type description: str
    :ivar created_at: Creation time of action rule. Date-Time in ISO-8601
     format.
    :vartype created_at: datetime
    :ivar last_modified_at: Last updated time of action rule. Date-Time in
     ISO-8601 format.
    :vartype last_modified_at: datetime
    :ivar created_by: Created by user name.
    :vartype created_by: str
    :ivar last_modified_by: Last modified by user name.
    :vartype last_modified_by: str
    :param status: Indicates if the given action rule is enabled or disabled.
     Possible values include: 'Enabled', 'Disabled'
    :type status: str or ~azure.mgmt.alertsmanagement.models.ActionRuleStatus
    :param type: Required. Constant filled by server.
    :type type: str
    :param action_group_id: Required. Action group to trigger if action rule
     matches
    :type action_group_id: str
    """

    _validation = {
        'created_at': {'readonly': True},
        'last_modified_at': {'readonly': True},
        'created_by': {'readonly': True},
        'last_modified_by': {'readonly': True},
        'type': {'required': True},
        'action_group_id': {'required': True},
    }

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'Scope'},
        'conditions': {'key': 'conditions', 'type': 'Conditions'},
        'description': {'key': 'description', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'action_group_id': {'key': 'actionGroupId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ActionGroup, self).__init__(**kwargs)
        self.action_group_id = kwargs.get('action_group_id', None)
        self.type = 'ActionGroup'
