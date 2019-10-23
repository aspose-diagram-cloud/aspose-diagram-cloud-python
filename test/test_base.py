# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)


from asposediagramcloud.rest import ApiException
from asposediagramcloud.apis.diagram_api import DiagramApi
from asposediagramcloud.apis.storage_api import StorageApi
from asposediagramcloud.api_client import ApiClient

grantType = "client_credentials"
clientId = "yourClientId"
clientSecret = "yourClientSecret"
diagramApi=None
storageApi=None

def GetDiagramApi():
    global diagramApi
    if diagramApi is None:
        diagramApi=DiagramApi(grantType,clientId,clientSecret)

    return diagramApi

def GetStorageApi():
    global storageApi
    if storageApi is None:
        storageApi=StorageApi(grantType,clientId,clientSecret)

    return storageApi

