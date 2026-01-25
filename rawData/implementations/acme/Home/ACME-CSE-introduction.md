Source: https://acmecse.net/home/ACME-CSE-introduction/

# A Short Introduction to the ACME oneM2M CSE

The **ACME oneM2M CSE** (*ACME CSE* for short) is an implementation of a *Common Service Entity* that supports a subset of the [oneM2M IoT standard](../oneM2M-introduction/). It provides a useful and rich implementation for educational purposes and small trials.

The goal is to provide an easy to [install](../../setup/Installation/) and [run](../../setup/Running/) oneM2M CSE. The ACME CSE is written in Python, and can be installed and run with a few commands almost everywhere where the Python runtime environment is available. By default, the implementation uses a simple file-based document database for data storage that is suitable for small installations. For more sophisticated deployments, the ACME CSE can connect to a PostgreSQL database.

The ACME CSE also offers a rich text-based user interface that runs directly inside an OS's terminal console and provides a convenient way to inspect and work with resources, requests, and status information. This UI is especially useful when running the CSE on a remote server or in a Docker container.
  
  
A more basic console UI is also available. It is the default UI when running the ACME CSE in a terminal console, and which is better suited to show log and debug output.

Text UI of the ACME CSE

Though the ACME CSE may not yet support all parts of the standard, the [support for more oneM2M resource types and functionalities](../Supported/) is growing as development continues.

The project and its source code is available on [GitHub](https://github.com/ankraft/ACME-oneM2M-CSE).