Data Ingestion
==============

Importing CSV from AWS S3 into Exasol
-------------------------------------
This example demonstrates how to import a CSV file from AWS S3 into Exasol using the `IMPORT FROM CSV` command.

Step 1: Create a Virtual Schema Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Establish a connection to your AWS S3 bucket using your AWS credentials:

.. code-block:: sql

    CREATE CONNECTION S3_MY_BUCKET
    TO 'http://<my_bucketname>.s3.<my_region>.amazonaws.com'
    USER '<my_access_key>'
    IDENTIFIED BY '<my_secret_key>';

Step 2: Create a Table
^^^^^^^^^^^^^^^^^^^^^^

Define the structure of the target table where the data from the CSV file will be stored:

.. code-block:: sql

    CREATE TABLE sales_data (
        order_id INT,
        product_name VARCHAR(100),
        quantity INT,
        price DOUBLE
    );

Step 3: Import Data
^^^^^^^^^^^^^^^^^^^

Execute the `IMPORT FROM CSV` command using the defined connection and specifying the details of the CSV file, such as its location, column separators, and encoding:

.. code-block:: sql

    IMPORT INTO sales_data
    FROM CSV
    AT S3_MY_BUCKET
    FILE 'sales_2025/sales.csv'
    COLUMN SEPARATOR = ';'
    ROW SEPARATOR = 'CRLF'
    COLUMN DELIMITER = '"'
    ENCODING = 'UTF-8'
    SKIP = 1;

.. note::
    Make sure to replace `my-access-key`, `my-secret-access`, `my-bucket-name` with your actual AWS S3 credentials.

For more detailed information and additional options, refer to the Exasol documentation at: `Exasol Documentation <https://docs.exasol.com/db/latest/sql/import.htm>`_



Parquet Files
-------------

Import from external sources
----------------------------

HTTP Transport
--------------
