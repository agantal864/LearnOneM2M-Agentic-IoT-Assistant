Source: https://acmecse.net/development/Overview/

# Overview

This article provides an overview of the ACME CSE's architecture, components, and database schemas.

## Components

The ACME CSE is divided into several components. The following diagram shows the components and their relationships.

UML Component Diagram of the ACME CSE

## Resource Class Hierarchy

The CSE's resources are implemented as classes. The following diagram shows the class hierarchy of the supported resource types.

UML Class Diagram of the Supported oneM2M Resources Types

## Database Schemas

Database Schemas of the ACME CSE

If the *tinyDB* database mode is used the database files are stored in the `data` sub-directory of the CSE's working directory.

The database used by the CSE is [TinyDB](https://github.com/msiemens/tinydb) which uses plain JSON files for storing the data. Some files only contain a single data table while other contain multiple tables.

The filenames include the *CSE-ID* of the running CSE, so if multiple CSEs are running and are using the same data directory then they won't interfere with each other. The database files are copied to a *backup* directory at CSE startup.

Some database tables duplicate attributes from actual resources, e.g. in the *subscription* database. This is mainly done for optimization reasons in order to prevent a retrieval and instantiation of a full resource when only a few attributes are needed.