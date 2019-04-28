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


class Body(Model):
    """Body.

    :param id: The id property for the item entity
    :type id: str
    :param number: The number property for the item entity
    :type number: str
    :param display_name: The displayName property for the item entity
    :type display_name: str
    :param type: The type property for the item entity
    :type type: str
    :param item_category_id: The itemCategoryId property for the item entity
    :type item_category_id: str
    :param item_category_code: The itemCategoryCode property for the item
     entity
    :type item_category_code: str
    :param blocked: The blocked property for the item entity
    :type blocked: bool
    :param base_unit_of_measure_id: The baseUnitOfMeasureId property for the
     item entity
    :type base_unit_of_measure_id: str
    :param base_unit_of_measure:
    :type base_unit_of_measure:
     ~azure.mgmt.devtestlabs.models.Unitofmeasuretype
    :param gtin: The gtin property for the item entity
    :type gtin: str
    :param inventory: The inventory property for the item entity
    :type inventory: decimal.Decimal
    :param unit_price: The unitPrice property for the item entity
    :type unit_price: decimal.Decimal
    :param price_includes_tax: The priceIncludesTax property for the item
     entity
    :type price_includes_tax: bool
    :param unit_cost: The unitCost property for the item entity
    :type unit_cost: decimal.Decimal
    :param tax_group_id: The taxGroupId property for the item entity
    :type tax_group_id: str
    :param tax_group_code: The taxGroupCode property for the item entity
    :type tax_group_code: str
    :param last_modified_date_time: The lastModifiedDateTime property for the
     item entity
    :type last_modified_date_time: datetime
    """

    _validation = {
        'number': {'max_length': 20},
        'display_name': {'max_length': 100},
        'item_category_code': {'max_length': 20},
        'gtin': {'max_length': 14},
        'tax_group_code': {'max_length': 20},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'number': {'key': 'number', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'item_category_id': {'key': 'itemCategoryId', 'type': 'str'},
        'item_category_code': {'key': 'itemCategoryCode', 'type': 'str'},
        'blocked': {'key': 'blocked', 'type': 'bool'},
        'base_unit_of_measure_id': {'key': 'baseUnitOfMeasureId', 'type': 'str'},
        'base_unit_of_measure': {'key': 'baseUnitOfMeasure', 'type': 'Unitofmeasuretype'},
        'gtin': {'key': 'gtin', 'type': 'str'},
        'inventory': {'key': 'inventory', 'type': 'decimal'},
        'unit_price': {'key': 'unitPrice', 'type': 'decimal'},
        'price_includes_tax': {'key': 'priceIncludesTax', 'type': 'bool'},
        'unit_cost': {'key': 'unitCost', 'type': 'decimal'},
        'tax_group_id': {'key': 'taxGroupId', 'type': 'str'},
        'tax_group_code': {'key': 'taxGroupCode', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, id: str=None, number: str=None, display_name: str=None, type: str=None, item_category_id: str=None, item_category_code: str=None, blocked: bool=None, base_unit_of_measure_id: str=None, base_unit_of_measure=None, gtin: str=None, inventory=None, unit_price=None, price_includes_tax: bool=None, unit_cost=None, tax_group_id: str=None, tax_group_code: str=None, last_modified_date_time=None, **kwargs) -> None:
        super(Body, self).__init__(**kwargs)
        self.id = id
        self.number = number
        self.display_name = display_name
        self.type = type
        self.item_category_id = item_category_id
        self.item_category_code = item_category_code
        self.blocked = blocked
        self.base_unit_of_measure_id = base_unit_of_measure_id
        self.base_unit_of_measure = base_unit_of_measure
        self.gtin = gtin
        self.inventory = inventory
        self.unit_price = unit_price
        self.price_includes_tax = price_includes_tax
        self.unit_cost = unit_cost
        self.tax_group_id = tax_group_id
        self.tax_group_code = tax_group_code
        self.last_modified_date_time = last_modified_date_time
