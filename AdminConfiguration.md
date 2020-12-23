Admin Configuration
===================

The scope of iSkyLIMS was that, it could be used for different organization with different requirements when handling samples in the laboratory.

This flexibility makes that you need to configure iSkyLIMS to adapt it, to get similar to your ways of working.

We are aware that a tool that claims to be commonly used, never will fit at 100% your needs, but this initial configuration iSkyLIMS tries to fit your main requirements.

There are 2 ways to define the configuration that iSkyLIMS uses for sampling tracking control:
*   Using Django admin menu
*   iSkyLIMS Customized forms

For the first one, it is used to define simple information, then in most cases consists only in one field.

For the rest of settings information, a customized form is creating for each specific needs.

## Group and User Definition

To use iSkyLIMS is mandatory to login in the tool. For that purpose, one of the first steps in the configuration is to define the user that can access to iSkyLIMS and the role that each user has in iSkyLIMS.

For each module there are 2 types of roles:
*   Manager. Which it is the responsible for defining the main parameters to be used and the access to see information from normal users.
*   User. Responsible for adding information to their own samples.

A user can only belong to one of these roles and by default when user is created on iSkyLIMS it has no group, meaning that they are normal user, does not have Manager privileges.
### Groups definition

By default, 3 groups (“WetlabManager”, “ServiceManager” and “ClinicManager”) are defined during the installation process.

These are the groups that are used for iSkyLIMS and you do not need add new, but if for any reason you need to rename any of the group, then after login as “admin” user, open your Navigator and type:

```
http://<server_name or IP_address>/admin/auth/group/
```

Use your iSkyLIMS admin credentials to access to the group definition webpage.

![Screenshot](images/admin_configuration/admin_add_group.png)

Type the name of the group and click on the “SAVE” button to apply your changes.

```
IMPORTANT
Do not add any available permissions to the group.
These are the Django permissions to access to database table.
Adding permissions could make unpredictable errors in iSkyLIMS
```

### Centers Definition
Define the centers that will be in your organization using your admin credentials. Open your Navigator and type
```
http://<server_name or IP_address>/admin/django_utils/center
```
![Screenshot](images/admin_configuration/admin_add_center.png)

Type the Center Name and the Acronym used for the Center and click on the SAVE bottom to apply your changes.

Repeat the process for all Center that are applicable in your organization.

### New User Definition
To use iSkyLIMS the user must be logged in, to validate the access credentials.
To create a new user in iSkyLIMS there are 2 possible options:
*   Admin user define the new user.
*   Users register themselves.

For the first option after login with your admin credential, open your Navigator and type
```
http://<server_name or IP_address>/admin/auth/user
```
You will get the Django administration form to create a new user.

![new user definition](images/admin_configuration/admin_add_new_user-1.png)

Type the username and the password

From the Profile section, assign the user to the right Center that his/her belongs to from the available Center that you define in the previous step.

![new user definition](images/admin_configuration/admin_add_new_user-2.png)
Add the additional information and click on the SAVE bottom.
A new page is presented to add additional information
