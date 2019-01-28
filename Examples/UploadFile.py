# For complete examples and data files, please go to https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-python/

import os
import asposediagramcloud
from asposediagramcloud.apis.diagram_file_api import DiagramFileApi
from asposediagramcloud.models import FileFormatRequest
import examples_base

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
dataFolder = os.path.join(ABSPATH, "testData")

# Upload file to Cloud Storage
filename ='file_get_1.vdx'
filePath = os.path.join(dataFolder, filename)
result = examples_base.Upload(filePath, filename, folder=None, storage=None)
print(result);