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


class MongoIndexOptions(Model):
    """Cosmos DB MongoDB collection index options.

    :param expire_after_seconds: Expire after seconds
    :type expire_after_seconds: int
    :param unique: Is unique or not
    :type unique: bool
    """

    _attribute_map = {
        'expire_after_seconds': {'key': 'expireAfterSeconds', 'type': 'int'},
        'unique': {'key': 'unique', 'type': 'bool'},
    }

    def __init__(self, *, expire_after_seconds: int=None, unique: bool=None, **kwargs) -> None:
        super(MongoIndexOptions, self).__init__(**kwargs)
        self.expire_after_seconds = expire_after_seconds
        self.unique = unique
