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


class GetPaymentMethodsOKResponse(Model):
    """GetPaymentMethodsOKResponse.

    :param value:
    :type value: list[~azure.mgmt.devtestlabs.models.PaymentMethod]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PaymentMethod]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(GetPaymentMethodsOKResponse, self).__init__(**kwargs)
        self.value = value
