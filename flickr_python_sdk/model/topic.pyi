# coding: utf-8

"""
    Flickr API Schema

    A subset of Flickr's API defined in Swagger format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from flickr_python_sdk import schemas  # noqa: F401


class Topic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            author = schemas.StrSchema
            author_is_deleted = schemas.BoolSchema
            author_path_alias = schemas.StrSchema
            authorname = schemas.StrSchema
            can_delete = schemas.BoolSchema
            can_edit = schemas.BoolSchema
            can_reply = schemas.BoolSchema
            count_replies = schemas.IntSchema
            datecreate = schemas.StrSchema
            datelastpost = schemas.StrSchema
            iconfarm = schemas.StrSchema
            iconserver = schemas.StrSchema
            id = schemas.StrSchema
            is_locked = schemas.BoolSchema
            is_pro = schemas.BoolSchema
            is_sticky = schemas.BoolSchema
            last_reply = schemas.StrSchema
            lastedit = schemas.StrSchema
        
            @staticmethod
            def message() -> typing.Type['TopicMessage']:
                return TopicMessage
            role = schemas.StrSchema
            subject = schemas.StrSchema
            __annotations__ = {
                "author": author,
                "author_is_deleted": author_is_deleted,
                "author_path_alias": author_path_alias,
                "authorname": authorname,
                "can_delete": can_delete,
                "can_edit": can_edit,
                "can_reply": can_reply,
                "count_replies": count_replies,
                "datecreate": datecreate,
                "datelastpost": datelastpost,
                "iconfarm": iconfarm,
                "iconserver": iconserver,
                "id": id,
                "is_locked": is_locked,
                "is_pro": is_pro,
                "is_sticky": is_sticky,
                "last_reply": last_reply,
                "lastedit": lastedit,
                "message": message,
                "role": role,
                "subject": subject,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author"]) -> MetaOapg.properties.author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_is_deleted"]) -> MetaOapg.properties.author_is_deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_path_alias"]) -> MetaOapg.properties.author_path_alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorname"]) -> MetaOapg.properties.authorname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_delete"]) -> MetaOapg.properties.can_delete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_edit"]) -> MetaOapg.properties.can_edit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_reply"]) -> MetaOapg.properties.can_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count_replies"]) -> MetaOapg.properties.count_replies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datecreate"]) -> MetaOapg.properties.datecreate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datelastpost"]) -> MetaOapg.properties.datelastpost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconfarm"]) -> MetaOapg.properties.iconfarm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconserver"]) -> MetaOapg.properties.iconserver: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_locked"]) -> MetaOapg.properties.is_locked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_pro"]) -> MetaOapg.properties.is_pro: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_sticky"]) -> MetaOapg.properties.is_sticky: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_reply"]) -> MetaOapg.properties.last_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastedit"]) -> MetaOapg.properties.lastedit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> 'TopicMessage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["author", "author_is_deleted", "author_path_alias", "authorname", "can_delete", "can_edit", "can_reply", "count_replies", "datecreate", "datelastpost", "iconfarm", "iconserver", "id", "is_locked", "is_pro", "is_sticky", "last_reply", "lastedit", "message", "role", "subject", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author"]) -> typing.Union[MetaOapg.properties.author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_is_deleted"]) -> typing.Union[MetaOapg.properties.author_is_deleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_path_alias"]) -> typing.Union[MetaOapg.properties.author_path_alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorname"]) -> typing.Union[MetaOapg.properties.authorname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_delete"]) -> typing.Union[MetaOapg.properties.can_delete, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_edit"]) -> typing.Union[MetaOapg.properties.can_edit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_reply"]) -> typing.Union[MetaOapg.properties.can_reply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count_replies"]) -> typing.Union[MetaOapg.properties.count_replies, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datecreate"]) -> typing.Union[MetaOapg.properties.datecreate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datelastpost"]) -> typing.Union[MetaOapg.properties.datelastpost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconfarm"]) -> typing.Union[MetaOapg.properties.iconfarm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconserver"]) -> typing.Union[MetaOapg.properties.iconserver, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_locked"]) -> typing.Union[MetaOapg.properties.is_locked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_pro"]) -> typing.Union[MetaOapg.properties.is_pro, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_sticky"]) -> typing.Union[MetaOapg.properties.is_sticky, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_reply"]) -> typing.Union[MetaOapg.properties.last_reply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastedit"]) -> typing.Union[MetaOapg.properties.lastedit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union['TopicMessage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["author", "author_is_deleted", "author_path_alias", "authorname", "can_delete", "can_edit", "can_reply", "count_replies", "datecreate", "datelastpost", "iconfarm", "iconserver", "id", "is_locked", "is_pro", "is_sticky", "last_reply", "lastedit", "message", "role", "subject", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        author: typing.Union[MetaOapg.properties.author, str, schemas.Unset] = schemas.unset,
        author_is_deleted: typing.Union[MetaOapg.properties.author_is_deleted, bool, schemas.Unset] = schemas.unset,
        author_path_alias: typing.Union[MetaOapg.properties.author_path_alias, str, schemas.Unset] = schemas.unset,
        authorname: typing.Union[MetaOapg.properties.authorname, str, schemas.Unset] = schemas.unset,
        can_delete: typing.Union[MetaOapg.properties.can_delete, bool, schemas.Unset] = schemas.unset,
        can_edit: typing.Union[MetaOapg.properties.can_edit, bool, schemas.Unset] = schemas.unset,
        can_reply: typing.Union[MetaOapg.properties.can_reply, bool, schemas.Unset] = schemas.unset,
        count_replies: typing.Union[MetaOapg.properties.count_replies, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        datecreate: typing.Union[MetaOapg.properties.datecreate, str, schemas.Unset] = schemas.unset,
        datelastpost: typing.Union[MetaOapg.properties.datelastpost, str, schemas.Unset] = schemas.unset,
        iconfarm: typing.Union[MetaOapg.properties.iconfarm, str, schemas.Unset] = schemas.unset,
        iconserver: typing.Union[MetaOapg.properties.iconserver, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        is_locked: typing.Union[MetaOapg.properties.is_locked, bool, schemas.Unset] = schemas.unset,
        is_pro: typing.Union[MetaOapg.properties.is_pro, bool, schemas.Unset] = schemas.unset,
        is_sticky: typing.Union[MetaOapg.properties.is_sticky, bool, schemas.Unset] = schemas.unset,
        last_reply: typing.Union[MetaOapg.properties.last_reply, str, schemas.Unset] = schemas.unset,
        lastedit: typing.Union[MetaOapg.properties.lastedit, str, schemas.Unset] = schemas.unset,
        message: typing.Union['TopicMessage', schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Topic':
        return super().__new__(
            cls,
            *args,
            author=author,
            author_is_deleted=author_is_deleted,
            author_path_alias=author_path_alias,
            authorname=authorname,
            can_delete=can_delete,
            can_edit=can_edit,
            can_reply=can_reply,
            count_replies=count_replies,
            datecreate=datecreate,
            datelastpost=datelastpost,
            iconfarm=iconfarm,
            iconserver=iconserver,
            id=id,
            is_locked=is_locked,
            is_pro=is_pro,
            is_sticky=is_sticky,
            last_reply=last_reply,
            lastedit=lastedit,
            message=message,
            role=role,
            subject=subject,
            _configuration=_configuration,
            **kwargs,
        )

from flickr_python_sdk.model.topic_message import TopicMessage