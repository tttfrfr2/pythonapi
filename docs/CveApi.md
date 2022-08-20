# openapi_client.CveApi

All URIs are relative to *http://https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cve_get_cve_detail**](CveApi.md#cve_get_cve_detail) | **GET** /v1/cve/{cveID} | getCveDetail cve
[**cve_get_cve_list**](CveApi.md#cve_get_cve_list) | **GET** /v1/cves | getCveList cve


# **cve_get_cve_detail**
> CveGetCveDetailResponseBody cve_get_cve_detail(cve_id)

getCveDetail cve

cve detail

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import cve_api
from openapi_client.model.cve_get_cve_detail_response_body import CveGetCveDetailResponseBody
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
    api_instance = cve_api.CveApi(api_client)
    cve_id = "cveID_example" # str | Cve ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getCveDetail cve
        api_response = api_instance.cve_get_cve_detail(cve_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CveApi->cve_get_cve_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getCveDetail cve
        api_response = api_instance.cve_get_cve_detail(cve_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CveApi->cve_get_cve_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**| Cve ID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**CveGetCveDetailResponseBody**](CveGetCveDetailResponseBody.md)

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

# **cve_get_cve_list**
> CveGetCveListResponseBody cve_get_cve_list()

getCveList cve

cve list

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import cve_api
from openapi_client.model.cve_get_cve_list_response_body import CveGetCveListResponseBody
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
    api_instance = cve_api.CveApi(api_client)
    page = 1 # int | Page Number (optional) if omitted the server will use the default value of 1
    limit = 20 # int | Limit (optional) if omitted the server will use the default value of 20
    offset = 0 # int | Offset (optional) if omitted the server will use the default value of 0
    filter_server_id = 1 # int | ServerID filter (optional)
    filter_role_id = 1 # int | ServerRoleID filter (optional)
    filter_pkg_id = 1 # int | PackageID filter (optional)
    filter_cpe_id = 1 # int | CpeID filter (optional)
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getCveList cve
        api_response = api_instance.cve_get_cve_list(page=page, limit=limit, offset=offset, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CveApi->cve_get_cve_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Limit | [optional] if omitted the server will use the default value of 20
 **offset** | **int**| Offset | [optional] if omitted the server will use the default value of 0
 **filter_server_id** | **int**| ServerID filter | [optional]
 **filter_role_id** | **int**| ServerRoleID filter | [optional]
 **filter_pkg_id** | **int**| PackageID filter | [optional]
 **filter_cpe_id** | **int**| CpeID filter | [optional]
 **authorization** | **str**| api key auth | [optional]

### Return type

[**CveGetCveListResponseBody**](CveGetCveListResponseBody.md)

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

