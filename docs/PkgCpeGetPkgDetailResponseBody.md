# PkgCpeGetPkgDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | crated time of package or cpe | 
**name** | **str** | Name of package or cpe | 
**release** | **str** | Release of package | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of package or cpe | 
**affected_procs** | [**[AffectedProcResponseBody]**](AffectedProcResponseBody.md) | AffectedProcess list of package | [optional] 
**id** | **int** | ID of package | [optional] 
**need_restart_procs** | [**[NeedRestartProcResponseBody]**](NeedRestartProcResponseBody.md) | NeedRestartProcess list of package | [optional] 
**new_release** | **str** | New Release of package | [optional] 
**new_version** | **str** | New Version of package | [optional] 
**package_statuses** | **{str: (str,)}** | package status of package | [optional] 
**repository** | **str** | Repository of package | [optional] 
**tasks** | [**[ChildTaskResponseBody]**](ChildTaskResponseBody.md) | updated time of server | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


