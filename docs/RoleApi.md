# openapi_client.RoleApi

All URIs are relative to *http://https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_delete_role**](RoleApi.md#role_delete_role) | **DELETE** /v1/role/{roleID} | deleteRole role
[**role_get_role_detail**](RoleApi.md#role_get_role_detail) | **GET** /v1/role/{roleID} | getRoleDetail role
[**role_get_role_list**](RoleApi.md#role_get_role_list) | **GET** /v1/roles | getRoleList role
[**role_update_role**](RoleApi.md#role_update_role) | **PUT** /v1/role/{roleID} | updateRole role


# **role_delete_role**
> role_delete_role(role_id)

deleteRole role

role delete

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import role_api
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.2119e7c929.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.2119e7c929.vuls.biz"
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
    api_instance = role_api.RoleApi(api_client)
    role_id = 1 # int | Role ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # deleteRole role
        api_instance.role_delete_role(role_id)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_delete_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # deleteRole role
        api_instance.role_delete_role(role_id, authorization=authorization)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Role ID |
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

# **role_get_role_detail**
> RoleGetRoleDetailResponseBody role_get_role_detail(role_id)

getRoleDetail role

role detail

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import role_api
from openapi_client.model.role_get_role_detail_response_body import RoleGetRoleDetailResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.2119e7c929.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.2119e7c929.vuls.biz"
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
    api_instance = role_api.RoleApi(api_client)
    role_id = 1 # int | Role ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getRoleDetail role
        api_response = api_instance.role_get_role_detail(role_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_get_role_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getRoleDetail role
        api_response = api_instance.role_get_role_detail(role_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_get_role_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Role ID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**RoleGetRoleDetailResponseBody**](RoleGetRoleDetailResponseBody.md)

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

# **role_get_role_list**
> RoleGetRoleListResponseBody role_get_role_list()

getRoleList role

role list

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import role_api
from openapi_client.model.role_get_role_list_response_body import RoleGetRoleListResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.2119e7c929.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.2119e7c929.vuls.biz"
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
    api_instance = role_api.RoleApi(api_client)
    page = 1 # int | Page Number (default: 1) (optional) if omitted the server will use the default value of 1
    limit = 20 # int | Limit (default: 20, max: 100) (optional) if omitted the server will use the default value of 20
    offset = 0 # int | Offset (optional) if omitted the server will use the default value of 0
    filter_cve_id = "filterCveID_example" # str | CveID filter (optional)
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getRoleList role
        api_response = api_instance.role_get_role_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_get_role_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number (default: 1) | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Limit (default: 20, max: 100) | [optional] if omitted the server will use the default value of 20
 **offset** | **int**| Offset | [optional] if omitted the server will use the default value of 0
 **filter_cve_id** | **str**| CveID filter | [optional]
 **authorization** | **str**| api key auth | [optional]

### Return type

[**RoleGetRoleListResponseBody**](RoleGetRoleListResponseBody.md)

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

# **role_update_role**
> RoleUpdateRoleResponseBody role_update_role(role_id, update_role_request_body)

updateRole role

update role

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import role_api
from openapi_client.model.role_update_role_request_body import RoleUpdateRoleRequestBody
from openapi_client.model.role_update_role_response_body import RoleUpdateRoleResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.2119e7c929.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.2119e7c929.vuls.biz"
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
    api_instance = role_api.RoleApi(api_client)
    role_id = 1 # int | Role ID
    update_role_request_body = RoleUpdateRoleRequestBody(
        role_name="new-role-name",
    ) # RoleUpdateRoleRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateRole role
        api_response = api_instance.role_update_role(role_id, update_role_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_update_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateRole role
        api_response = api_instance.role_update_role(role_id, update_role_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleApi->role_update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Role ID |
 **update_role_request_body** | [**RoleUpdateRoleRequestBody**](RoleUpdateRoleRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**RoleUpdateRoleResponseBody**](RoleUpdateRoleResponseBody.md)

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

