 # Team Data Science Process from Microsoft

This repository contains an instantiation of the [**Team Data Science Process (TDSP) from Microsoft**](https://github.com/Azure/Microsoft-TDSP) for project **Vienna**. The TDSP is an agile, iterative, data science methodology designed to improve team collaboration and learning. It facilitates better coordinated and more productive data science enterprises by providing:

- a lifecycle that defines the steps in project development
- a standard project structure
- artifact templates for reporting
- tools to assist with data science tasks

## Information about TDSP in Azure ML Workbench
When you instantiate the TDSP from Vienna, you get the TDSP-recommended standardized directory structure and document templates for project execution and delivery. The workflow then consists of the following steps:

- modify the documentation templates provided here for your project
- execute your project
- prepare the Data Science deliverables for your client or customer, including the ProjectReport.md report.

We provide [instructions on how to instantiate and use TDSP in Azure ML Workbench](./Docs/Using-TDSP-in-Vienna.md).

## The Data Science Lifecycle 
TDSP uses the data science lifecycle to structure projects. The lifecycle defines the steps that a project typically must execute, from start to finish. This lifecycle is valid for data science projects that build data products and intelligent applications that include predictive analytics. The goal is to incorporate machine learning or artificial intelligence (AI) models into commercial products. Exploratory data science projects or ad hoc/on-off analytics projects can also use this process, but in this case some steps of this lifecycle may not be needed.    

Here is a depiction of the TDSP lifecycle. 

![TDSP_LIFECYCLE](./Images/tdsp-lifecycle.jpg) 

The TDSP data science lifecycle is composed of four major stages that are executed iteratively. This includes:

* Business Understanding
* Data Acquisition and Understanding
* Modeling
* Deployment

These stages should, ideally, be followed by customer acceptance for successful projects. 

If you are using a different lifecycle schema, such as [CRISP-DM](https://wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining), [KDD](https://wikipedia.org/wiki/Data_mining#Process) or your own custom process that is working well in your organization, you can still use the TDSP in the context of those development lifecycles. 

For reference, see a more [detailed description of the TDSP life-cycle](https://github.com/Azure/Microsoft-TDSP/blob/master/Docs/lifecycle-detail.md). That version also provides additional documentation templates that are associated with each phase of the TDSP lifecycle.

## Documenting your project
Refer to [TDSP doumentation templates](https://github.com/Azure/Azure-TDSP-ProjectTemplate) to see how you can document your project for efficient collaboration and reproducibility. In the current Vienna TDSP documentation template, we recommend that you include all the information in the [ProjectReport](./ProjectReport.md) file. This template needs to be filled out with information that is specific to your project. 

In addition to the [ProjectReport](./ProjectReport.md), which serves as the primary project document, we provide another template, [ProjectLearnings](./Docs/ProjectLearnings.md), to include any learnings and information, which may not be included in the primary project document, but still useful to document. 

Documents received from a customer can be stored in .\Docs\CustomerDocs. Documents prepared for sharing information with a customer (e.g. ProjectReport, graphs, tables etc.) can be stored in .\Docs\DeliveralbeDocs.

## Project folder structure
The TDSP project template contains following top-level folders:
1. **Code**: Contains code
2. **Docs**: Contains neccessary documentation about the project
3. **Sample_Data**: Contains **SAMPLE (small)** data that can be used for early development or testing. Typically, not more than several Mbs. Not for full or large data-sets.


## Project planning and execution
To deploy [Visual Studio Online (Team Services)](https://azure.microsoft.com/en-us/services/visual-studio-team-services/) for planning, managing and executing your data science projects, detailed instructions are provided [here](https://github.com/Azure/Microsoft-TDSP/blob/master/Docs/project-execution.md).

## Release notes
This is an **early preview (Sept 2016)** release of [TDSP](https://github.com/Azure/Microsoft-TDSP). We are continuously improving TDSP based on customer experience and feedback, and releasing new features. Refer to [TDSP](https://github.com/Azure/Microsoft-TDSP) page for more information. 

## Ask questions. 
We would love to hear back from your own experience with the TDSP. Should you have any questions or suggestions, please create a new discussion thread on the [Issues Tab](https://github.com/Azure/Microsoft-TDSP/issues).

