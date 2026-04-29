<<<<<<< Updated upstream
=====================
automojo-dataprofiles
=====================

Automation Mojo - Data Profiles Package

Overview
========
automojo-dataprofiles is a core component of the Automation Mojo technology stack. It provides robust, reusable foundation code designed to enable and orchestrate complex software automation tasks.

Installation
============
Using Poetry:

.. code-block:: bash

    poetry add automojo-dataprofiles

Development
===========
This repository provides a standard Poetry environment.

1. Activate virtual environment:
   Run `poetry shell` and `poetry install`
2. Test Execution:
   Run `poetry run pytest`

References
==========
- `User Guide <userguide/userguide.rst>`
- `Coding Standards <userguide/10-00-coding-standards.rst>`
=======
=============================
Automation Mojo Data Profiles
=============================

The ``automojo-dataprofiles`` package provides a catalogue of connection-profile classes for the data stores that automojo-based applications and tests talk to. Its job is to let callers declare a named profile once (in configuration) and then look it up at runtime, rather than scattering hostnames, ports, and credentials through the codebase. The package complements ``automojo-credentials`` and is consumed by ``automojo-configuration`` and other packages that open data-store connections.

Highlights
==========

- ``BaseDataProfile`` root with specialised subclasses for common transports and backends.
- Generic transport profiles: ``DatabaseBasicSocketProfile`` and ``DatabaseBasicTcpProfile``.
- Concrete profiles for ``CouchDBProfile``, ``MongoDBAtlasProfile``, and ``SnowflakeProfile``.
- ``DataProfileManager`` and the ``wellknown.py`` singleton for lookup by name.

Repository Structure
====================

- ``development/`` - Runtime environment scripts.
- ``repository-setup/`` - Repository homing and setup scripts.
- ``source/packages/`` - Package source code.
- ``source/tests/`` - ``unittest``-based tests.
- ``specs/`` - Requirements, design, and task documentation.
- ``userguide/`` - Standards, conventions, and documentation.

Environment Setup
=================

When working in a Codex container:

.. code-block:: bash

   ./development/setup-agent-container

For local development:

.. code-block:: bash

   ./repository-setup/rehome-repository
   ./development/setup-envrionment

Running Tests
=============

Activate the virtual environment:

.. code-block:: bash

   source .venv/bin/activate

Run ``unittest`` tests:

.. code-block:: bash

   python -m unittest discover -s source/tests -p "test_*.py"

Standards and Conventions
=========================

- Naming conventions: ``userguide/10-02-naming-conventions.rst``
- Code organization: ``userguide/10-01-code-organization.rst``
- Coding standards: ``userguide/10-00-coding-standards.rst``

Additional Resources
====================

- User guide entry point: ``userguide/userguide.rst``
- Design documentation: ``specs/design.md``
- Requirements: ``specs/requirements.md``
>>>>>>> Stashed changes
