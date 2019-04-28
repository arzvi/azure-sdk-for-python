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


class VendorPurchase(Model):
    """VendorPurchase.

    :param vendor_id: The vendorId property for the vendorPurchase entity
    :type vendor_id: str
    :param vendor_number: The vendorNumber property for the vendorPurchase
     entity
    :type vendor_number: str
    :param name: The name property for the vendorPurchase entity
    :type name: str
    :param total_purchase_amount: The totalPurchaseAmount property for the
     vendorPurchase entity
    :type total_purchase_amount: decimal.Decimal
    :param date_filter_filter_only: The dateFilter_FilterOnly property for the
     vendorPurchase entity
    :type date_filter_filter_only: datetime
    """

    _validation = {
        'vendor_number': {'max_length': 20},
        'name': {'max_length': 100},
    }

    _attribute_map = {
        'vendor_id': {'key': 'vendorId', 'type': 'str'},
        'vendor_number': {'key': 'vendorNumber', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'total_purchase_amount': {'key': 'totalPurchaseAmount', 'type': 'decimal'},
        'date_filter_filter_only': {'key': 'dateFilter_FilterOnly', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(VendorPurchase, self).__init__(**kwargs)
        self.vendor_id = kwargs.get('vendor_id', None)
        self.vendor_number = kwargs.get('vendor_number', None)
        self.name = kwargs.get('name', None)
        self.total_purchase_amount = kwargs.get('total_purchase_amount', None)
        self.date_filter_filter_only = kwargs.get('date_filter_filter_only', None)
