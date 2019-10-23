# coding: utf-8

"""
    Aspose.Diagram Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SaveOptionsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_name': 'str',
        'folder': 'str',
        'save_options': 'SaveOptionsModel'
    }

    attribute_map = {
        'file_name': 'FileName',
        'folder': 'Folder',
        'save_options': 'SaveOptions'
    }
    
    @staticmethod
    def get_swagger_types():
        return SaveOptionsRequest.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return SaveOptionsRequest.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, file_name=None, folder=None, save_options=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        SaveOptionsRequest - a model defined in Swagger
        """

        self.container['file_name'] = None
        self.container['folder'] = None
        self.container['save_options'] = None

        if file_name is not None:
          self.file_name = file_name
        if folder is not None:
          self.folder = folder
        if save_options is not None:
          self.save_options = save_options

    @property
    def file_name(self):
        """
        Gets the file_name of this SaveOptionsRequest.

        :return: The file_name of this SaveOptionsRequest.
        :rtype: str
        """
        return self.container['file_name']

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this SaveOptionsRequest.

        :param file_name: The file_name of this SaveOptionsRequest.
        :type: str
        """

        self.container['file_name'] = file_name

    @property
    def folder(self):
        """
        Gets the folder of this SaveOptionsRequest.

        :return: The folder of this SaveOptionsRequest.
        :rtype: str
        """
        return self.container['folder']

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder of this SaveOptionsRequest.

        :param folder: The folder of this SaveOptionsRequest.
        :type: str
        """

        self.container['folder'] = folder

    @property
    def save_options(self):
        """
        Gets the save_options of this SaveOptionsRequest.

        :return: The save_options of this SaveOptionsRequest.
        :rtype: SaveOptionsModel
        """
        return self.container['save_options']

    @save_options.setter
    def save_options(self, save_options):
        """
        Sets the save_options of this SaveOptionsRequest.

        :param save_options: The save_options of this SaveOptionsRequest.
        :type: SaveOptionsModel
        """

        self.container['save_options'] = save_options

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SaveOptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other