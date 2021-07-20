# Installation Instruction

The introduction of massive sequencing (MS) in genomics facilities has meant an exponential growth in data generation, requiring a precise tracking system, from library preparation to fastq file generation, analysis and delivery to the researcher.

Software designed to handle those tasks are called Laboratory Information Management Systems (LIMS), and its software has to be adapted to their own genomics laboratory particular needs.

iSkyLIMS is born with the aim of helping with the wet laboratory tasks, and implementing a workflow that guides genomics labs on their activities from library preparation to data production, reducing potential errors associated to high throughput technology, and facilitating the quality control of the sequencing.

Also, iSkyLIMS connects the wet lab with dry lab facilitating data analysis by bioinformaticians.

## Install iSkyLIMS in Docker

To create the Docker image execute the following commands to download and run then installation script


```
wget https://raw.githubusercontent.com/BU-ISCIII/iSkyLIMS/develop/iskylims_install.sh
bash iskylims_install.sh
```

The script creates a Docker compose container with 2 services:

* web1. Which contains the iSkyLIMS web application
* db1. With the mySQL database

After Docker is created and services are up, database structure and initial data are loaded into database. When this step is completed you will
prompt to define the super user which will be the one to connect to "django admin pages". You can type any name, but we recommend that you use "admin" ,
because admin user is requested later on when defining the initial settings.

Follow the prompt message to create the super user account.

When script ends open your navigator and type to access to iSkyLIMS

```
localhost:8000
```

## Installation prerequisites
