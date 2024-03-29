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

from flickr_python_sdk.type.topic_reply_message import TopicReplyMessage

class RequiredTopicReply(TypedDict):
    pass

class OptionalTopicReply(TypedDict, total=False):
    author: str

    author_is_deleted: bool

    author_path_alias: str

    authorname: str

    can_delete: bool

    can_edit: bool

    datecreate: str

    iconfarm: str

    iconserver: str

    id: str

    is_pro: bool

    lastedit: str

    message: TopicReplyMessage

class TopicReply(RequiredTopicReply, OptionalTopicReply):
    pass
