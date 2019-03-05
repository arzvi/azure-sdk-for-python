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


class ScaleSettings(Model):
    """scale settings for BatchAI Compute.

    :param max_node_count: Max number of nodes to use
    :type max_node_count: int
    :param min_node_count: Min number of nodes to use
    :type min_node_count: int
    :param auto_scale_enabled: Enable or disable auto scale
    :type auto_scale_enabled: bool
    """

    _attribute_map = {
        'max_node_count': {'key': 'maxNodeCount', 'type': 'int'},
        'min_node_count': {'key': 'minNodeCount', 'type': 'int'},
        'auto_scale_enabled': {'key': 'autoScaleEnabled', 'type': 'bool'},
    }

    def __init__(self, *, max_node_count: int=None, min_node_count: int=None, auto_scale_enabled: bool=None, **kwargs) -> None:
        super(ScaleSettings, self).__init__(**kwargs)
        self.max_node_count = max_node_count
        self.min_node_count = min_node_count
        self.auto_scale_enabled = auto_scale_enabled