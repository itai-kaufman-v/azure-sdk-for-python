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


class ClientDiscoveryForProperties(Model):
    """Class to represent shoebox properties in json client discovery.

    :param service_specification: Operation properties.
    :type service_specification:
     ~azure.mgmt.recoveryservices.models.ClientDiscoveryForServiceSpecification
    """

    _attribute_map = {
        'service_specification': {'key': 'serviceSpecification', 'type': 'ClientDiscoveryForServiceSpecification'},
    }

    def __init__(self, **kwargs):
        super(ClientDiscoveryForProperties, self).__init__(**kwargs)
        self.service_specification = kwargs.get('service_specification', None)