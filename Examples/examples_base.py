import os
import sys

import asposediagramcloud
from asposediagramcloud.apis.o_auth_api import OAuthApi
from asposediagramcloud.api_client import ApiClient
import asposestoragecloud

grantType = "client_credentials"
clientId = "" # Get App Key and App SID from https://dashboard.aspose.cloud/
clientSecret = "" # Get App Key and App SID from https://dashboard.aspose.cloud/

def GetAccessToken():
	client = ApiClient('https://api.aspose.cloud/')
	api = asposediagramcloud.apis.o_auth_api.OAuthApi(client)
	data = api.o_auth_post(grantType, clientId, clientSecret)
	return data.access_token

api_client = None

def GetApiClient():
	global api_client
	if api_client == None:
		api_client = ApiClient('https://api.aspose.cloud/v1.1')
		api_client.set_default_header("Authorization", "Bearer " + GetAccessToken())
	return api_client

def Upload(local_file_path, filename, folder, storage=None):
	storage_apiClient = asposestoragecloud.ApiClient(clientSecret, clientId)
	storageApi = asposestoragecloud.StorageApi(storage_apiClient)
	
	if  folder != None: 
		path = folder + '/' + filename
	else:
		path = filename

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
