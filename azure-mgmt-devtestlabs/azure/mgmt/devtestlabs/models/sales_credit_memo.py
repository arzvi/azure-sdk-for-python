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


class SalesCreditMemo(Model):
    """SalesCreditMemo.

    :param id: The id property for the salesCreditMemo entity
    :type id: str
    :param number: The number property for the salesCreditMemo entity
    :type number: str
    :param external_document_number: The externalDocumentNumber property for
     the salesCreditMemo entity
    :type external_document_number: str
    :param credit_memo_date: The creditMemoDate property for the
     salesCreditMemo entity
    :type credit_memo_date: datetime
    :param due_date: The dueDate property for the salesCreditMemo entity
    :type due_date: datetime
    :param customer_id: The customerId property for the salesCreditMemo entity
    :type customer_id: str
    :param contact_id: The contactId property for the salesCreditMemo entity
    :type contact_id: str
    :param customer_number: The customerNumber property for the
     salesCreditMemo entity
    :type customer_number: str
    :param customer_name: The customerName property for the salesCreditMemo
     entity
    :type customer_name: str
    :param bill_to_name: The billToName property for the salesCreditMemo
     entity
    :type bill_to_name: str
    :param bill_to_customer_id: The billToCustomerId property for the
     salesCreditMemo entity
    :type bill_to_customer_id: str
    :param bill_to_customer_number: The billToCustomerNumber property for the
     salesCreditMemo entity
    :type bill_to_customer_number: str
    :param selling_postal_address:
    :type selling_postal_address:
     ~azure.mgmt.devtestlabs.models.Postaladdresstype
    :param billing_postal_address:
    :type billing_postal_address:
     ~azure.mgmt.devtestlabs.models.Postaladdresstype
    :param currency_id: The currencyId property for the salesCreditMemo entity
    :type currency_id: str
    :param currency_code: The currencyCode property for the salesCreditMemo
     entity
    :type currency_code: str
    :param payment_terms_id: The paymentTermsId property for the
     salesCreditMemo entity
    :type payment_terms_id: str
    :param salesperson: The salesperson property for the salesCreditMemo
     entity
    :type salesperson: str
    :param prices_include_tax: The pricesIncludeTax property for the
     salesCreditMemo entity
    :type prices_include_tax: bool
    :param discount_amount: The discountAmount property for the
     salesCreditMemo entity
    :type discount_amount: decimal.Decimal
    :param discount_applied_before_tax: The discountAppliedBeforeTax property
     for the salesCreditMemo entity
    :type discount_applied_before_tax: bool
    :param total_amount_excluding_tax: The totalAmountExcludingTax property
     for the salesCreditMemo entity
    :type total_amount_excluding_tax: decimal.Decimal
    :param total_tax_amount: The totalTaxAmount property for the
     salesCreditMemo entity
    :type total_tax_amount: decimal.Decimal
    :param total_amount_including_tax: The totalAmountIncludingTax property
     for the salesCreditMemo entity
    :type total_amount_including_tax: decimal.Decimal
    :param status: The status property for the salesCreditMemo entity
    :type status: str
    :param last_modified_date_time: The lastModifiedDateTime property for the
     salesCreditMemo entity
    :type last_modified_date_time: datetime
    :param invoice_id: The invoiceId property for the salesCreditMemo entity
    :type invoice_id: str
    :param invoice_number: The invoiceNumber property for the salesCreditMemo
     entity
    :type invoice_number: str
    :param phone_number: The phoneNumber property for the salesCreditMemo
     entity
    :type phone_number: str
    :param email: The email property for the salesCreditMemo entity
    :type email: str
    :param sales_credit_memo_lines:
    :type sales_credit_memo_lines:
     list[~azure.mgmt.devtestlabs.models.SalesCreditMemoLine]
    :param pdf_document:
    :type pdf_document: list[~azure.mgmt.devtestlabs.models.PdfDocument]
    :param customer:
    :type customer: ~azure.mgmt.devtestlabs.models.Customer
    :param currency:
    :type currency: ~azure.mgmt.devtestlabs.models.Currency
    :param payment_term:
    :type payment_term: ~azure.mgmt.devtestlabs.models.PaymentTerm
    """

    _validation = {
        'number': {'max_length': 20},
        'external_document_number': {'max_length': 35},
        'contact_id': {'max_length': 250},
        'customer_number': {'max_length': 20},
        'customer_name': {'max_length': 100},
        'bill_to_name': {'max_length': 100},
        'bill_to_customer_number': {'max_length': 20},
        'salesperson': {'max_length': 20},
        'invoice_number': {'max_length': 20},
        'phone_number': {'max_length': 30},
        'email': {'max_length': 80},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'number': {'key': 'number', 'type': 'str'},
        'external_document_number': {'key': 'externalDocumentNumber', 'type': 'str'},
        'credit_memo_date': {'key': 'creditMemoDate', 'type': 'iso-8601'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'customer_id': {'key': 'customerId', 'type': 'str'},
        'contact_id': {'key': 'contactId', 'type': 'str'},
        'customer_number': {'key': 'customerNumber', 'type': 'str'},
        'customer_name': {'key': 'customerName', 'type': 'str'},
        'bill_to_name': {'key': 'billToName', 'type': 'str'},
        'bill_to_customer_id': {'key': 'billToCustomerId', 'type': 'str'},
        'bill_to_customer_number': {'key': 'billToCustomerNumber', 'type': 'str'},
        'selling_postal_address': {'key': 'sellingPostalAddress', 'type': 'Postaladdresstype'},
        'billing_postal_address': {'key': 'billingPostalAddress', 'type': 'Postaladdresstype'},
        'currency_id': {'key': 'currencyId', 'type': 'str'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'payment_terms_id': {'key': 'paymentTermsId', 'type': 'str'},
        'salesperson': {'key': 'salesperson', 'type': 'str'},
        'prices_include_tax': {'key': 'pricesIncludeTax', 'type': 'bool'},
        'discount_amount': {'key': 'discountAmount', 'type': 'decimal'},
        'discount_applied_before_tax': {'key': 'discountAppliedBeforeTax', 'type': 'bool'},
        'total_amount_excluding_tax': {'key': 'totalAmountExcludingTax', 'type': 'decimal'},
        'total_tax_amount': {'key': 'totalTaxAmount', 'type': 'decimal'},
        'total_amount_including_tax': {'key': 'totalAmountIncludingTax', 'type': 'decimal'},
        'status': {'key': 'status', 'type': 'str'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'invoice_id': {'key': 'invoiceId', 'type': 'str'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'sales_credit_memo_lines': {'key': 'salesCreditMemoLines', 'type': '[SalesCreditMemoLine]'},
        'pdf_document': {'key': 'pdfDocument', 'type': '[PdfDocument]'},
        'customer': {'key': 'customer', 'type': 'Customer'},
        'currency': {'key': 'currency', 'type': 'Currency'},
        'payment_term': {'key': 'paymentTerm', 'type': 'PaymentTerm'},
    }

    def __init__(self, **kwargs):
        super(SalesCreditMemo, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.number = kwargs.get('number', None)
        self.external_document_number = kwargs.get('external_document_number', None)
        self.credit_memo_date = kwargs.get('credit_memo_date', None)
        self.due_date = kwargs.get('due_date', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.contact_id = kwargs.get('contact_id', None)
        self.customer_number = kwargs.get('customer_number', None)
        self.customer_name = kwargs.get('customer_name', None)
        self.bill_to_name = kwargs.get('bill_to_name', None)
        self.bill_to_customer_id = kwargs.get('bill_to_customer_id', None)
        self.bill_to_customer_number = kwargs.get('bill_to_customer_number', None)
        self.selling_postal_address = kwargs.get('selling_postal_address', None)
        self.billing_postal_address = kwargs.get('billing_postal_address', None)
        self.currency_id = kwargs.get('currency_id', None)
        self.currency_code = kwargs.get('currency_code', None)
        self.payment_terms_id = kwargs.get('payment_terms_id', None)
        self.salesperson = kwargs.get('salesperson', None)
        self.prices_include_tax = kwargs.get('prices_include_tax', None)
        self.discount_amount = kwargs.get('discount_amount', None)
        self.discount_applied_before_tax = kwargs.get('discount_applied_before_tax', None)
        self.total_amount_excluding_tax = kwargs.get('total_amount_excluding_tax', None)
        self.total_tax_amount = kwargs.get('total_tax_amount', None)
        self.total_amount_including_tax = kwargs.get('total_amount_including_tax', None)
        self.status = kwargs.get('status', None)
        self.last_modified_date_time = kwargs.get('last_modified_date_time', None)
        self.invoice_id = kwargs.get('invoice_id', None)
        self.invoice_number = kwargs.get('invoice_number', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.email = kwargs.get('email', None)
        self.sales_credit_memo_lines = kwargs.get('sales_credit_memo_lines', None)
        self.pdf_document = kwargs.get('pdf_document', None)
        self.customer = kwargs.get('customer', None)
        self.currency = kwargs.get('currency', None)
        self.payment_term = kwargs.get('payment_term', None)
