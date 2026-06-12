=============================
Code Craft AI Data Profiles
=============================

The ``codecraftai-dataprofiles`` package provides a catalogue of connection-profile classes for the data stores that codecraftai-based applications and tests talk to. Its job is to let callers declare a named profile once (in configuration) and then look it up at runtime, rather than scattering hostnames, ports, and credentials through the codebase. The package complements ``codecraftai-credentials`` and is consumed by ``codecraftai-configuration`` and other packages that open data-store connections.

Highlights
==========

- ``BaseDataProfile`` root with specialised subclasses for common transports and backends.
- Generic transport profiles: ``DatabaseBasicSocketProfile`` and ``DatabaseBasicTcpProfile``.
- Concrete profiles for ``CouchDbProfile``, ``MongoDBAtlasProfile``, and ``SnowflakeProfile``.
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
