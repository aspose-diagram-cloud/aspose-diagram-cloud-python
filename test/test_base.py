# coding: utf-8

import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

import asposediagramcloud
from asposediagramcloud.rest import ApiException
from asposediagramcloud.apis.o_auth_api import OAuthApi
from asposediagramcloud.api_client import ApiClient
from asposediagramcloud.configuration import Configuration
import asposestoragecloud

grantType = "client_credentials"
clientId = "xxxxxxxx"
clientSecret = "xxxxxx"

def GetAccessToken():
    client = ApiClient('https://api.aspose.cloud/')
    api = asposediagramcloud.apis.o_auth_api.OAuthApi(client)
    data = api.o_auth_post(grantType, clientId, clientSecret)
    return data.access_token

api_client = None

def GetApiClient():
    global api_client
    if api_client == None:
        configuration=Configuration()
        configuration.api_key['app_sid'] = '84220e69-32e2-41c4-ba2f-662a0a01433e' # Put your appSid here
        configuration.api_key['api_key'] = '883dc8d6b8ecd879dae35cb363e9eb56' # Put your appkey here
        api_client = ApiClient('https://api.aspose.cloud/v1.1',configuration)
       
        #api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
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
