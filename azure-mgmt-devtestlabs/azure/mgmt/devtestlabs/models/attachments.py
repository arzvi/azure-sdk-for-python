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


class Attachments(Model):
    """Attachments.

    :param parent_id: The parentId property for the attachments entity
    :type parent_id: str
    :param id: The id property for the attachments entity
    :type id: str
    :param file_name: The fileName property for the attachments entity
    :type file_name: str
    :param byte_size: The byteSize property for the attachments entity
    :type byte_size: int
    :param content: The content property for the attachments entity
    :type content: str
    :param last_modified_date_time: The lastModifiedDateTime property for the
     attachments entity
    :type last_modified_date_time: datetime
    """

    _validation = {
        'file_name': {'max_length': 250},
    }

    _attribute_map = {
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'byte_size': {'key': 'byteSize', 'type': 'int'},
        'content': {'key': 'content', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(Attachments, self).__init__(**kwargs)
        self.parent_id = kwargs.get('parent_id', None)
        self.id = kwargs.get('id', None)
        self.file_name = kwargs.get('file_name', None)
        self.byte_size = kwargs.get('byte_size', None)
        self.content = kwargs.get('content', None)
        self.last_modified_date_time = kwargs.get('last_modified_date_time', None)
