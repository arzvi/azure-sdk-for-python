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


class SslConfiguration(Model):
    """The SSL configuration for scoring.

    :param status: Enable or disable SSL for scoring. Possible values include:
     'Disabled', 'Enabled'
    :type status: str or ~azure.mgmt.machinelearningservices.models.enum
    :param cert: Cert data
    :type cert: str
    :param key: Key data
    :type key: str
    :param cname: CNAME of the cert
    :type cname: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'cert': {'key': 'cert', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'cname': {'key': 'cname', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SslConfiguration, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.cert = kwargs.get('cert', None)
        self.key = kwargs.get('key', None)
        self.cname = kwargs.get('cname', None)