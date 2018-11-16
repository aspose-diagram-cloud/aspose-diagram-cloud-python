# asposeDiagramcloud.DiagramFileApi

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagram_file_get_diagram**](DiagramFileApi.md#diagram_file_get_diagram) | **GET** /diagram/{name} | Read document info or export.
[**diagram_file_post_save_as**](DiagramFileApi.md#diagram_file_post_save_as) | **POST** /diagram/{name}/SaveAs | Convert document and save result to storage.
[**diagram_file_put_create**](DiagramFileApi.md#diagram_file_put_create) | **PUT** /diagram/{name} | Create new diagram and save result to storage.
[**diagram_file_put_upload**](DiagramFileApi.md#diagram_file_put_upload) | **PUT** /diagram/{name}/upload | Upload file and save result to storage.


# **diagram_file_get_diagram**
> file diagram_file_get_diagram(name, format=format, folder=folder, storage=storage)

Read document info or export.

### Example 
```python
from __future__ import print_function
import time
import asposeDiagramcloud
from asposeDiagramcloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposeDiagramcloud.DiagramFileApi()
name = 'name_example' # str | The document name.
format = 'format_example' # str | The exported file format. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Read document info or export.
    api_response = api_instance.diagram_file_get_diagram(name, format=format, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramFileApi->diagram_file_get_diagram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The exported file format. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagram_file_post_save_as**
> SaveResponse diagram_file_post_save_as(name, format=format, newfilename=newfilename, folder=folder, is_overwrite=is_overwrite, storage=storage)

Convert document and save result to storage.

### Example 
```python
from __future__ import print_function
import time
import asposeDiagramcloud
from asposeDiagramcloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposeDiagramcloud.DiagramFileApi()
name = 'name_example' # str | The document name.
format = asposeDiagramcloud.FileFormatRequest() # FileFormatRequest | Save format. (optional)
newfilename = 'newfilename_example' # str | The new file name. (optional)
folder = 'folder_example' # str | The document folder. (optional)
is_overwrite = false # bool | If true overwrite the same name file.The default value is false. (optional) (default to false)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Convert document and save result to storage.
    api_response = api_instance.diagram_file_post_save_as(name, format=format, newfilename=newfilename, folder=folder, is_overwrite=is_overwrite, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramFileApi->diagram_file_post_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | [**FileFormatRequest**](FileFormatRequest.md)| Save format. | [optional] 
 **newfilename** | **str**| The new file name. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **is_overwrite** | **bool**| If true overwrite the same name file.The default value is false. | [optional] [default to false]
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagram_file_put_create**
> SaaSposeResponse diagram_file_put_create(name, folder=folder, is_overwrite=is_overwrite, storage=storage)

Create new diagram and save result to storage.

### Example 
```python
from __future__ import print_function
import time
import asposeDiagramcloud
from asposeDiagramcloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposeDiagramcloud.DiagramFileApi()
name = 'name_example' # str | The new document name.
folder = 'folder_example' # str | The new document folder. (optional)
is_overwrite = false # bool | If true overwrite the same name file.The default value is false. (optional) (default to false)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Create new diagram and save result to storage.
    api_response = api_instance.diagram_file_put_create(name, folder=folder, is_overwrite=is_overwrite, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramFileApi->diagram_file_put_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new document name. | 
 **folder** | **str**| The new document folder. | [optional] 
 **is_overwrite** | **bool**| If true overwrite the same name file.The default value is false. | [optional] [default to false]
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagram_file_put_upload**
> SaaSposeResponse diagram_file_put_upload(name, folder=folder, is_overwrite=is_overwrite, storage=storage)

Upload file and save result to storage.

### Example 
```python
from __future__ import print_function
import time
import asposeDiagramcloud
from asposeDiagramcloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = asposeDiagramcloud.DiagramFileApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
is_overwrite = false # bool | If true overwrite the same name file.The default value is false. (optional) (default to false)
storage = 'storage_example' # str | storage name. (optional)

try: 
    # Upload file and save result to storage.
    api_response = api_instance.diagram_file_put_upload(name, folder=folder, is_overwrite=is_overwrite, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramFileApi->diagram_file_put_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **is_overwrite** | **bool**| If true overwrite the same name file.The default value is false. | [optional] [default to false]
 **storage** | **str**| storage name. | [optional] 

### Return type

[**SaaSposeResponse**](SaaSposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

