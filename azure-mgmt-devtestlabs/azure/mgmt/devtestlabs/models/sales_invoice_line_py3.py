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


class SalesInvoiceLine(Model):
    """SalesInvoiceLine.

    :param id: The id property for the salesInvoiceLine entity
    :type id: str
    :param document_id: The documentId property for the salesInvoiceLine
     entity
    :type document_id: str
    :param sequence: The sequence property for the salesInvoiceLine entity
    :type sequence: int
    :param item_id: The itemId property for the salesInvoiceLine entity
    :type item_id: str
    :param account_id: The accountId property for the salesInvoiceLine entity
    :type account_id: str
    :param line_type: The lineType property for the salesInvoiceLine entity
    :type line_type: str
    :param line_details:
    :type line_details:
     ~azure.mgmt.devtestlabs.models.Documentlineobjectdetailstype
    :param description: The description property for the salesInvoiceLine
     entity
    :type description: str
    :param unit_of_measure_id: The unitOfMeasureId property for the
     salesInvoiceLine entity
    :type unit_of_measure_id: str
    :param unit_of_measure:
    :type unit_of_measure: ~azure.mgmt.devtestlabs.models.Unitofmeasuretype
    :param unit_price: The unitPrice property for the salesInvoiceLine entity
    :type unit_price: decimal.Decimal
    :param quantity: The quantity property for the salesInvoiceLine entity
    :type quantity: decimal.Decimal
    :param discount_amount: The discountAmount property for the
     salesInvoiceLine entity
    :type discount_amount: decimal.Decimal
    :param discount_percent: The discountPercent property for the
     salesInvoiceLine entity
    :type discount_percent: decimal.Decimal
    :param discount_applied_before_tax: The discountAppliedBeforeTax property
     for the salesInvoiceLine entity
    :type discount_applied_before_tax: bool
    :param amount_excluding_tax: The amountExcludingTax property for the
     salesInvoiceLine entity
    :type amount_excluding_tax: decimal.Decimal
    :param tax_code: The taxCode property for the salesInvoiceLine entity
    :type tax_code: str
    :param tax_percent: The taxPercent property for the salesInvoiceLine
     entity
    :type tax_percent: decimal.Decimal
    :param total_tax_amount: The totalTaxAmount property for the
     salesInvoiceLine entity
    :type total_tax_amount: decimal.Decimal
    :param amount_including_tax: The amountIncludingTax property for the
     salesInvoiceLine entity
    :type amount_including_tax: decimal.Decimal
    :param invoice_discount_allocation: The invoiceDiscountAllocation property
     for the salesInvoiceLine entity
    :type invoice_discount_allocation: decimal.Decimal
    :param net_amount: The netAmount property for the salesInvoiceLine entity
    :type net_amount: decimal.Decimal
    :param net_tax_amount: The netTaxAmount property for the salesInvoiceLine
     entity
    :type net_tax_amount: decimal.Decimal
    :param net_amount_including_tax: The netAmountIncludingTax property for
     the salesInvoiceLine entity
    :type net_amount_including_tax: decimal.Decimal
    :param shipment_date: The shipmentDate property for the salesInvoiceLine
     entity
    :type shipment_date: datetime
    :param item:
    :type item: ~azure.mgmt.devtestlabs.models.Item
    :param account:
    :type account: ~azure.mgmt.devtestlabs.models.Account
    """

    _validation = {
        'id': {'max_length': 50},
        'description': {'max_length': 100},
        'tax_code': {'max_length': 50},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'document_id': {'key': 'documentId', 'type': 'str'},
        'sequence': {'key': 'sequence', 'type': 'int'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'line_type': {'key': 'lineType', 'type': 'str'},
        'line_details': {'key': 'lineDetails', 'type': 'Documentlineobjectdetailstype'},
        'description': {'key': 'description', 'type': 'str'},
        'unit_of_measure_id': {'key': 'unitOfMeasureId', 'type': 'str'},
        'unit_of_measure': {'key': 'unitOfMeasure', 'type': 'Unitofmeasuretype'},
        'unit_price': {'key': 'unitPrice', 'type': 'decimal'},
        'quantity': {'key': 'quantity', 'type': 'decimal'},
        'discount_amount': {'key': 'discountAmount', 'type': 'decimal'},
        'discount_percent': {'key': 'discountPercent', 'type': 'decimal'},
        'discount_applied_before_tax': {'key': 'discountAppliedBeforeTax', 'type': 'bool'},
        'amount_excluding_tax': {'key': 'amountExcludingTax', 'type': 'decimal'},
        'tax_code': {'key': 'taxCode', 'type': 'str'},
        'tax_percent': {'key': 'taxPercent', 'type': 'decimal'},
        'total_tax_amount': {'key': 'totalTaxAmount', 'type': 'decimal'},
        'amount_including_tax': {'key': 'amountIncludingTax', 'type': 'decimal'},
        'invoice_discount_allocation': {'key': 'invoiceDiscountAllocation', 'type': 'decimal'},
        'net_amount': {'key': 'netAmount', 'type': 'decimal'},
        'net_tax_amount': {'key': 'netTaxAmount', 'type': 'decimal'},
        'net_amount_including_tax': {'key': 'netAmountIncludingTax', 'type': 'decimal'},
        'shipment_date': {'key': 'shipmentDate', 'type': 'iso-8601'},
        'item': {'key': 'item', 'type': 'Item'},
        'account': {'key': 'account', 'type': 'Account'},
    }

    def __init__(self, *, id: str=None, document_id: str=None, sequence: int=None, item_id: str=None, account_id: str=None, line_type: str=None, line_details=None, description: str=None, unit_of_measure_id: str=None, unit_of_measure=None, unit_price=None, quantity=None, discount_amount=None, discount_percent=None, discount_applied_before_tax: bool=None, amount_excluding_tax=None, tax_code: str=None, tax_percent=None, total_tax_amount=None, amount_including_tax=None, invoice_discount_allocation=None, net_amount=None, net_tax_amount=None, net_amount_including_tax=None, shipment_date=None, item=None, account=None, **kwargs) -> None:
        super(SalesInvoiceLine, self).__init__(**kwargs)
        self.id = id
        self.document_id = document_id
        self.sequence = sequence
        self.item_id = item_id
        self.account_id = account_id
        self.line_type = line_type
        self.line_details = line_details
        self.description = description
        self.unit_of_measure_id = unit_of_measure_id
        self.unit_of_measure = unit_of_measure
        self.unit_price = unit_price
        self.quantity = quantity
        self.discount_amount = discount_amount
        self.discount_percent = discount_percent
        self.discount_applied_before_tax = discount_applied_before_tax
        self.amount_excluding_tax = amount_excluding_tax
        self.tax_code = tax_code
        self.tax_percent = tax_percent
        self.total_tax_amount = total_tax_amount
        self.amount_including_tax = amount_including_tax
        self.invoice_discount_allocation = invoice_discount_allocation
        self.net_amount = net_amount
        self.net_tax_amount = net_tax_amount
        self.net_amount_including_tax = net_amount_including_tax
        self.shipment_date = shipment_date
        self.item = item
        self.account = account
