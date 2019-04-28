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


class PurchaseInvoice(Model):
    """PurchaseInvoice.

    :param id: The id property for the purchaseInvoice entity
    :type id: str
    :param number: The number property for the purchaseInvoice entity
    :type number: str
    :param invoice_date: The invoiceDate property for the purchaseInvoice
     entity
    :type invoice_date: datetime
    :param due_date: The dueDate property for the purchaseInvoice entity
    :type due_date: datetime
    :param vendor_invoice_number: The vendorInvoiceNumber property for the
     purchaseInvoice entity
    :type vendor_invoice_number: str
    :param vendor_id: The vendorId property for the purchaseInvoice entity
    :type vendor_id: str
    :param vendor_number: The vendorNumber property for the purchaseInvoice
     entity
    :type vendor_number: str
    :param vendor_name: The vendorName property for the purchaseInvoice entity
    :type vendor_name: str
    :param pay_to_name: The payToName property for the purchaseInvoice entity
    :type pay_to_name: str
    :param pay_to_contact: The payToContact property for the purchaseInvoice
     entity
    :type pay_to_contact: str
    :param pay_to_vendor_id: The payToVendorId property for the
     purchaseInvoice entity
    :type pay_to_vendor_id: str
    :param pay_to_vendor_number: The payToVendorNumber property for the
     purchaseInvoice entity
    :type pay_to_vendor_number: str
    :param ship_to_name: The shipToName property for the purchaseInvoice
     entity
    :type ship_to_name: str
    :param ship_to_contact: The shipToContact property for the purchaseInvoice
     entity
    :type ship_to_contact: str
    :param buy_from_address:
    :type buy_from_address: ~azure.mgmt.devtestlabs.models.Postaladdresstype
    :param pay_to_address:
    :type pay_to_address: ~azure.mgmt.devtestlabs.models.Postaladdresstype
    :param ship_to_address:
    :type ship_to_address: ~azure.mgmt.devtestlabs.models.Postaladdresstype
    :param currency_id: The currencyId property for the purchaseInvoice entity
    :type currency_id: str
    :param currency_code: The currencyCode property for the purchaseInvoice
     entity
    :type currency_code: str
    :param prices_include_tax: The pricesIncludeTax property for the
     purchaseInvoice entity
    :type prices_include_tax: bool
    :param discount_amount: The discountAmount property for the
     purchaseInvoice entity
    :type discount_amount: decimal.Decimal
    :param discount_applied_before_tax: The discountAppliedBeforeTax property
     for the purchaseInvoice entity
    :type discount_applied_before_tax: bool
    :param total_amount_excluding_tax: The totalAmountExcludingTax property
     for the purchaseInvoice entity
    :type total_amount_excluding_tax: decimal.Decimal
    :param total_tax_amount: The totalTaxAmount property for the
     purchaseInvoice entity
    :type total_tax_amount: decimal.Decimal
    :param total_amount_including_tax: The totalAmountIncludingTax property
     for the purchaseInvoice entity
    :type total_amount_including_tax: decimal.Decimal
    :param status: The status property for the purchaseInvoice entity
    :type status: str
    :param last_modified_date_time: The lastModifiedDateTime property for the
     purchaseInvoice entity
    :type last_modified_date_time: datetime
    :param purchase_invoice_lines:
    :type purchase_invoice_lines:
     list[~azure.mgmt.devtestlabs.models.PurchaseInvoiceLine]
    :param pdf_document:
    :type pdf_document: list[~azure.mgmt.devtestlabs.models.PdfDocument]
    :param vendor:
    :type vendor: ~azure.mgmt.devtestlabs.models.Vendor
    :param currency:
    :type currency: ~azure.mgmt.devtestlabs.models.Currency
    """

    _validation = {
        'number': {'max_length': 20},
        'vendor_invoice_number': {'max_length': 35},
        'vendor_number': {'max_length': 20},
        'vendor_name': {'max_length': 100},
        'pay_to_name': {'max_length': 100},
        'pay_to_contact': {'max_length': 100},
        'pay_to_vendor_number': {'max_length': 20},
        'ship_to_name': {'max_length': 100},
        'ship_to_contact': {'max_length': 100},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'number': {'key': 'number', 'type': 'str'},
        'invoice_date': {'key': 'invoiceDate', 'type': 'iso-8601'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'vendor_invoice_number': {'key': 'vendorInvoiceNumber', 'type': 'str'},
        'vendor_id': {'key': 'vendorId', 'type': 'str'},
        'vendor_number': {'key': 'vendorNumber', 'type': 'str'},
        'vendor_name': {'key': 'vendorName', 'type': 'str'},
        'pay_to_name': {'key': 'payToName', 'type': 'str'},
        'pay_to_contact': {'key': 'payToContact', 'type': 'str'},
        'pay_to_vendor_id': {'key': 'payToVendorId', 'type': 'str'},
        'pay_to_vendor_number': {'key': 'payToVendorNumber', 'type': 'str'},
        'ship_to_name': {'key': 'shipToName', 'type': 'str'},
        'ship_to_contact': {'key': 'shipToContact', 'type': 'str'},
        'buy_from_address': {'key': 'buyFromAddress', 'type': 'Postaladdresstype'},
        'pay_to_address': {'key': 'payToAddress', 'type': 'Postaladdresstype'},
        'ship_to_address': {'key': 'shipToAddress', 'type': 'Postaladdresstype'},
        'currency_id': {'key': 'currencyId', 'type': 'str'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'prices_include_tax': {'key': 'pricesIncludeTax', 'type': 'bool'},
        'discount_amount': {'key': 'discountAmount', 'type': 'decimal'},
        'discount_applied_before_tax': {'key': 'discountAppliedBeforeTax', 'type': 'bool'},
        'total_amount_excluding_tax': {'key': 'totalAmountExcludingTax', 'type': 'decimal'},
        'total_tax_amount': {'key': 'totalTaxAmount', 'type': 'decimal'},
        'total_amount_including_tax': {'key': 'totalAmountIncludingTax', 'type': 'decimal'},
        'status': {'key': 'status', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'purchase_invoice_lines': {'key': 'purchaseInvoiceLines', 'type': '[PurchaseInvoiceLine]'},
        'pdf_document': {'key': 'pdfDocument', 'type': '[PdfDocument]'},
        'vendor': {'key': 'vendor', 'type': 'Vendor'},
        'currency': {'key': 'currency', 'type': 'Currency'},
    }

    def __init__(self, **kwargs):
        super(PurchaseInvoice, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.number = kwargs.get('number', None)
        self.invoice_date = kwargs.get('invoice_date', None)
        self.due_date = kwargs.get('due_date', None)
        self.vendor_invoice_number = kwargs.get('vendor_invoice_number', None)
        self.vendor_id = kwargs.get('vendor_id', None)
        self.vendor_number = kwargs.get('vendor_number', None)
        self.vendor_name = kwargs.get('vendor_name', None)
        self.pay_to_name = kwargs.get('pay_to_name', None)
        self.pay_to_contact = kwargs.get('pay_to_contact', None)
        self.pay_to_vendor_id = kwargs.get('pay_to_vendor_id', None)
        self.pay_to_vendor_number = kwargs.get('pay_to_vendor_number', None)
        self.ship_to_name = kwargs.get('ship_to_name', None)
        self.ship_to_contact = kwargs.get('ship_to_contact', None)
        self.buy_from_address = kwargs.get('buy_from_address', None)
        self.pay_to_address = kwargs.get('pay_to_address', None)
        self.ship_to_address = kwargs.get('ship_to_address', None)
        self.currency_id = kwargs.get('currency_id', None)
        self.currency_code = kwargs.get('currency_code', None)
        self.prices_include_tax = kwargs.get('prices_include_tax', None)
        self.discount_amount = kwargs.get('discount_amount', None)
        self.discount_applied_before_tax = kwargs.get('discount_applied_before_tax', None)
        self.total_amount_excluding_tax = kwargs.get('total_amount_excluding_tax', None)
        self.total_tax_amount = kwargs.get('total_tax_amount', None)
        self.total_amount_including_tax = kwargs.get('total_amount_including_tax', None)
        self.status = kwargs.get('status', None)
        self.last_modified_date_time = kwargs.get('last_modified_date_time', None)
        self.purchase_invoice_lines = kwargs.get('purchase_invoice_lines', None)
        self.pdf_document = kwargs.get('pdf_document', None)
        self.vendor = kwargs.get('vendor', None)
        self.currency = kwargs.get('currency', None)
