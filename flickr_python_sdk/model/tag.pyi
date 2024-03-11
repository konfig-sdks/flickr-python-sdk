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


class Tag(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            _content = schemas.StrSchema
            author = schemas.StrSchema
            authorname = schemas.StrSchema
            id = schemas.StrSchema
            machine_tag = schemas.BoolSchema
            raw = schemas.StrSchema
            __annotations__ = {
                "_content": _content,
                "author": author,
                "authorname": authorname,
                "id": id,
                "machine_tag": machine_tag,
                "raw": raw,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_content"]) -> MetaOapg.properties._content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author"]) -> MetaOapg.properties.author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorname"]) -> MetaOapg.properties.authorname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machine_tag"]) -> MetaOapg.properties.machine_tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw"]) -> MetaOapg.properties.raw: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_content", "author", "authorname", "id", "machine_tag", "raw", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_content"]) -> typing.Union[MetaOapg.properties._content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author"]) -> typing.Union[MetaOapg.properties.author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorname"]) -> typing.Union[MetaOapg.properties.authorname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machine_tag"]) -> typing.Union[MetaOapg.properties.machine_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw"]) -> typing.Union[MetaOapg.properties.raw, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_content", "author", "authorname", "id", "machine_tag", "raw", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _content: typing.Union[MetaOapg.properties._content, str, schemas.Unset] = schemas.unset,
        author: typing.Union[MetaOapg.properties.author, str, schemas.Unset] = schemas.unset,
        authorname: typing.Union[MetaOapg.properties.authorname, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        machine_tag: typing.Union[MetaOapg.properties.machine_tag, bool, schemas.Unset] = schemas.unset,
        raw: typing.Union[MetaOapg.properties.raw, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tag':
        return super().__new__(
            cls,
            *args,
            _content=_content,
            author=author,
            authorname=authorname,
            id=id,
            machine_tag=machine_tag,
            raw=raw,
            _configuration=_configuration,
            **kwargs,
        )
