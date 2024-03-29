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


class Group(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def description() -> typing.Type['GroupDescription']:
                return GroupDescription
        
            @staticmethod
            def blast() -> typing.Type['GroupBlast']:
                return GroupBlast
        
            @staticmethod
            def cover() -> typing.Type['Cover']:
                return Cover
            coverphoto_farm = schemas.StrSchema
            coverphoto_server = schemas.StrSchema
        
            @staticmethod
            def coverphoto_url() -> typing.Type['PhotoURLs']:
                return PhotoURLs
            iconfarm = schemas.StrSchema
            iconserver = schemas.StrSchema
            id = schemas.StrSchema
            is_admin = schemas.BoolSchema
            is_member = schemas.BoolSchema
            is_moderator = schemas.BoolSchema
            ispoolmoderated = schemas.BoolSchema
            lang = schemas.StrSchema
        
            @staticmethod
            def members() -> typing.Type['GroupMembers']:
                return GroupMembers
        
            @staticmethod
            def name() -> typing.Type['GroupName']:
                return GroupName
            path_alias = schemas.StrSchema
        
            @staticmethod
            def pool_count() -> typing.Type['GroupPoolCount']:
                return GroupPoolCount
            pool_rows = schemas.IntSchema
        
            @staticmethod
            def privacy() -> typing.Type['GroupPrivacy']:
                return GroupPrivacy
        
            @staticmethod
            def restrictions() -> typing.Type['GroupRestrictions']:
                return GroupRestrictions
        
            @staticmethod
            def roles() -> typing.Type['GroupRoles']:
                return GroupRoles
        
            @staticmethod
            def rules() -> typing.Type['GroupRules']:
                return GroupRules
        
            @staticmethod
            def throttle() -> typing.Type['GroupThrottle']:
                return GroupThrottle
        
            @staticmethod
            def topic_count() -> typing.Type['GroupTopicCount']:
                return GroupTopicCount
            __annotations__ = {
                "description": description,
                "blast": blast,
                "cover": cover,
                "coverphoto_farm": coverphoto_farm,
                "coverphoto_server": coverphoto_server,
                "coverphoto_url": coverphoto_url,
                "iconfarm": iconfarm,
                "iconserver": iconserver,
                "id": id,
                "is_admin": is_admin,
                "is_member": is_member,
                "is_moderator": is_moderator,
                "ispoolmoderated": ispoolmoderated,
                "lang": lang,
                "members": members,
                "name": name,
                "path_alias": path_alias,
                "pool_count": pool_count,
                "pool_rows": pool_rows,
                "privacy": privacy,
                "restrictions": restrictions,
                "roles": roles,
                "rules": rules,
                "throttle": throttle,
                "topic_count": topic_count,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'GroupDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blast"]) -> 'GroupBlast': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover"]) -> 'Cover': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverphoto_farm"]) -> MetaOapg.properties.coverphoto_farm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverphoto_server"]) -> MetaOapg.properties.coverphoto_server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverphoto_url"]) -> 'PhotoURLs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconfarm"]) -> MetaOapg.properties.iconfarm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconserver"]) -> MetaOapg.properties.iconserver: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_admin"]) -> MetaOapg.properties.is_admin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_member"]) -> MetaOapg.properties.is_member: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_moderator"]) -> MetaOapg.properties.is_moderator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ispoolmoderated"]) -> MetaOapg.properties.ispoolmoderated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lang"]) -> MetaOapg.properties.lang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> 'GroupMembers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'GroupName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path_alias"]) -> MetaOapg.properties.path_alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pool_count"]) -> 'GroupPoolCount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pool_rows"]) -> MetaOapg.properties.pool_rows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> 'GroupPrivacy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrictions"]) -> 'GroupRestrictions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> 'GroupRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rules"]) -> 'GroupRules': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["throttle"]) -> 'GroupThrottle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic_count"]) -> 'GroupTopicCount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "blast", "cover", "coverphoto_farm", "coverphoto_server", "coverphoto_url", "iconfarm", "iconserver", "id", "is_admin", "is_member", "is_moderator", "ispoolmoderated", "lang", "members", "name", "path_alias", "pool_count", "pool_rows", "privacy", "restrictions", "roles", "rules", "throttle", "topic_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['GroupDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blast"]) -> typing.Union['GroupBlast', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover"]) -> typing.Union['Cover', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverphoto_farm"]) -> typing.Union[MetaOapg.properties.coverphoto_farm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverphoto_server"]) -> typing.Union[MetaOapg.properties.coverphoto_server, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverphoto_url"]) -> typing.Union['PhotoURLs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconfarm"]) -> typing.Union[MetaOapg.properties.iconfarm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconserver"]) -> typing.Union[MetaOapg.properties.iconserver, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_admin"]) -> typing.Union[MetaOapg.properties.is_admin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_member"]) -> typing.Union[MetaOapg.properties.is_member, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_moderator"]) -> typing.Union[MetaOapg.properties.is_moderator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ispoolmoderated"]) -> typing.Union[MetaOapg.properties.ispoolmoderated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lang"]) -> typing.Union[MetaOapg.properties.lang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> typing.Union['GroupMembers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['GroupName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path_alias"]) -> typing.Union[MetaOapg.properties.path_alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pool_count"]) -> typing.Union['GroupPoolCount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pool_rows"]) -> typing.Union[MetaOapg.properties.pool_rows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union['GroupPrivacy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrictions"]) -> typing.Union['GroupRestrictions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union['GroupRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rules"]) -> typing.Union['GroupRules', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["throttle"]) -> typing.Union['GroupThrottle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic_count"]) -> typing.Union['GroupTopicCount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "blast", "cover", "coverphoto_farm", "coverphoto_server", "coverphoto_url", "iconfarm", "iconserver", "id", "is_admin", "is_member", "is_moderator", "ispoolmoderated", "lang", "members", "name", "path_alias", "pool_count", "pool_rows", "privacy", "restrictions", "roles", "rules", "throttle", "topic_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union['GroupDescription', schemas.Unset] = schemas.unset,
        blast: typing.Union['GroupBlast', schemas.Unset] = schemas.unset,
        cover: typing.Union['Cover', schemas.Unset] = schemas.unset,
        coverphoto_farm: typing.Union[MetaOapg.properties.coverphoto_farm, str, schemas.Unset] = schemas.unset,
        coverphoto_server: typing.Union[MetaOapg.properties.coverphoto_server, str, schemas.Unset] = schemas.unset,
        coverphoto_url: typing.Union['PhotoURLs', schemas.Unset] = schemas.unset,
        iconfarm: typing.Union[MetaOapg.properties.iconfarm, str, schemas.Unset] = schemas.unset,
        iconserver: typing.Union[MetaOapg.properties.iconserver, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        is_admin: typing.Union[MetaOapg.properties.is_admin, bool, schemas.Unset] = schemas.unset,
        is_member: typing.Union[MetaOapg.properties.is_member, bool, schemas.Unset] = schemas.unset,
        is_moderator: typing.Union[MetaOapg.properties.is_moderator, bool, schemas.Unset] = schemas.unset,
        ispoolmoderated: typing.Union[MetaOapg.properties.ispoolmoderated, bool, schemas.Unset] = schemas.unset,
        lang: typing.Union[MetaOapg.properties.lang, str, schemas.Unset] = schemas.unset,
        members: typing.Union['GroupMembers', schemas.Unset] = schemas.unset,
        name: typing.Union['GroupName', schemas.Unset] = schemas.unset,
        path_alias: typing.Union[MetaOapg.properties.path_alias, str, schemas.Unset] = schemas.unset,
        pool_count: typing.Union['GroupPoolCount', schemas.Unset] = schemas.unset,
        pool_rows: typing.Union[MetaOapg.properties.pool_rows, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        privacy: typing.Union['GroupPrivacy', schemas.Unset] = schemas.unset,
        restrictions: typing.Union['GroupRestrictions', schemas.Unset] = schemas.unset,
        roles: typing.Union['GroupRoles', schemas.Unset] = schemas.unset,
        rules: typing.Union['GroupRules', schemas.Unset] = schemas.unset,
        throttle: typing.Union['GroupThrottle', schemas.Unset] = schemas.unset,
        topic_count: typing.Union['GroupTopicCount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Group':
        return super().__new__(
            cls,
            *args,
            description=description,
            blast=blast,
            cover=cover,
            coverphoto_farm=coverphoto_farm,
            coverphoto_server=coverphoto_server,
            coverphoto_url=coverphoto_url,
            iconfarm=iconfarm,
            iconserver=iconserver,
            id=id,
            is_admin=is_admin,
            is_member=is_member,
            is_moderator=is_moderator,
            ispoolmoderated=ispoolmoderated,
            lang=lang,
            members=members,
            name=name,
            path_alias=path_alias,
            pool_count=pool_count,
            pool_rows=pool_rows,
            privacy=privacy,
            restrictions=restrictions,
            roles=roles,
            rules=rules,
            throttle=throttle,
            topic_count=topic_count,
            _configuration=_configuration,
            **kwargs,
        )

from flickr_python_sdk.model.cover import Cover
from flickr_python_sdk.model.group_blast import GroupBlast
from flickr_python_sdk.model.group_description import GroupDescription
from flickr_python_sdk.model.group_members import GroupMembers
from flickr_python_sdk.model.group_name import GroupName
from flickr_python_sdk.model.group_pool_count import GroupPoolCount
from flickr_python_sdk.model.group_privacy import GroupPrivacy
from flickr_python_sdk.model.group_restrictions import GroupRestrictions
from flickr_python_sdk.model.group_roles import GroupRoles
from flickr_python_sdk.model.group_rules import GroupRules
from flickr_python_sdk.model.group_throttle import GroupThrottle
from flickr_python_sdk.model.group_topic_count import GroupTopicCount
from flickr_python_sdk.model.photo_urls import PhotoURLs
