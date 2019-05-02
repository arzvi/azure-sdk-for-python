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

from msrest.serialization import Model


class PatchObject(Model):
    """Data contract for patch.

    :param status: Indicates if the given action rule is enabled or disabled.
     Possible values include: 'Enabled', 'Disabled'
    :type status: str or ~azure.mgmt.alertsmanagement.models.ActionRuleStatus
    :param tags: tags to be updated
    :type tags: object
    """

    _attribute_map = {
        'status': {'key': 'properties.status', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(PatchObject, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.tags = kwargs.get('tags', None)
