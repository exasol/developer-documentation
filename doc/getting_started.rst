
Getting Started
===============

There are three ways to get started with Exasol:

-  Download the `community
   edition <https://www.exasol.com/free-signup-community-edition/>`__
-  Use the `docker version <https://github.com/exasol/docker-db>`__
-  Signup for a free `SaaS trial <https://cloud.exasol.com/signup>`__

In the following we are going to use the SaaS version.

Setting up the db
-----------------

Our `main
documentation <https://docs.exasol.com/saas/get_started/saas_first_steps.htm>`__
shows you how to create a SaaS account and setup your first database and
cluster.

Installing pyexasol
-------------------

Once your database is up and running you can connect via any client.
From Python we use `PyExasol <https://github.com/exasol/pyexasol>`__. It
can be easily installed via

::

   pip install pyexasol[pandas]

Connecting to the db
--------------------

Connecting to an Exasol database is performed via:

.. code:: python

   import pyexasol

   C = pyexasol.connect(dsn='<host:port>', user='sys', password='exasol')

It is slightly different when connecting to a SaaS database as we need a
`personal access
token <https://docs.exasol.com/saas/administration/access_mngt/access_token.htm>`__:

.. code:: python

   import pyexasol

   C = pyexasol.connect(dsn='<host:port>', user='sys', password='<token>')

Finally you can also wrap all credentials into a `local config
file <https://exasol.github.io/pyexasol/master/user_guide/local_config.html>`__:

.. code:: python

   C = pyexasol.connect_local_config('my_exasol')

Executing SQL
-------------

Running your first query is pretty straightforward:

.. code:: python

   stmt = C.execute("SELECT * FROM EXA_ALL_USERS")

   for row in stmt:
       print(row)

It also allows you to load resultsets into a pandas dataframe:

.. code:: python

   C = pyexasol.connect(dsn='<host:port>', user='sys', password='exasol', compression=True)

   df = C.export_to_pandas("SELECT * FROM EXA_ALL_USERS")
   print(df.head())
