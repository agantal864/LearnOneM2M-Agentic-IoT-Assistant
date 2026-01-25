Source: https://acmecse.net/development/ACMEScript-metatags/

# ACMEScript - Meta Tags

Meta tags are special commands in a script that are not executed during the runtime of a script, but describe certain capabilities of the script or give, for example, the script a name or provide instructions when a script should be executed.

Meta tags are keywords that start with an at-character `@`. They can appear anywhere in a script file on a single line, but it is recommended to collect them either at the start or the end of a script.

Important

Meta tag names are case sensitive.

## Accessing Meta Tags

Meta tags are added as constants to the script's environment and are prefixed with `meta.`.
They can be accessed like any other environment variable, for example:

Accessing a Meta Tag

```
(if (is-defined 'meta.name)            ;; note the quote in front of meta.name to prevent evaluation
    (print "Script name:" meta.name))  ;; prints the script's name
```

## Basic Meta Tags

### @at

`@at <cron pattern>`

The `@at` meta tag specifies a time / date pattern when a script should be executed. This pattern follows the Unix [crontab](https://crontab.guru/crontab.5.html) pattern.

A crontab pattern consists of the following six fields:

`second minute hour dayOfMonth month dayOfWeek year`

Each field is mandatory and must comply to the following values:

* `*` : any valid integer number for that field, or
* `*/<number>` : step, or
* `<number>-<number` : range, or
* `value[,value]*` : value is either a number, a step, or a range

Examples

```
;; Run a script every 5 minutes
@at 0 */5 * * * * *

;; Run a script every Friday at 2:30 am
@at 0 30 2 * * 4 *
```

---

### @description

`@description <string>`

A short one-line description of a script's purpose. This is used, for example, for the console's script catalog.

A description must be a single line, but may include line breaks (i.e. `\n` characters). A description may also be formatted as markdown. This is then correctly displayed in the Text UI.

See also

[@usage](#usage)

Examples

```
@description The purpose of this script is to demonstrate the @description meta tag

@description # Markdown header\n\nFormatted **Markdown** text.
```

---

### @filename

`@filename <string>`

This meta tag is for internal use. It contains the script's full filename when read by the script manager.

---

### @hidden

`@hidden`

This meta tag indicates that a script will not be listed in the console's script catalog.

Example

```
@hidden
```

---

### @init

`@init`

This meta tag indicates that the script will be executed during the CSE's startup and restart. It is used to initialize the CSE and creates the basic resources.

Important

Only one script can have this meta tag set.

See-also

[@onRestart](#onrestart), [@onShutdown](#onshutdown), [@onStartup](#onstartup)

Example

```
@init
```

---

### @name

`@name <string>`

This meta tag assigns a name to a script. This name is used for identifying the script, for example when running a script from the console.

See-also

[@uppertester](#uppertester)

Example

```
@name exampleScript
```

---

### @onKey

`@onKey <key>`

With this meta tag a script registers to a key-press event of the console interface. If the key is pressed then the script is run. The event and the key are passed as the environment variables [event.type](../ACMEScript-variables/#eventtype) and [event.data](../ACMEScript-variables/#eventdata), respectively.

The keys may be normal ASCII characters or a function key. Please consult the console's [supported function key table](../../setup/Console/#supported-function-keys) for the function key's names. Note, that not all function keys are available on all OS platforms.

A script can only register for a single key event.

Example

```
;; Run the script when the '9' key is pressed
@onkey F9

(print (event.data))
```

---

### @onNotification

`@onNotification <URI: acme://someID>`

With this meta tag a script acts as a handler for a notification request from the CSE.

The ACME URL scheme "acme://<identifier>" is used to define a URI that is targeting the script. Such a URI must be used in either the *notificationURI* attribute of a subscription resource, or the *pointOfAccess* of an AE.

When a notification is received and the handler script is run the following variables are set:

* [notification.originator](../ACMEScript-variables/#notificationoriginator) : The notification's originator
* [notification.resource](../ACMEScript-variables/#notificationresource) : The notification's resource
* [notification.uri](../ACMEScript-variables/#notificationuri) : The notification's target URI

Example

```
;; Run the script when the 'acme://aNotification' notificastion is received
@onNotification acme://aNotification

(print (notification.resource))
```

---

### @onRestart

`@onRestart`

This meta tag indicates that the script will be executed just after the CSE restarted, for example after a reset.

If multiple scripts have this meta tag set then they will run in random order.

See-also

[@init](#init), [@onShutdown](#onshutdown), [@onStartup](#onstartup)

Example

```
@onRestart
```

---

### @onShutdown

`@onShutdown`

This meta tag indicates that the script will be executed just before the CSE shuts down.

If more than one script have this meta tag set then they will run in random order.

See-also

[@init](#init), [@onRestart](#onrestart), [@onStartup](#onstartup)

Example

```
@onShutdown
```

---

### @onStartup

`@onStartup`

This meta tag indicates that the script will be executed just after the CSE started. It will be run only after start up, but not when the CSE restarted. If more than one script have this meta tag set then they will be run in random order.

See-also

[@init](#init), [@onRestart](#onrestart), [@onShutdown](#onshutdown)

Example

```
@onStartup
```

---

### @prompt

`@prompt <prompt text>`

A script with this meta tag will present a prompt before it is executed and ask a user for input. The result is then passed on as [script arguments](../ACMEScript-loading/#script-arguments).

This meta tag should only be used when human interaction can be ensured. Running a script with this meta tag scheduled or unattended will cause the script to wait forever for user input.

Example

```
@prompt Enter some arguments
```

---

### @timeout

`@timeout <seconds>`

This meta tag sets a timeout after which the script execution is terminated with a *timeout* error

Note, that the script may terminate some time after the timeout when a script command takes longer to run.

Example

```
@timeout 10
```

---

### @tuiNoExecute

`@tuiNoExecute`

This meta tag disables the `Execute` button for this script in the Text UI's *Tools* section.

Example

```
@tuiNoExecute
```

---

### @uppertester

`@uppertester`

This meta tag indicates that a script is runnable through the [Upper Tester Interface](../../setup/Operation-uppertester/). In this case the script name specified by the [@name](#name) meta tag is used as the command name.

Scripts without this meta tag cannot be run through the Upper Tester interface.

See-also

[@name](#name), [Upper Tester Integration](../ACMEScript-uppertester/), [Upper Tester Interface](../../setup/Operation-uppertester/)

Example

```
@uppertester
```

---

### @usage

`@usage <string>`

This meta tag provides a short help message for a script's usage.

See-also

[@description](#description)

Example

```
@usage exampleScript <a parameter> <another parameter>
```

---

## Text UI

### @category

`@category <string>`

A category name for the script. This is used, for example, in the text UI tools to group scripts.

See-also

[@name](#name), [@tuiTool](#tuitool)

Example

```
@categoy System
```

---

### @tuiAutoRun

`@tuiAutoRun [<interval:positive float>]`

This meta tag, when present, configures a script that it is run automatically when it is selected in the *Tools* overview in the text UI.

Without the optional *interval* argument the script runs only once when it is selected.

When the *interval* argument is present it must be a positive float number that specifies the interval, in seconds, after which the script is repeatedly run again.

If this meta tag is present, with or without the *interval* argument, the environment variable `tui.autorun` is set to *true* when the script is run.

Example

```
@tuiAutoRun 10
```

---

### @tuiExecuteButton

`@tuiExecuteButton [<label:string>]`

This meta tag configures the script's `Execute` button of the text UI.

The following configurations are possible:

* Not present in a script: The button displays the default text "Execute".
* Present in a script with an argument: The argument is used for the button's label.
* Present in a script with no argument: The button is hidden.

Example

```
@tuiExecuteButton A Label
```

---

### @tuiInput

`@tuiInput [<label:string>]`

This meta tag adds an input field to text UI. Text entered in this field is passed as
arguments to the script that can be access using the [argv](../ACMEScript-functions/#argv) function.

The following configurations are possible:

* Not present in a script or without a label: No input field is added.
* Present in a script with an argument: The argument is used for the input field's label.

Example

```
@tuiInput A Label
```

---

### @tuiSortOrder

`@tuiSortOrder <priority:number>`

With this meta tag one can specify the sort order of a script in the Text UI's *Tools* section.

The default sort order is 500. Scripts with a lower priority number are listed first. Scripts with the same priority are sorted alphabetically.

Example

```
@tuiSortOrder 100
```

---

### @tuiTool

`@tuiTool`

This meta tag categorizes a script as a tool. Scripts marked as *tuiTools* are listed in the Text UI's *Tools* section.

Example

```
@tuiTool
```