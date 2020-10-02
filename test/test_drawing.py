# coding: utf-8

"""
    Aspose.Diagram Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

#from asposediagramcloud.apis.diagram_api import DiagramApi
#from asposediagramcloud.rest import ApiException
#import asposediagramcloud
import os
import sys
import unittest
import test_base

from asposediagramcloud.models import *

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

localtestFile = "testData/FileUpload.vdx"
storageTestFOLDER = "SDKTests\\Python"
fileName="drawingTest.vsdx"


class TestDrawing(unittest.TestCase):
    """ DiagramApi unit test stubs """

    def setUp(self):
        self.api = test_base.GetDiagramApi()
        self.storageApi = test_base.GetStorageApi()

    def tearDown(self):
        pass

    def test_create_new(self):
        folder = storageTestFOLDER
        is_overwrite = "true"
        result = self.api.create_new(fileName, folder=folder, is_overwrite=is_overwrite)
        self.assertIsNotNone(result.created, 'Error has occurred while create file')
        pass

    def test_draw_line(self):
        draw_data = LineData()
        draw_data.pin_x = 1
        draw_data.pin_y = 2
        draw_data.width = 1
        draw_data.height = 1
        draw_data.points =[PointF(False,0,1),PointF(False,1,0)]
        draw_data.text = "test draw line"
        shapeStyleData = ShapeStyleData()
        shapeStyleData.back_ground_color = "#FF0000"
        textStyleData = TextStyleData(style="Bold")
        textStyleData.font_size = 0.2
        textStyleData.font_name = "Times New Roman"
        draw_data.shape_style_data = shapeStyleData
        draw_data.text_style_data = textStyleData
        result=self.api.put_draw_line(fileName, "Page-0",draw_data, folder = storageTestFOLDER)
        self.assertTrue(result.is_success)
        pass

    def test_draw_ellipse(self):
        draw_data = EllipseData()
        draw_data.pin_x = 5
        draw_data.pin_y = 5
        draw_data.width = 1
        draw_data.height = 1
        draw_data.text = "test draw ellipse"
        shapeStyleData = ShapeStyleData()
        shapeStyleData.back_ground_color = "#FF0000"
        textStyleData = TextStyleData(style="Bold")
        textStyleData.font_size = 0.2
        textStyleData.font_name = "Times New Roman"
        draw_data.shape_style_data = shapeStyleData
        draw_data.text_style_data = textStyleData
        result=self.api.put_draw_ellipse(fileName, "Page-0",draw_data, folder = storageTestFOLDER)
        self.assertTrue(result.is_success)
        pass

    def test_draw_poly_line(self):
        draw_data = PolylineData()
        draw_data.pin_x = 3
        draw_data.pin_y = 3
        draw_data.width = 1
        draw_data.height = 1
        draw_data.points =[PointF(False,0,0),PointF(False,0,1),PointF(False,1,1),PointF(False,1,0)]
        draw_data.text = "test draw polyline"
        shapeStyleData = ShapeStyleData()
        shapeStyleData.back_ground_color = "#FF0000"
        textStyleData = TextStyleData(style="Bold")
        textStyleData.font_size = 0.2
        textStyleData.font_name = "Times New Roman"
        draw_data.shape_style_data = shapeStyleData
        draw_data.text_style_data = textStyleData
        result=self.api.put_draw_line(fileName, "Page-0",draw_data, folder = storageTestFOLDER)
        self.assertTrue(result.is_success)
        pass

if __name__ == '__main__':
    unittest.main()