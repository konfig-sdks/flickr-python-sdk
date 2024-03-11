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


class RequiredAlbum(TypedDict):
    pass

class OptionalAlbum(TypedDict, total=False):
    title: str

    description: str

    can_comment: bool

    count_comments: typing.Union[int, float]

    count_views: typing.Union[int, float]

    date_create: typing.Union[int, float]

    date_update: typing.Union[int, float]

    farm: str

    id: str

    photos: typing.Union[int, float]

    primary: str

    secret: str

    server: str

    videos: typing.Union[int, float]

class Album(RequiredAlbum, OptionalAlbum):
    pass
