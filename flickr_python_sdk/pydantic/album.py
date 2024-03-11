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


class Album(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    can_comment: typing.Optional[bool] = Field(None, alias='can_comment')

    count_comments: typing.Optional[typing.Union[int, float]] = Field(None, alias='count_comments')

    count_views: typing.Optional[typing.Union[int, float]] = Field(None, alias='count_views')

    date_create: typing.Optional[typing.Union[int, float]] = Field(None, alias='date_create')

    date_update: typing.Optional[typing.Union[int, float]] = Field(None, alias='date_update')

    farm: typing.Optional[str] = Field(None, alias='farm')

    id: typing.Optional[str] = Field(None, alias='id')

    photos: typing.Optional[typing.Union[int, float]] = Field(None, alias='photos')

    primary: typing.Optional[str] = Field(None, alias='primary')

    secret: typing.Optional[str] = Field(None, alias='secret')

    server: typing.Optional[str] = Field(None, alias='server')

    videos: typing.Optional[typing.Union[int, float]] = Field(None, alias='videos')
    class Config:
        arbitrary_types_allowed = True
