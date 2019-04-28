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


class UnitOfMeasure(Model):
    """UnitOfMeasure.

    :param id: The id property for the unitOfMeasure entity
    :type id: str
    :param code: The code property for the unitOfMeasure entity
    :type code: str
    :param display_name: The displayName property for the unitOfMeasure entity
    :type display_name: str
    :param international_standard_code: The internationalStandardCode property
     for the unitOfMeasure entity
    :type international_standard_code: str
    :param last_modified_date_time: The lastModifiedDateTime property for the
     unitOfMeasure entity
    :type last_modified_date_time: datetime
    """

    _validation = {
        'code': {'max_length': 10},
        'display_name': {'max_length': 50},
        'international_standard_code': {'max_length': 10},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'international_standard_code': {'key': 'internationalStandardCode', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, id: str=None, code: str=None, display_name: str=None, international_standard_code: str=None, last_modified_date_time=None, **kwargs) -> None:
        super(UnitOfMeasure, self).__init__(**kwargs)
        self.id = id
        self.code = code
        self.display_name = display_name
        self.international_standard_code = international_standard_code
        self.last_modified_date_time = last_modified_date_time
