Source: https://acmecse.net/howtos/EnablingSyntaxHighlighting/

# Enabling Syntax Highlighting in the Resource Text Editor

The ACME CSE supports syntax highlighting in the text UI by default, but not for the resource text editor. This feature is provided by the *textual[syntax]* package. To install it, run the following commands:

Install Syntax Highlighting Package

```
python -m pip uninstall textual
python -m pip install textual[syntax]
```

Note

The *textual[syntax]* package is not required for the basic functionality of the ACME CSE. It is only needed if you want to use the syntax highlighting feature in the resource text editor.

This package may not be available for all platforms. If you encounter any issues, please use the normal installation without the *syntax* feature.

After installing the package, you can enable syntax highlighting in the resource text editor. To do this, set the configuration setting [enableTextEditorSyntaxHighlighting](../../setup/Configuration-uis/#text-ui) to *True* in the local *acme.ini* file:

Enable Syntax Highlighting for the resource text editor

```
[textui]
enableTextEditorSyntaxHighlighting = True
```