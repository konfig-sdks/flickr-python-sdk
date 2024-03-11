import typing_extensions

from flickr_python_sdk.apis.tags import TagValues
from flickr_python_sdk.apis.tags.public_api import PublicApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PUBLIC: PublicApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PUBLIC: PublicApi,
    }
)
