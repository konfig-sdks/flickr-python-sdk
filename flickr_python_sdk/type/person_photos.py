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

from flickr_python_sdk.type.person_photos_count import PersonPhotosCount
from flickr_python_sdk.type.person_photos_firstdate import PersonPhotosFirstdate
from flickr_python_sdk.type.person_photos_firstdatetaken import PersonPhotosFirstdatetaken
from flickr_python_sdk.type.person_photos_views import PersonPhotosViews

class RequiredPersonPhotos(TypedDict):
    pass

class OptionalPersonPhotos(TypedDict, total=False):
    count: PersonPhotosCount

    firstdate: PersonPhotosFirstdate

    firstdatetaken: PersonPhotosFirstdatetaken

    views: PersonPhotosViews

class PersonPhotos(RequiredPersonPhotos, OptionalPersonPhotos):
    pass
