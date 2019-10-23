# asposediagramcloud.StorageApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_file**](StorageApi.md#copy_file) | **PUT** /diagram/storage/file/copy/{srcPath} | Copy file
[**copy_folder**](StorageApi.md#copy_folder) | **PUT** /diagram/storage/folder/copy/{srcPath} | Copy folder
[**create_folder**](StorageApi.md#create_folder) | **PUT** /diagram/storage/folder/{path} | Create the folder
[**delete_file**](StorageApi.md#delete_file) | **DELETE** /diagram/storage/file/{path} | Delete file
[**delete_folder**](StorageApi.md#delete_folder) | **DELETE** /diagram/storage/folder/{path} | Delete folder
[**download_file**](StorageApi.md#download_file) | **GET** /diagram/storage/file/{path} | Download file
[**get_disc_usage**](StorageApi.md#get_disc_usage) | **GET** /diagram/storage/disc | Get disc usage
[**get_file_versions**](StorageApi.md#get_file_versions) | **GET** /diagram/storage/version/{path} | Get file versions
[**get_files_list**](StorageApi.md#get_files_list) | **GET** /diagram/storage/folder/{path} | Get all files and folders within a folder
[**move_file**](StorageApi.md#move_file) | **PUT** /diagram/storage/file/move/{srcPath} | Move file
[**move_folder**](StorageApi.md#move_folder) | **PUT** /diagram/storage/folder/move/{srcPath} | Move folder
[**object_exists**](StorageApi.md#object_exists) | **GET** /diagram/storage/exist/{path} | Check if file or folder exists
[**storage_exists**](StorageApi.md#storage_exists) | **GET** /diagram/storage/{storageName}/exist | Check if storage exists
[**upload_file**](StorageApi.md#upload_file) | **PUT** /diagram/storage/file/{path} | Upload file


# **copy_file**
> copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

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
api_instance = asposediagramcloud.StorageApi()
src_path = 'src_path_example' # str | Source file path e.g. '/folder/file.ext'
dest_path = 'dest_path_example' # str | Destination file path
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to copy (optional)

try: 
    # Copy file
    api_instance.copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling StorageApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

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
api_instance = asposediagramcloud.StorageApi()
src_path = 'src_path_example' # str | Source folder path e.g. '/src'
dest_path = 'dest_path_example' # str | Destination folder path e.g. '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try: 
    # Copy folder
    api_instance.copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling StorageApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | Folder path to create e.g. 'folder_1/folder_2/'
storage_name = 'storage_name_example' # str | Storage name (optional)

try: 
    # Create the folder
    api_instance.create_folder(path, storage_name=storage_name)
except ApiException as e:
    print("Exception when calling StorageApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to delete (optional)

try: 
    # Delete file
    api_instance.delete_file(path, storage_name=storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling StorageApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
recursive = false # bool | Enable to delete folders, subfolders and files (optional) (default to false)

try: 
    # Delete folder
    api_instance.delete_folder(path, storage_name=storage_name, recursive=recursive)
except ApiException as e:
    print("Exception when calling StorageApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(path, storage_name=storage_name, version_id=version_id)

Download file

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to download (optional)

try: 
    # Download file
    api_response = api_instance.download_file(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disc_usage**
> DiscUsage get_disc_usage(storage_name=storage_name)

Get disc usage

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
api_instance = asposediagramcloud.StorageApi()
storage_name = 'storage_name_example' # str | Storage name (optional)

try: 
    # Get disc usage
    api_response = api_instance.get_disc_usage(storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_disc_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**DiscUsage**](DiscUsage.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_versions**
> FileVersions get_file_versions(path, storage_name=storage_name)

Get file versions

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | File path e.g. '/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)

try: 
    # Get file versions
    api_response = api_instance.get_file_versions(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_file_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FileVersions**](FileVersions.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)

try: 
    # Get all files and folders within a folder
    api_response = api_instance.get_files_list(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

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
api_instance = asposediagramcloud.StorageApi()
src_path = 'src_path_example' # str | Source file path e.g. '/src.ext'
dest_path = 'dest_path_example' # str | Destination file path e.g. '/dest.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to move (optional)

try: 
    # Move file
    api_instance.move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling StorageApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

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
api_instance = asposediagramcloud.StorageApi()
src_path = 'src_path_example' # str | Folder path to move e.g. '/folder'
dest_path = 'dest_path_example' # str | Destination folder path to move to e.g '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try: 
    # Move folder
    api_instance.move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling StorageApi->move_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_exists**
> ObjectExist object_exists(path, storage_name=storage_name, version_id=version_id)

Check if file or folder exists

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | File or folder path e.g. '/file.ext' or '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID (optional)

try: 
    # Check if file or folder exists
    api_response = api_instance.object_exists(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->object_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

### Return type

[**ObjectExist**](ObjectExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_exists**
> StorageExist storage_exists(storage_name)

Check if storage exists

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
api_instance = asposediagramcloud.StorageApi()
storage_name = 'storage_name_example' # str | Storage name

try: 
    # Check if storage exists
    api_response = api_instance.storage_exists(storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->storage_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

### Return type

[**StorageExist**](StorageExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(path, file, storage_name=storage_name)

Upload file

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
api_instance = asposediagramcloud.StorageApi()
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.             
file = '/path/to/file.txt' # file | File to upload
storage_name = 'storage_name_example' # str | Storage name (optional)

try: 
    # Upload file
    api_response = api_instance.upload_file(path, file, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

