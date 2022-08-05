# CveGetCveDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time | 
**cve_id** | **str** | Cve ID string of cve | 
**cvss** | **file_type** | cvss of cve | 
**cwes** | [**[CweResponseBody]**](CweResponseBody.md) | cwes of cve | 
**env_metric_v2s** | [**[EnvMetricV2ResponseBody]**](EnvMetricV2ResponseBody.md) | envMetricV2 of cve | 
**env_metric_v3s** | [**[EnvMetricV3ResponseBody]**](EnvMetricV3ResponseBody.md) | envMetricV3 of cve | 
**references** | **{str: (str,)}** | references of cve | 
**sec_metrics** | [**[SecMetricResponseBody]**](SecMetricResponseBody.md) | secMetric of cve | 
**server_os_families** | **[str]** | serverOsFamilies of cve | 
**tmp_metric_v2** | [**TmpMetricResponseBody**](TmpMetricResponseBody.md) |  | 
**tmp_metric_v3** | [**TmpMetricResponseBody**](TmpMetricResponseBody.md) |  | 
**updated_at** | **datetime** | updated time | 
**advisories** | [**[AdvisoryResponseBody]**](AdvisoryResponseBody.md) | advisory of cve | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


