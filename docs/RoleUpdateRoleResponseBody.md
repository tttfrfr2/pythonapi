# RoleUpdateRoleResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time of server role | 
**id** | **int** | ID of server role | 
**name** | **str** | Name of server role | 
**updated_at** | **datetime** | updated time of server role | 
**all_task_count** | **int** | AllTaskCount of server role | [optional] 
**env_metric_v2s** | [**[EnvMetricV2ResponseBody]**](EnvMetricV2ResponseBody.md) | envMetricV2s of server role | [optional] 
**env_metric_v3s** | [**[EnvMetricV3ResponseBody]**](EnvMetricV3ResponseBody.md) | envMetricV3s of server role | [optional] 
**is_default** | **bool** | isDefault of server role | [optional] 
**new_task_count** | **int** | NewTaskCount of server role | [optional] 
**sec_metric** | [**SecMetricResponseBody**](SecMetricResponseBody.md) |  | [optional] 
**servers** | [**[ServerChildResponseBody]**](ServerChildResponseBody.md) | Servers of server role | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


