Integrations
============

SQLAlchemy
----------

Install SQLAlchemy

.. code-block:: python

    pip install sqlalchemy-exasol


Connect to Exasol database using SQLAlchemy

.. code-block:: python

    from sqlalchemy import create_engine, text, URL

    url_object = URL.create(
        drivername="exa+websocket",
        username="sys",
        password="exasol",
        host="127.0.0.1",
        port="8563",
    )

    engine = create_engine(url_object)
    # All literal text should be passed through `text()` before execution
    sql_text = text("SELECT 42 FROM DUAL")
    with engine.connect() as con:
        result = con.execute(sql_text).fetchall()

Please also refer to `sqlalchemy exasol documentation <https://exasol.github.io/sqlalchemy-exasol/master/user_guide/index.html>`_.

JupySQL
-------

How to work with JupySQL in JupyterLab is described in :doc:`environments`.

Pandas
------

Importing Data into Pandas
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can fetch data from Exasol into a Pandas DataFrame using pyexasol.

.. code-block:: python

    import pandas as pd

    # Execute a query and fetch data into a Pandas DataFrame, Conn is an existing pyexasol connection.
    df = conn.export_to_pandas('SELECT * FROM <your_table_name>')

    # Display the DataFrame
    print(df)

Exporting Data from Pandas to Exasol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also export data from a Pandas DataFrame to an Exasol table.

.. code-block:: python

    # Assume you have a Pandas DataFrame `df` you wish to export
    conn.import_from_pandas(df, '<your_target_table_name>')

Ibis
----

Please refer to the `IBIS documentation <https://ibis-project.org/backends/exasol>`_.

You can also watch `this video <https://www.youtube.com/watch?v=0YaQo3o5ePI&t=2s>`_ for a step by step walk through of using Ibis with Exasol via AI Lab.
