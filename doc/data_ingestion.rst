Data Ingestion
==============

CSV files
---------

The example below shows how to import a CSV file into an Exasol database using `pyexasol` and the `import_from_file` function.

.. code-block:: python

    import pyexasol

    # Connection details
    dsn = 'your_exasol_dsn'
    user = 'your_username'
    password = 'your_password'

    # Connect to Exasol
    C = pyexasol.connect(dsn=dsn, user=user, password=password)

    # Path to the local CSV file
    file_path = '/path/to/your/file.csv'

    # Import CSV file into Exasol
    C.import_from_file(file_path, 'your_schema.your_table')

For more detailed information and additional options, refer to the `pyexasol documentation <https://exasol.github.io/pyexasol/master/user_guide/http_transport.html#import-from-file>`_


Other options to import CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exasol also provides a bulk loader to import CSV from various external sources, details can be found in the `Exasol documentation <https://docs.exasol.com/db/latest/sql/import.htm>`_


Parquet Files
-------------

The example below shows how to read a local Parquet file into a pandas DataFrame and then insert that data into an Exasol database using `pyexasol`.

Reading the Parquet File
^^^^^^^^^^^^^^^^^^^^^^^^
Use the `pandas.read_parquet` function to read the Parquet file into a DataFrame.

.. code-block:: python

    import pandas as pd

    # Path to the local Parquet file
    file_path = 'path/to/your/file.parquet'

    # Read the Parquet file into a DataFrame
    df = pd.read_parquet(file_path)

Inserting Data into Exasol
^^^^^^^^^^^^^^^^^^^^^^^^^^
Use the `pyexasol` library to connect to the Exasol database and insert the DataFrame.

.. code-block:: python

    import pyexasol

    # Connection details
    dsn = 'your_exasol_dsn'
    user = 'your_username'
    password = 'your_password'

    # Connect to Exasol
    conn = pyexasol.connect(dsn=dsn, user=user, password=password)

    # Insert DataFrame into Exasol
    conn.import_from_pandas(df, 'your_schema.your_table')


Other options to import parquet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To import a Parquet file from e.g. Amazon S3 into Exasol, you can also use the Exasol Cloud Storage Extensions. 
Detailed instructions and examples can be found in the the following `Cloud Storage Extensions User guide <https://github.com/exasol/cloud-storage-extension/blob/main/doc/user_guide/user_guide.md>`__.


Loading Data from External Sources
----------------------------------
Exasol supports loading data from various external sources using the `IMPORT` statement. 
You can connect to external databases via JDBC, or load data from files stored in e.g. Cloud Object Storage / Kafka and more.

Example: Loading Data from a JDBC Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here is an example of how to load data from a PostgreSQL database using JDBC:

.. code-block:: python

    import pyexasol

    # Connection details
    dsn = 'your_exasol_dsn'
    user = 'your_username'
    password = 'your_password'

    # Connect to Exasol
    conn = pyexasol.connect(dsn=dsn, user=user, password=password)

    # Define the connection to the PostgreSQL database
    conn.execute("""
        CREATE OR REPLACE CONNECTION my_pg_conn
        TO 'jdbc:postgresql://your_postgresql_host:5432/your_database'
        USER 'your_pg_username'
        IDENTIFIED BY 'your_pg_password'
    """)

    # Import data from PostgreSQL into Exasol
    conn.execute("""
        IMPORT INTO your_schema.your_table
        FROM JDBC AT my_pg_conn
        STATEMENT 'SELECT * FROM your_pg_table'
    """)

Example: Loading Data from an HTTP Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here is an example of how to load data from a CSV file stored on an HTTPS server:

.. code-block:: python

    import pyexasol

    # Connection details
    dsn = 'your_exasol_dsn'
    user = 'your_username'
    password = 'your_password'

    # Connect to Exasol
    conn = pyexasol.connect(dsn=dsn, user=user, password=password)

    # Import data from a CSV file on an HTTP server
    conn.execute("""
        IMPORT INTO your_schema.your_table
        FROM CSV AT 'https://your_https_server/path/to/your/file.csv'
        FILE OPTIONS 'DELIMITER=; ENCODING=UTF-8 SKIP_ROWS=1 NULL=NULL'
    """)

For more detailed information on loading data from external sources, please refer to the Exasol documentation:
* `Loading Data from External Sources <https://docs.exasol.com/db/latest/loading_data/load_data_from_externalsources.htm>`_.

Using Virtual Schemas
^^^^^^^^^^^^^^^^^^^^^
Virtual Schemas in Exasol provide an abstraction layer that makes external data sources accessible through regular SQL commands. 
This allows you to query external data as if it were stored in Exasol, without the need to physically load the data into the database.

For more information on virtual schemas and the supported dialects, please refer to the following resources:
* `Virtual Schemas User Guide <https://github.com/exasol/virtual-schemas/blob/main/doc/user_guide/dialects.md>`_.
* `Virtual Schemas Documentation <https://docs.exasol.com/db/latest/database_concepts/virtual_schemas.htm>`_.
