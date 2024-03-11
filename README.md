<div align="center">

[![Visit Flickr](./header.png)](https://flickr.com)

# Flickr<a id="flickr"></a>

A subset of Flickr's API defined in Swagger format.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`flickr.public.flickr_groups_pools_get_context`](#flickrpublicflickr_groups_pools_get_context)
  * [`flickr.public.get_access_token`](#flickrpublicget_access_token)
  * [`flickr.public.get_album_photos`](#flickrpublicget_album_photos)
  * [`flickr.public.get_favorite_photos`](#flickrpublicget_favorite_photos)
  * [`flickr.public.get_favorites_context`](#flickrpublicget_favorites_context)
  * [`flickr.public.get_flickr_test_echo`](#flickrpublicget_flickr_test_echo)
  * [`flickr.public.get_gallery_photos`](#flickrpublicget_gallery_photos)
  * [`flickr.public.get_group_discussion_topics`](#flickrpublicget_group_discussion_topics)
  * [`flickr.public.get_group_info`](#flickrpublicget_group_info)
  * [`flickr.public.get_group_pool_photos`](#flickrpublicget_group_pool_photos)
  * [`flickr.public.get_group_topic_info`](#flickrpublicget_group_topic_info)
  * [`flickr.public.get_group_topic_replies_info`](#flickrpublicget_group_topic_replies_info)
  * [`flickr.public.get_o_auth_token`](#flickrpublicget_o_auth_token)
  * [`flickr.public.get_person_information`](#flickrpublicget_person_information)
  * [`flickr.public.get_photo_exif`](#flickrpublicget_photo_exif)
  * [`flickr.public.get_photo_info`](#flickrpublicget_photo_info)
  * [`flickr.public.get_photo_licenses`](#flickrpublicget_photo_licenses)
  * [`flickr.public.get_photo_list_context`](#flickrpublicget_photo_list_context)
  * [`flickr.public.get_photo_set_context`](#flickrpublicget_photo_set_context)
  * [`flickr.public.get_photo_sizes`](#flickrpublicget_photo_sizes)
  * [`flickr.public.get_photostream_context`](#flickrpublicget_photostream_context)
  * [`flickr.public.get_user_albums`](#flickrpublicget_user_albums)
  * [`flickr.public.get_user_photos`](#flickrpublicget_user_photos)
  * [`flickr.public.search_photos`](#flickrpublicsearch_photos)
  * [`flickr.public.upload_photo`](#flickrpublicupload_photo)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Flickr&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from flickr_python_sdk import Flickr, ApiException

flickr = Flickr()

try:
    flickr_groups_pools_get_context_response = (
        flickr.public.flickr_groups_pools_get_context(
            api_key="api_key_example",
            photo_id="4",
            group_id="BAMDT",
        )
    )
    print(flickr_groups_pools_get_context_response)
except ApiException as e:
    print("Exception when calling PublicApi.flickr_groups_pools_get_context: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from flickr_python_sdk import Flickr, ApiException

flickr = Flickr()


async def main():
    try:
        flickr_groups_pools_get_context_response = (
            await flickr.public.aflickr_groups_pools_get_context(
                api_key="api_key_example",
                photo_id="4",
                group_id="BAMDT",
            )
        )
        print(flickr_groups_pools_get_context_response)
    except ApiException as e:
        print(
            "Exception when calling PublicApi.flickr_groups_pools_get_context: %s\n" % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from flickr_python_sdk import Flickr, ApiException

flickr = Flickr()

try:
    flickr_groups_pools_get_context_response = (
        flickr.public.raw.flickr_groups_pools_get_context(
            api_key="api_key_example",
            photo_id="4",
            group_id="BAMDT",
        )
    )
    pprint(flickr_groups_pools_get_context_response.body)
    pprint(flickr_groups_pools_get_context_response.body["count"])
    pprint(flickr_groups_pools_get_context_response.body["nextphoto"])
    pprint(flickr_groups_pools_get_context_response.body["prevphoto"])
    pprint(flickr_groups_pools_get_context_response.body["stat"])
    pprint(flickr_groups_pools_get_context_response.headers)
    pprint(flickr_groups_pools_get_context_response.status)
    pprint(flickr_groups_pools_get_context_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PublicApi.flickr_groups_pools_get_context: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `flickr.public.flickr_groups_pools_get_context`<a id="flickrpublicflickr_groups_pools_get_context"></a>

Returns next and previous photos for a photo in a group pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
flickr_groups_pools_get_context_response = (
    flickr.public.flickr_groups_pools_get_context(
        api_key="api_key_example",
        photo_id="4",
        group_id="BAMDT",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicFlickrGroupsPoolsGetContextResponse`](./flickr_python_sdk/pydantic/public_flickr_groups_pools_get_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.groups.pools.getContext` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_access_token`<a id="flickrpublicget_access_token"></a>

Returns an access token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_access_token_response = flickr.public.get_access_token(
    oauth_consumer_key="oauth_consumer_key_example",
    oauth_nonce="oauth_nonce_example",
    oauth_timestamp="4",
    oauth_signature_method="oauth_signature_method_example",
    oauth_version="oauth_version_example",
    oauth_signature="oauth_signature_example",
    oauth_verifier="oauth_verifier_example",
    oauth_token="oauth_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### oauth_consumer_key: `str`<a id="oauth_consumer_key-str"></a>

##### oauth_nonce: `str`<a id="oauth_nonce-str"></a>

##### oauth_timestamp: `str`<a id="oauth_timestamp-str"></a>

##### oauth_signature_method: `str`<a id="oauth_signature_method-str"></a>

##### oauth_version: `str`<a id="oauth_version-str"></a>

##### oauth_signature: `str`<a id="oauth_signature-str"></a>

##### oauth_verifier: `str`<a id="oauth_verifier-str"></a>

##### oauth_token: `str`<a id="oauth_token-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/access_token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_album_photos`<a id="flickrpublicget_album_photos"></a>

Returns a list of photos in an album.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_album_photos_response = flickr.public.get_album_photos(
    api_key="api_key_example",
    photoset_id="4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photoset_id: `str`<a id="photoset_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetAlbumPhotosResponse`](./flickr_python_sdk/pydantic/public_get_album_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photosets.getPhotos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_favorite_photos`<a id="flickrpublicget_favorite_photos"></a>

Returns a list of the user's favorite photos. Only photos which the calling user has permission to see are returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_favorite_photos_response = flickr.public.get_favorite_photos(
    api_key="api_key_example",
    user_id="user_id_example",
    min_fave_date=3.14,
    max_fave_date=3.14,
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### min_fave_date: `Union[int, float]`<a id="min_fave_date-unionint-float"></a>

##### max_fave_date: `Union[int, float]`<a id="max_fave_date-unionint-float"></a>

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetFavoritePhotosResponse`](./flickr_python_sdk/pydantic/public_get_favorite_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.favorites.getList` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_favorites_context`<a id="flickrpublicget_favorites_context"></a>

Returns next and previous favorites for a photo in a user's favorites

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_favorites_context_response = flickr.public.get_favorites_context(
    api_key="api_key_example",
    photo_id="4",
    user_id="BAMDT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetFavoritesContextResponse`](./flickr_python_sdk/pydantic/public_get_favorites_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.favorites.getContext` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_flickr_test_echo`<a id="flickrpublicget_flickr_test_echo"></a>

Echos the input parameters back in the response

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_flickr_test_echo_response = flickr.public.get_flickr_test_echo(
    api_key="api_key_example",
    echo="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### echo: `str`<a id="echo-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetFlickrTestEchoResponse`](./flickr_python_sdk/pydantic/public_get_flickr_test_echo_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.test.echo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_gallery_photos`<a id="flickrpublicget_gallery_photos"></a>

Returns a list of photos in a gallery.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_gallery_photos_response = flickr.public.get_gallery_photos(
    api_key="api_key_example",
    gallery_id="gallery_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### gallery_id: `str`<a id="gallery_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetGalleryPhotosResponse`](./flickr_python_sdk/pydantic/public_get_gallery_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.galleries.getPhotos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_group_discussion_topics`<a id="flickrpublicget_group_discussion_topics"></a>

Get a list of discussion topics in a group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_discussion_topics_response = flickr.public.get_group_discussion_topics(
    api_key="api_key_example",
    group_id="BAMDT",
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetGroupDiscussionTopicsResponse`](./flickr_python_sdk/pydantic/public_get_group_discussion_topics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.groups.discuss.topics.getList` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_group_info`<a id="flickrpublicget_group_info"></a>

Get information about a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_info_response = flickr.public.get_group_info(
    api_key="api_key_example",
    group_id="BAMDT",
    group_path_alias="string_example",
    lang="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### group_path_alias: `str`<a id="group_path_alias-str"></a>

##### lang: `str`<a id="lang-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetGroupInfoResponse`](./flickr_python_sdk/pydantic/public_get_group_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.groups.getInfo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_group_pool_photos`<a id="flickrpublicget_group_pool_photos"></a>

Returns a list of pool photos for a given group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_pool_photos_response = flickr.public.get_group_pool_photos(
    api_key="api_key_example",
    group_id="BAMDT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetGroupPoolPhotosResponse`](./flickr_python_sdk/pydantic/public_get_group_pool_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.groups.pools.getPhotos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_group_topic_info`<a id="flickrpublicget_group_topic_info"></a>

Get information about a group discussion topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_topic_info_response = flickr.public.get_group_topic_info(
    api_key="api_key_example",
    topic_id="4",
    group_id="BAMDT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetGroupTopicInfoResponse`](./flickr_python_sdk/pydantic/public_get_group_topic_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.groups.discuss.topics.getInfo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_group_topic_replies_info`<a id="flickrpublicget_group_topic_replies_info"></a>

Get information on a group topic reply

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_topic_replies_info_response = flickr.public.get_group_topic_replies_info(
    api_key="api_key_example",
    topic_id="4",
    reply_id="4",
    group_id="BAMDT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

##### reply_id: `str`<a id="reply_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetGroupTopicRepliesInfoResponse`](./flickr_python_sdk/pydantic/public_get_group_topic_replies_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.groups.discuss.replies.getInfo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_o_auth_token`<a id="flickrpublicget_o_auth_token"></a>

Returns an oauth token and oauth token secret

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_o_auth_token_response = flickr.public.get_o_auth_token(
    oauth_consumer_key="oauth_consumer_key_example",
    oauth_nonce="oauth_nonce_example",
    oauth_timestamp="4",
    oauth_signature_method="oauth_signature_method_example",
    oauth_version="oauth_version_example",
    oauth_signature="oauth_signature_example",
    oauth_callback="httpjUR,rZ#UM/?R,Fp^l6$ARj",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### oauth_consumer_key: `str`<a id="oauth_consumer_key-str"></a>

##### oauth_nonce: `str`<a id="oauth_nonce-str"></a>

##### oauth_timestamp: `str`<a id="oauth_timestamp-str"></a>

##### oauth_signature_method: `str`<a id="oauth_signature_method-str"></a>

##### oauth_version: `str`<a id="oauth_version-str"></a>

##### oauth_signature: `str`<a id="oauth_signature-str"></a>

##### oauth_callback: `str`<a id="oauth_callback-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/request_token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_person_information`<a id="flickrpublicget_person_information"></a>

Returns a person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_person_information_response = flickr.public.get_person_information(
    api_key="api_key_example",
    user_id="BAMDT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPersonInformationResponse`](./flickr_python_sdk/pydantic/public_get_person_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.people.getInfo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photo_exif`<a id="flickrpublicget_photo_exif"></a>

Retrieves a list of EXIF/TIFF/GPS tags for a given photo. The calling user must have permission to view the photo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_exif_response = flickr.public.get_photo_exif(
    api_key="api_key_example",
    photo_id="4",
    secret="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

##### secret: `str`<a id="secret-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotoExifResponse`](./flickr_python_sdk/pydantic/public_get_photo_exif_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photos.getExif` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photo_info`<a id="flickrpublicget_photo_info"></a>

Returns a photo

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_info_response = flickr.public.get_photo_info(
    api_key="api_key_example",
    photo_id="4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotoInfoResponse`](./flickr_python_sdk/pydantic/public_get_photo_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photos.getInfo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photo_licenses`<a id="flickrpublicget_photo_licenses"></a>

Fetches a list of available photo licenses for Flickr

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_licenses_response = flickr.public.get_photo_licenses(
    api_key="api_key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotoLicensesResponse`](./flickr_python_sdk/pydantic/public_get_photo_licenses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photos.licenses.getInfo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photo_list_context`<a id="flickrpublicget_photo_list_context"></a>

Returns next and previous photos in a photo list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_list_context_response = flickr.public.get_photo_list_context(
    api_key="api_key_example",
    photo_id="4",
    photolist_id="photolist_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

##### photolist_id: `str`<a id="photolist_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotoListContextResponse`](./flickr_python_sdk/pydantic/public_get_photo_list_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photolist.getContext` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photo_set_context`<a id="flickrpublicget_photo_set_context"></a>

Returns next and previous photos for a photo in a set

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_set_context_response = flickr.public.get_photo_set_context(
    api_key="api_key_example",
    photo_id="4",
    photoset_id="4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

##### photoset_id: `str`<a id="photoset_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotoSetContextResponse`](./flickr_python_sdk/pydantic/public_get_photo_set_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photosets.getContext` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photo_sizes`<a id="flickrpublicget_photo_sizes"></a>

Returns photo sizes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_sizes_response = flickr.public.get_photo_sizes(
    api_key="api_key_example",
    photo_id="4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotoSizesResponse`](./flickr_python_sdk/pydantic/public_get_photo_sizes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photos.getSizes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_photostream_context`<a id="flickrpublicget_photostream_context"></a>

Returns next and previous photos for a photo in a photostream

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photostream_context_response = flickr.public.get_photostream_context(
    api_key="api_key_example",
    photo_id="4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo_id: `str`<a id="photo_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetPhotostreamContextResponse`](./flickr_python_sdk/pydantic/public_get_photostream_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photos.getContext` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_user_albums`<a id="flickrpublicget_user_albums"></a>

Returns the albums belonging to the specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_albums_response = flickr.public.get_user_albums(
    api_key="api_key_example",
    user_id="user_id_example",
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetUserAlbumsResponse`](./flickr_python_sdk/pydantic/public_get_user_albums_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photosets.getList` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.get_user_photos`<a id="flickrpublicget_user_photos"></a>

Return photos from the given user's photostream

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_photos_response = flickr.public.get_user_photos(
    api_key="api_key_example",
    user_id="user_id_example",
    safe_search=3.14,
    min_upload_date=3.14,
    max_upload_date=3.14,
    min_taken_date=3.14,
    max_taken_date=3.14,
    content_type=3.14,
    privacy_filter=3.14,
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### safe_search: `Union[int, float]`<a id="safe_search-unionint-float"></a>

##### min_upload_date: `Union[int, float]`<a id="min_upload_date-unionint-float"></a>

##### max_upload_date: `Union[int, float]`<a id="max_upload_date-unionint-float"></a>

##### min_taken_date: `Union[int, float]`<a id="min_taken_date-unionint-float"></a>

##### max_taken_date: `Union[int, float]`<a id="max_taken_date-unionint-float"></a>

##### content_type: `Union[int, float]`<a id="content_type-unionint-float"></a>

##### privacy_filter: `Union[int, float]`<a id="privacy_filter-unionint-float"></a>

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PublicGetUserPhotosResponse`](./flickr_python_sdk/pydantic/public_get_user_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.people.getPhotos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.search_photos`<a id="flickrpublicsearch_photos"></a>

Return a list of photos matching some criteria.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_photos_response = flickr.public.search_photos(
    api_key="api_key_example",
    text="string_example",
    tags="string_example",
    user_id="string_example",
    min_upload_date="string_example",
    max_upload_date="string_example",
    min_taken_date="string_example",
    max_taken_date="string_example",
    license="string_example",
    sort="string_example",
    privacy_filter=3.14,
    bbox="string_example",
    accuracy="string_example",
    safe_search=3.14,
    content_type=3.14,
    machine_tags="string_example",
    machine_tag_mode="string_example",
    group_id="string_example",
    contacts="string_example",
    woe_id="string_example",
    place_id="string_example",
    media="string_example",
    has_geo="string_example",
    geo_context="string_example",
    lat="string_example",
    lon="string_example",
    radius=3.14,
    radius_units="string_example",
    is_commons=True,
    in_gallery=True,
    is_getty=True,
    per_page=3.14,
    page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### text: `str`<a id="text-str"></a>

A free text search. Photos who's title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character.

##### tags: `str`<a id="tags-str"></a>

A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character.

##### user_id: `str`<a id="user_id-str"></a>

The NSID of the user who's photo to search. If this parameter isn't passed then everybody's public photos will be searched. A value of \"me\" will search against the calling user's photos for authenticated calls.

##### min_upload_date: `str`<a id="min_upload_date-str"></a>

Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.

##### max_upload_date: `str`<a id="max_upload_date-str"></a>

Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.

##### min_taken_date: `str`<a id="min_taken_date-str"></a>

Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.

##### max_taken_date: `str`<a id="max_taken_date-str"></a>

Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.

##### license: `str`<a id="license-str"></a>

The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated.

##### sort: `str`<a id="sort-str"></a>

The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are:   date-posted-asc,   date-posted-desc,   date-taken-asc,   date-taken-desc,   interestingness-desc,   interestingness-asc, and   relevance. 

##### privacy_filter: `Union[int, float]`<a id="privacy_filter-unionint-float"></a>

Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:,   1: public photos,   2: private photos visible to friends,   3: private photos visible to family,   4: private photos visible to friends & family,   5: completely private photos 

##### bbox: `str`<a id="bbox-str"></a>

A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched.

##### accuracy: `str`<a id="accuracy-str"></a>

Recorded accuracy level of the location information. Current range is 1-16:   World level is 1   Country is ~3   Region is ~6   City is ~11   Street is ~16 

##### safe_search: `Union[int, float]`<a id="safe_search-unionint-float"></a>

Safe search setting:   1: for safe,   2: for moderate,   3: for restricted 

##### content_type: `Union[int, float]`<a id="content_type-unionint-float"></a>

Content Type setting:   1: photos only.   2: screenshots only.   3: 'other' only.   4: photos and screenshots.   5: screenshots and 'other'.   6: photos and 'other'.   7: photos, screenshots, and 'other' (all). 

##### machine_tags: `str`<a id="machine_tags-str"></a>

Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties : Find photos using the 'dc' namespace : \"machine_tags\" => \"dc:\" Find photos with a title in the 'dc' namespace : \"machine_tags\" => \"dc:title=\" Find photos titled \"mr. camera\" in the 'dc' namespace : \"machine_tags\" => \"dc:title=\\\"mr. camera\\\" Find photos whose value is \"mr. camera\" : \"machine_tags\" => \"*:*=\\\"mr. camera\\\"\" Find photos that have a title, in any namespace : \"machine_tags\" => \"*:title=\" Find photos that have a title, in any namespace, whose value is \"mr. camera\" : \"machine_tags\" => \"*:title=\\\"mr. camera\\\"\" Find photos, in the 'dc' namespace whose value is \"mr. camera\" : \"machine_tags\" => \"dc:*=\\\"mr. camera\\\"\" Multiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. \"AND\" queries are limited to (16) machine tags. \"OR\" queries are limited to (8). 

##### machine_tag_mode: `str`<a id="machine_tag_mode-str"></a>

Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.

##### group_id: `str`<a id="group_id-str"></a>

The id of a group who's pool to search. If specified, only matching photos posted to the group's pool will be returned.

##### contacts: `str`<a id="contacts-str"></a>

Search your contacts. Either 'all' or 'ff' for just friends and family. (Experimental)

##### woe_id: `str`<a id="woe_id-str"></a>

A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present).

##### place_id: `str`<a id="place_id-str"></a>

A Flickr place id. (not used if bbox argument is present). Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 

##### media: `str`<a id="media-str"></a>

Filter results by media type. Possible values are all (default), photos or videos

##### has_geo: `str`<a id="has_geo-str"></a>

Any photo that has been geotagged, or if the value is \"0\" any photo that has not been geotagged. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 

##### geo_context: `str`<a id="geo_context-str"></a>

Geo context is a numeric value representing the photo's geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken \"indoors\" or \"outdoors\". The current list of context IDs is: 0, not defined. 1, indoors. 2, outdoors. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 

##### lat: `str`<a id="lat-str"></a>

A valid latitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 

##### lon: `str`<a id="lon-str"></a>

A valid longitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 

##### radius: `Union[int, float]`<a id="radius-unionint-float"></a>

A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km).

##### radius_units: `str`<a id="radius_units-str"></a>

The unit of measure when doing radial geo queries. Valid options are \"mi\" (miles) and \"km\" (kilometers). The default is \"km\".

##### is_commons: `bool`<a id="is_commons-bool"></a>

Limit the scope of the search to only photos that are part of the Flickr Commons project. Default is false.

##### in_gallery: `bool`<a id="in_gallery-bool"></a>

Limit the scope of the search to only photos that are in a gallery? Default is false, search all photos.

##### is_getty: `bool`<a id="is_getty-bool"></a>

Limit the scope of the search to only photos that are for sale on Getty. Default is false.

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page of results to return. If this argument is omitted, it defaults to 1.

#### 🔄 Return<a id="🔄-return"></a>

[`PublicSearchPhotosResponse`](./flickr_python_sdk/pydantic/public_search_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest?method&#x3D;flickr.photos.search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `flickr.public.upload_photo`<a id="flickrpublicupload_photo"></a>

Uploads a new photo to Flickr

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_photo_response = flickr.public.upload_photo(
    api_key="string_example",
    photo=open("/path/to/file", "rb"),
    tags="string_example",
    title="string_example",
    description="string_example",
    content_type="1",
    hidden="1",
    is_family="0",
    is_friend="0",
    is_public="0",
    safety_level="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### photo: `IO`<a id="photo-io"></a>

##### tags: `str`<a id="tags-str"></a>

##### title: `str`<a id="title-str"></a>

##### description: `str`<a id="description-str"></a>

##### content_type: `str`<a id="content_type-str"></a>

##### hidden: `str`<a id="hidden-str"></a>

##### is_family: `str`<a id="is_family-str"></a>

##### is_friend: `str`<a id="is_friend-str"></a>

##### is_public: `str`<a id="is_public-str"></a>

##### safety_level: `str`<a id="safety_level-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PublicUploadPhotoRequest`](./flickr_python_sdk/type/public_upload_photo_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
