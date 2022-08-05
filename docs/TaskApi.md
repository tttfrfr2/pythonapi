# openapi_client.TaskApi

All URIs are relative to *http://rest.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_add_task_comment**](TaskApi.md#task_add_task_comment) | **POST** /v1/task/{taskID}/comment | addTaskComment task
[**task_get_task_detail**](TaskApi.md#task_get_task_detail) | **GET** /v1/task/{taskID} | getTaskDetail task
[**task_get_task_list**](TaskApi.md#task_get_task_list) | **GET** /v1/tasks | getTaskList task
[**task_update_task**](TaskApi.md#task_update_task) | **PUT** /v1/task/{taskID} | updateTask task
[**task_update_task_ignore**](TaskApi.md#task_update_task_ignore) | **PUT** /v1/task/{taskID}/ignore | updateTaskIgnore task


# **task_add_task_comment**
> TaskAddTaskCommentResponseBody task_add_task_comment(task_id, add_task_comment_request_body)

addTaskComment task

add task comment

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import task_api
from openapi_client.model.task_add_task_comment_request_body import TaskAddTaskCommentRequestBody
from openapi_client.model.task_add_task_comment_response_body import TaskAddTaskCommentResponseBody
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
    api_instance = task_api.TaskApi(api_client)
    task_id = 1 # int | Task ID
    add_task_comment_request_body = TaskAddTaskCommentRequestBody(
        comment_content="comment",
    ) # TaskAddTaskCommentRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # addTaskComment task
        api_response = api_instance.task_add_task_comment(task_id, add_task_comment_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_add_task_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # addTaskComment task
        api_response = api_instance.task_add_task_comment(task_id, add_task_comment_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_add_task_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID |
 **add_task_comment_request_body** | [**TaskAddTaskCommentRequestBody**](TaskAddTaskCommentRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**TaskAddTaskCommentResponseBody**](TaskAddTaskCommentResponseBody.md)

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

# **task_get_task_detail**
> TaskGetTaskDetailResponseBody task_get_task_detail(task_id)

getTaskDetail task

task detail

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import task_api
from openapi_client.model.task_get_task_detail_response_body import TaskGetTaskDetailResponseBody
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
    api_instance = task_api.TaskApi(api_client)
    task_id = 1 # int | Task ID
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # getTaskDetail task
        api_response = api_instance.task_get_task_detail(task_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_get_task_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getTaskDetail task
        api_response = api_instance.task_get_task_detail(task_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_get_task_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**TaskGetTaskDetailResponseBody**](TaskGetTaskDetailResponseBody.md)

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

# **task_get_task_list**
> TaskGetTaskListResponseBody task_get_task_list()

getTaskList task

task list

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import task_api
from openapi_client.model.task_get_task_list_response_body import TaskGetTaskListResponseBody
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
    api_instance = task_api.TaskApi(api_client)
    page = 1 # int | Page Number (optional) if omitted the server will use the default value of 1
    limit = 20 # int | Limit (optional) if omitted the server will use the default value of 20
    offset = 0 # int | Offset (optional) if omitted the server will use the default value of 0
    filter_status = [
        "["new","investigating","ongoing"]",
    ] # [str] | Status filter (optional) if omitted the server will use the default value of ["new","investigating","ongoing"]
    filter_priority = [
        "none",
    ] # [str] | Priority filter (optional)
    filter_ignore = True # bool | Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得) (optional)
    filter_main_user_ids = [
        1,
    ] # [int] | MainUserIDs filter (optional)
    filter_sub_user_ids = [
        1,
    ] # [int] | SubUserIDs filter (optional)
    filter_cve_id = "filterCveID_example" # str | CveID filter (optional)
    filter_server_id = 1 # int | ServerID filter (optional)
    filter_role_id = 1 # int | ServerRoleID filter (optional)
    filter_pkg_id = 1 # int | PackageID filter (optional)
    filter_cpe_id = 1 # int | CpeID filter (optional)
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getTaskList task
        api_response = api_instance.task_get_task_list(page=page, limit=limit, offset=offset, filter_status=filter_status, filter_priority=filter_priority, filter_ignore=filter_ignore, filter_main_user_ids=filter_main_user_ids, filter_sub_user_ids=filter_sub_user_ids, filter_cve_id=filter_cve_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_get_task_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Limit | [optional] if omitted the server will use the default value of 20
 **offset** | **int**| Offset | [optional] if omitted the server will use the default value of 0
 **filter_status** | **[str]**| Status filter | [optional] if omitted the server will use the default value of ["new","investigating","ongoing"]
 **filter_priority** | **[str]**| Priority filter | [optional]
 **filter_ignore** | **bool**| Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得) | [optional]
 **filter_main_user_ids** | **[int]**| MainUserIDs filter | [optional]
 **filter_sub_user_ids** | **[int]**| SubUserIDs filter | [optional]
 **filter_cve_id** | **str**| CveID filter | [optional]
 **filter_server_id** | **int**| ServerID filter | [optional]
 **filter_role_id** | **int**| ServerRoleID filter | [optional]
 **filter_pkg_id** | **int**| PackageID filter | [optional]
 **filter_cpe_id** | **int**| CpeID filter | [optional]
 **authorization** | **str**| api key auth | [optional]

### Return type

[**TaskGetTaskListResponseBody**](TaskGetTaskListResponseBody.md)

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

# **task_update_task**
> TaskUpdateTaskResponseBody task_update_task(task_id, update_task_request_body)

updateTask task

update task

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import task_api
from openapi_client.model.task_update_task_response_body import TaskUpdateTaskResponseBody
from openapi_client.model.task_update_task_request_body import TaskUpdateTaskRequestBody
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
    api_instance = task_api.TaskApi(api_client)
    task_id = 1 # int | Task ID
    update_task_request_body = TaskUpdateTaskRequestBody(
        applying_patch_on=dateutil_parser('Sat Jul 14 00:00:00 UTC 2018').date(),
        main_user_id=1,
        priority="medium",
        status="ongoing",
        sub_user_id=2,
    ) # TaskUpdateTaskRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateTask task
        api_response = api_instance.task_update_task(task_id, update_task_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_update_task: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateTask task
        api_response = api_instance.task_update_task(task_id, update_task_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_update_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID |
 **update_task_request_body** | [**TaskUpdateTaskRequestBody**](TaskUpdateTaskRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**TaskUpdateTaskResponseBody**](TaskUpdateTaskResponseBody.md)

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

# **task_update_task_ignore**
> TaskUpdateTaskIgnoreResponseBody task_update_task_ignore(task_id, update_task_ignore_request_body)

updateTaskIgnore task

update task ignore

### Example

* Api Key Authentication (api_key_header_Authorization):

```python
import time
import openapi_client
from openapi_client.api import task_api
from openapi_client.model.task_update_task_ignore_request_body import TaskUpdateTaskIgnoreRequestBody
from openapi_client.model.task_update_task_ignore_response_body import TaskUpdateTaskIgnoreResponseBody
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
    api_instance = task_api.TaskApi(api_client)
    task_id = 1 # int | Task ID
    update_task_ignore_request_body = TaskUpdateTaskIgnoreRequestBody(
        ignore_until="forever",
    ) # TaskUpdateTaskIgnoreRequestBody | 
    authorization = "Authorization_example" # str | api key auth (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateTaskIgnore task
        api_response = api_instance.task_update_task_ignore(task_id, update_task_ignore_request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_update_task_ignore: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateTaskIgnore task
        api_response = api_instance.task_update_task_ignore(task_id, update_task_ignore_request_body, authorization=authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TaskApi->task_update_task_ignore: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID |
 **update_task_ignore_request_body** | [**TaskUpdateTaskIgnoreRequestBody**](TaskUpdateTaskIgnoreRequestBody.md)|  |
 **authorization** | **str**| api key auth | [optional]

### Return type

[**TaskUpdateTaskIgnoreResponseBody**](TaskUpdateTaskIgnoreResponseBody.md)

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

