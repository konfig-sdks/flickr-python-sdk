# coding: utf-8

"""
    Flickr API Schema

    A subset of Flickr's API defined in Swagger format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import flickr_python_sdk
from flickr_python_sdk.paths.restmethodflickr_people_get_info import get
from flickr_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRestmethodflickrPeopleGetInfo(ApiTestMixin, unittest.TestCase):
    """
    RestmethodflickrPeopleGetInfo unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
