# coding: utf-8

"""
    Flickr API Schema

    A subset of Flickr's API defined in Swagger format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from flickr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from flickr_python_sdk.api_response import AsyncGeneratorResponse
from flickr_python_sdk import api_client, exceptions
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

from flickr_python_sdk.model.public_flickr_groups_pools_get_context_response import PublicFlickrGroupsPoolsGetContextResponse as PublicFlickrGroupsPoolsGetContextResponseSchema

from flickr_python_sdk.type.public_flickr_groups_pools_get_context_response import PublicFlickrGroupsPoolsGetContextResponse

from ...api_client import Dictionary
from flickr_python_sdk.pydantic.public_flickr_groups_pools_get_context_response import PublicFlickrGroupsPoolsGetContextResponse as PublicFlickrGroupsPoolsGetContextResponsePydantic

from . import path

# Query params
ApiKeySchema = schemas.StrSchema


class PhotoIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[0-9]+$',
        }]


class GroupIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^([0-9]+@N[0-9]+)|([0-9a-zA-Z-_]+)$',
        }]
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'api_key': typing.Union[ApiKeySchema, str, ],
        'photo_id': typing.Union[PhotoIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'group_id': typing.Union[GroupIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_api_key = api_client.QueryParameter(
    name="api_key",
    style=api_client.ParameterStyle.FORM,
    schema=ApiKeySchema,
    required=True,
    explode=True,
)
request_query_photo_id = api_client.QueryParameter(
    name="photo_id",
    style=api_client.ParameterStyle.FORM,
    schema=PhotoIdSchema,
    required=True,
    explode=True,
)
request_query_group_id = api_client.QueryParameter(
    name="group_id",
    style=api_client.ParameterStyle.FORM,
    schema=GroupIdSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PublicFlickrGroupsPoolsGetContextResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PublicFlickrGroupsPoolsGetContextResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PublicFlickrGroupsPoolsGetContextResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _flickr_groups_pools_get_context_mapped_args(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if api_key is not None:
            _query_params["api_key"] = api_key
        if photo_id is not None:
            _query_params["photo_id"] = photo_id
        if group_id is not None:
            _query_params["group_id"] = group_id
        args.query = _query_params
        return args

    async def _aflickr_groups_pools_get_context_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_api_key,
            request_query_photo_id,
            request_query_group_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest?method=flickr.groups.pools.getContext',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _flickr_groups_pools_get_context_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_api_key,
            request_query_photo_id,
            request_query_group_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/rest?method=flickr.groups.pools.getContext',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class FlickrGroupsPoolsGetContextRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aflickr_groups_pools_get_context(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._flickr_groups_pools_get_context_mapped_args(
            api_key=api_key,
            photo_id=photo_id,
            group_id=group_id,
        )
        return await self._aflickr_groups_pools_get_context_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def flickr_groups_pools_get_context(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._flickr_groups_pools_get_context_mapped_args(
            api_key=api_key,
            photo_id=photo_id,
            group_id=group_id,
        )
        return self._flickr_groups_pools_get_context_oapg(
            query_params=args.query,
        )

class FlickrGroupsPoolsGetContext(BaseApi):

    async def aflickr_groups_pools_get_context(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PublicFlickrGroupsPoolsGetContextResponsePydantic:
        raw_response = await self.raw.aflickr_groups_pools_get_context(
            api_key=api_key,
            photo_id=photo_id,
            group_id=group_id,
            **kwargs,
        )
        if validate:
            return PublicFlickrGroupsPoolsGetContextResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PublicFlickrGroupsPoolsGetContextResponsePydantic, raw_response.body)
    
    
    def flickr_groups_pools_get_context(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PublicFlickrGroupsPoolsGetContextResponsePydantic:
        raw_response = self.raw.flickr_groups_pools_get_context(
            api_key=api_key,
            photo_id=photo_id,
            group_id=group_id,
        )
        if validate:
            return PublicFlickrGroupsPoolsGetContextResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PublicFlickrGroupsPoolsGetContextResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._flickr_groups_pools_get_context_mapped_args(
            api_key=api_key,
            photo_id=photo_id,
            group_id=group_id,
        )
        return await self._aflickr_groups_pools_get_context_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        api_key: str,
        photo_id: str,
        group_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._flickr_groups_pools_get_context_mapped_args(
            api_key=api_key,
            photo_id=photo_id,
            group_id=group_id,
        )
        return self._flickr_groups_pools_get_context_oapg(
            query_params=args.query,
        )

