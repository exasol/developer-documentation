Querying Using PyExasol
=========================================

In this section, we will create a table and insert data inside that table using PyExasol.
The schema we are working with in this example is named 'SCHEMA'. You can replace it with your own schema name.


Creating a Table
----------------------

Using the **execute** method of the connection object we created earlier in the :ref:`installation-pyexasol` section.
We are creating a table called **Employee**.

.. code-block:: python

    create_table = connection.execute("CREATE OR REPLACE TABLE SCHEMA.Employee(employee_id INT PRIMARY KEY, " \
    "name VARCHAR(50), " \
    "hire_date DATE)")

For more information about the **execute** method. Check out `ExaConnection.execute class <https://exasol.github.io/pyexasol/master/_modules/pyexasol/connection.html#ExaConnection.execute>`_.


Inserting Data into the Table
------------------------------------

Using Pandas DataFrame
^^^^^^^^^^^^^^^^^^^^^^^

This is an example of inserting values into the "EMPLOYEE" table using pandas dataframe.

.. code-block:: python

    data = {
        "employee_id": [15, 20, 30, 40, 50],
        "name": ['John', 'Jane', 'Michael', 'Emily', 'David'],
        "hire_date": ['2023-01-15', '2022-07-10', '2021-03-05', '2023-06-20', '2020-11-12'],
    }
    df_employees = pd.DataFrame(data)
    connection.import_from_pandas(df_employees, ('SCHEMA', 'EMPLOYEE'))

For custom params check out `ExaConnection.import_from_pandas <https://exasol.github.io/pyexasol/master/api.html#pyexasol.ExaConnection.import_from_pandas>`_

Using a file
^^^^^^^^^^^^^^

.. code-block:: python

    inserting_a_file = connection.import_from_file('file.csv', ('SCHEMA','EMPLOYEE'))

Make sure to that your file has the same column names as your table.

There are multiple options to import data from using PyExasol. Check out more options from `here <https://exasol.github.io/pyexasol/master/api.html#pyexasol.ExaConnection.import_from_callback>`_


Retrieving Data From the Database
------------------------------------

Like importing there are multiple options of **retrieving** data using PyExasol.
Here is an example of exporting data into a pandas dataframe.

.. code-block:: python

    retrieve_into_pandas = connection.export_to_pandas('SELECT * FROM SCHEMA.EMPLOYEE')
    print(retrieve_into_pandas.shape)

