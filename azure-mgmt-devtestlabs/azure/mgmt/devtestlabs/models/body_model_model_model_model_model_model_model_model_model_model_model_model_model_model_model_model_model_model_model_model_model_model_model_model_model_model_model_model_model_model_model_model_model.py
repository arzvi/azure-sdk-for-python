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


class BodyModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModel(Model):
    """BodyModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModel.

    :param id: The id property for the purchaseInvoiceLine entity
    :type id: str
    :param document_id: The documentId property for the purchaseInvoiceLine
     entity
    :type document_id: str
    :param sequence: The sequence property for the purchaseInvoiceLine entity
    :type sequence: int
    :param item_id: The itemId property for the purchaseInvoiceLine entity
    :type item_id: str
    :param account_id: The accountId property for the purchaseInvoiceLine
     entity
    :type account_id: str
    :param line_type: The lineType property for the purchaseInvoiceLine entity
    :type line_type: str
    :param line_details:
    :type line_details:
     ~azure.mgmt.devtestlabs.models.Documentlineobjectdetailstype
    :param description: The description property for the purchaseInvoiceLine
     entity
    :type description: str
    :param unit_of_measure:
    :type unit_of_measure: ~azure.mgmt.devtestlabs.models.Unitofmeasuretype
    :param unit_cost: The unitCost property for the purchaseInvoiceLine entity
    :type unit_cost: decimal.Decimal
    :param quantity: The quantity property for the purchaseInvoiceLine entity
    :type quantity: decimal.Decimal
    :param discount_amount: The discountAmount property for the
     purchaseInvoiceLine entity
    :type discount_amount: decimal.Decimal
    :param discount_percent: The discountPercent property for the
     purchaseInvoiceLine entity
    :type discount_percent: decimal.Decimal
    :param discount_applied_before_tax: The discountAppliedBeforeTax property
     for the purchaseInvoiceLine entity
    :type discount_applied_before_tax: bool
    :param amount_excluding_tax: The amountExcludingTax property for the
     purchaseInvoiceLine entity
    :type amount_excluding_tax: decimal.Decimal
    :param tax_code: The taxCode property for the purchaseInvoiceLine entity
    :type tax_code: str
    :param tax_percent: The taxPercent property for the purchaseInvoiceLine
     entity
    :type tax_percent: decimal.Decimal
    :param total_tax_amount: The totalTaxAmount property for the
     purchaseInvoiceLine entity
    :type total_tax_amount: decimal.Decimal
    :param amount_including_tax: The amountIncludingTax property for the
     purchaseInvoiceLine entity
    :type amount_including_tax: decimal.Decimal
    :param invoice_discount_allocation: The invoiceDiscountAllocation property
     for the purchaseInvoiceLine entity
    :type invoice_discount_allocation: decimal.Decimal
    :param net_amount: The netAmount property for the purchaseInvoiceLine
     entity
    :type net_amount: decimal.Decimal
    :param net_tax_amount: The netTaxAmount property for the
     purchaseInvoiceLine entity
    :type net_tax_amount: decimal.Decimal
    :param net_amount_including_tax: The netAmountIncludingTax property for
     the purchaseInvoiceLine entity
    :type net_amount_including_tax: decimal.Decimal
    :param expected_receipt_date: The expectedReceiptDate property for the
     purchaseInvoiceLine entity
    :type expected_receipt_date: datetime
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
        'unit_of_measure': {'key': 'unitOfMeasure', 'type': 'Unitofmeasuretype'},
        'unit_cost': {'key': 'unitCost', 'type': 'decimal'},
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
        'expected_receipt_date': {'key': 'expectedReceiptDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(BodyModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModel, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.document_id = kwargs.get('document_id', None)
        self.sequence = kwargs.get('sequence', None)
        self.item_id = kwargs.get('item_id', None)
        self.account_id = kwargs.get('account_id', None)
        self.line_type = kwargs.get('line_type', None)
        self.line_details = kwargs.get('line_details', None)
        self.description = kwargs.get('description', None)
        self.unit_of_measure = kwargs.get('unit_of_measure', None)
        self.unit_cost = kwargs.get('unit_cost', None)
        self.quantity = kwargs.get('quantity', None)
        self.discount_amount = kwargs.get('discount_amount', None)
        self.discount_percent = kwargs.get('discount_percent', None)
        self.discount_applied_before_tax = kwargs.get('discount_applied_before_tax', None)
        self.amount_excluding_tax = kwargs.get('amount_excluding_tax', None)
        self.tax_code = kwargs.get('tax_code', None)
        self.tax_percent = kwargs.get('tax_percent', None)
        self.total_tax_amount = kwargs.get('total_tax_amount', None)
        self.amount_including_tax = kwargs.get('amount_including_tax', None)
        self.invoice_discount_allocation = kwargs.get('invoice_discount_allocation', None)
        self.net_amount = kwargs.get('net_amount', None)
        self.net_tax_amount = kwargs.get('net_tax_amount', None)
        self.net_amount_including_tax = kwargs.get('net_amount_including_tax', None)
        self.expected_receipt_date = kwargs.get('expected_receipt_date', None)
