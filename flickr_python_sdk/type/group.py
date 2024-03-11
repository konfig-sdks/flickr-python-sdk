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

from flickr_python_sdk.type.cover import Cover
from flickr_python_sdk.type.group_blast import GroupBlast
from flickr_python_sdk.type.group_description import GroupDescription
from flickr_python_sdk.type.group_members import GroupMembers
from flickr_python_sdk.type.group_name import GroupName
from flickr_python_sdk.type.group_pool_count import GroupPoolCount
from flickr_python_sdk.type.group_privacy import GroupPrivacy
from flickr_python_sdk.type.group_restrictions import GroupRestrictions
from flickr_python_sdk.type.group_roles import GroupRoles
from flickr_python_sdk.type.group_rules import GroupRules
from flickr_python_sdk.type.group_throttle import GroupThrottle
from flickr_python_sdk.type.group_topic_count import GroupTopicCount
from flickr_python_sdk.type.photo_urls import PhotoURLs

class RequiredGroup(TypedDict):
    pass

class OptionalGroup(TypedDict, total=False):
    description: GroupDescription

    blast: GroupBlast

    cover: Cover

    coverphoto_farm: str

    coverphoto_server: str

    coverphoto_url: PhotoURLs

    iconfarm: str

    iconserver: str

    id: str

    is_admin: bool

    is_member: bool

    is_moderator: bool

    ispoolmoderated: bool

    lang: str

    members: GroupMembers

    name: GroupName

    path_alias: str

    pool_count: GroupPoolCount

    pool_rows: int

    privacy: GroupPrivacy

    restrictions: GroupRestrictions

    roles: GroupRoles

    rules: GroupRules

    throttle: GroupThrottle

    topic_count: GroupTopicCount

class Group(RequiredGroup, OptionalGroup):
    pass