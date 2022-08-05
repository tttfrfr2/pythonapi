# TaskListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time of task | 
**cve_id** | **str** | CVE ID of task | 
**id** | **int** | ID of task | 
**ignore** | **bool** | Ignore of task | 
**os_family** | **str** | OS Name of server | 
**os_version** | **str** | OS Version of server | 
**priority** | **str** | Priority of task | 
**role_id** | **int** | ServerRoleID of task | 
**role_name** | **str** | ServerRoleName of task | 
**server_id** | **int** | ServerID of task | 
**server_name** | **str** | ServerName of task | 
**server_uuid** | **str** | ServerUUID of task | 
**status** | **str** | Status of task | 
**updated_at** | **datetime** | updated time of task | 
**advisory_ids** | **[str]** | advisoryIDs of cve | [optional] 
**applying_patch_on** | **date** | ApplyingPatchOn of task | [optional] 
**detection_tools** | [**[DetectionToolResponseBody]**](DetectionToolResponseBody.md) | DetectionTools of task | [optional] 
**has_exploit** | **bool** | hasExploit of cve | [optional] 
**has_mitigation** | **bool** | hasMitigation of cve | [optional] 
**has_workaround** | **bool** | hasWorkaroundof cve | [optional] 
**ignore_until** | **str** | Ignore until of task | [optional] 
**main_user_id** | **int** | MainUserID of task | [optional] 
**main_user_name** | **str** | MainUserName of task | [optional] 
**pkg_cpe_names** | **[str]** | Package And CPE Names of task | [optional] 
**pkg_not_fixed_yet** | **bool** | Flag of Not Fixed Yet of task | [optional] 
**server_tags** | **[str]** | ServerTags of task | [optional] 
**sub_user_id** | **int** | SubUserID of task | [optional] 
**sub_user_name** | **str** | SubUserName of task | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


