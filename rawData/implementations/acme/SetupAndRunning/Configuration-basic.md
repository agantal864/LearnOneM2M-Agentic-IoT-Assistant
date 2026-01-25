Source: https://acmecse.net/setup/Configuration-basic/

# Configuration - Basic Settings

The CSE is configured using the configuration file `acme.ini`. This file contains all necessary settings for the CSE to run.
These settings are used throughout the configuration settings using [interpolation](../Configuration-introduction/#settings-interpolation).

When creating the configuration file, it is recommended to use the [interactive procedure](../Installation/#guided-onboarding) to generate a file with basic configuration settings. [1](#fn:1)

## Basic Configuration

**Section: `[basic.config]`**

These are the general settings for the CSE.
Some settings are mandatory, others are optional. This depends on the type of CSE to run.

These basic settings are used in the [default configuration file](../Configuration-introduction/#the-acmeini-configuration-file) and
can be set by using the [interactive procedure](../Installation/#guided-onboarding) or by editing the configuration file directly.

| Setting | Description | Optional | Default |
| --- | --- | --- | --- |
| cseType | The type of CSE to run. Allowed values: `IN`, `MN`, `ASN` | No |  |
| cseID | The CSE-ID of the CSE. This is a unique identifier for the CSE. This ID provided here must not start with `/` and must not contain a further `/` or white space. | No |  |
| serviceProviderID | The ID of the service provider for the CSE. This is a unique identifier for the service provider. This ID provided here must not start with `//` and must not contain a further `/` or white space. | yes | acme.example.com |
| cseName | The resource name of the CSE. | No |  |
| adminID | The ID for the CSE's admin originator. | No |  |
| networkInterface | The network interface to use. | Yes | 0.0.0.0 |
| cseHost | The IP address of the CSE. | No |  |
| httpPort | The port for the HTTP server. | No |  |
| registrarCseID | The CSE-ID of the registrar CSE. This setting is mandatory for *cseType* = *MN* and *ASN*. | No[2](#fn:2) |  |
| registrarCseName | The name of the registrar CSE. This setting is mandatory for *cseType* = *MN* and *ASN*. | No[2](#fn:2) |  |
| registrarCseHost | The IP address of the registrar CSE. This setting is mandatory for *cseType* = *MN* and *ASN*.. | Yes | [${hostIPAddress}](../Configuration-introduction/#built-in-settings) |
| registrarCsePort | The port of the registrar CSE. This setting is mandatory for *cseType* = *MN* and *ASN*. | No[2](#fn:2) |  |
| databaseType | The type of database to use. Allowed values: `memory`, `tinydb`, `postgresql` | No |  |
| logLevel | The log level for the CSE. Allowed values: `debug`, `info`, `warning`, `error`, `off` | Yes | debug |
| consoleTheme | The theme for the console and text UI. Allowed values: `light`, `dark` | Yes | dark |
| secret | The secret for the CSE. This is used for seeding hash functions and encryption. The default value is 'acme'. | Yes | acme |

In addition to the settings in this table, the [built-in configuration settings](../Configuration-introduction/#built-in-settings)
and [environment variables](../Configuration-introduction/#environment-variables) can be used in the configuration.

---

1. You can add further configurations if necessary by copying sections and settings from [acme.ini.default](https://github.com/ankraft/ACME-oneM2M-CSE/blob/master/acme/init/acme.ini.default). [↩](#fnref:1 "Jump back to footnote 1 in the text")
2. This setting is mandatory for *cseType* = *MN* and *ASN*, and it is not required for *cseType* = *IN*. [↩](#fnref:2 "Jump back to footnote 2 in the text")[↩](#fnref2:2 "Jump back to footnote 2 in the text")[↩](#fnref3:2 "Jump back to footnote 2 in the text")