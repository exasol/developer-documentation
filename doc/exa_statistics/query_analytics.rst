===========================
Query Performance Analytics
===========================

The ``EXA_SQL_*`` tables record every SQL statement that Exasol successfully compiles and executes.
Use them to identify slow queries, measure CPU consumption, and understand workload patterns over time.

EXA_SQL_LAST_DAY
================

Contains one row per executed statement within the rolling 24-hour window. Key columns:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Description
   * - ``SESSION_ID``
     - Identifier of the session that ran the statement
   * - ``STMT_ID``
     - Statement identifier within the session
   * - ``COMMAND_NAME``
     - SQL command type (e.g., ``SELECT``, ``INSERT``, ``COMMIT``)
   * - ``EXECUTION_MODE``
     - How the statement was handled — see Execution Modes below
   * - ``DURATION``
     - Execution time in seconds
   * - ``CPU``
     - CPU usage percentage during execution
   * - ``SUCCESS``
     - ``TRUE`` if the statement completed without error
   * - ``START_TIME`` / ``STOP_TIME``
     - Execution window timestamps
   * - ``TEMP_DB_RAM_PEAK``
     - Peak temporary memory used (bytes)

.. note::
   ``EXA_SQL_LAST_DAY`` does not record the SQL text or the executing user name. For the full audit
   trail including SQL text, see ``EXA_DBA_AUDIT_SQL`` in :doc:`auditing`.

EXA_SQL_DAILY and EXA_SQL_HOURLY
=================================

Aggregated views of SQL activity. Each row represents a command type (``SELECT``, ``MERGE``, etc.)
within a time period. Key aggregated columns include ``COUNT``, ``DURATION_AVG``, ``DURATION_MAX``,
``CPU_AVG``, and ``CPU_MAX``.

Use these tables to spot workload trends without scanning per-statement detail.

Execution Modes
===============

The ``EXECUTION_MODE`` column classifies how each statement was handled:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Mode
     - Meaning
   * - ``EXECUTE``
     - Statement was fully compiled and executed
   * - ``PREPARE``
     - Statement was prepared but not yet executed
   * - ``CACHED``
     - Result was served from the query cache — no recomputation
   * - ``CRASHED``
     - Statement failed during execution

Recipes
=======

Find the Slowest Queries (Last 24 Hours)
-----------------------------------------

.. code-block:: sql

   SELECT SESSION_ID, STMT_ID, COMMAND_NAME, DURATION, SUCCESS
   FROM EXA_SQL_LAST_DAY
   ORDER BY DURATION DESC
   LIMIT 20;

Identify CPU-Intensive Statements
-----------------------------------

.. code-block:: sql

   SELECT SESSION_ID, STMT_ID, COMMAND_NAME, CPU, DURATION
   FROM EXA_SQL_LAST_DAY
   WHERE CPU > 50
   ORDER BY CPU DESC;

Check Cache Hit Rate
---------------------

A high proportion of ``CACHED`` executions indicates effective use of Exasol's query cache.

.. code-block:: sql

   WITH totals AS (
       SELECT EXECUTION_MODE, COUNT(*) AS statement_count
       FROM EXA_SQL_LAST_DAY
       GROUP BY EXECUTION_MODE
   )
   SELECT
       EXECUTION_MODE,
       statement_count,
       ROUND(statement_count * 100.0 / SUM(statement_count) OVER (), 1) AS pct
   FROM totals
   ORDER BY statement_count DESC;

Daily Workload Summary by Command Type
----------------------------------------

.. code-block:: sql

   SELECT COMMAND_NAME, COUNT AS statement_count,
          DURATION_AVG, DURATION_MAX
   FROM EXA_SQL_DAILY
   WHERE SUCCESS = TRUE
   ORDER BY DURATION_MAX DESC;

**Further reading:** `EXA_SQL_LAST_DAY <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_sql_last_day.htm>`_ · `EXA_SQL_DAILY <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_sql_daily.htm>`_
