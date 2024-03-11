# coding: utf-8

"""
    Flickr API Schema

    A subset of Flickr's API defined in Swagger format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from flickr_python_sdk.type.context_photo import ContextPhoto
from flickr_python_sdk.type.public_flickr_groups_pools_get_context_response_count import PublicFlickrGroupsPoolsGetContextResponseCount

class RequiredPublicFlickrGroupsPoolsGetContextResponse(TypedDict):
    pass

class OptionalPublicFlickrGroupsPoolsGetContextResponse(TypedDict, total=False):
    count: PublicFlickrGroupsPoolsGetContextResponseCount

    nextphoto: ContextPhoto

    prevphoto: ContextPhoto

    stat: str

class PublicFlickrGroupsPoolsGetContextResponse(RequiredPublicFlickrGroupsPoolsGetContextResponse, OptionalPublicFlickrGroupsPoolsGetContextResponse):
    pass