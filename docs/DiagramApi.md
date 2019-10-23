# asposediagramcloud.DiagramApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_document**](DiagramApi.md#convert_document) | **PUT** /diagram/{name}/convert | Converts document from the request&#39;s content to the specified format.
[**create_new**](DiagramApi.md#create_new) | **PUT** /diagram/{name} | Create Empty file into the specified format.
[**download_file_with_format**](DiagramApi.md#download_file_with_format) | **GET** /diagram/{name} | Exports the document into the specified format.
[**save_as**](DiagramApi.md#save_as) | **POST** /diagram/{name}/saveAs | Converts document to destination format with detailed settings and saves result to storage.


# **convert_document**
> file convert_document(name, file, source_filename=source_filename)

Converts document from the request's content to the specified format.

### Example 
```python
from __future__ import print_function
import time
import asposediagramcloud
from asposediagramcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
asposediagramcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposediagramcloud.DiagramApi()
name = 'name_example' # str | Download document name.
file = '/path/to/file.txt' # file | File to upload
source_filename = 'source_filename_example' # str | Source document name. (optional)

try: 
    # Converts document from the request's content to the specified format.
    api_response = api_instance.convert_document(name, file, source_filename=source_filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramApi->convert_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Download document name. | 
 **file** | **file**| File to upload | 
 **source_filename** | **str**| Source document name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new**
> CreateNewResponse create_new(name, folder=folder, is_overwrite=is_overwrite)

Create Empty file into the specified format.

### Example 
```python
from __future__ import print_function
import time
import asposediagramcloud
from asposediagramcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
asposediagramcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposediagramcloud.DiagramApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
is_overwrite = false # bool | If true overwrite the same name file.The default value is false  (optional) (default to false)

try: 
    # Create Empty file into the specified format.
    api_response = api_instance.create_new(name, folder=folder, is_overwrite=is_overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramApi->create_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **is_overwrite** | **bool**| If true overwrite the same name file.The default value is false  | [optional] [default to false]

### Return type

[**CreateNewResponse**](CreateNewResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_with_format**
> file download_file_with_format(name, format, folder=folder)

Exports the document into the specified format.

### Example 
```python
from __future__ import print_function
import time
import asposediagramcloud
from asposediagramcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
asposediagramcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposediagramcloud.DiagramApi()
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
folder = 'folder_example' # str | Original document folder. (optional)

try: 
    # Exports the document into the specified format.
    api_response = api_instance.download_file_with_format(name, format, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramApi->download_file_with_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **folder** | **str**| Original document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as**
> SaveAsResponse save_as(name, save_options_request, folder=folder, is_overwrite=is_overwrite)

Converts document to destination format with detailed settings and saves result to storage.

### Example 
```python
from __future__ import print_function
import time
import asposediagramcloud
from asposediagramcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
asposediagramcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposediagramcloud.DiagramApi()
name = 'name_example' # str | Original document name.
save_options_request = asposediagramcloud.SaveOptionsRequest() # SaveOptionsRequest | Save options.
folder = 'folder_example' # str | Original document folder. (optional)
is_overwrite = false # bool | If true overwrite the same name file.The default value is false  (optional) (default to false)

try: 
    # Converts document to destination format with detailed settings and saves result to storage.
    api_response = api_instance.save_as(name, save_options_request, folder=folder, is_overwrite=is_overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramApi->save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original document name. | 
 **save_options_request** | [**SaveOptionsRequest**](SaveOptionsRequest.md)| Save options. | 
 **folder** | **str**| Original document folder. | [optional] 
 **is_overwrite** | **bool**| If true overwrite the same name file.The default value is false  | [optional] [default to false]

### Return type

[**SaveAsResponse**](SaveAsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

