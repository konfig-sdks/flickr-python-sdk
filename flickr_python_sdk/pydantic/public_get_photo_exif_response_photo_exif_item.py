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

from flickr_python_sdk.pydantic.public_get_photo_exif_response_photo_exif_item_raw import PublicGetPhotoExifResponsePhotoExifItemRaw

class PublicGetPhotoExifResponsePhotoExifItem(BaseModel):
    label: typing.Optional[str] = Field(None, alias='label')

    raw: typing.Optional[PublicGetPhotoExifResponsePhotoExifItemRaw] = Field(None, alias='raw')

    tag: typing.Optional[str] = Field(None, alias='tag')

    tagspace: typing.Optional[str] = Field(None, alias='tagspace')

    tagspaceid: typing.Optional[str] = Field(None, alias='tagspaceid')
    class Config:
        arbitrary_types_allowed = True