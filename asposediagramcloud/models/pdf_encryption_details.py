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


class PdfEncryptionDetails(object):
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
        'permissions': 'str',
        'encryption_algorithm': 'str',
        'user_password': 'str',
        'owner_password': 'str'
    }

    attribute_map = {
        'permissions': 'Permissions',
        'encryption_algorithm': 'EncryptionAlgorithm',
        'user_password': 'UserPassword',
        'owner_password': 'OwnerPassword'
    }
    
    @staticmethod
    def get_swagger_types():
        return PdfEncryptionDetails.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PdfEncryptionDetails.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, permissions=None, encryption_algorithm=None, user_password=None, owner_password=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PdfEncryptionDetails - a model defined in Swagger
        """

        self.container['permissions'] = None
        self.container['encryption_algorithm'] = None
        self.container['user_password'] = None
        self.container['owner_password'] = None

        if permissions is not None:
          self.permissions = permissions
        if encryption_algorithm is not None:
          self.encryption_algorithm = encryption_algorithm
        if user_password is not None:
          self.user_password = user_password
        if owner_password is not None:
          self.owner_password = owner_password

    @property
    def permissions(self):
        """
        Gets the permissions of this PdfEncryptionDetails.

        :return: The permissions of this PdfEncryptionDetails.
        :rtype: str
        """
        return self.container['permissions']

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this PdfEncryptionDetails.

        :param permissions: The permissions of this PdfEncryptionDetails.
        :type: str
        """
        allowed_values = ["DisallowAll", "Printing", "ModifyContents", "ContentCopy", "ModifyAnnotations", "FillIn", "ContentCopyForAccessibility", "DocumentAssembly", "HighResolutionPrinting", "AllowAll"]
        if permissions not in allowed_values:
            raise ValueError(
                "Invalid value for `permissions` ({0}), must be one of {1}"
                .format(permissions, allowed_values)
            )

        self.container['permissions'] = permissions

    @property
    def encryption_algorithm(self):
        """
        Gets the encryption_algorithm of this PdfEncryptionDetails.

        :return: The encryption_algorithm of this PdfEncryptionDetails.
        :rtype: str
        """
        return self.container['encryption_algorithm']

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """
        Sets the encryption_algorithm of this PdfEncryptionDetails.

        :param encryption_algorithm: The encryption_algorithm of this PdfEncryptionDetails.
        :type: str
        """
        allowed_values = ["RC4_40", "RC4_128"]
        if encryption_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `encryption_algorithm` ({0}), must be one of {1}"
                .format(encryption_algorithm, allowed_values)
            )

        self.container['encryption_algorithm'] = encryption_algorithm

    @property
    def user_password(self):
        """
        Gets the user_password of this PdfEncryptionDetails.

        :return: The user_password of this PdfEncryptionDetails.
        :rtype: str
        """
        return self.container['user_password']

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this PdfEncryptionDetails.

        :param user_password: The user_password of this PdfEncryptionDetails.
        :type: str
        """

        self.container['user_password'] = user_password

    @property
    def owner_password(self):
        """
        Gets the owner_password of this PdfEncryptionDetails.

        :return: The owner_password of this PdfEncryptionDetails.
        :rtype: str
        """
        return self.container['owner_password']

    @owner_password.setter
    def owner_password(self, owner_password):
        """
        Sets the owner_password of this PdfEncryptionDetails.

        :param owner_password: The owner_password of this PdfEncryptionDetails.
        :type: str
        """

        self.container['owner_password'] = owner_password

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
        if not isinstance(other, PdfEncryptionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other