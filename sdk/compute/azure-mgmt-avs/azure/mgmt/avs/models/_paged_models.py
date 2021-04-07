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

from msrest.paging import Paged


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.avs.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class PrivateCloudPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateCloud <azure.mgmt.avs.models.PrivateCloud>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateCloud]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateCloudPaged, self).__init__(*args, **kwargs)
class ClusterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Cluster <azure.mgmt.avs.models.Cluster>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Cluster]'}
    }

    def __init__(self, *args, **kwargs):

        super(ClusterPaged, self).__init__(*args, **kwargs)
class HcxEnterpriseSitePaged(Paged):
    """
    A paging container for iterating over a list of :class:`HcxEnterpriseSite <azure.mgmt.avs.models.HcxEnterpriseSite>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[HcxEnterpriseSite]'}
    }

    def __init__(self, *args, **kwargs):

        super(HcxEnterpriseSitePaged, self).__init__(*args, **kwargs)
class ExpressRouteAuthorizationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteAuthorization <azure.mgmt.avs.models.ExpressRouteAuthorization>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteAuthorization]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteAuthorizationPaged, self).__init__(*args, **kwargs)