# Investigator workflow

The activities that Investigator needs to do in iSkyLIMS is enter the data that are collected during sample manipulation.  
These activities required for massive sequencing are separated in 3 main steps:

1. Record new sample.
2. Molecule extraction.
3. Library preparation.

The figure below shows the workflow activities from the time the new sample is recorded in iSkyLIMS until sample is included in the sequencer.

![](../images/wetlab_workflow/wetlab_sample_workflow2.png)


## Record new Sample

At this point, we assume that the requirements defined on, [WetlabManager workflow](massiveSequencing/wetlabManagerWorkflow.md) are defined.

To record a new sample (or a set of them) select “Record Samples” from the RUN PREPARATION menu.  

> Any logged user can record new samples.  
>Because in some organization there is one person which receives all samples and he/she is responsible to recorded them.   
>But it is also possible, that every one in the laboratory recorded their own sample.  
> For those reason any user can record new samples.


As we already mention the recorded sample option is available for all registered users, but **once a sample was recorded**  by a user, he/she is the only one allowed to add information.

In the record sample form, you can extend it to fit all samples that you need, by pressing “ENTER” key at the bottom line.

![](../images/wetlab_workflow/wetlab_record_new_sample.png)

**Patient Code ID**. When personnel in the lab receives the sample in very rare cases you the full name of the patient, due to patient privacy you get only the coding value of the patient.  
You do not need to define in advance the patient code, iSyLIMS create a new entry on database or link this sample to the patient if it is already defined.

**Sample Name**. It is the identification code for a sample that is received in the lab.  
The sample name cannot be repeated, in order to avoid add information to a wrong sample, just because they are named the same. Then iSKyLIMS will not allow to define a new sample that is already defined, getting a warning message to rename the sample.
It is very common that some case samples need to be processed again, because of many reason. For these ones you do not need to define the sample, because it is already defined, but you have to specify which step need to be reprocessed.  
Sometimes for reprocessing again the sample, you need to require another/more sample for the patient. In this case you have to considered a new sample, which will have of course a new sample name. You can join these sample because they are assigned to the same patient.

**Sample Origin**. You will select from the option list the place from where the sample comes from, like the hospital name, organization name, laboratory name, etc. You only get the option from the ones that were defined in [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Sample-origin) Sample origin.

**Type of sample**. You select from the option list the type of sample that sample belongs to. The type of sample were defined [WetlabManager workflow](massiveSequencing/wetlabManagerWorkflow.md).

**Species**. Select for the option list the specie of the sample. Species list were defined in [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Species-definition) Species.

**Project/Service**. We have defined these 8 fields, which in most of the situations are not enough. To customized with the additional information that you need to set for each example iSkyLIMS allows you to defined your own fields. To select them you need to select from the option list the one that fit you. Remember that these projects were defined in [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Define-sample-project) sample Project.

**Date sample extraction**. Date were the sample was extracted from the patient. Do not set the date that you recorded in iSkyLIMS. Select the date from the calendar window.

**Sample Storage Location**. Besides to record de sample is important to track where the sample has been storage. This is a free text that you can write anything that helps to identify where the sample is located.
For each sample, all fields must be filled in, unless they were set as optional when defining the type of sample in [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Samples-origin) Samples Origin.


After submit the form, iSkyLIMS returns you back to this page in case that some mandatory information was missing.

### Recording additional sample information

When all samples in the previous menu are recorded you can have 2 different scenarios according if:
*   You need to add **additional information**, according to the project that was selected during sample definition.
*   **No additional** information is required.

For the first scenario, where you need to set more data to the sample, a new form is displayed to write this information.

![](../images/wetlab_workflow/wetlab_additional_info_new_sample_form.png)


Note that the fields that you see in the picture above, on the next column to Sample Name, are only for writing this document. The column names that you will get are the additional parameters that were defined at the time to Define a new Sample Project in [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Define-sample-project).

When setting information to the sample you can have 3 types of choices, according as the type of field was defining during the sample project creation.   
The field when you click on it you can have:
*   **Option list** to select one of the choices.
*   **Calendar window** to select the date.
*   **Normal text** to type directly on the field any character.

When all information is included in the form, click on the submit to save the additional information.  
You will get the confirmation that samples are successfully recorded.

![](../images/wetlab_workflow/wetlab_successful_recorded_new_sample.png)

### Recording pending additional sample information

In case you decided do not complete the additional information, not just after the form for adding additional sample information is showed, you can still add this information at any time.  
Select again from the main menu “**Record Samples**” and this time above to the form for recording a new sample you will get a table with the list of the pending samples which require adding more information.

![](../images/wetlab_workflow/wetlab_additional_info_new_sample_form2.png)

In the table click on the check box for all samples that you need to add the information.

You will get the form to fill in, same form as described above, and when it was completed you will have the same windows confirmation.

## Molecule extraction

The next step after the sample is defined in iSkyLIMS is the process for **DNA/RNA extraction**.  

During this process the people in the laboratory will use specific commercial kits to extract the DNA/RNA.  
These kits, as we described in  [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Define-commercial-kits) define Commercial kits for molecule extraction, the user with wetlab manager rights needs to define the commercial kits that are used in the lab for the DNA/RNA extraction.

Then using these kits as input the investigator has to define his/her own lot kit, as described in  [Investigator  configuration](massiveSequencing/investigatorConfiguration.html#User-lot-kit-configuration).Define User Lot Commercial Kit.  
Before starting the molecule extraction definition in iSkyLIMS, check that the protocol you want to use for this extraction is available form the select list. See chapter  [WetlabManager configuration](massiveSequencing/wetlabManagerConfiguration.html#Protocol-and-parameter-definitions) Protocol and Parameter definitions.

To handle the extraction molecule process in iSkyLIMS select “Handling Molecules” from the RUN PREPARATION menu.

![](../images/wetlab_workflow/wetlab_molecule_extraction_tabs.png)

In the new window you can see 3 tabs that you can select:
*   New Samples
*   My pending molecules
*   Molecules use specification

The first time you access to this panel you only have data in the “**New Samples**” tab, because the tab “**My pending molecules**” only shows the molecules that are you started to work with.

On **New Samples** you will see the samples that have been already define which need to start the extraction of DNA/RNA.

The sample field has the sample name, where you identify the sample that you need to work on, but also this table is displayed in date order, to help you to select the older samples.

**Sample Code ID** field can help you to select the samples that have been created by a user, in that way you can easily filter the ones that you need to work with.

To get more information of how Sample Code ID is built check the  [Understanding Code ID](massiveSequencing/understandingCodeID.md) in each step.

Select the samples that you are going to take over of and click on the submit button.

![](../images/wetlab_workflow/wetlab_molecule_new_samples_form.png)

After submitting, you get a new page to assign the molecule protocol, as well as other information used for the extraction in an excel table format.

![](../images/wetlab_workflow/wetlab_sample_add_molecule_information_form.png)

*   **Molecule type**. Select if you are going to use DNA or RNA extraction from the original sample.
*   **Type of Extraction**. Select Manual if the sample is pipetted, or Automated if a Robot is used.
*   **Extraction date**. Set the date from the extracted molecule process starts.
*   **Protocol to be used**. Select from the option list the protocol name that will be used for the extraction.

Note that for helping the selection of "protocol to be used", it is linked to the value that you select on the molecule type field.  
Then selecting for example DNA as type of molecule the option list that you can select are the ones that are defined to be used with DNA molecule.  
If you select first an option from the “Protocol to be used” field you will get the full list, containing the protocols used for DNA as well as RNA.

You can select now the one that you will use, however when selecting Molecule Type field, the value that you select on the protocol is reset. So it is recommended to select the molecule type first and then the protocol from the option list.  
When you submit the information these samples, they will store in database and also they will assign to you as the owner. From now on, you (or the user in your friend list) are the only one that can set the parameter values.
Keep in mind that at the time you get this page to include information, the samples have been not assign yet to you. Only when you click on the submit button they will.

In “**My pending molecules**” tab is displayed the molecules that are assigned to you and they require to fill the information with the parameter values defined in the selected protocol.

![](../images/wetlab_workflow/wetlab_my_pending_molecules_form.png)




## Handling Library Preparation
