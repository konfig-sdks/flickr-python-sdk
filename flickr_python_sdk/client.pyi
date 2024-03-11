# coding: utf-8
"""
    Flickr API Schema

    A subset of Flickr's API defined in Swagger format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from flickr_python_sdk.client_custom import ClientCustom
from flickr_python_sdk.configuration import Configuration
from flickr_python_sdk.api_client import ApiClient
from flickr_python_sdk.type_util import copy_signature
from flickr_python_sdk.apis.tags.public_api import PublicApi



class Flickr(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.public: PublicApi = PublicApi(api_client)
