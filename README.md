[Aspose.Diagram Cloud](https://products.aspose.cloud/Diagram) helps you develop diagrams manipulation applications. Our REST API based Diagram Cloud SDK allows your applications to work with Microsoft Visio Object Model. 

This repository contains Aspose.Diagram Cloud SDK source code. This SDK allows you to work with Aspose.Diagram Cloud REST APIs in your applications quickly and easily, with zero initial cost.

To use this SDK, you will need App SID and App Key which can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/apps) (free registration in Aspose Cloud is required for this).


# Features

### Support Import Formats  
* VSDX
* VDX
* VSD
* VSX
* VTX
* VSSX
* VSTX
* VSDM
* VSSM
* VSTM
* VDW
* VSS
* VST

### Support Export Formats  
* VSDX
* VDX
* VSX
* VTX
* VSSX
* VSTX
* VSDM
* VSSM
* VSTM
* PDF
* XPS
* SWF
* SVG
* EMF
* JPEG
* PNG
* BMP
* TIFF
* HTML

### Supported Operations
* Convert document format
* Create new document
* Upload document and save it with supported format
* Download document with supported format 

For the complete list of use-cases, please refer to [common operations format support map](https://docs.aspose.cloud/display/diagramcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap) to see what you can achieve!


# Storage API support
#### Since version 19.10, SDK includes support of storage operations for better user experience and unification, so now there's no need to use 2 different SDKs!

It gives you an ability to:
* Upload, download, copy, move and delete files, including versions handling (if you are using Cloud storage that supports this feature - true by default)
* Create, copy, move and delete folders
* Copy and move files and folders accross separate storages in scope of a single operation
* Check if certain file, folder or storage exists

# Examples
Please, look at [Examples](EXAMPLES.md) document for basic usage or use the [Examples](Examples) folder for more sophisticated scenarios.

### Aspose Cloud-hosted service VS on-premise deployment (*experimental feature*)
Starting from v19.10, you can choose either to use Aspose Cloud-hosted image processing service (the standard way) or the Docker image from Docker Hub deployed on-premise to serve the requests.
The details about key differences and deployment process will be described on the dedicated Docker Hub page as soon as it's released.

To succeed with your on-premise service usage by the SDK, you need to:
1. Use the new API class constructor with grantType parameter, clientId and clientSecret parameters.
```
diagramApi=DiagramApi(grantType,clientId,clientSecret)
```
2. Set *storage* or *storageName* parameters for each request where they're present (mandatory!).

# Tests
Tests are intended for internal usage only.

# Licensing
All Aspose.Diagram Cloud SDKs, helper scripts and templates are licensed under [MIT License](LICENSE).

# Contact Us
Your feedback is very important to us. Please feel free to contact via
+ [**Free Support Forum**](https://forum.aspose.cloud/c/diagram)
+ [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)

# Resources
+ [**Website**](https://www.aspose.cloud)
+ [**Product Home**](https://products.aspose.cloud/diagram)
+ [**Documentation**](https://docs.aspose.cloud/display/diagramcloud/Home)
+ [**API Reference**](https://apireference.aspose.cloud/diagram/)
+ [**Free Support Forum**](https://forum.aspose.cloud/c/diagram)
+ [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)
+ [**Blog**](https://blog.aspose.cloud/category/diagram/