dbt
===

dbt introduction
----------------

dbt (data build tool) is a framework for analytics engineering. It lets you write
data transformations in SQL and Jinja, version them in Git, test data quality, and
build documented data models as part of repeatable pipelines.

Use Exasol with dbt
-------------------

You can use Exasol as a dbt target platform through the community adapter
`dbt-exasol <https://docs.getdbt.com/docs/core/connect-data-platform/exasol-setup>`_.
This page shows the end-to-end setup so you can start building with dbt on Exasol.

Support status
--------------

* Maintainer: Community
* Adapter package: `dbt-exasol <https://docs.getdbt.com/docs/core/connect-data-platform/exasol-setup>`_
* Supported dbt Core: 1.8.0+
* Minimum Exasol version: 6.x
* dbt Cloud: not supported

Prerequisites
-------------

Before you start, make sure you have:

* Access to an Exasol cluster (host and port)
* Exasol credentials (username/password or OpenID token)
* A local Python environment

Install dbt Core and the Exasol adapter
---------------------------------------

Starting with dbt Core 1.8, installing an adapter no longer installs ``dbt-core``
automatically. Install both explicitly:

.. code-block:: bash

    python -m pip install --upgrade pip
    python -m pip install dbt-core dbt-exasol

Create a new dbt project
------------------------

.. code-block:: bash

    dbt init my_exasol_project

This creates a project directory and a profile entry in ``~/.dbt/profiles.yml``.

Configure your Exasol profile
-----------------------------

Set up ``~/.dbt/profiles.yml`` with one of the following authentication methods.

Username and password
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    my_exasol_project:
      target: dev
      outputs:
        dev:
          type: exasol
          threads: 4
          dsn: HOST:PORT
          user: USERNAME
          password: PASSWORD
          dbname: DB_NAME
          schema: SCHEMA_NAME

OpenID authentication (Exasol SaaS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use either ``access_token`` or ``refresh_token`` (not both).
For Exasol SaaS, set ``encryption: True``.

.. code-block:: yaml

    my_exasol_project:
      target: dev
      outputs:
        dev:
          type: exasol
          threads: 4
          dsn: HOST:PORT
          user: USERNAME
          access_token: YOUR_ACCESS_TOKEN
          # refresh_token: YOUR_REFRESH_TOKEN
          dbname: DB_NAME
          schema: SCHEMA_NAME
          encryption: True

Optional connection parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can add the following output-level parameters:

* ``connection_timeout`` (pyexasol default)
* ``socket_timeout`` (pyexasol default)
* ``query_timeout`` (pyexasol default)
* ``compression`` (default: ``False``)
* ``encryption`` (default: ``True``)
* ``validate_server_certificate`` (default: ``True``)
* ``protocol_version`` (default: ``v3``)
* ``row_separator`` (default: ``CRLF`` on Windows, ``LF`` otherwise)
* ``timestamp_format`` (default: ``YYYY-MM-DDTHH:MI:SS.FF6``)

TLS and certificate validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When ``encryption=True``, certificate validation is enabled by default.

For development with self-signed certificates, you can:

* Set ``validate_server_certificate: False`` (not recommended for production)
* Use a certificate fingerprint in DSN: ``myhost/FINGERPRINT:8563``
* Skip certificate validation in DSN: ``myhost/nocertcheck:8563`` (testing only)

Validate your setup
-------------------

Run these commands in your dbt project directory:

.. code-block:: bash

    dbt debug
    dbt parse

If ``dbt debug`` succeeds, your profile and connection are valid.

Build your first model
----------------------

Create ``models/stg_orders.sql``:

.. code-block:: sql

    select
        order_id,
        customer_id,
        order_date,
        order_total
    from raw.orders

Run and test:

.. code-block:: bash

    dbt run --select stg_orders
    dbt test --select stg_orders

Exasol-specific model configuration
-----------------------------------

Incremental strategies
^^^^^^^^^^^^^^^^^^^^^^

`dbt-exasol <https://docs.getdbt.com/docs/core/connect-data-platform/exasol-setup>`_ supports:

* ``append`` (default when ``unique_key`` is not set)
* ``delete+insert`` (default when ``unique_key`` is set)
* ``merge``
* ``microbatch``

Distribution, partitioning, and primary keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For ``table`` and ``incremental`` models (`dbt-exasol <https://docs.getdbt.com/docs/core/connect-data-platform/exasol-setup>`_ 1.8.1+), you can tune table layout:

* ``partition_by_config``: partition by one or more columns
* ``distribute_by_config``: distribute by a column
* ``primary_key_config``: define primary key columns



Model contracts
^^^^^^^^^^^^^^^

Exasol supports these dbt model contract constraints:

* ``not_null``: supported
* ``primary_key``: supported
* ``foreign_key``: supported
* ``check``: not supported
* ``unique``: not supported

Important limitations and behavior
----------------------------------

* ``materialized='materialized_view'`` is not supported in Exasol.
* Clone operations are not supported.
* Empty strings are treated as ``NULL`` in Exasol (important for unit test fixtures).
* Unit tests that rely on sources in a different database are not supported.
* ``LISTAGG``, ``MEDIAN``, and ``PERCENTILE_CONT`` may fail in CTE-based unit test fixtures.

References
----------

* `dbt Exasol setup <https://docs.getdbt.com/docs/core/connect-data-platform/exasol-setup>`_
* `dbt Exasol configurations <https://docs.getdbt.com/reference/resource-configs/exasol-configs>`_
* `Adapter repository on GitHub <https://github.com/exasol/dbt-exasol>`_
