import typing_extensions

from flickr_python_sdk.paths import PathValues
from flickr_python_sdk.apis.paths.oauth_access_token import OauthAccessToken
from flickr_python_sdk.apis.paths.oauth_request_token import OauthRequestToken
from flickr_python_sdk.apis.paths.restmethodflickr_favorites_get_context import RestmethodflickrFavoritesGetContext
from flickr_python_sdk.apis.paths.restmethodflickr_favorites_get_list import RestmethodflickrFavoritesGetList
from flickr_python_sdk.apis.paths.restmethodflickr_galleries_get_photos import RestmethodflickrGalleriesGetPhotos
from flickr_python_sdk.apis.paths.restmethodflickr_groups_discuss_replies_get_info import RestmethodflickrGroupsDiscussRepliesGetInfo
from flickr_python_sdk.apis.paths.restmethodflickr_groups_discuss_topics_get_info import RestmethodflickrGroupsDiscussTopicsGetInfo
from flickr_python_sdk.apis.paths.restmethodflickr_groups_discuss_topics_get_list import RestmethodflickrGroupsDiscussTopicsGetList
from flickr_python_sdk.apis.paths.restmethodflickr_groups_get_info import RestmethodflickrGroupsGetInfo
from flickr_python_sdk.apis.paths.restmethodflickr_groups_pools_get_context import RestmethodflickrGroupsPoolsGetContext
from flickr_python_sdk.apis.paths.restmethodflickr_groups_pools_get_photos import RestmethodflickrGroupsPoolsGetPhotos
from flickr_python_sdk.apis.paths.restmethodflickr_people_get_info import RestmethodflickrPeopleGetInfo
from flickr_python_sdk.apis.paths.restmethodflickr_people_get_photos import RestmethodflickrPeopleGetPhotos
from flickr_python_sdk.apis.paths.restmethodflickr_photolist_get_context import RestmethodflickrPhotolistGetContext
from flickr_python_sdk.apis.paths.restmethodflickr_photos_get_context import RestmethodflickrPhotosGetContext
from flickr_python_sdk.apis.paths.restmethodflickr_photos_get_exif import RestmethodflickrPhotosGetExif
from flickr_python_sdk.apis.paths.restmethodflickr_photos_get_info import RestmethodflickrPhotosGetInfo
from flickr_python_sdk.apis.paths.restmethodflickr_photos_get_sizes import RestmethodflickrPhotosGetSizes
from flickr_python_sdk.apis.paths.restmethodflickr_photos_licenses_get_info import RestmethodflickrPhotosLicensesGetInfo
from flickr_python_sdk.apis.paths.restmethodflickr_photos_search import RestmethodflickrPhotosSearch
from flickr_python_sdk.apis.paths.restmethodflickr_photosets_get_context import RestmethodflickrPhotosetsGetContext
from flickr_python_sdk.apis.paths.restmethodflickr_photosets_get_list import RestmethodflickrPhotosetsGetList
from flickr_python_sdk.apis.paths.restmethodflickr_photosets_get_photos import RestmethodflickrPhotosetsGetPhotos
from flickr_python_sdk.apis.paths.restmethodflickr_test_echo import RestmethodflickrTestEcho
from flickr_python_sdk.apis.paths.upload import Upload

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.OAUTH_ACCESS_TOKEN: OauthAccessToken,
        PathValues.OAUTH_REQUEST_TOKEN: OauthRequestToken,
        PathValues.RESTMETHODFLICKR_FAVORITES_GET_CONTEXT: RestmethodflickrFavoritesGetContext,
        PathValues.RESTMETHODFLICKR_FAVORITES_GET_LIST: RestmethodflickrFavoritesGetList,
        PathValues.RESTMETHODFLICKR_GALLERIES_GET_PHOTOS: RestmethodflickrGalleriesGetPhotos,
        PathValues.RESTMETHODFLICKR_GROUPS_DISCUSS_REPLIES_GET_INFO: RestmethodflickrGroupsDiscussRepliesGetInfo,
        PathValues.RESTMETHODFLICKR_GROUPS_DISCUSS_TOPICS_GET_INFO: RestmethodflickrGroupsDiscussTopicsGetInfo,
        PathValues.RESTMETHODFLICKR_GROUPS_DISCUSS_TOPICS_GET_LIST: RestmethodflickrGroupsDiscussTopicsGetList,
        PathValues.RESTMETHODFLICKR_GROUPS_GET_INFO: RestmethodflickrGroupsGetInfo,
        PathValues.RESTMETHODFLICKR_GROUPS_POOLS_GET_CONTEXT: RestmethodflickrGroupsPoolsGetContext,
        PathValues.RESTMETHODFLICKR_GROUPS_POOLS_GET_PHOTOS: RestmethodflickrGroupsPoolsGetPhotos,
        PathValues.RESTMETHODFLICKR_PEOPLE_GET_INFO: RestmethodflickrPeopleGetInfo,
        PathValues.RESTMETHODFLICKR_PEOPLE_GET_PHOTOS: RestmethodflickrPeopleGetPhotos,
        PathValues.RESTMETHODFLICKR_PHOTOLIST_GET_CONTEXT: RestmethodflickrPhotolistGetContext,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_CONTEXT: RestmethodflickrPhotosGetContext,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_EXIF: RestmethodflickrPhotosGetExif,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_INFO: RestmethodflickrPhotosGetInfo,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_SIZES: RestmethodflickrPhotosGetSizes,
        PathValues.RESTMETHODFLICKR_PHOTOS_LICENSES_GET_INFO: RestmethodflickrPhotosLicensesGetInfo,
        PathValues.RESTMETHODFLICKR_PHOTOS_SEARCH: RestmethodflickrPhotosSearch,
        PathValues.RESTMETHODFLICKR_PHOTOSETS_GET_CONTEXT: RestmethodflickrPhotosetsGetContext,
        PathValues.RESTMETHODFLICKR_PHOTOSETS_GET_LIST: RestmethodflickrPhotosetsGetList,
        PathValues.RESTMETHODFLICKR_PHOTOSETS_GET_PHOTOS: RestmethodflickrPhotosetsGetPhotos,
        PathValues.RESTMETHODFLICKR_TEST_ECHO: RestmethodflickrTestEcho,
        PathValues.UPLOAD: Upload,
    }
)

path_to_api = PathToApi(
    {
        PathValues.OAUTH_ACCESS_TOKEN: OauthAccessToken,
        PathValues.OAUTH_REQUEST_TOKEN: OauthRequestToken,
        PathValues.RESTMETHODFLICKR_FAVORITES_GET_CONTEXT: RestmethodflickrFavoritesGetContext,
        PathValues.RESTMETHODFLICKR_FAVORITES_GET_LIST: RestmethodflickrFavoritesGetList,
        PathValues.RESTMETHODFLICKR_GALLERIES_GET_PHOTOS: RestmethodflickrGalleriesGetPhotos,
        PathValues.RESTMETHODFLICKR_GROUPS_DISCUSS_REPLIES_GET_INFO: RestmethodflickrGroupsDiscussRepliesGetInfo,
        PathValues.RESTMETHODFLICKR_GROUPS_DISCUSS_TOPICS_GET_INFO: RestmethodflickrGroupsDiscussTopicsGetInfo,
        PathValues.RESTMETHODFLICKR_GROUPS_DISCUSS_TOPICS_GET_LIST: RestmethodflickrGroupsDiscussTopicsGetList,
        PathValues.RESTMETHODFLICKR_GROUPS_GET_INFO: RestmethodflickrGroupsGetInfo,
        PathValues.RESTMETHODFLICKR_GROUPS_POOLS_GET_CONTEXT: RestmethodflickrGroupsPoolsGetContext,
        PathValues.RESTMETHODFLICKR_GROUPS_POOLS_GET_PHOTOS: RestmethodflickrGroupsPoolsGetPhotos,
        PathValues.RESTMETHODFLICKR_PEOPLE_GET_INFO: RestmethodflickrPeopleGetInfo,
        PathValues.RESTMETHODFLICKR_PEOPLE_GET_PHOTOS: RestmethodflickrPeopleGetPhotos,
        PathValues.RESTMETHODFLICKR_PHOTOLIST_GET_CONTEXT: RestmethodflickrPhotolistGetContext,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_CONTEXT: RestmethodflickrPhotosGetContext,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_EXIF: RestmethodflickrPhotosGetExif,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_INFO: RestmethodflickrPhotosGetInfo,
        PathValues.RESTMETHODFLICKR_PHOTOS_GET_SIZES: RestmethodflickrPhotosGetSizes,
        PathValues.RESTMETHODFLICKR_PHOTOS_LICENSES_GET_INFO: RestmethodflickrPhotosLicensesGetInfo,
        PathValues.RESTMETHODFLICKR_PHOTOS_SEARCH: RestmethodflickrPhotosSearch,
        PathValues.RESTMETHODFLICKR_PHOTOSETS_GET_CONTEXT: RestmethodflickrPhotosetsGetContext,
        PathValues.RESTMETHODFLICKR_PHOTOSETS_GET_LIST: RestmethodflickrPhotosetsGetList,
        PathValues.RESTMETHODFLICKR_PHOTOSETS_GET_PHOTOS: RestmethodflickrPhotosetsGetPhotos,
        PathValues.RESTMETHODFLICKR_TEST_ECHO: RestmethodflickrTestEcho,
        PathValues.UPLOAD: Upload,
    }
)
