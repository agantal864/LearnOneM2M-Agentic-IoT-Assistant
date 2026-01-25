Source: https://acmecse.net/setup/Running/

# Running

This article describes how to start and stop the CSE, and how to use the command console interface.

## Running the CSE

You can start the CSE by running it from the command line. This is the simplest way to start the ACME CSE.

Package installationManual Installation

Starting the ACME CSE

```
acmecse
```

Starting the ACME CSE as a module

```
python3 -m acme
```

The current working directory is used as the base directory for the CSE and the *acme.ini* [configuration file](../Configuration-introduction/#the-acmeini-configuration-file) must be in the same directory. An [interactive configuration process](../Installation/#guided-onboarding) is started if the configuration file is not found.

### Different Configuration File

The CSE can also be started with a different configuration file:

Package InstallationManual Installation

Starting the ACME CSE with a different configuration file

```
acmecse --config <filename>
```

Starting the ACME CSE with a different configuration file

```
python3 -m acme --config <filename>
```

The current working directory is still the base directory for the CSE and the configuration file is still expected to be located in this directory.

### Different Base Directory

The CSE can also be started with a different base directory:

Package InstallationManual Installation

Starting the ACME CSE with a different base directory

```
acmecse -dir <directory>
```

Starting the ACME CSE with a different base directory

```
python3 -m acme -dir <directory>
```

This will use the specified directory as the root directory for runtime data such as *data*, *logs*, own provided *plugins*, and *temporary* files. The configuration file *acme.ini*is expected to be in the specified directory, or it will be created there if it does not exist.

The default base directory, if not specified, is the current working directory.

### Secondary *init* Directory

A base directory may also host a secondary *init* directory that is used for importing further resources such as attribute definitions and scripts. Resources in this directory are automatically imported when the CSE starts, and processed after the resources in the primary *init* directory have been imported and processed.

## Command Line Arguments

The ACME CSE provides a number of command line arguments that will override the respective settings from the configuration file. They can be used to change certain CSE behaviours without changing the configuration file.

| Command Line Argument | Description |
| --- | --- |
| -h, --help | Show a help message and exit. |
| --coap, --no-coap | Enable or disable the CoAP binding. This overrides the [coap.enable](../Configuration-coap/#general-settings) configuration setting. |
| --config <filename> | Specify a configuration file that is used instead of the default (*acme.ini*) one. |
| --config-zk-host | Specify the Zookeeper host name. This together with the `--config-zk-root` option is used to enable the CSE to use Zookeeper for remote configuration. |
| --config-zk-port | Specify the Zookeeper port (default: 2181) |
| --config-zk-root | Specify the Zookeeper root node (default: None). This should be unique, for example the the CSE ID |
| --base-directory <directory>, -dir <directory> | Specify the root directory for runtime data such as data, logs, and temporary files. |
| --dark, --light | Enable *dark* or *light* theme for the console and text UI. |
| --db-directory <directory> | Specify the directory where the CSE's data base files are stored. |
| --db-reset | Reset and clear the database when starting the CSE. |
| --db-type | Specify the DB's storage type. This overrides the [database.type](../Configuration-database/#general-settings) configuration setting. |
| --headless | Operate the CSE in headless mode. This disables almost all screen output and also the build-in console interface. |
| --http, --https | Run the CSE with http or https server. This overrides the [useTLS](../Configuration-http/#security) configuration setting. |
| --http-wsgi | Run CSE with http WSGI support. This overrides the [http.wsgi.enable](../Configuration-http/#wsgi) configuration setting. |
| --http-address <server URL> | Specify the CSE's http server URL. This overrides the [address](../Configuration-http/#general-settings) configuration setting. |
| --http-port <http port> | Specify the CSE's http server port. This overrides the [address](../Configuration-http/#general-settings) configuration setting. |
| --init-directory <directory> | Specify the import directory. This overrides the [resourcesPath](../Configuration-cse/#general-settings) configuration setting. |
| --log-level | Set the log level, or turn logging off. This overrides the [level](../Configuration-logging/#general-settings) configuration setting. |
| --mqtt, --no-mqtt | Enable or disable the MQTT binding. This overrides the [mqtt.enable](../Configuration-mqtt/#general-settings) configuration setting. |
| --network-interface <ip address | Specify the network interface/IP address to bind to. This overrides the [listenIF](../Configuration-http/#general-settings) configuration setting. |
| --print-config, -pc | Print the configuration during startup to the "info" level log. |
| --remote-cse, --no-remote-cse | Enable or disable remote CSE connections and checking. This overrides the [enableRemoteCSE](../Configuration-cse/#general-settings) configuration setting. |
| --statistics, --no-statistics | Enable or disable collecting CSE statistics. This overrides the [enable](../Configuration-cse/#statistics) configuration setting. |
| --textui | Run the CSE's text UI after startup. |
| --ws, --no-ws | Enable or disable the WebSocket binding. This overrides the [websocket.enable](../Configuration-ws/#general-settings) configuration setting. |

### Reading Command Line Arguments from a File

Command line arguments can also be read from a file. This is useful when you have a large number of arguments that you want to pass to the CSE. The file should contain one argument per line. Empty lines and lines starting with a hash sign (`#`) are ignored.

**Example:**

argsfile.txtRuning the CSE with arguments from an arguments file

The content of the arguments file 'argsfile.txt'

```
--db-type memory

# enable the http server
--http

# enable the mqtt server
--mqtt

# set the log level to debug
--log-level debug
```

Runing the CSE with arguments from an arguments file

```
acmecse @argsfile.txt
```

## Stopping the CSE

The CSE can be stopped by pressing pressing the uppercase *Q* key or *CTRL-C* **once** on the command line.[1](#fn:1)

Please note, that the shutdown might take a moment (e.g. gracefully terminating background processes, writing database caches, sending notifications etc).

Warning

Being impatient and hitting *CTRL-C* twice might lead to data corruption.

---

1. You can configure this behavior with the [[cse.console].confirmQuit](../Configuration-uis/#console) configuration setting. [↩](#fnref:1 "Jump back to footnote 1 in the text")