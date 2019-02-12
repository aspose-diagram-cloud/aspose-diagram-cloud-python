# For complete examples and data files, please go to https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-python/

import os
import asposediagramcloud
from asposediagramcloud.apis.diagram_file_api import DiagramFileApi
from asposediagramcloud.models import FileFormatRequest
import examples_base

api_client = examples_base.GetApiClient()
diagramAPI = asposediagramcloud.apis.diagram_file_api.DiagramFileApi(api_client)

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
dataFolder = os.path.join(ABSPATH, "testData")

filename ='file_get_1.vdx'

# Upload file to Cloud Storage
filePath = os.path.join(dataFolder, filename)
examples_base.Upload(filePath, filename, folder=None, storage=None)

# Convert file to PDF format
folder = ""
is_overwrite = "true"
format =FileFormatRequest(format="pdf")
newfilename = "file_saveas_python.pdf"
result = diagramAPI.diagram_file_post_save_as(filename, folder=folder, newfilename=newfilename, format=format, is_overwrite=is_overwrite)
print(result);