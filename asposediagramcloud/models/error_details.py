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


class ErrorDetails(object):
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
        'request_id': 'str',
        'date': 'datetime'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'date': 'Date'
    }
    
    @staticmethod
    def get_swagger_types():
        return ErrorDetails.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ErrorDetails.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, request_id=None, date=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ErrorDetails - a model defined in Swagger
        """

        self.container['request_id'] = None
        self.container['date'] = None

        if request_id is not None:
          self.request_id = request_id
        self.date = date

    @property
    def request_id(self):
        """
        Gets the request_id of this ErrorDetails.
        The request id

        :return: The request_id of this ErrorDetails.
        :rtype: str
        """
        return self.container['request_id']

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this ErrorDetails.
        The request id

        :param request_id: The request_id of this ErrorDetails.
        :type: str
        """

        self.container['request_id'] = request_id

    @property
    def date(self):
        """
        Gets the date of this ErrorDetails.
        Date

        :return: The date of this ErrorDetails.
        :rtype: datetime
        """
        return self.container['date']

    @date.setter
    def date(self, date):
        """
        Sets the date of this ErrorDetails.
        Date

        :param date: The date of this ErrorDetails.
        :type: datetime
        """
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        """

        self.container['date'] = date

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
        if not isinstance(other, ErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
