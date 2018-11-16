# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposeDiagramcloud
from asposeDiagramcloud.rest import ApiException
from asposeDiagramcloud.apis.o_auth_api import OAuthApi
from asposeDiagramcloud.api_client import ApiClient
import asposestoragecloud

grantType = "client_credentials"
clientId = "84220e69-32e2-41c4-ba2f-662a0a01433e"
clientSecret = "883dc8d6b8ecd879dae35cb363e9eb56"

def GetAccessToken():
    client = ApiClient('https://api.aspose.cloud/')
    api = asposeDiagramcloud.apis.o_auth_api.OAuthApi(client)
    data = api.o_auth_post(grantType, clientId, clientSecret)
    return data.access_token

api_client = None

def GetApiClient():
    global api_client
    if api_client == None:
        api_client = ApiClient('https://api.aspose.cloud/v1.1')
        api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
    return api_client


def Upload(local_file_path,filename, folder, storage=None):
    storage_apiClient = asposestoragecloud.ApiClient(clientSecret, clientId)
    storageApi = asposestoragecloud.StorageApi(storage_apiClient)
  
    path = folder + '/' + filename
    
    with open(local_file_path, 'rb') as file_object:
        contents = file_object.read()
        response = None
        if storage == None:
            response = storageApi.put_create(path, contents)
        else:    
            response = storageApi.put_create(path, contents, storage=storage)
        if response['Status'] == "OK":
            return True

    return False
