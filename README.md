# aspose-digaram-cloud-python

Aspose.Digaram Cloud SDK for Python allows you to use Aspose.Digaram APIs in your Python applications

- Package version: 18.10
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.5

## Installation & Usage
### pip install

```sh
pip install asposeDiagramcloud
```
(you may need to run `pip` with root permission: `sudo pip install asposeDiagramcloud`)

Then import the package:
```python
import asposeDiagramcloud 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asposeDiagramcloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.aspose.cloud/v1.1/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DiagramFileApi* | [**diagram_file_get_diagram**](docs/DiagramFileApi.md#diagram_file_get_diagram) | **GET** /diagram/{name} | Read document info or export.
*DiagramFileApi* | [**diagram_file_post_save_as**](docs/DiagramFileApi.md#diagram_file_post_save_as) | **POST** /diagram/{name}/SaveAs | Convert document and save result to storage.
*DiagramFileApi* | [**diagram_file_put_create**](docs/DiagramFileApi.md#diagram_file_put_create) | **PUT** /diagram/{name} | Create new diagram and save result to storage.
*DiagramFileApi* | [**diagram_file_put_upload**](docs/DiagramFileApi.md#diagram_file_put_upload) | **PUT** /diagram/{name}/upload | Upload file and save result to storage.
*OAuthApi* | [**o_auth_post**](docs/OAuthApi.md#o_auth_post) | **POST** /oauth2/token | Get Access token


## Documentation For Models

 - [AccessTokenResponse](docs/AccessTokenResponse.md)
 - [DiagramModel](docs/DiagramModel.md)
 - [FileFormatRequest](docs/FileFormatRequest.md)
 - [Link](docs/Link.md)
 - [PageModel](docs/PageModel.md)
 - [SaaSposeResponse](docs/SaaSposeResponse.md)
 - [SaveResult](docs/SaveResult.md)
 - [SharpModel](docs/SharpModel.md)
 - [DiagramResponse](docs/DiagramResponse.md)
 - [SaveResponse](docs/SaveResponse.md)


## Documentation For Authorization


## appsid

- **Type**: API key
- **API key parameter name**: appsid
- **Location**: URL query string

## oauth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: 
 - **write:pets**: modify pets in your account

## signature

- **Type**: API key
- **API key parameter name**: signature
- **Location**: URL query string




