# openapi_client.PkgCpeApi

All URIs are relative to *http://rest.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pkg_cpe_add_cpe**](PkgCpeApi.md#pkg_cpe_add_cpe) | **POST** /v1/pkgCpe/cpe | addCpe pkgCpe
[**pkg_cpe_delete_cpe**](PkgCpeApi.md#pkg_cpe_delete_cpe) | **DELETE** /v1/pkgCpe/cpe/{cpeID} | deleteCpe pkgCpe
[**pkg_cpe_delete_cpe_deprecated**](PkgCpeApi.md#pkg_cpe_delete_cpe_deprecated) | **DELETE** /v1/pkgCpe/cpe | deleteCpe_deprecated pkgCpe
[**pkg_cpe_get_cpe_detail**](PkgCpeApi.md#pkg_cpe_get_cpe_detail) | **GET** /v1/pkgCpe/cpe/{cpeID} | getCpeDetail pkgCpe
[**pkg_cpe_get_pkg_cpe_list**](PkgCpeApi.md#pkg_cpe_get_pkg_cpe_list) | **GET** /v1/pkgCpes | getPkgCpeList pkgCpe
[**pkg_cpe_get_pkg_detail**](PkgCpeApi.md#pkg_cpe_get_pkg_detail) | **GET** /v1/pkgCpe/pkg/{pkgID} | getPkgDetail pkgCpe


# **pkg_cpe_add_cpe**
> PkgCpeAddCpeResponseBody pkg_cpe_add_cpe(add_cpe_request_body)

addCpe pkgCpe

add cpe

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import pkg_cpe_api
from openapi_client.model.pkg_cpe_add_cpe_response_body import PkgCpeAddCpeResponseBody
from openapi_client.model.pkg_cpe_add_cpe_request_body import PkgCpeAddCpeRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://rest.vuls.biz"
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
    api_instance = pkg_cpe_api.PkgCpeApi(api_client)
    add_cpe_request_body = PkgCpeAddCpeRequestBody(
        cpe_name="cpe:/a:berlios:discussion_forum_2k:3.3",
        is_uri=True,
        server_id=1,
    ) # PkgCpeAddCpeRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # addCpe pkgCpe
        api_response = api_instance.pkg_cpe_add_cpe(add_cpe_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_add_cpe: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # addCpe pkgCpe
        api_response = api_instance.pkg_cpe_add_cpe(add_cpe_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_add_cpe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_cpe_request_body** | [**PkgCpeAddCpeRequestBody**](PkgCpeAddCpeRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**PkgCpeAddCpeResponseBody**](PkgCpeAddCpeResponseBody.md)

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

# **pkg_cpe_delete_cpe**
> pkg_cpe_delete_cpe(cpe_id)

deleteCpe pkgCpe

delete cpe (urlにcpeIDを指定してください。cpeIDの指定のないアクセス方法は今後削除されます。)

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import pkg_cpe_api
from pprint import pprint
# Defining the host is optional and defaults to http://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://rest.vuls.biz"
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
    api_instance = pkg_cpe_api.PkgCpeApi(api_client)
    cpe_id = 1 # int | cpe ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # deleteCpe pkgCpe
        api_instance.pkg_cpe_delete_cpe(cpe_id)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_delete_cpe: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # deleteCpe pkgCpe
        api_instance.pkg_cpe_delete_cpe(cpe_id, authorization=authorization)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_delete_cpe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_id** | **int**| cpe ID |
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

# **pkg_cpe_delete_cpe_deprecated**
> pkg_cpe_delete_cpe_deprecated(delete_cpe_deprecated_request_body)

deleteCpe_deprecated pkgCpe

[deprecated] urlにcpeIDを指定して利用してください。cpeIDの指定のないこちらのアクセス方法は今後削除されます。

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import pkg_cpe_api
from openapi_client.model.pkg_cpe_delete_cpe_deprecated_request_body import PkgCpeDeleteCpeDeprecatedRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://rest.vuls.biz"
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
    api_instance = pkg_cpe_api.PkgCpeApi(api_client)
    delete_cpe_deprecated_request_body = PkgCpeDeleteCpeDeprecatedRequestBody(
        cpe_id=4046142736569201742,
    ) # PkgCpeDeleteCpeDeprecatedRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # deleteCpe_deprecated pkgCpe
        api_instance.pkg_cpe_delete_cpe_deprecated(delete_cpe_deprecated_request_body)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_delete_cpe_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # deleteCpe_deprecated pkgCpe
        api_instance.pkg_cpe_delete_cpe_deprecated(delete_cpe_deprecated_request_body, authorization=authorization)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_delete_cpe_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_cpe_deprecated_request_body** | [**PkgCpeDeleteCpeDeprecatedRequestBody**](PkgCpeDeleteCpeDeprecatedRequestBody.md)|  |
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

# **pkg_cpe_get_cpe_detail**
> PkgCpeGetCpeDetailResponseBody pkg_cpe_get_cpe_detail(cpe_id)

getCpeDetail pkgCpe

cpe detail

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import pkg_cpe_api
from openapi_client.model.pkg_cpe_get_cpe_detail_response_body import PkgCpeGetCpeDetailResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://rest.vuls.biz"
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
    api_instance = pkg_cpe_api.PkgCpeApi(api_client)
    cpe_id = 1 # int | cpe ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getCpeDetail pkgCpe
        api_response = api_instance.pkg_cpe_get_cpe_detail(cpe_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_cpe_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getCpeDetail pkgCpe
        api_response = api_instance.pkg_cpe_get_cpe_detail(cpe_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_cpe_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_id** | **int**| cpe ID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**PkgCpeGetCpeDetailResponseBody**](PkgCpeGetCpeDetailResponseBody.md)

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

# **pkg_cpe_get_pkg_cpe_list**
> PkgCpeGetPkgCpeListResponseBody pkg_cpe_get_pkg_cpe_list()

getPkgCpeList pkgCpe

pkgCpe list

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import pkg_cpe_api
from openapi_client.model.pkg_cpe_get_pkg_cpe_list_response_body import PkgCpeGetPkgCpeListResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://rest.vuls.biz"
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
    api_instance = pkg_cpe_api.PkgCpeApi(api_client)
    page = 1 # int | Page Number (optional) if omitted the server will use the default value of 1
    limit = 20 # int | Limit (optional) if omitted the server will use the default value of 20
    offset = 0 # int | Offset (optional) if omitted the server will use the default value of 0
    filter_cve_id = "filterCveID_example" # str | CveID filter (optional)
    filter_task_id = 1 # int | TaskID filter (optional)
    filter_server_id = 1 # int | ServerID filter (optional)
    filter_role_id = 1 # int | ServerRoleID filter (optional)
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getPkgCpeList pkgCpe
        api_response = api_instance.pkg_cpe_get_pkg_cpe_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_task_id=filter_task_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_pkg_cpe_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Limit | [optional] if omitted the server will use the default value of 20
 **offset** | **int**| Offset | [optional] if omitted the server will use the default value of 0
 **filter_cve_id** | **str**| CveID filter | [optional]
 **filter_task_id** | **int**| TaskID filter | [optional]
 **filter_server_id** | **int**| ServerID filter | [optional]
 **filter_role_id** | **int**| ServerRoleID filter | [optional]
 **authorization** | **str**| api key auth | [optional]

### Return type

[**PkgCpeGetPkgCpeListResponseBody**](PkgCpeGetPkgCpeListResponseBody.md)

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

# **pkg_cpe_get_pkg_detail**
> PkgCpeGetPkgDetailResponseBody pkg_cpe_get_pkg_detail(pkg_id)

getPkgDetail pkgCpe

pkg detail

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import pkg_cpe_api
from openapi_client.model.pkg_cpe_get_pkg_detail_response_body import PkgCpeGetPkgDetailResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://rest.vuls.biz"
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
    api_instance = pkg_cpe_api.PkgCpeApi(api_client)
    pkg_id = 1 # int | PackageID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getPkgDetail pkgCpe
        api_response = api_instance.pkg_cpe_get_pkg_detail(pkg_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_pkg_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getPkgDetail pkgCpe
        api_response = api_instance.pkg_cpe_get_pkg_detail(pkg_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_pkg_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkg_id** | **int**| PackageID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**PkgCpeGetPkgDetailResponseBody**](PkgCpeGetPkgDetailResponseBody.md)

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

