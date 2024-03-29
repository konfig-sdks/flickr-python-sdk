# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from flickr_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from flickr_python_sdk.model.album import Album
from flickr_python_sdk.model.context_photo import ContextPhoto
from flickr_python_sdk.model.context_photos import ContextPhotos
from flickr_python_sdk.model.cover import Cover
from flickr_python_sdk.model.group import Group
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
from flickr_python_sdk.model.note import Note
from flickr_python_sdk.model.owner import Owner
from flickr_python_sdk.model.person import Person
from flickr_python_sdk.model.person_description import PersonDescription
from flickr_python_sdk.model.person_disable_keyboard_shortcuts import PersonDisableKeyboardShortcuts
from flickr_python_sdk.model.person_location import PersonLocation
from flickr_python_sdk.model.person_mbox_sha1_sum import PersonMboxSha1Sum
from flickr_python_sdk.model.person_mobileurl import PersonMobileurl
from flickr_python_sdk.model.person_photos import PersonPhotos
from flickr_python_sdk.model.person_photos_count import PersonPhotosCount
from flickr_python_sdk.model.person_photos_firstdate import PersonPhotosFirstdate
from flickr_python_sdk.model.person_photos_firstdatetaken import PersonPhotosFirstdatetaken
from flickr_python_sdk.model.person_photos_views import PersonPhotosViews
from flickr_python_sdk.model.person_photosurl import PersonPhotosurl
from flickr_python_sdk.model.person_profileurl import PersonProfileurl
from flickr_python_sdk.model.person_realname import PersonRealname
from flickr_python_sdk.model.person_timezone import PersonTimezone
from flickr_python_sdk.model.person_unread_messages import PersonUnreadMessages
from flickr_python_sdk.model.person_username import PersonUsername
from flickr_python_sdk.model.photo import Photo
from flickr_python_sdk.model.photo_comments import PhotoComments
from flickr_python_sdk.model.photo_dates import PhotoDates
from flickr_python_sdk.model.photo_description import PhotoDescription
from flickr_python_sdk.model.photo_editability import PhotoEditability
from flickr_python_sdk.model.photo_notes import PhotoNotes
from flickr_python_sdk.model.photo_people import PhotoPeople
from flickr_python_sdk.model.photo_permissions import PhotoPermissions
from flickr_python_sdk.model.photo_publiceditability import PhotoPubliceditability
from flickr_python_sdk.model.photo_tags import PhotoTags
from flickr_python_sdk.model.photo_title import PhotoTitle
from flickr_python_sdk.model.photo_urls import PhotoURLs
from flickr_python_sdk.model.photo_urls import PhotoUrls
from flickr_python_sdk.model.photo_usage import PhotoUsage
from flickr_python_sdk.model.photo_visibility import PhotoVisibility
from flickr_python_sdk.model.public_flickr_groups_pools_get_context_response import PublicFlickrGroupsPoolsGetContextResponse
from flickr_python_sdk.model.public_flickr_groups_pools_get_context_response_count import PublicFlickrGroupsPoolsGetContextResponseCount
from flickr_python_sdk.model.public_get_access_token_response import PublicGetAccessTokenResponse
from flickr_python_sdk.model.public_get_album_photos_response import PublicGetAlbumPhotosResponse
from flickr_python_sdk.model.public_get_favorite_photos_response import PublicGetFavoritePhotosResponse
from flickr_python_sdk.model.public_get_favorites_context_response import PublicGetFavoritesContextResponse
from flickr_python_sdk.model.public_get_favorites_context_response_count import PublicGetFavoritesContextResponseCount
from flickr_python_sdk.model.public_get_flickr_test_echo_response import PublicGetFlickrTestEchoResponse
from flickr_python_sdk.model.public_get_flickr_test_echo_response_echo import PublicGetFlickrTestEchoResponseEcho
from flickr_python_sdk.model.public_get_gallery_photos_response import PublicGetGalleryPhotosResponse
from flickr_python_sdk.model.public_get_group_discussion_topics_response import PublicGetGroupDiscussionTopicsResponse
from flickr_python_sdk.model.public_get_group_info_response import PublicGetGroupInfoResponse
from flickr_python_sdk.model.public_get_group_pool_photos_response import PublicGetGroupPoolPhotosResponse
from flickr_python_sdk.model.public_get_group_topic_info_response import PublicGetGroupTopicInfoResponse
from flickr_python_sdk.model.public_get_group_topic_replies_info_response import PublicGetGroupTopicRepliesInfoResponse
from flickr_python_sdk.model.public_get_o_auth_token_response import PublicGetOAuthTokenResponse
from flickr_python_sdk.model.public_get_person_information_response import PublicGetPersonInformationResponse
from flickr_python_sdk.model.public_get_photo_exif_response import PublicGetPhotoExifResponse
from flickr_python_sdk.model.public_get_photo_exif_response_photo import PublicGetPhotoExifResponsePhoto
from flickr_python_sdk.model.public_get_photo_exif_response_photo_exif import PublicGetPhotoExifResponsePhotoExif
from flickr_python_sdk.model.public_get_photo_exif_response_photo_exif_item import PublicGetPhotoExifResponsePhotoExifItem
from flickr_python_sdk.model.public_get_photo_exif_response_photo_exif_item_raw import PublicGetPhotoExifResponsePhotoExifItemRaw
from flickr_python_sdk.model.public_get_photo_info_response import PublicGetPhotoInfoResponse
from flickr_python_sdk.model.public_get_photo_licenses_response import PublicGetPhotoLicensesResponse
from flickr_python_sdk.model.public_get_photo_licenses_response_licenses import PublicGetPhotoLicensesResponseLicenses
from flickr_python_sdk.model.public_get_photo_licenses_response_licenses_license import PublicGetPhotoLicensesResponseLicensesLicense
from flickr_python_sdk.model.public_get_photo_licenses_response_licenses_license_item import PublicGetPhotoLicensesResponseLicensesLicenseItem
from flickr_python_sdk.model.public_get_photo_list_context_response import PublicGetPhotoListContextResponse
from flickr_python_sdk.model.public_get_photo_list_context_response_count import PublicGetPhotoListContextResponseCount
from flickr_python_sdk.model.public_get_photo_set_context_response import PublicGetPhotoSetContextResponse
from flickr_python_sdk.model.public_get_photo_set_context_response_count import PublicGetPhotoSetContextResponseCount
from flickr_python_sdk.model.public_get_photo_sizes_response import PublicGetPhotoSizesResponse
from flickr_python_sdk.model.public_get_photo_sizes_response_sizes import PublicGetPhotoSizesResponseSizes
from flickr_python_sdk.model.public_get_photostream_context_response import PublicGetPhotostreamContextResponse
from flickr_python_sdk.model.public_get_photostream_context_response_count import PublicGetPhotostreamContextResponseCount
from flickr_python_sdk.model.public_get_user_albums_response import PublicGetUserAlbumsResponse
from flickr_python_sdk.model.public_get_user_photos_response import PublicGetUserPhotosResponse
from flickr_python_sdk.model.public_search_photos_response import PublicSearchPhotosResponse
from flickr_python_sdk.model.public_upload_photo_request import PublicUploadPhotoRequest
from flickr_python_sdk.model.size import Size
from flickr_python_sdk.model.stat import Stat
from flickr_python_sdk.model.tag import Tag
from flickr_python_sdk.model.topic import Topic
from flickr_python_sdk.model.topic_message import TopicMessage
from flickr_python_sdk.model.topic_reply import TopicReply
from flickr_python_sdk.model.topic_reply_message import TopicReplyMessage
from flickr_python_sdk.model.url import URL
