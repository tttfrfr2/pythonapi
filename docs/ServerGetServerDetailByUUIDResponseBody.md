# ServerGetServerDetailByUUIDResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | crated time of server | 
**host_uuid** | **str** | UUID of server | 
**id** | **int** | ID of server | 
**need_kernel_restart** | **bool** | Whether server needs kernel restart | 
**os_family** | **str** | OS Name of server | 
**os_version** | **str** | OS Version of server | 
**platform_instance_id** | **str** | platformInstanceId of server | 
**platform_name** | **str** | platformName of server | 
**server_ipv4** | **str** | IPv4 of server | 
**server_name** | **str** | Name of server | 
**server_uuid** | **str** | UUID of server | 
**serverrole_id** | **int** | ID of server role | 
**serverrole_name** | **str** | Name of server role | 
**updated_at** | **str** | updated time of server | 
**default_user_id** | **int** | default user ID of server | [optional] 
**default_user_name** | **str** | default user name of server | [optional] 
**last_scanned_at** | **str** | last scanned time of server | [optional] 
**last_uploaded_at** | **str** | last uploaded time of server | [optional] 
**tags** | [**[ServerTagResponseBody]**](ServerTagResponseBody.md) | tags is list of server tag | [optional] 
**tasks** | [**[ChildTaskResponseBody]**](ChildTaskResponseBody.md) | tasks of server | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


