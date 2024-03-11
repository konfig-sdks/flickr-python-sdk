# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flickr_python_sdk.paths.oauth_request_token import Api

from flickr_python_sdk.paths import PathValues

path = PathValues.OAUTH_REQUEST_TOKEN