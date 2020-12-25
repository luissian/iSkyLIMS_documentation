# Wetlab Manager Configuration

The following configuration is only available when your user login belongs to the “Wetlab Manager” group.

Wetlab Manager, has the responsibility to define the main parameters/settings that will be used in the Massive Sequencing application, and they will be the ones that are showed when the Investigator fill the information in the form.

There are 4 main groups for configuration:
*   Initial settings definitions
*   Protocol and Parameters definitions
*   Samples parameter definitions
*   Commercial Kits used in the laboratory


## Initial settings
This section will show you how to define the initial data that Massive Sequencing module needs as base from where the rest of information is referenced to.

During the installation already some data are loaded in database, but if you need to add extra information follow the instructions bellow.  

There are 4 type of information that you need to define in the  **initial settings**
*   Species
*   Sample Origin
*   Molecule type
*   Protocol type

For selecting these settings select **Preliminary Preparation --> Initial Settings** from the main menu.

![](../images/wetlab_configuration/initial_settings_menu.png)

### Species definition
Define the name of the species that you are working with by clicking on the "Species" Tab.
![species form](../images/wetlab_configuration/species_definition_form.png)

Write the specie name and click on the Submit button.

As you can see on the right side "human" and "mouse" species are already defined. This was done during the installation.

### Samples Origin
Define the location from the sample could came from, by clicking on the "Sample Origin" Tab.

![](../images/wetlab_configuration/samples_origin_form.png)

There are 3 fields that you need to fill in:
*   New Origin
*   Origin coding name
*   Location data

**New Origin** is the organization/hospital name who sends the sample to your organization.

**Coding name** is any short name that can identify the origin of the sample.

**Location data** is the country/Area which he origin is located.

For example if you receives samples from the Metropolitan Hospital at New York. You could define the samples origin fields like this:
*   New Origin. **Metropolitan Hospital**
*   Origin coding name. **Metropolitan**
*   Location data. **New York**

On the right side you will see the Samples Origin that have been defined so far.
### Molecule Type
During the installation 2 Molecule types were defined.
*   DNA
*   RNA

If you need to define an additional molecule type click on the "Molecule type" tab and write the new molecule type.


![](../images/wetlab_configuration/molecule_type_form.png)

### Protocol Type
During the installation 3 protocol types were defined:
*   DNA Extraction
*   RNA Extraction
*   Library Preparation

If you have a look to the right side, inside "Protocol Type" tab, you can see that **DNA Extraction** protocol type was defined to use **DNA** as molecule type. **RNA Extraction** use the **RNA** molecule and the **Library Preparation** does not use any molecule, because this protocol type will be used later, when defining the library preparation parameters.

These are the basic one that you will need when defining the Protocol and their parameter in section    [Protocol and Parameters definitions](#protocol-and-parameters-definitions). If you are new in iSkyLIMS, we recommended to you to keep these 3 protocol type settings, so you can skip this section and continue with the next section.

But if you need to add an additional protocol type, because you create a new type of molecule, or for any other reason, you can create a new one using the form inside "Protocol Type" tab.

![](../images/wetlab_configuration/protocol_type_form.png)


## Protocol and Parameters definitions
When a protocol is defined it uses one of the "Protocol Type" that was defined during the installation or it was added in the previous section.

There are 2 steps to do when defining a new Protocol.
1. Define the Protocol name
2. Define the Parameters used on the protocol

### Protocol definition
To define a new protocol  select from the main menu PRELIMINARY PREPARATION  Create New Protocol.

![](../images/wetlab_configuration/new_protocol_form.png)

**Select Protocol Type** shows you the list of available protocol types.

**Define new Protocol name** , write the name to identify the protocol-

**Description**, write some information about the scope and use of this protocol.

```
You have to repeat this process to define a protocol for each protocol type defined:
- "DNA Extraction" or "RNA Extraction" or both
  (depends on the sequence types, used in your organization)
- "Library Preparation"
```

After click on the submit button the confirmation page is displayed allowing to continue with parameter used on this protocol.

### Protocol Parameter definitions

On the protocol parameter form, you can define the parameter names, the order that will be presented to the investigator when filling it, a checkbox to set if the parameter is used, range of values that parameter can have, and a short description of the parameter.

![](../images/wetlab_configuration/protocol_parameter_form.png)

Notice that **Parameter name** and **Order** fields are mandatory. If Parameter Name is empty, the line is ignored.  

Click on the **Used** check box to display the parameter when Investigator fills the parameter values.

**Parameter Type** field, list the type of parameter for this parameter name. There are 3 types:

*   **string**. For having any kind of letter and numbers
*   **Date**. To display a calender
*   **Option List**. To select only the predefined values.

**Option Values** is only valid when the parameter is defined as "Option List". Set the possible values that parameter could have, when presenting to the Investigator as a selection option list.
To define the values, write them separating by commas “,” and without any blank space between the option values.

**Min Value** and **Max Value** are optional.

**Description** field is optional and you can type some few words to explain the parameter.

As normal protocol definition workflow, we mention before that when confirmation panel, after defining a new protocol,  you could click on the "add Parameter" button to add them. However, it is not mandatory that you fill this information on this moment, you can always add them, by defining a new protocol again, but now scroll down to the "protocol already defined" panel.

![](../images/wetlab_configuration/protocol_already_defined.png)



## Samples parameter definitions
To store the different information that each organization needs for the laboratory samples, makes that iSkyLIMS has to be flexible by adding in the forms those parameters, but also do not consider the ones that we found as recommended.

To explain better, the **Samples Parameters**, let me show to you the information that you need to fill in, when defining a new sample.



## Commercial Kits used in the laboratory

Inside the kits configuration, the following type of kits need to be defined:
*   Define the Collection Index kits
*   Define Commercial Kits
*   User Lot Commercial Kits

To store the different information that each organization needs for the laboratory samples, makes that iSkyLIMS has to be flexible by adding in the forms those parameters, but also do not consider the ones that we found as recommended.

To explain better, the “Samples Parameters”, let me show to you the information that you need to fill in, when defining a new sample.
