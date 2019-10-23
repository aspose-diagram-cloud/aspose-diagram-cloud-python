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
from . import RenderingSaveOptions

class ImageSaveOptions(RenderingSaveOptions):
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
        'image_brightness': 'float',
        'image_contrast': 'float',
        'jpeg_quality': 'int',
        'page_count': 'int',
        'resolution': 'float',
        'scale': 'float',
        'tiff_compression': 'str',
        'export_hidden_page': 'bool',
        'image_color_mode': 'str',
        'page_index': 'int',
        'save_foreground_pages_only': 'bool',
        'same_as_pdf_conversion_area': 'bool',
        'pixel_offset_mode': 'str',
        'smoothing_mode': 'str',
        'compositing_quality': 'str',
        'interpolation_mode': 'str'
    }

    attribute_map = {
        'image_brightness': 'ImageBrightness',
        'image_contrast': 'ImageContrast',
        'jpeg_quality': 'JpegQuality',
        'page_count': 'PageCount',
        'resolution': 'Resolution',
        'scale': 'Scale',
        'tiff_compression': 'TiffCompression',
        'export_hidden_page': 'ExportHiddenPage',
        'image_color_mode': 'ImageColorMode',
        'page_index': 'PageIndex',
        'save_foreground_pages_only': 'SaveForegroundPagesOnly',
        'same_as_pdf_conversion_area': 'SameAsPdfConversionArea',
        'pixel_offset_mode': 'PixelOffsetMode',
        'smoothing_mode': 'SmoothingMode',
        'compositing_quality': 'CompositingQuality',
        'interpolation_mode': 'InterpolationMode'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ImageSaveOptions.swagger_types, **RenderingSaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ImageSaveOptions.attribute_map, **RenderingSaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, image_brightness=None, image_contrast=None, jpeg_quality=None, page_count=None, resolution=None, scale=None, tiff_compression=None, export_hidden_page=None, image_color_mode=None, page_index=None, save_foreground_pages_only=None, same_as_pdf_conversion_area=None, pixel_offset_mode=None, smoothing_mode=None, compositing_quality=None, interpolation_mode=None, **kw):
        super(ImageSaveOptions, self).__init__(**kw)
		    
        """
        ImageSaveOptions - a model defined in Swagger
        """

        self.container['image_brightness'] = None
        self.container['image_contrast'] = None
        self.container['jpeg_quality'] = None
        self.container['page_count'] = None
        self.container['resolution'] = None
        self.container['scale'] = None
        self.container['tiff_compression'] = None
        self.container['export_hidden_page'] = None
        self.container['image_color_mode'] = None
        self.container['page_index'] = None
        self.container['save_foreground_pages_only'] = None
        self.container['same_as_pdf_conversion_area'] = None
        self.container['pixel_offset_mode'] = None
        self.container['smoothing_mode'] = None
        self.container['compositing_quality'] = None
        self.container['interpolation_mode'] = None

        if image_brightness is not None:
          self.image_brightness = image_brightness
        if image_contrast is not None:
          self.image_contrast = image_contrast
        if jpeg_quality is not None:
          self.jpeg_quality = jpeg_quality
        if page_count is not None:
          self.page_count = page_count
        if resolution is not None:
          self.resolution = resolution
        if scale is not None:
          self.scale = scale
        if tiff_compression is not None:
          self.tiff_compression = tiff_compression
        if export_hidden_page is not None:
          self.export_hidden_page = export_hidden_page
        if image_color_mode is not None:
          self.image_color_mode = image_color_mode
        if page_index is not None:
          self.page_index = page_index
        if save_foreground_pages_only is not None:
          self.save_foreground_pages_only = save_foreground_pages_only
        if same_as_pdf_conversion_area is not None:
          self.same_as_pdf_conversion_area = same_as_pdf_conversion_area
        if pixel_offset_mode is not None:
          self.pixel_offset_mode = pixel_offset_mode
        if smoothing_mode is not None:
          self.smoothing_mode = smoothing_mode
        if compositing_quality is not None:
          self.compositing_quality = compositing_quality
        if interpolation_mode is not None:
          self.interpolation_mode = interpolation_mode

    @property
    def image_brightness(self):
        """
        Gets the image_brightness of this ImageSaveOptions.

        :return: The image_brightness of this ImageSaveOptions.
        :rtype: float
        """
        return self.container['image_brightness']

    @image_brightness.setter
    def image_brightness(self, image_brightness):
        """
        Sets the image_brightness of this ImageSaveOptions.

        :param image_brightness: The image_brightness of this ImageSaveOptions.
        :type: float
        """

        self.container['image_brightness'] = image_brightness

    @property
    def image_contrast(self):
        """
        Gets the image_contrast of this ImageSaveOptions.

        :return: The image_contrast of this ImageSaveOptions.
        :rtype: float
        """
        return self.container['image_contrast']

    @image_contrast.setter
    def image_contrast(self, image_contrast):
        """
        Sets the image_contrast of this ImageSaveOptions.

        :param image_contrast: The image_contrast of this ImageSaveOptions.
        :type: float
        """

        self.container['image_contrast'] = image_contrast

    @property
    def jpeg_quality(self):
        """
        Gets the jpeg_quality of this ImageSaveOptions.

        :return: The jpeg_quality of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['jpeg_quality']

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """
        Sets the jpeg_quality of this ImageSaveOptions.

        :param jpeg_quality: The jpeg_quality of this ImageSaveOptions.
        :type: int
        """

        self.container['jpeg_quality'] = jpeg_quality

    @property
    def page_count(self):
        """
        Gets the page_count of this ImageSaveOptions.

        :return: The page_count of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['page_count']

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this ImageSaveOptions.

        :param page_count: The page_count of this ImageSaveOptions.
        :type: int
        """

        self.container['page_count'] = page_count

    @property
    def resolution(self):
        """
        Gets the resolution of this ImageSaveOptions.

        :return: The resolution of this ImageSaveOptions.
        :rtype: float
        """
        return self.container['resolution']

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this ImageSaveOptions.

        :param resolution: The resolution of this ImageSaveOptions.
        :type: float
        """

        self.container['resolution'] = resolution

    @property
    def scale(self):
        """
        Gets the scale of this ImageSaveOptions.

        :return: The scale of this ImageSaveOptions.
        :rtype: float
        """
        return self.container['scale']

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this ImageSaveOptions.

        :param scale: The scale of this ImageSaveOptions.
        :type: float
        """

        self.container['scale'] = scale

    @property
    def tiff_compression(self):
        """
        Gets the tiff_compression of this ImageSaveOptions.

        :return: The tiff_compression of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['tiff_compression']

    @tiff_compression.setter
    def tiff_compression(self, tiff_compression):
        """
        Sets the tiff_compression of this ImageSaveOptions.

        :param tiff_compression: The tiff_compression of this ImageSaveOptions.
        :type: str
        """
        allowed_values = ["None", "Rle", "Ccitt3", "Ccitt4", "Lzw"]
        if tiff_compression not in allowed_values:
            raise ValueError(
                "Invalid value for `tiff_compression` ({0}), must be one of {1}"
                .format(tiff_compression, allowed_values)
            )

        self.container['tiff_compression'] = tiff_compression

    @property
    def export_hidden_page(self):
        """
        Gets the export_hidden_page of this ImageSaveOptions.

        :return: The export_hidden_page of this ImageSaveOptions.
        :rtype: bool
        """
        return self.container['export_hidden_page']

    @export_hidden_page.setter
    def export_hidden_page(self, export_hidden_page):
        """
        Sets the export_hidden_page of this ImageSaveOptions.

        :param export_hidden_page: The export_hidden_page of this ImageSaveOptions.
        :type: bool
        """

        self.container['export_hidden_page'] = export_hidden_page

    @property
    def image_color_mode(self):
        """
        Gets the image_color_mode of this ImageSaveOptions.

        :return: The image_color_mode of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['image_color_mode']

    @image_color_mode.setter
    def image_color_mode(self, image_color_mode):
        """
        Sets the image_color_mode of this ImageSaveOptions.

        :param image_color_mode: The image_color_mode of this ImageSaveOptions.
        :type: str
        """
        allowed_values = ["None", "Grayscale", "BlackAndWhite"]
        if image_color_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `image_color_mode` ({0}), must be one of {1}"
                .format(image_color_mode, allowed_values)
            )

        self.container['image_color_mode'] = image_color_mode

    @property
    def page_index(self):
        """
        Gets the page_index of this ImageSaveOptions.

        :return: The page_index of this ImageSaveOptions.
        :rtype: int
        """
        return self.container['page_index']

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this ImageSaveOptions.

        :param page_index: The page_index of this ImageSaveOptions.
        :type: int
        """

        self.container['page_index'] = page_index

    @property
    def save_foreground_pages_only(self):
        """
        Gets the save_foreground_pages_only of this ImageSaveOptions.

        :return: The save_foreground_pages_only of this ImageSaveOptions.
        :rtype: bool
        """
        return self.container['save_foreground_pages_only']

    @save_foreground_pages_only.setter
    def save_foreground_pages_only(self, save_foreground_pages_only):
        """
        Sets the save_foreground_pages_only of this ImageSaveOptions.

        :param save_foreground_pages_only: The save_foreground_pages_only of this ImageSaveOptions.
        :type: bool
        """

        self.container['save_foreground_pages_only'] = save_foreground_pages_only

    @property
    def same_as_pdf_conversion_area(self):
        """
        Gets the same_as_pdf_conversion_area of this ImageSaveOptions.

        :return: The same_as_pdf_conversion_area of this ImageSaveOptions.
        :rtype: bool
        """
        return self.container['same_as_pdf_conversion_area']

    @same_as_pdf_conversion_area.setter
    def same_as_pdf_conversion_area(self, same_as_pdf_conversion_area):
        """
        Sets the same_as_pdf_conversion_area of this ImageSaveOptions.

        :param same_as_pdf_conversion_area: The same_as_pdf_conversion_area of this ImageSaveOptions.
        :type: bool
        """

        self.container['same_as_pdf_conversion_area'] = same_as_pdf_conversion_area

    @property
    def pixel_offset_mode(self):
        """
        Gets the pixel_offset_mode of this ImageSaveOptions.

        :return: The pixel_offset_mode of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['pixel_offset_mode']

    @pixel_offset_mode.setter
    def pixel_offset_mode(self, pixel_offset_mode):
        """
        Sets the pixel_offset_mode of this ImageSaveOptions.

        :param pixel_offset_mode: The pixel_offset_mode of this ImageSaveOptions.
        :type: str
        """
        allowed_values = ["Default", "HighSpeed", "HighQuality", "None", "Half", "Invalid"]
        if pixel_offset_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `pixel_offset_mode` ({0}), must be one of {1}"
                .format(pixel_offset_mode, allowed_values)
            )

        self.container['pixel_offset_mode'] = pixel_offset_mode

    @property
    def smoothing_mode(self):
        """
        Gets the smoothing_mode of this ImageSaveOptions.

        :return: The smoothing_mode of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['smoothing_mode']

    @smoothing_mode.setter
    def smoothing_mode(self, smoothing_mode):
        """
        Sets the smoothing_mode of this ImageSaveOptions.

        :param smoothing_mode: The smoothing_mode of this ImageSaveOptions.
        :type: str
        """
        allowed_values = ["Default", "HighSpeed", "HighQuality", "None", "AntiAlias", "Invalid"]
        if smoothing_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `smoothing_mode` ({0}), must be one of {1}"
                .format(smoothing_mode, allowed_values)
            )

        self.container['smoothing_mode'] = smoothing_mode

    @property
    def compositing_quality(self):
        """
        Gets the compositing_quality of this ImageSaveOptions.

        :return: The compositing_quality of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['compositing_quality']

    @compositing_quality.setter
    def compositing_quality(self, compositing_quality):
        """
        Sets the compositing_quality of this ImageSaveOptions.

        :param compositing_quality: The compositing_quality of this ImageSaveOptions.
        :type: str
        """
        allowed_values = ["Default", "HighSpeed", "HighQuality", "GammaCorrected", "AssumeLinear", "Invalid"]
        if compositing_quality not in allowed_values:
            raise ValueError(
                "Invalid value for `compositing_quality` ({0}), must be one of {1}"
                .format(compositing_quality, allowed_values)
            )

        self.container['compositing_quality'] = compositing_quality

    @property
    def interpolation_mode(self):
        """
        Gets the interpolation_mode of this ImageSaveOptions.

        :return: The interpolation_mode of this ImageSaveOptions.
        :rtype: str
        """
        return self.container['interpolation_mode']

    @interpolation_mode.setter
    def interpolation_mode(self, interpolation_mode):
        """
        Sets the interpolation_mode of this ImageSaveOptions.

        :param interpolation_mode: The interpolation_mode of this ImageSaveOptions.
        :type: str
        """
        allowed_values = ["Default", "Low", "High", "Bilinear", "Bicubic", "NearestNeighbor", "HighQualityBilinear", "HighQualityBicubic", "Invalid"]
        if interpolation_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `interpolation_mode` ({0}), must be one of {1}"
                .format(interpolation_mode, allowed_values)
            )

        self.container['interpolation_mode'] = interpolation_mode

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
        if not isinstance(other, ImageSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
