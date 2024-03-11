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


class PublicGetAlbumPhotosResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class photoset(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Photo']:
                        return Photo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Photo'], typing.List['Photo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'photoset':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Photo':
                    return super().__getitem__(i)
            __annotations__ = {
                "photoset": photoset,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photoset"]) -> MetaOapg.properties.photoset: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["photoset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photoset"]) -> typing.Union[MetaOapg.properties.photoset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["photoset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        photoset: typing.Union[MetaOapg.properties.photoset, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublicGetAlbumPhotosResponse':
        return super().__new__(
            cls,
            *args,
            photoset=photoset,
            _configuration=_configuration,
            **kwargs,
        )

from flickr_python_sdk.model.photo import Photo
