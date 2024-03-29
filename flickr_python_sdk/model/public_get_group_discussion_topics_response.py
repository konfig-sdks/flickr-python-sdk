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


class PublicGetGroupDiscussionTopicsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            iconfarm = schemas.NumberSchema
            iconserver = schemas.NumberSchema
            ispoolmoderated = schemas.BoolSchema
            lang = schemas.StrSchema
            members = schemas.NumberSchema
            name = schemas.StrSchema
            page = schemas.NumberSchema
            pages = schemas.NumberSchema
            per_page = schemas.NumberSchema
            privacy = schemas.NumberSchema
            
            
            class topics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Topic']:
                        return Topic
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Topic'], typing.List['Topic']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'topics':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Topic':
                    return super().__getitem__(i)
            total = schemas.NumberSchema
            __annotations__ = {
                "iconfarm": iconfarm,
                "iconserver": iconserver,
                "ispoolmoderated": ispoolmoderated,
                "lang": lang,
                "members": members,
                "name": name,
                "page": page,
                "pages": pages,
                "per_page": per_page,
                "privacy": privacy,
                "topics": topics,
                "total": total,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconfarm"]) -> MetaOapg.properties.iconfarm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iconserver"]) -> MetaOapg.properties.iconserver: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ispoolmoderated"]) -> MetaOapg.properties.ispoolmoderated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lang"]) -> MetaOapg.properties.lang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> MetaOapg.properties.privacy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topics"]) -> MetaOapg.properties.topics: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["iconfarm", "iconserver", "ispoolmoderated", "lang", "members", "name", "page", "pages", "per_page", "privacy", "topics", "total", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconfarm"]) -> typing.Union[MetaOapg.properties.iconfarm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iconserver"]) -> typing.Union[MetaOapg.properties.iconserver, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ispoolmoderated"]) -> typing.Union[MetaOapg.properties.ispoolmoderated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lang"]) -> typing.Union[MetaOapg.properties.lang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> typing.Union[MetaOapg.properties.members, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> typing.Union[MetaOapg.properties.pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union[MetaOapg.properties.privacy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topics"]) -> typing.Union[MetaOapg.properties.topics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["iconfarm", "iconserver", "ispoolmoderated", "lang", "members", "name", "page", "pages", "per_page", "privacy", "topics", "total", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        iconfarm: typing.Union[MetaOapg.properties.iconfarm, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        iconserver: typing.Union[MetaOapg.properties.iconserver, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ispoolmoderated: typing.Union[MetaOapg.properties.ispoolmoderated, bool, schemas.Unset] = schemas.unset,
        lang: typing.Union[MetaOapg.properties.lang, str, schemas.Unset] = schemas.unset,
        members: typing.Union[MetaOapg.properties.members, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pages: typing.Union[MetaOapg.properties.pages, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        privacy: typing.Union[MetaOapg.properties.privacy, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        topics: typing.Union[MetaOapg.properties.topics, list, tuple, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublicGetGroupDiscussionTopicsResponse':
        return super().__new__(
            cls,
            *args,
            iconfarm=iconfarm,
            iconserver=iconserver,
            ispoolmoderated=ispoolmoderated,
            lang=lang,
            members=members,
            name=name,
            page=page,
            pages=pages,
            per_page=per_page,
            privacy=privacy,
            topics=topics,
            total=total,
            _configuration=_configuration,
            **kwargs,
        )

from flickr_python_sdk.model.topic import Topic
