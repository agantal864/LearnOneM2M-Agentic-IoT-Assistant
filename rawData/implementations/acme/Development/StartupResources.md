Source: https://acmecse.net/development/StartupResources/

# Start-Up Resources

This article describes the startup process of the CSE, how to import resources, and attribute definitions.

## Initial Resources

During CSE startup and restart it is necessary to import a first set of resources to the CSE. This is done automatically by the CSE by running a script that has the [@init](../ACMEScript-metatags/#init) meta tag set. By default this is the [init.as](https://github.com/ankraft/ACME-oneM2M-CSE/blob/master/acme/init/init.as) script from the [init](https://github.com/ankraft/ACME-oneM2M-CSE/blob/master/acme/init) directory.

Not much validation, access control, or registration procedures are performed when importing resources this way.

See also

The meta tag [@init](../ACMEScript-metatags/#init)

### Adding Mandatory Resources to the CSE

Please note that it is required for a functional CSE deployment to create the CSE's *CSEBase*, the administration *AE*, and a general-access *ACP* resources. Those are created before all other resources, so that the *CSEBase* resource can act as the root for the resource tree, and basic permissions are provided.

### Adding other Resources

An option to import more resources automatically whenever the CSE starts or restarts is to have a script as an event handler for the [onStartup](../ACMEScript-metatags/#onstartup) and [onRestart](../ACMEScript-metatags/#onrestart) events.

These scripts can be added to the [Secondary *init* Directory](../../setup/Running/#secondary-init-directory), which is located in the base directory of the CSE, and from where resources are imported after the primary *init* directory has been processed.

See also

The meta tags [onStartup](../ACMEScript-metatags/#onstartup), [onRestart](../ACMEScript-metatags/#onrestart)  
[Secondary *init* Directory](../../setup/Running/#secondary-init-directory)

### Referencing Configuration Settings

By using macros the initial resources can be kept independent from individual settings.
Most [configuration](../../setup/Configuration-basic/) settings can be added by macro replacement.
For this a given macro name is enclosed by `${...}`, e.g. `${cse.cseID}`.

The following example shows the initial *CSEBase* resource definition from the [init.as](https://github.com/ankraft/ACME-oneM2M-CSE/blob/master/acme/init/init.as) script file:

init.as

```
(import-raw 
    (get-config "cse.originator") ;(1)!
    {"m2m:cb": {
        "ri":   "${ get-config \"cse.resourceID\" }", ;(2)!
        "rn":   "${ get-config \"cse.resourceName\" }",
        "csi":  "${ get-config \"cse.cseID\" }",
        "rr":   true,
        "csz":  [ "application/json", "application/cbor" ],
        "acpi": [ "${ get-config \"cse.cseID\" }/acpCreateACPs" ],
        "poa":  [ "${ get-config \"http.address\" }" ]
    }})
```

1. The `get-config` function is used to retrieve the configuration setting for the CSE's originator.
2. The `${...}` macro is used to replace the configuration setting for the CSE's resource ID in a string.

See also

[Evaluating S-Expressions in Strings and JSON Structures](../ACMEScript/#evaluating-s-expressions-in-strings-and-json-structures)