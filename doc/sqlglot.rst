SQLGlot
=======

SQLGlot is a Python SQL parser and transpiler. Since Exasol is available as a SQLGlot dialect, you can convert SQL from many dialects into Exasol SQL and also transpile Exasol SQL to other dialects.

Please refer to the official `SQLGlot documentation <https://sqlglot.com/sqlglot.html>`_ for feature details and the current list of `supported dialects <https://sqlglot.com/sqlglot.html#supported-dialects>`_.

Install SQLGlot
---------------

.. code-block:: bash

    pip install sqlglot

Try it online
-------------

You can test SQL dialect conversion directly in the browser using SQLingual:
`SQLingual app <https://sqlingual.streamlit.app/>`_.

Convert another dialect to Exasol
---------------------------------

.. code-block:: python

    import sqlglot

    postgres_sql = "SELECT DATE_TRUNC('day', created_at) AS day, COUNT(*) FROM events GROUP BY 1"
    exasol_sql = sqlglot.transpile(postgres_sql, read="postgres", write="exasol")[0]
    print(exasol_sql)

Convert Exasol to another dialect
---------------------------------

.. code-block:: python

    import sqlglot

    exasol_sql = "SELECT ADD_DAYS(CURRENT_DATE, 7) AS due_date FROM DUAL"
    spark_sql = sqlglot.transpile(exasol_sql, read="exasol", write="spark")[0]
    print(spark_sql)

Parse and normalize Exasol SQL
------------------------------

.. code-block:: python

    import sqlglot

    query = "SELECT CURRENT_DATE, 42 AS answer FROM DUAL"
    expression = sqlglot.parse_one(query, read="exasol")
    print(expression.sql(dialect="exasol", pretty=True))

Typical use cases
-----------------

* SQL linting and normalization for Exasol-focused projects
* Translating SQL from other engines into Exasol-compatible SQL
* Translating Exasol SQL for cross-platform analytics tooling
* Building migration and refactoring tooling with a parser instead of regex

Practical note
--------------

Not every SQL feature has a 1:1 equivalent across all engines. Always test transpiled SQL in the target environment.
