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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.list_operations import ListOperations
from .operations.list_console_operations import ListConsoleOperations
from .operations.console_operations import ConsoleOperations
from . import models


class MicrosoftSerialConsoleClientConfiguration(AzureConfiguration):
    """Configuration for MicrosoftSerialConsoleClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(MicrosoftSerialConsoleClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-serialconsole/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class MicrosoftSerialConsoleClient(SDKClient):
    """Azure Virtual Machine Serial Console allows you to access serial console of a Virtual Machine

    :ivar config: Configuration for client.
    :vartype config: MicrosoftSerialConsoleClientConfiguration

    :ivar list: List operations
    :vartype list: azure.mgmt.serialconsole.operations.ListOperations
    :ivar list_console: ListConsole operations
    :vartype list_console: azure.mgmt.serialconsole.operations.ListConsoleOperations
    :ivar console: Console operations
    :vartype console: azure.mgmt.serialconsole.operations.ConsoleOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MicrosoftSerialConsoleClientConfiguration(credentials, subscription_id, base_url)
        super(MicrosoftSerialConsoleClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-05-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.list = ListOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.list_console = ListConsoleOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.console = ConsoleOperations(
            self._client, self.config, self._serialize, self._deserialize)
