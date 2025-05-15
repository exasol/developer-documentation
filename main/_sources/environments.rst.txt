Environments
============

.. _jupyterlab:

JupyterLab and JupySQL
----------------------

Install SQLAlchemy and JupySQL

.. code-block:: python

    pip install sqlalchemy-exasol
    pip install jupysql

Connect to Exasol database using SQLAlchemy

.. code-block:: python

    import sqlalchemy
    from sqlalchemy.engine.url import URL
    import getpass

    db_host = 'my_exasol_host'
    db_port = 8563
    db_username = input('User Name:')
    db_password = getpass.getpass('Password:')

    websocket_url = URL.create(
        'exa+websocket',
        host=db_host,
        port=db_port,
        username=db_username,
        password=db_password
    )

    db_engine = sqlalchemy.create_engine(websocket_url)

Enable the Jupyter SQL Extension

.. code-block:: python

    %load_ext sql
    %sql db_engine



Run queries against Exasol

.. code-block:: python

    %%sql
    SELECT * FROM "FLIGHTS"."AIRLINE" LIMIT 10

Positron
--------

You can either connect to Exasol with pyexasol as described in :doc:`getting_started` or using JupySQL as described  in :ref:`jupyterlab`.

pyCharm
-------

Please follow the instructions of the official documentation of `pyCharm <https://www.jetbrains.com/help/pycharm/exasol.html>`_.


VS Code
-------

To connect to Exasol install the plugin `Database Client JDBC <https://marketplace.visualstudio.com/items?itemName=cweijan.dbclient-jdbc>`_ from the marketplace.