=================================
System Health & Capacity Planning
=================================

The ``EXA_MONITOR_*`` and ``EXA_DB_SIZE_*`` tables provide a continuous record of hardware resource
usage and storage consumption. Use them to detect performance bottlenecks, identify memory pressure,
and plan infrastructure growth.

EXA_MONITOR_LAST_DAY
=====================

Contains one row per measurement interval (approximately every minute) for the past 24 hours.
Key columns:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Description
   * - ``MEASURE_TIME``
     - Timestamp of the measurement
   * - ``CPU``
     - Average CPU usage across all cluster nodes (%)
   * - ``LOAD``
     - System load average
   * - ``TEMP_DB_RAM``
     - Temporary DB RAM in use (MiB)
   * - ``PERSISTENT_DB_RAM``
     - Persistent DB RAM in use (MiB)
   * - ``SWAP``
     - Swap space in use — values above 0 indicate memory pressure (MiB)
   * - ``HDD_READ`` / ``HDD_WRITE``
     - Disk read/write throughput (MiB/s)
   * - ``NET``
     - Network traffic (MiB/s)

EXA_MONITOR_DAILY
==================

Aggregates monitor data per calendar day. Each metric has both an ``_AVG`` and ``_MAX`` variant
(e.g., ``CPU_AVG``, ``CPU_MAX``). Use this table to identify days with unusual load or to compare
weekly performance trends.

EXA_DB_SIZE_LAST_DAY
=====================

Tracks storage volume metrics at the cluster level, measured approximately every hour. Key columns:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Column
     - Description
   * - ``SIZE_RAW_COMPRESSED``
     - Compressed data volume (MiB)
   * - ``SIZE_UNCOMPRESSED``
     - Uncompressed (raw) data volume (MiB)
   * - ``RECOMMENDED_DB_RAM_SIZE``
     - RAM size Exasol recommends for optimal query performance (MiB)
   * - ``SIZE_PERSISTENT_VOLUME``
     - Total persistent storage allocated (MiB)
   * - ``SIZE_PERSISTENT_VOLUME_PERCENTAGE``
     - Percentage of persistent volume currently used

EXA_DB_SIZE_DAILY
==================

Daily aggregation of database size metrics. Use this table to track storage growth over weeks and
months and to feed capacity planning reports.

Recipes
=======

Snapshot Current System Resource Usage
----------------------------------------

.. code-block:: sql

   SELECT MEASURE_TIME, CPU, LOAD, TEMP_DB_RAM, PERSISTENT_DB_RAM, SWAP
   FROM EXA_MONITOR_LAST_DAY
   ORDER BY MEASURE_TIME DESC
   LIMIT 10;

Detect Memory Pressure
-----------------------

Swap usage above zero suggests the database is under memory pressure. Sustained swap values
warrant a RAM review or workload optimisation.

.. code-block:: sql

   SELECT MEASURE_TIME, SWAP, CPU, TEMP_DB_RAM
   FROM EXA_MONITOR_LAST_DAY
   WHERE SWAP > 0
   ORDER BY MEASURE_TIME DESC;

Check Storage Utilization and Recommended RAM
----------------------------------------------

.. code-block:: sql

   SELECT MEASURE_TIME,
          SIZE_RAW_COMPRESSED,
          SIZE_PERSISTENT_VOLUME,
          SIZE_PERSISTENT_VOLUME_PERCENTAGE,
          RECOMMENDED_DB_RAM_SIZE
   FROM EXA_DB_SIZE_LAST_DAY
   ORDER BY MEASURE_TIME DESC
   LIMIT 1;

Track Storage Growth Over the Last Two Weeks
---------------------------------------------

.. code-block:: sql

   SELECT MEASURE_TIME,
          SIZE_RAW_COMPRESSED
   FROM EXA_DB_SIZE_DAILY
   ORDER BY MEASURE_TIME DESC
   LIMIT 14;

**Further reading:** `EXA_MONITOR_LAST_DAY <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_monitor_last_day.htm>`_ · `EXA_MONITOR_DAILY <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_monitor_daily.htm>`_ · `EXA_DB_SIZE_LAST_DAY <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_db_size_last_day.htm>`_
