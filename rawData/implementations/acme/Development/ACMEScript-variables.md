Source: https://acmecse.net/development/ACMEScript-variables/

# ACMEScript - Variables

This section describes the built-in variables that are available in ACMEScript.

## argc

`argc`

Evaluates to the number of elements in [argv](../ACMEScript-functions/#argv). A script called with no arguments still has `argc` set to 1, because the name of the script is always the first element in [argv](../ACMEScript-functions/#argv).

See also

[argv](../ACMEScript-functions/#argv)

Example

```
(if (> argc 2)
    ((log-error "Wrong number of arguments")
    (quit-with-error)))
```

---

## event.data

`event.data`

Evaluates to the payload data of an event. This could be, for example, the string representation in case of an [onKey](../ACMEScript-metatags/#onkey) event.

Note

This variable is only set when the script was invoked by an event.

See also

[event.type](#eventtype)

Example

```
(if (== event.type "onKey")     ;; If the event is "onKey"
    (print "Key:" event.data))  ;; Print the pressed key
```

---

## event.type

`event.type`

Evaluates to the type of an event. This could be, for example, the value *"onKey"* in case of an [onKey](../ACMEScript-metatags/#onkey) event.

Note

This variable is only set when the script was invoked by an event.

See also

[event.data](#eventdata)

Example

```
(if (== event.type "onKey")     ;; If the event is "onKey"
    (print "Key:" event.data))  ;; Print the pressed key
```

---

## notification.originator

`notification.originator`

The `notification.originator` variable is set when a script is called to process a notification request.

It contains the notification's originator.

Example

```
(print notification.originator)
```

---

## notification.resource

`notification.resource`

The `notification.resource` variable is set when a script is called to process a notification request.

It contains the notification's JSON body.

Example

```
(print notification.resource)
```

---

## notification.uri

`notification.uri`

The `notification.uri` variable is set when a script is called to process a notification request.

It contains the notification's target URI.

Example

```
(print notification.uri)
```

---

## tui.autorun

`tui.autorun`

Evaluates to *true* if the script was started as an "autorun" script. This is the case when the [@tuiAutoRun](../ACMEScript-metatags/#tuiautorun) meta tag is set in a script.

See also

[tuiAutoRun](../ACMEScript-metatags/#tuiautorun)

Note

This variable is only set when the script is run from the text UI.

Example

```
(if (is-defined 'tui.autorun)     ;; If the variable is defined
    (if (== tui.autorun true)     ;; If the script is an autorun script
        (print "Autorun: True")))  ;; Print a message
```

---

## tui.theme

`tui.theme`

Evaluates to the state of the current theme of the text UI. This can either be the values *light* or *dark*.

Example

```
(print "Theme: " tui.theme)  ;; Print the theme name
```