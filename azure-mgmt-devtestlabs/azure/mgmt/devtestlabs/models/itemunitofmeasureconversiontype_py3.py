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


class Itemunitofmeasureconversiontype(Model):
    """Itemunitofmeasureconversiontype.

    :param to_unit_of_measure: The toUnitOfMeasure property for the
     itemunitofmeasureconversiontype entity
    :type to_unit_of_measure: str
    :param from_to_conversion_rate: The fromToConversionRate property for the
     itemunitofmeasureconversiontype entity
    :type from_to_conversion_rate: decimal.Decimal
    :param picture:
    :type picture: list[~azure.mgmt.devtestlabs.models.Picture]
    :param default_dimensions:
    :type default_dimensions:
     list[~azure.mgmt.devtestlabs.models.DefaultDimensions]
    :param item_category:
    :type item_category: ~azure.mgmt.devtestlabs.models.ItemCategory
    """

    _validation = {
        'to_unit_of_measure': {'max_length': 10},
    }

    _attribute_map = {
        'to_unit_of_measure': {'key': 'toUnitOfMeasure', 'type': 'str'},
        'from_to_conversion_rate': {'key': 'fromToConversionRate', 'type': 'decimal'},
        'picture': {'key': 'picture', 'type': '[Picture]'},
        'default_dimensions': {'key': 'defaultDimensions', 'type': '[DefaultDimensions]'},
        'item_category': {'key': 'itemCategory', 'type': 'ItemCategory'},
    }

    def __init__(self, *, to_unit_of_measure: str=None, from_to_conversion_rate=None, picture=None, default_dimensions=None, item_category=None, **kwargs) -> None:
        super(Itemunitofmeasureconversiontype, self).__init__(**kwargs)
        self.to_unit_of_measure = to_unit_of_measure
        self.from_to_conversion_rate = from_to_conversion_rate
        self.picture = picture
        self.default_dimensions = default_dimensions
        self.item_category = item_category
