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


class CustomImagePropertiesCustom(Model):
    """Properties for creating a custom image from a VHD.

    All required parameters must be populated in order to send to Azure.

    :param image_name: The image name.
    :type image_name: str
    :param sys_prep: Indicates whether sysprep has been run on the VHD.
    :type sys_prep: bool
    :param os_type: Required. The OS type of the custom image (i.e. Windows,
     Linux). Possible values include: 'Windows', 'Linux', 'None'
    :type os_type: str or ~azure.mgmt.devtestlabs.models.CustomImageOsType
    """

    _validation = {
        'os_type': {'required': True},
    }

    _attribute_map = {
        'image_name': {'key': 'imageName', 'type': 'str'},
        'sys_prep': {'key': 'sysPrep', 'type': 'bool'},
        'os_type': {'key': 'osType', 'type': 'str'},
    }

    def __init__(self, *, os_type, image_name: str=None, sys_prep: bool=None, **kwargs) -> None:
        super(CustomImagePropertiesCustom, self).__init__(**kwargs)
        self.image_name = image_name
        self.sys_prep = sys_prep
        self.os_type = os_type
