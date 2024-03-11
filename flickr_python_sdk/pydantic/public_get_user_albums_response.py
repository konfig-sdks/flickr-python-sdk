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
from pydantic import BaseModel, Field, RootModel

from flickr_python_sdk.pydantic.album import Album

class PublicGetUserAlbumsResponse(BaseModel):
    page: typing.Optional[typing.Union[int, float]] = Field(None, alias='page')

    pages: typing.Optional[typing.Union[int, float]] = Field(None, alias='pages')

    perpage: typing.Optional[typing.Union[int, float]] = Field(None, alias='perpage')

    photosets: typing.Optional[typing.List[Album]] = Field(None, alias='photosets')

    total: typing.Optional[typing.Union[int, float]] = Field(None, alias='total')
    class Config:
        arbitrary_types_allowed = True