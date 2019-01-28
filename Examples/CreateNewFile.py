# For complete examples and data files, please go to https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-python/

import os
import asposediagramcloud
from asposediagramcloud.apis.diagram_file_api import DiagramFileApi
from asposediagramcloud.models import FileFormatRequest
import examples_base

api_client = examples_base.GetApiClient()
diagramAPI = asposediagramcloud.apis.diagram_file_api.DiagramFileApi(api_client)

filename ='file_create_python.vdx'       
folder = ""
is_overwrite = "true"
result = diagramAPI.diagram_file_put_create(filename, folder=folder, is_overwrite=is_overwrite)
print(result);