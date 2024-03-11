# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flickr_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    OAUTH_ACCESS_TOKEN = "/oauth/access_token"
    OAUTH_REQUEST_TOKEN = "/oauth/request_token"
    RESTMETHODFLICKR_FAVORITES_GET_CONTEXT = "/rest?method&#x3D;flickr.favorites.getContext"
    RESTMETHODFLICKR_FAVORITES_GET_LIST = "/rest?method&#x3D;flickr.favorites.getList"
    RESTMETHODFLICKR_GALLERIES_GET_PHOTOS = "/rest?method&#x3D;flickr.galleries.getPhotos"
    RESTMETHODFLICKR_GROUPS_DISCUSS_REPLIES_GET_INFO = "/rest?method&#x3D;flickr.groups.discuss.replies.getInfo"
    RESTMETHODFLICKR_GROUPS_DISCUSS_TOPICS_GET_INFO = "/rest?method&#x3D;flickr.groups.discuss.topics.getInfo"
    RESTMETHODFLICKR_GROUPS_DISCUSS_TOPICS_GET_LIST = "/rest?method&#x3D;flickr.groups.discuss.topics.getList"
    RESTMETHODFLICKR_GROUPS_GET_INFO = "/rest?method&#x3D;flickr.groups.getInfo"
    RESTMETHODFLICKR_GROUPS_POOLS_GET_CONTEXT = "/rest?method&#x3D;flickr.groups.pools.getContext"
    RESTMETHODFLICKR_GROUPS_POOLS_GET_PHOTOS = "/rest?method&#x3D;flickr.groups.pools.getPhotos"
    RESTMETHODFLICKR_PEOPLE_GET_INFO = "/rest?method&#x3D;flickr.people.getInfo"
    RESTMETHODFLICKR_PEOPLE_GET_PHOTOS = "/rest?method&#x3D;flickr.people.getPhotos"
    RESTMETHODFLICKR_PHOTOLIST_GET_CONTEXT = "/rest?method&#x3D;flickr.photolist.getContext"
    RESTMETHODFLICKR_PHOTOS_GET_CONTEXT = "/rest?method&#x3D;flickr.photos.getContext"
    RESTMETHODFLICKR_PHOTOS_GET_EXIF = "/rest?method&#x3D;flickr.photos.getExif"
    RESTMETHODFLICKR_PHOTOS_GET_INFO = "/rest?method&#x3D;flickr.photos.getInfo"
    RESTMETHODFLICKR_PHOTOS_GET_SIZES = "/rest?method&#x3D;flickr.photos.getSizes"
    RESTMETHODFLICKR_PHOTOS_LICENSES_GET_INFO = "/rest?method&#x3D;flickr.photos.licenses.getInfo"
    RESTMETHODFLICKR_PHOTOS_SEARCH = "/rest?method&#x3D;flickr.photos.search"
    RESTMETHODFLICKR_PHOTOSETS_GET_CONTEXT = "/rest?method&#x3D;flickr.photosets.getContext"
    RESTMETHODFLICKR_PHOTOSETS_GET_LIST = "/rest?method&#x3D;flickr.photosets.getList"
    RESTMETHODFLICKR_PHOTOSETS_GET_PHOTOS = "/rest?method&#x3D;flickr.photosets.getPhotos"
    RESTMETHODFLICKR_TEST_ECHO = "/rest?method&#x3D;flickr.test.echo"
    UPLOAD = "/upload"
