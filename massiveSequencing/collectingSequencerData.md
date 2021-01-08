# Collecting Sequencer data

When you finish the massive workflow, it does not mean that the job is completed, is from now on when the automatic process in iSkyLIMS starts.

To allow that this automatic job is successful there are some requirements that must be fulfill:

*   Illumina Sequencer must be configured to save the sequencing information in a shared folder.
*   This shared folder must be accessed by iSkyLIMS using SAMBA connection.
*   This folder requires write permission if iSkyLIMS is configured to copy the sample sheet of the run (for NextSeq runs).
*   Interop program installed on your system
*   Script to execute the “bcl2fastq”

Once these requirements are satisfied, iSkyLIMS checks on a regularly bases any changes that occurs on the shared folder. For that propose iSkyLIMS uses crontab linux utility.
Crontab schedule is defined on setting.py file, located at <your_installation_directory>/iSkyLIMS. At the bottom of the file you will see the crontab settings.

## test
