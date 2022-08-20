# openapi_client.ServerApi

All URIs are relative to *http://https://rest.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_create_pkg_paste_server**](ServerApi.md#server_create_pkg_paste_server) | **POST** /v1/server/paste | createPkgPasteServer server
[**server_delete_server**](ServerApi.md#server_delete_server) | **DELETE** /v1/server/{serverID} | deleteServer server
[**server_get_server_detail**](ServerApi.md#server_get_server_detail) | **GET** /v1/server/{serverID} | getServerDetail server
[**server_get_server_detail_by_uuid**](ServerApi.md#server_get_server_detail_by_uuid) | **GET** /v1/server/uuid/{serverUuid} | getServerDetailByUUID server
[**server_get_server_list**](ServerApi.md#server_get_server_list) | **GET** /v1/servers | getServerList server
[**server_update_pkg_paste_server**](ServerApi.md#server_update_pkg_paste_server) | **PUT** /v1/server/paste/{serverID} | updatePkgPasteServer server
[**server_update_server**](ServerApi.md#server_update_server) | **PUT** /v1/server/{serverID} | updateServer server


# **server_create_pkg_paste_server**
> ServerCreatePkgPasteServerResponseBody server_create_pkg_paste_server(create_pkg_paste_server_request_body)

createPkgPasteServer server

create paste server

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.server_create_pkg_paste_server_response_body import ServerCreatePkgPasteServerResponseBody
from openapi_client.model.server_create_pkg_paste_server_request_body import ServerCreatePkgPasteServerRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    create_pkg_paste_server_request_body = ServerCreatePkgPasteServerRequestBody(
        kernel_release="kernel release",
        kernel_version="kernel version",
        os_family="20",
        os_version="20",
        pkg_paste_text="",
        server_name="Server Name",
    ) # ServerCreatePkgPasteServerRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # createPkgPasteServer server
        api_response = api_instance.server_create_pkg_paste_server(create_pkg_paste_server_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_create_pkg_paste_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createPkgPasteServer server
        api_response = api_instance.server_create_pkg_paste_server(create_pkg_paste_server_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_create_pkg_paste_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pkg_paste_server_request_body** | [**ServerCreatePkgPasteServerRequestBody**](ServerCreatePkgPasteServerRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**ServerCreatePkgPasteServerResponseBody**](ServerCreatePkgPasteServerResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/gob
 - **Accept**: application/json, application/xml, application/gob


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_delete_server**
> server_delete_server(server_id)

deleteServer server

server delete

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    server_id = 1 # int | Server ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # deleteServer server
        api_instance.server_delete_server(server_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_delete_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # deleteServer server
        api_instance.server_delete_server(server_id, authorization=authorization)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_delete_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID |
 **authorization** | **str**| api key auth | [optional]

### Return type

void (empty response body)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get_server_detail**
> ServerGetServerDetailResponseBody server_get_server_detail(server_id)

getServerDetail server

server detail

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.server_get_server_detail_response_body import ServerGetServerDetailResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    server_id = 1 # int | Server ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getServerDetail server
        api_response = api_instance.server_get_server_detail(server_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_get_server_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getServerDetail server
        api_response = api_instance.server_get_server_detail(server_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_get_server_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**ServerGetServerDetailResponseBody**](ServerGetServerDetailResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/gob


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get_server_detail_by_uuid**
> ServerGetServerDetailByUUIDResponseBody server_get_server_detail_by_uuid(server_uuid)

getServerDetailByUUID server

server detail by UUID

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.server_get_server_detail_by_uuid_response_body import ServerGetServerDetailByUUIDResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    server_uuid = "serverUuid_example" # str | Server UUID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getServerDetailByUUID server
        api_response = api_instance.server_get_server_detail_by_uuid(server_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_get_server_detail_by_uuid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getServerDetailByUUID server
        api_response = api_instance.server_get_server_detail_by_uuid(server_uuid, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_get_server_detail_by_uuid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_uuid** | **str**| Server UUID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**ServerGetServerDetailByUUIDResponseBody**](ServerGetServerDetailByUUIDResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/gob


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get_server_list**
> ServerGetServerListResponseBody server_get_server_list()

getServerList server

server list

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.server_get_server_list_response_body import ServerGetServerListResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    page = 1 # int | Page Number (optional) if omitted the server will use the default value of 1
    limit = 20 # int | Limit (optional) if omitted the server will use the default value of 20
    offset = 0 # int | Offset (optional) if omitted the server will use the default value of 0
    filter_cve_id = "filterCveID_example" # str | CveID filter (optional)
    filter_role_id = 1 # int | ServerRoleID filter (optional)
    filter_tag_name = "filterTagName_example" # str | ServerTagName filter (optional)
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getServerList server
        api_response = api_instance.server_get_server_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_role_id=filter_role_id, filter_tag_name=filter_tag_name, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_get_server_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Limit | [optional] if omitted the server will use the default value of 20
 **offset** | **int**| Offset | [optional] if omitted the server will use the default value of 0
 **filter_cve_id** | **str**| CveID filter | [optional]
 **filter_role_id** | **int**| ServerRoleID filter | [optional]
 **filter_tag_name** | **str**| ServerTagName filter | [optional]
 **authorization** | **str**| api key auth | [optional]

### Return type

[**ServerGetServerListResponseBody**](ServerGetServerListResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/gob


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_update_pkg_paste_server**
> server_update_pkg_paste_server(server_id, update_pkg_paste_server_request_body)

updatePkgPasteServer server

update paste server

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.server_update_pkg_paste_server_request_body import ServerUpdatePkgPasteServerRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    server_id = 1 # int | Server ID
    update_pkg_paste_server_request_body = ServerUpdatePkgPasteServerRequestBody(
        kernel_release="kernel release",
        kernel_version="kernel version",
        os_version="20",
        pkg_paste_text="",
    ) # ServerUpdatePkgPasteServerRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # updatePkgPasteServer server
        api_instance.server_update_pkg_paste_server(server_id, update_pkg_paste_server_request_body)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_update_pkg_paste_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updatePkgPasteServer server
        api_instance.server_update_pkg_paste_server(server_id, update_pkg_paste_server_request_body, authorization=authorization)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_update_pkg_paste_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID |
 **update_pkg_paste_server_request_body** | [**ServerUpdatePkgPasteServerRequestBody**](ServerUpdatePkgPasteServerRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

void (empty response body)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/gob
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_update_server**
> ServerUpdateServerResponseBody server_update_server(server_id, update_server_request_body)

updateServer server

update server

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.server_update_server_request_body import ServerUpdateServerRequestBody
from openapi_client.model.server_update_server_response_body import ServerUpdateServerResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)
    server_id = 1 # int | Server ID
    update_server_request_body = ServerUpdateServerRequestBody(
        additional_info="This server is expensive",
        default_user_id=1,
        role_id=1,
        server_name="new-server-name",
    ) # ServerUpdateServerRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateServer server
        api_response = api_instance.server_update_server(server_id, update_server_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_update_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateServer server
        api_response = api_instance.server_update_server(server_id, update_server_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->server_update_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID |
 **update_server_request_body** | [**ServerUpdateServerRequestBody**](ServerUpdateServerRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**ServerUpdateServerResponseBody**](ServerUpdateServerResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/gob
 - **Accept**: application/json, application/xml, application/gob


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

