# Installation Instruction

The introduction of massive sequencing (MS) in genomics facilities has meant an exponential growth in data generation, requiring a precise tracking system, from library preparation to fastq file generation, analysis and delivery to the researcher.

Software designed to handle those tasks are called Laboratory Information Management Systems (LIMS), and its software has to be adapted to their own genomics laboratory particular needs.

iSkyLIMS is born with the aim of helping with the wet laboratory tasks, and implementing a workflow that guides genomics labs on their activities from library preparation to data production, reducing potential errors associated to high throughput technology, and facilitating the quality control of the sequencing.

Also, iSkyLIMS connects the wet lab with dry lab facilitating data analysis by bioinformaticians.

## Install iSkyLIMS in Docker

To create the Docker image execute the following commands to download and run then installation script


```bash
git clone https://github.com/BU-ISCIII/iSkyLIMS.git iSkyLIMS
bash docker_iskylims_install.sh
```

The script creates a Docker compose container with 2 services:

- web1. Which contains the iSkyLIMS web application
- db1. With the mySQL database

After Docker is created and services are up, database structure and initial data are loaded into database.

When this step is completed you will prompt to define the super user which will be the one to connect to "django admin pages". You can type any name, but we recommend that you use "admin" , because admin user is requested later on when defining the initial settings.

Follow the prompt message to create the super user account.

When script ends open your navigator typing **localhost:8000** to access to iSkyLIMS


## Install iSkyLIMS in your server running ubuntu

### Pre-requesites
Before starting the installation check :
- You have **sudo privileges** to install the additional software packets that iSkyLIMS needs.
- Database (MySQL/MariaDB) is running  
- Local server configured for sending emails
- Apache server is running on local server

#### Clone github repository
```bash
cd /opt
sudo git clone https://github.com/BU-ISCIII/iSkyLIMS.git iSkyLIMS
```
#### Configuration settings

Open with your favourite editor the configuration file to set your own values for
database ,email settings and the local IP of the server where iSkyLIMS will run.
```bash
sudo nano install_settings.txt
```

### Run installation script

iSkyLIMS will be installed on the "/opt" directory. Before start the installation be sure you have sudo priveleges.

Execute the following commands in a linux terminal.

```bash

sudo bash install.sh
```

After installation is completed open you navigator typing "localhost" or the "server local IP".
