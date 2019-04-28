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


class BodyModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModel(Model):
    """BodyModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModel.

    :param id: The id property for the paymentTerm entity
    :type id: str
    :param code: The code property for the paymentTerm entity
    :type code: str
    :param display_name: The displayName property for the paymentTerm entity
    :type display_name: str
    :param due_date_calculation: The dueDateCalculation property for the
     paymentTerm entity
    :type due_date_calculation: str
    :param discount_date_calculation: The discountDateCalculation property for
     the paymentTerm entity
    :type discount_date_calculation: str
    :param discount_percent: The discountPercent property for the paymentTerm
     entity
    :type discount_percent: decimal.Decimal
    :param calculate_discount_on_credit_memos: The
     calculateDiscountOnCreditMemos property for the paymentTerm entity
    :type calculate_discount_on_credit_memos: bool
    :param last_modified_date_time: The lastModifiedDateTime property for the
     paymentTerm entity
    :type last_modified_date_time: datetime
    """

    _validation = {
        'code': {'max_length': 10},
        'display_name': {'max_length': 100},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'due_date_calculation': {'key': 'dueDateCalculation', 'type': 'str'},
        'discount_date_calculation': {'key': 'discountDateCalculation', 'type': 'str'},
        'discount_percent': {'key': 'discountPercent', 'type': 'decimal'},
        'calculate_discount_on_credit_memos': {'key': 'calculateDiscountOnCreditMemos', 'type': 'bool'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, id: str=None, code: str=None, display_name: str=None, due_date_calculation: str=None, discount_date_calculation: str=None, discount_percent=None, calculate_discount_on_credit_memos: bool=None, last_modified_date_time=None, **kwargs) -> None:
        super(BodyModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModelModel, self).__init__(**kwargs)
        self.id = id
        self.code = code
        self.display_name = display_name
        self.due_date_calculation = due_date_calculation
        self.discount_date_calculation = discount_date_calculation
        self.discount_percent = discount_percent
        self.calculate_discount_on_credit_memos = calculate_discount_on_credit_memos
        self.last_modified_date_time = last_modified_date_time
