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


class ContextPhoto(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    farm: typing.Optional[str] = Field(None, alias='farm')

    id: typing.Optional[str] = Field(None, alias='id')

    is_faved: typing.Optional[bool] = Field(None, alias='is_faved')

    license: typing.Optional[int] = Field(None, alias='license')

    media: typing.Optional[str] = Field(None, alias='media')

    owner: typing.Optional[str] = Field(None, alias='owner')

    safe: typing.Optional[bool] = Field(None, alias='safe')

    secret: typing.Optional[str] = Field(None, alias='secret')

    server: typing.Optional[str] = Field(None, alias='server')

    thumb: typing.Optional[str] = Field(None, alias='thumb')

    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
