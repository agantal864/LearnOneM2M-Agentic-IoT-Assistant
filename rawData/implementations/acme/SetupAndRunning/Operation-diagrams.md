Source: https://acmecse.net/setup/Operation-diagrams/

# Operation - Infrastructure Diagrams

## Resource Tree and Deployment Infrastructure Diagram

The CSE can generate a diagram with an overview about the hosted resource tree and the current deployment infrastructure of remote CSEs.
This is available by sending a GET request as follows:

GET request to retrieve the diagram script

```
curl localhost:8080/__structure__
```

This returns a PlantUML diagram script that can be rendered with the [PlantUML](https://plantuml.com) tool. The diagram shows the resource tree and the deployment infrastructure of remote CSEs. The diagram can be used to get an overview of the current deployment and to identify potential issues.

Example Deployment Diagram

An optional argument *lvl=<int>* can be provided to the URL to limit the number if levels of the resource tree in the diagram.

This feature must be enabled in the configuration file under [`[server.http].enableStructureEndpoint`](../Configuration-http/#general-settings).

Attention

Enabling this feature might reveal sensitive data. It should be disabled if not used.

When enabled the http server creates an additional endpoint */\_\_structure\_\_*. A GET request to that endpoint returns a diagram description in [PlantUML](https://plantuml.com) format that can be transformed in images with various tools (for example, with the online editor on the PlantUML website).

A similar text representation of the resource tree only can be retrieved from the endpoint */\_\_structure\_\_/text* .

GET Request to retrieve the text representation of the resource tree

```
curl localhost:8080/__structure__/text
...

cse-in -> m2m:cb (csi=/id-in) | ri=id-in
├── acpCreateACPs -> m2m:acp | ri=acpCreateACPs
├── CAdmin -> m2m:ae | ri=CAdmin
...
```