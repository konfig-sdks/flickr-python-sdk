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


class PublicFlickrGroupsPoolsGetContextResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def count() -> typing.Type['PublicFlickrGroupsPoolsGetContextResponseCount']:
                return PublicFlickrGroupsPoolsGetContextResponseCount
        
            @staticmethod
            def nextphoto() -> typing.Type['ContextPhoto']:
                return ContextPhoto
        
            @staticmethod
            def prevphoto() -> typing.Type['ContextPhoto']:
                return ContextPhoto
            stat = schemas.StrSchema
            __annotations__ = {
                "count": count,
                "nextphoto": nextphoto,
                "prevphoto": prevphoto,
                "stat": stat,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> 'PublicFlickrGroupsPoolsGetContextResponseCount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextphoto"]) -> 'ContextPhoto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prevphoto"]) -> 'ContextPhoto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stat"]) -> MetaOapg.properties.stat: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["count", "nextphoto", "prevphoto", "stat", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union['PublicFlickrGroupsPoolsGetContextResponseCount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextphoto"]) -> typing.Union['ContextPhoto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prevphoto"]) -> typing.Union['ContextPhoto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stat"]) -> typing.Union[MetaOapg.properties.stat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count", "nextphoto", "prevphoto", "stat", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        count: typing.Union['PublicFlickrGroupsPoolsGetContextResponseCount', schemas.Unset] = schemas.unset,
        nextphoto: typing.Union['ContextPhoto', schemas.Unset] = schemas.unset,
        prevphoto: typing.Union['ContextPhoto', schemas.Unset] = schemas.unset,
        stat: typing.Union[MetaOapg.properties.stat, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublicFlickrGroupsPoolsGetContextResponse':
        return super().__new__(
            cls,
            *args,
            count=count,
            nextphoto=nextphoto,
            prevphoto=prevphoto,
            stat=stat,
            _configuration=_configuration,
            **kwargs,
        )

from flickr_python_sdk.model.context_photo import ContextPhoto
from flickr_python_sdk.model.public_flickr_groups_pools_get_context_response_count import PublicFlickrGroupsPoolsGetContextResponseCount
