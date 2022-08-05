# CveListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_task_count** | **int** | AllTaskCount of cve | 
**created_at** | **datetime** | created time | 
**cve_id** | **str** | Cve ID string of cve | 
**cwes** | [**[CweResponseBody]**](CweResponseBody.md) | cwes of cve | 
**is_not_active** | **bool** | Flag of active cve | 
**is_owasp_top_ten2017** | **bool** | isOwaspTopTen2017 of cve | 
**max_v2** | **float** | maxV2 of cve | 
**max_v3** | **float** | maxV3 of cve | 
**new_task_count** | **int** | NewTaskCount of cve | 
**score_v2s** | **{str: (float,)}** | cvss v2 scores of cve | 
**score_v3s** | **{str: (float,)}** | cvss v3 scores of cve | 
**title** | **str** | Title of cve | 
**topic_count** | **int** | topicCount of cve | 
**topic_last_updated_at** | **datetime** | topicLastUpdatedAt of cve | 
**updated_at** | **datetime** | updated time | 
**vector_v2s** | **{str: (str,)}** | cvss v2 vectors of cve | 
**vector_v3s** | **{str: (str,)}** | cvss v3 vectors of cve | 
**advisory_ids** | **[str]** | advisoryIDs of cve | [optional] 
**has_exploit** | **bool** | hasExploit of cve | [optional] 
**has_mitigation** | **bool** | hasMitigation of cve | [optional] 
**has_workaround** | **bool** | hasWorkaroundof cve | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


