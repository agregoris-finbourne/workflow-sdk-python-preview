# CreateTaskRequest

Contains required info to create a new Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**correlation_ids** | **list[str]** | A set of guid identifiers that allow correlation across the application tier | [optional] 
**fields** | [**list[TaskInstanceField]**](TaskInstanceField.md) | Fields and their initial values - should correspond with the Task Definition field schema | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


