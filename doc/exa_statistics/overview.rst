========
Overview
========

What is EXA_STATISTICS
=======================

``EXA_STATISTICS`` is a system schema built into every Exasol database. It continuously collects
statistics about SQL execution, hardware resource usage, storage, and user sessions. Data is updated
automatically every minute and is immediately available for querying — no configuration required.

The schema covers four functional areas:

* **SQL Activity** — historical record of every executed statement
* **System Monitor** — CPU, memory, I/O, and network metrics over time
* **Database Size** — storage volume, compression ratios, and RAM recommendations
* **Audit** — full audit trail of SQL statements and user sessions

Namespace Integration
=====================

``EXA_STATISTICS`` and ``SYS`` are automatically integrated into Exasol's namespace. You can query
statistical tables directly without specifying the schema name:

.. code-block:: sql

   -- Both are equivalent:
   SELECT * FROM EXA_SQL_LAST_DAY;
   SELECT * FROM EXA_STATISTICS.EXA_SQL_LAST_DAY;

.. _exa-statistics-access-control:

Access Control
==============

Most statistical tables are readable by all database users. Tables with ``DBA`` in their name
contain sensitive data and require the ``SELECT ANY DICTIONARY`` system privilege.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Table Group
     - Required Privilege
   * - ``EXA_SQL_*``, ``EXA_MONITOR_*``, ``EXA_DB_SIZE_*``
     - None — any connected user
   * - ``EXA_DBA_AUDIT_*``
     - ``SELECT ANY DICTIONARY``

To grant the privilege to a user:

.. code-block:: sql

   GRANT SELECT ANY DICTIONARY TO my_user;

Aggregation Levels
==================

Each metric category is available at multiple time granularities:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Suffix
     - Description
   * - ``_LAST_DAY``
     - Rolling 24-hour window — one row per measurement interval
   * - ``_HOURLY``
     - Aggregated per hour
   * - ``_DAILY``
     - Aggregated per calendar day
   * - ``_MONTHLY``
     - Aggregated per calendar month

Use ``_LAST_DAY`` tables for real-time investigation and the aggregated tables for trend analysis
and capacity planning.

Time Zone
=========

All timestamps in ``EXA_STATISTICS`` are stored in the database's configured time zone
(``DBTIMEZONE``). To check your current setting:

.. code-block:: sql

   SELECT DBTIMEZONE;

Refreshing Statistics
=====================

Statistics are updated automatically every minute. To force an immediate refresh:

.. code-block:: sql

   FLUSH STATISTICS;
   COMMIT;

.. note::
   Open a new transaction after flushing to see the latest data reflected in your queries.

**Further reading:** `Statistical System Tables <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical_system_tables.htm>`_ · `FLUSH STATISTICS <https://docs.exasol.com/db/latest/sql/flush_statistics.htm>`_
