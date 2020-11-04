![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/asposediagramcloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/asposediagramcloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposediagramcloud) [![GitHub license](https://img.shields.io/github/license/aspose-diagram-cloud/aspose-Diagram-cloud-python)](https://github.com/aspose-diagram-cloud/aspose-Diagram-cloud-python/blob/master/LICENSE) 

# Python SDK for Visio® Files

[Aspose.Diagram Cloud SDK for Python](https://products.aspose.cloud/diagram/python) offers to create new Visio files as well as export Visio files (VSD, VSDX, VSS, VSSX, VTX, VDX, VDW, VST, VSTX, and VSX) to image formats (PNG, SVG, EMF, TIFF, BMP & JPEG), export Visio flowcharts to HTML, SWF & XAML, and export diagrams to fixed-layouts, such as PDF & XPS. Feel free to explore the [Developer's Guide](https://docs.aspose.cloud/diagram/developer-guide/) for all usage scenarios. 

## Visio File Processing in the Cloud

- Retrieve document information of a Visio diagram.
- Programmatically create a new Microsoft Visio diagram file.
- Convert Visio flow-charts to other supported formats.
- Upload your business oriented Visio diagrams to cloud storage.
- Export Visio files to raster images, fixed-layout and HTML formats.

## New Features in Version 20.3

Added support to draw following objects on a page:
- Polyline
- Line
- Ellipse

Added support to:
- Set page setting  
- Add new empty page
- Get pages info

For the detailed notes, please visit [Aspose.Diagram Cloud 20.3 Release Notes](https://docs.aspose.cloud/diagram/aspose-diagram-cloud-20-3-release-notes/).

## Read & Write Visio Formats

**Microsoft Visio:** VSDX, VSX, VTX, VDX, VSSX, VSTX, VSDM, VSSM, VSTM

## Save Visio As

**Fixed Layout:** PDF, XPS
**Images:** JPEG, PNG, BMP, TIFF, SVG, EMF
**Web:** HTML
**Other:** XAML, SWF

## Read Visio Formats

**Microsoft Visio:** VDW, VSD, VSS, VST

## Getting Started with Aspose.Diagram Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/) to get your application information and free quota to use the API. Now execute `pip install asposediagramcloud` from the command line to get the get the SDK from PIP. 

## Convert Visio VDX to PDF 

```python
import os
import asposediagramcloud
from asposediagramcloud.apis.diagram_file_api import DiagramFileApi
from asposediagramcloud.models import FileFormatRequest
import examples_base

api_client = examples_base.GetApiClient()
diagramAPI = asposediagramcloud.apis.diagram_file_api.DiagramFileApi(api_client)

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
dataFolder = os.path.join(ABSPATH, "testData")

filename ='file_get_1.vdx'

# Upload file to Cloud Storage
filePath = os.path.join(dataFolder, filename)
examples_base.Upload(filePath, filename, folder=None, storage=None)

# Convert file to PDF format
folder = ""
is_overwrite = "true"
format =FileFormatRequest(format="pdf")
newfilename = "file_saveas_python.pdf"
result = diagramAPI.diagram_file_post_save_as(filename, folder=folder, newfilename=newfilename, format=format, is_overwrite=is_overwrite)
print(result);
```

## Aspose.Diagram Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js | Android | Perl | Swift |
|---|---|---|---|---|---|---|---|---|
| [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-dotnet) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-java) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-php) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-python) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-ruby)  | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-node) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-android) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-perl) | [GitHub](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-swift) |
| [NuGet](https://www.nuget.org/packages/Aspose.Diagram-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-diagram-cloud) | [Composer](https://packagist.org/packages/aspose/diagram-sdk-php) | [PIP](https://pypi.org/project/asposediagramcloud/) | [GEM](https://rubygems.org/gems/aspose_diagram_cloud)  | [NPM](https://www.npmjs.com/package/asposediagramcloud) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-diagram-cloud-android) |  [CPAN](https://metacpan.org/release/AsposeDiagramCloud-DiagramApi) | [POD](https://cocoapods.org/pods/AsposeDiagramCloud) |

[Home](https://www.aspose.cloud) | [Product Page](https://products.aspose.cloud/diagram/python) | [Documentation](https://docs.aspose.cloud/diagram/) | [Live Demo](https://products.aspose.app/diagram/family) | [API Reference](https://apireference.aspose.cloud/diagram/) | [Code Samples](https://github.com/aspose-diagram-cloud/aspose-diagram-cloud-ruby) | [Blog](https://blog.aspose.cloud/category/diagram/) | [Free Support](https://forum.aspose.cloud/c/diagram) | [Free Trial](https://dashboard.aspose.cloud/)
