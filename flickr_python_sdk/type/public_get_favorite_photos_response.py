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

from flickr_python_sdk.type.photo import Photo

class RequiredPublicGetFavoritePhotosResponse(TypedDict):
    pass

class OptionalPublicGetFavoritePhotosResponse(TypedDict, total=False):
    page: typing.Union[int, float]

    pages: typing.Union[int, float]

    perpage: typing.Union[int, float]

    photos: typing.List[Photo]

    total: typing.Union[int, float]

class PublicGetFavoritePhotosResponse(RequiredPublicGetFavoritePhotosResponse, OptionalPublicGetFavoritePhotosResponse):
    pass
