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

from flickr_python_sdk.pydantic.group import Group

class PublicGetGroupInfoResponse(BaseModel):
    group: typing.Optional[Group] = Field(None, alias='group')

    stat: typing.Optional[str] = Field(None, alias='stat')
    class Config:
        arbitrary_types_allowed = True
