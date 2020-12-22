# Admin Configuration

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

Type the name of the group and click on the “SAVE” button to apply your changes.
