Establishing a Connection
==============================



The **connect()** method creates a connection to the database and returns an object **ExaConnection**.

The following example show how to connect with Exasol.

.. code-block:: python

    import pyexasol

    try:
        # Connect to Exasol
        connection = pyexasol.connect(dsn='127.0.0.1', 
                             user='scott', 
                             password='password')
        print("Connected successfully to Exasol.")
    except Exception as e:
        print(f"Error: {e}")

For additional parameter list please visit `ExaConnection API ref <https://exasol.github.io/pyexasol/master/api.html#pyexasol.ExaConnection>`_. 
To handle connection errors, use the try statement and catch all errors using the errors.Error exception:





