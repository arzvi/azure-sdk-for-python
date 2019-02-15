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


class MigrateSyncCompleteCommandOutput(Model):
    """Output for command that completes sync migration for a database.

    :param errors: List of errors that happened during the command execution
    :type errors: list[~azure.mgmt.datamigration.models.ReportableException]
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ReportableException]'},
    }

    def __init__(self, **kwargs):
        super(MigrateSyncCompleteCommandOutput, self).__init__(**kwargs)
        self.errors = kwargs.get('errors', None)