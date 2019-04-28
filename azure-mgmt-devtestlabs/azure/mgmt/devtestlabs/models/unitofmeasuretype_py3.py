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


class Unitofmeasuretype(Model):
    """Unitofmeasuretype.

    :param code: The code property for the unitofmeasuretype entity
    :type code: str
    :param display_name: The displayName property for the unitofmeasuretype
     entity
    :type display_name: str
    :param symbol: The symbol property for the unitofmeasuretype entity
    :type symbol: str
    :param unit_conversion:
    :type unit_conversion:
     ~azure.mgmt.devtestlabs.models.Itemunitofmeasureconversiontype
    :param picture:
    :type picture: list[~azure.mgmt.devtestlabs.models.Picture]
    :param default_dimensions:
    :type default_dimensions:
     list[~azure.mgmt.devtestlabs.models.DefaultDimensions]
    :param item_category:
    :type item_category: ~azure.mgmt.devtestlabs.models.ItemCategory
    """

    _validation = {
        'code': {'max_length': 10},
        'display_name': {'max_length': 50},
        'symbol': {'max_length': 10},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'symbol': {'key': 'symbol', 'type': 'str'},
        'unit_conversion': {'key': 'unitConversion', 'type': 'Itemunitofmeasureconversiontype'},
        'picture': {'key': 'picture', 'type': '[Picture]'},
        'default_dimensions': {'key': 'defaultDimensions', 'type': '[DefaultDimensions]'},
        'item_category': {'key': 'itemCategory', 'type': 'ItemCategory'},
    }

    def __init__(self, *, code: str=None, display_name: str=None, symbol: str=None, unit_conversion=None, picture=None, default_dimensions=None, item_category=None, **kwargs) -> None:
        super(Unitofmeasuretype, self).__init__(**kwargs)
        self.code = code
        self.display_name = display_name
        self.symbol = symbol
        self.unit_conversion = unit_conversion
        self.picture = picture
        self.default_dimensions = default_dimensions
        self.item_category = item_category
