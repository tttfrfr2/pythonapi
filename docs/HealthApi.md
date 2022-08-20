# openapi_client.HealthApi

All URIs are relative to *http://https://rest.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_health**](HealthApi.md#health_health) | **GET** /health | health health


# **health_health**
> bool health_health()

health health

health

### Example


```python
import time
import openapi_client
from openapi_client.api import health_api
from pprint import pprint
# Defining the host is optional and defaults to http://https://rest.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://rest.vuls.biz"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # health health
        api_response = api_instance.health_health()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HealthApi->health_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/gob


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

