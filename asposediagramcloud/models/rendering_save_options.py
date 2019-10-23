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
from . import SaveOptionsModel

class RenderingSaveOptions(SaveOptionsModel):
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
        'area': 'RectangleF',
        'export_guide_shapes': 'bool',
        'page_size': 'PageSize',
        'is_export_comments': 'bool'
    }

    attribute_map = {
        'area': 'Area',
        'export_guide_shapes': 'ExportGuideShapes',
        'page_size': 'PageSize',
        'is_export_comments': 'IsExportComments'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(RenderingSaveOptions.swagger_types, **SaveOptionsModel.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(RenderingSaveOptions.attribute_map, **SaveOptionsModel.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, area=None, export_guide_shapes=None, page_size=None, is_export_comments=None, **kw):
        super(RenderingSaveOptions, self).__init__(**kw)
		    
        """
        RenderingSaveOptions - a model defined in Swagger
        """

        self.container['area'] = None
        self.container['export_guide_shapes'] = None
        self.container['page_size'] = None
        self.container['is_export_comments'] = None

        self.area = area
        if export_guide_shapes is not None:
          self.export_guide_shapes = export_guide_shapes
        if page_size is not None:
          self.page_size = page_size
        if is_export_comments is not None:
          self.is_export_comments = is_export_comments

    @property
    def area(self):
        """
        Gets the area of this RenderingSaveOptions.

        :return: The area of this RenderingSaveOptions.
        :rtype: RectangleF
        """
        return self.container['area']

    @area.setter
    def area(self, area):
        """
        Sets the area of this RenderingSaveOptions.

        :param area: The area of this RenderingSaveOptions.
        :type: RectangleF
        """
        """
        if area is None:
            raise ValueError("Invalid value for `area`, must not be `None`")
        """

        self.container['area'] = area

    @property
    def export_guide_shapes(self):
        """
        Gets the export_guide_shapes of this RenderingSaveOptions.

        :return: The export_guide_shapes of this RenderingSaveOptions.
        :rtype: bool
        """
        return self.container['export_guide_shapes']

    @export_guide_shapes.setter
    def export_guide_shapes(self, export_guide_shapes):
        """
        Sets the export_guide_shapes of this RenderingSaveOptions.

        :param export_guide_shapes: The export_guide_shapes of this RenderingSaveOptions.
        :type: bool
        """

        self.container['export_guide_shapes'] = export_guide_shapes

    @property
    def page_size(self):
        """
        Gets the page_size of this RenderingSaveOptions.

        :return: The page_size of this RenderingSaveOptions.
        :rtype: PageSize
        """
        return self.container['page_size']

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this RenderingSaveOptions.

        :param page_size: The page_size of this RenderingSaveOptions.
        :type: PageSize
        """

        self.container['page_size'] = page_size

    @property
    def is_export_comments(self):
        """
        Gets the is_export_comments of this RenderingSaveOptions.

        :return: The is_export_comments of this RenderingSaveOptions.
        :rtype: bool
        """
        return self.container['is_export_comments']

    @is_export_comments.setter
    def is_export_comments(self, is_export_comments):
        """
        Sets the is_export_comments of this RenderingSaveOptions.

        :param is_export_comments: The is_export_comments of this RenderingSaveOptions.
        :type: bool
        """

        self.container['is_export_comments'] = is_export_comments

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
        if not isinstance(other, RenderingSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other