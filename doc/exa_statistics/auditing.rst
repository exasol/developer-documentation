======================
Auditing & Compliance
======================

The ``EXA_DBA_AUDIT_*`` tables provide a full audit trail of SQL execution and user sessions.
They are designed for security investigations, compliance reporting, and operational support.

.. note::
   All tables in this section require the ``SELECT ANY DICTIONARY`` system privilege.
   See :ref:`exa-statistics-access-control` for details on granting this privilege.

EXA_DBA_AUDIT_SQL
==================

Records every SQL statement executed in the database. Key columns:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Description
   * - ``USER_NAME``
     - Database user who executed the statement
   * - ``SESSION_ID``
     - Session identifier
   * - ``STMT_ID``
     - Statement identifier within the session
   * - ``COMMAND_NAME``
     - SQL command type (e.g., ``SELECT``, ``CREATE TABLE``)
   * - ``COMMAND_CLASS``
     - Broad category: ``DQL``, ``DML``, ``DDL``, ``DCL``, ``TCL``
   * - ``SQL_TEXT``
     - Full SQL text (up to 2,000,000 characters)
   * - ``SUCCESS``
     - ``TRUE`` if the statement completed without error
   * - ``ERROR_CODE`` / ``ERROR_TEXT``
     - Error details for failed statements
   * - ``DURATION``
     - Execution time in seconds
   * - ``STMT_START_TIME``
     - Timestamp when the statement began executing

EXA_DBA_AUDIT_SESSIONS
========================

Records every database session, including login and logout events. Key columns:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Description
   * - ``SESSION_ID``
     - Unique session identifier
   * - ``USER_NAME``
     - Database user who opened the session
   * - ``OS_USER``
     - Operating system user on the client machine
   * - ``HOST``
     - Client host address
   * - ``LOGIN_TIME``
     - Session start timestamp
   * - ``LOGOUT_TIME``
     - Session end timestamp (``NULL`` if session is still active)
   * - ``SUCCESS``
     - ``TRUE`` for successful logins; ``FALSE`` for failed login attempts
   * - ``ENCRYPTED``
     - ``TRUE`` if the connection was encrypted

Managing Audit Log Size
========================

Audit tables grow continuously. Remove old records while retaining recent history with
``TRUNCATE AUDIT LOGS``:

.. code-block:: sql

   -- Keep the last 30 days; remove everything older
   TRUNCATE AUDIT LOGS KEEP FROM DAYS=30;

.. warning::
   ``TRUNCATE AUDIT LOGS`` permanently deletes the removed records. This action cannot be undone.

Recipes
=======

Find All Failed Statements with Error Details
----------------------------------------------

.. code-block:: sql

   SELECT USER_NAME, COMMAND_NAME, SQL_TEXT,
          ERROR_CODE, ERROR_TEXT, STMT_START_TIME
   FROM EXA_DBA_AUDIT_SQL
   WHERE SUCCESS = FALSE
   ORDER BY STMT_START_TIME DESC
   LIMIT 50;

Track Login History for a Specific User
-----------------------------------------

.. code-block:: sql

   SELECT SESSION_ID, LOGIN_TIME, LOGOUT_TIME,
          HOST, OS_USER, ENCRYPTED
   FROM EXA_DBA_AUDIT_SESSIONS
   WHERE USER_NAME = 'MY_USER'
   ORDER BY LOGIN_TIME DESC;

List All DDL Statements Executed Today
----------------------------------------

.. code-block:: sql

   SELECT USER_NAME, COMMAND_NAME, SQL_TEXT, STMT_START_TIME
   FROM EXA_DBA_AUDIT_SQL
   WHERE COMMAND_CLASS = 'DDL'
     AND CAST(STMT_START_TIME AS DATE) = CURRENT_DATE
   ORDER BY STMT_START_TIME DESC;

Remove Audit Logs Older Than 30 Days
--------------------------------------

.. code-block:: sql

   TRUNCATE AUDIT LOGS KEEP FROM DAYS=30;

**Further reading:** `EXA_DBA_AUDIT_SQL <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_dba_audit_sql.htm>`_ · `EXA_DBA_AUDIT_SESSIONS <https://docs.exasol.com/db/latest/sql_references/system_tables/statistical/exa_dba_audit_sessions.htm>`_ · `Auditing Concepts <https://docs.exasol.com/db/latest/database_concepts/auditing.htm>`_
