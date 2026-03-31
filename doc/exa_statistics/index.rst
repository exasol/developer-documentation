==========================================
EXA_STATISTICS: Database Monitoring & Audit
==========================================

``EXA_STATISTICS`` is a built-in system schema present in every Exasol database. It automatically
collects and stores historical data about query activity, resource usage, database size, and user
sessions. Use it to monitor performance, plan capacity, and maintain a full audit trail — without
installing any additional tools.

.. list-table:: Table Groups at a Glance
   :header-rows: 1
   :widths: 25 50 25

   * - Group
     - Purpose
     - Access
   * - SQL Activity (``EXA_SQL_*``)
     - Track executed statements, execution modes, duration, and CPU usage
     - All users
   * - System Monitor (``EXA_MONITOR_*``)
     - Monitor CPU, memory, swap, I/O, and network metrics
     - All users
   * - Database Size (``EXA_DB_SIZE_*``)
     - Track storage volume, compression ratios, and recommended RAM
     - All users
   * - Audit (``EXA_DBA_AUDIT_*``)
     - Full SQL and session audit trail for compliance and security
     - ``SELECT ANY DICTIONARY`` required

.. toctree::
   :maxdepth: 2

   overview
   query_analytics
   system_health
   auditing
