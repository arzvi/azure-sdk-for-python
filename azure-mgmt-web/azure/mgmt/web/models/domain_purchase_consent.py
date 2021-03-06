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


class DomainPurchaseConsent(Model):
    """Domain purchase consent object, representing acceptance of applicable legal
    agreements.

    :param agreement_keys: List of applicable legal agreement keys. This list
     can be retrieved using ListLegalAgreements API under
     <code>TopLevelDomain</code> resource.
    :type agreement_keys: list[str]
    :param agreed_by: Client IP address.
    :type agreed_by: str
    :param agreed_at: Timestamp when the agreements were accepted.
    :type agreed_at: datetime
    """

    _attribute_map = {
        'agreement_keys': {'key': 'agreementKeys', 'type': '[str]'},
        'agreed_by': {'key': 'agreedBy', 'type': 'str'},
        'agreed_at': {'key': 'agreedAt', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(DomainPurchaseConsent, self).__init__(**kwargs)
        self.agreement_keys = kwargs.get('agreement_keys', None)
        self.agreed_by = kwargs.get('agreed_by', None)
        self.agreed_at = kwargs.get('agreed_at', None)
