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


class RequiredPublicGetPhotoLicensesResponseLicensesLicenseItem(TypedDict):
    pass

class OptionalPublicGetPhotoLicensesResponseLicensesLicenseItem(TypedDict, total=False):
    id: int

    name: str

    url: str

class PublicGetPhotoLicensesResponseLicensesLicenseItem(RequiredPublicGetPhotoLicensesResponseLicensesLicenseItem, OptionalPublicGetPhotoLicensesResponseLicensesLicenseItem):
    pass
