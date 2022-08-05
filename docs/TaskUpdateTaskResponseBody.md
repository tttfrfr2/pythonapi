# TaskUpdateTaskResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time of task | 
**cve_id** | **str** | CVE ID of task | 
**id** | **int** | ID of task | 
**ignore** | **bool** | Ignore of task | 
**priority** | **str** | Priority of task | 
**role_id** | **int** | ServerRoleID of task | 
**role_name** | **str** | ServerRoleName of task | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | 
**server_id** | **int** | ServerID of task | 
**status** | **str** | Status of task | 
**updated_at** | **datetime** | updated time of task | 
**advisory_ids** | **[str]** | advisoryIDs of cve | [optional] 
**applying_patch_on** | **date** | ApplyingPatchOn of task | [optional] 
**comments** | [**[TaskCommentResponseBody]**](TaskCommentResponseBody.md) | Comment of task | [optional] 
**cvss** | **{str: (file_type,)}** | Key Value of CveID and Cvss of task | [optional] 
**detection_methods** | [**[DetectionMethodResponseBody]**](DetectionMethodResponseBody.md) | DetectionMethod of task | [optional] 
**detection_tools** | [**[DetectionToolResponseBody]**](DetectionToolResponseBody.md) | DetectionTools of task | [optional] 
**ignore_until** | **str** | Ignore until of task | [optional] 
**main_user_id** | **int** | MainUserID of task | [optional] 
**main_user_name** | **str** | MainUserName of task | [optional] 
**package_statuses** | **{str: (str,)}** | packageStatus of task | [optional] 
**pkg_cpes** | [**[PkgCpeChildResponseBody]**](PkgCpeChildResponseBody.md) | Pcakge And Cpe list of task | [optional] 
**sub_user_id** | **int** | SubUserID of task | [optional] 
**sub_user_name** | **str** | SubUserName of task | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


