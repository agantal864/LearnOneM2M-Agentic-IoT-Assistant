Source: https://acmecse.net/development/ThirdPartyLibraries/

# Third Party Components

The following third-party components are used by the ACME CSE.

## Core CSE

* The [cachetools](https://github.com/tkem/cachetools/) package provides caching utilities. MIT License.
* The [cbor2](https://github.com/agronholm/cbor2) package is used to parse and create CBOR serializations. MIT License.
* [InquirerPy](https://github.com/kazhala/InquirerPy/) is a collection of common interactive command-line interfaces. MIT License.
* The [isodate](https://github.com/gweis/isodate) package is used to parse and handle ISO 8601 time, date, and duration. BSD License.
* [kazoo](https://github.com/python-zk/kazoo) is a high-level library to access Zookeeper. Apache License 2.0.
* [rdflib](https://github.com/RDFLib/rdflib) is a Python library for working with RDF. BSD 3-Clause License.
* The CSE uses the [Rich](https://github.com/willmcgugan/rich) text formatter library to format various terminal output. MIT License.
* [shapely](https://github.com/shapely/shapely) is a library for manipulation and analysis of geometric objects. BSD 3-Clause License.

## Connectivity

* For the CoAP protocol binding implementation the ACME CSE uses a fork of the [coapthon3](https://github.com/Tanganelli/CoAPthon3) library. MIT Licsense.  
  The fork is available on GitHub as [CoAPthon3-ACME-CSE](https://github.com/ankraft/CoAPthon3-ACME-CSE) and on PyPi as [coapthon3-acme-cse](https://pypi.org/project/CoAPthon3-ACME-CSE/).
* The CSE uses the [Flask](https://flask.palletsprojects.com/) web framework to service http(s) requests. BSD 3-Clause License.
* [flask-cors](https://github.com/corydolphin/flask-cors/) is a *Flask* extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
* The [paho-mqtt](https://www.eclipse.org/paho/) library provides a client class which enables applications to connect to an MQTT broker. Eclipse Public License 1.0 .
* The CSE uses the [requests](https://requests.readthedocs.io) HTTP Library to send requests vi http. Apache2 License
* [waitress](https://github.com/Pylons/waitress) is a production-quality pure-Python WSGI server with very acceptable performance. ZPL 2.1 License.
* [websockets](https://github.com/python-websockets/websockets) is a library for building WebSocket servers and clients in Python. MIT License.

## Database

* [Psycopg](https://www.psycopg.org) is a PostgreSQL adapter for the Python programming language. GNU Lesser General Public License.
* To store resources the CSE uses the lightweight [TinyDB](https://github.com/msiemens/tinydb) document database. MIT License.

## Text UI

* The [plotext](https://github.com/piccolomo/plotext) library offers functions to plot graphs in the text console. MIT License.
* [pyperclip](https://github.com/asweigart/pyperclip) is a cross-platform Python module for copying and pasting text to the clipboard. BSD-3-Clause License.
* [textual](https://github.com/textualize/textual) is a Rapid Application Development framework for to build textual user interfaces in Python. MIT License.
* [textual-plotext](https://github.com/textualize/textual-plotext) is a plugin for integrating Plotext with Textual. MIT License.

## Web UI

* TreeJS: <https://github.com/m-thalmann/treejs>, MIT License.
* Picnic CSS : <https://picnicss.com>, MIT License.