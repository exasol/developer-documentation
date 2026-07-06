
Getting Started
===============

There are four ways to get started with Exasol:

-  Install `Exasol Personal <https://www.exasol.com/personal/>`__ — the
   full Exasol database, completely free for personal use
-  Download the `community
   edition <https://www.exasol.com/free-signup-community-edition/>`__
-  Use the `docker version <https://github.com/exasol/docker-db>`__
-  Signup for a free `SaaS trial <https://cloud.exasol.com/signup>`__

In the following we are going to use Exasol Personal.

Setting up the DB
-----------------

`Exasol Personal <https://www.exasol.com/personal/>`__ is a completely
free, single-user edition of Exasol with all enterprise features
included — unlimited data, unlimited cluster size (MPP), UDFs, and the
Exasol Admin web UI. You can run it locally on your own machine
(currently macOS with at least 8 GB RAM) or deploy it into your own
cloud account (AWS, Azure, Exoscale, or STACKIT).

First, download the Exasol Launcher (Linux / macOS):

.. code:: bash

   curl https://downloads.exasol.com/exasol-personal/installer.sh | sh

Then install Exasol Personal on your local system or in the cloud of
your choice:

.. code:: bash

   exasol install local      # local system, macOS
   exasol install aws        # Amazon Web Services
   exasol install azure      # Microsoft Azure
   exasol install exoscale   # Exoscale
   exasol install stackit    # STACKIT

A cloud deployment takes about 10 to 20 minutes. Once the installation
has finished, run ``exasol info`` to see how to connect to your
database. For local deployments the initial credentials are ``sys`` /
``exasol``. For Windows installation, sample data, and full details see
the `Exasol Personal
repository <https://github.com/exasol/exasol-personal>`__ and the
`Quick Start
Guide <https://docs.exasol.com/db/latest/get_started/exasol_personal.htm>`__.

Alternatively, if you prefer a managed database, our `main
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

For Exasol Personal, ``exasol info`` shows the connection details of
your deployment; ``sys`` / ``exasol`` are the defaults for a local
deployment.

It is slightly different when connecting to a SaaS database as we need a
`personal access
token <https://docs.exasol.com/saas/administration/access_mngt/access_token.htm>`__:

.. code:: python

   import pyexasol

   C = pyexasol.connect(dsn='<host:port>', user='sys', password='<token>')

Finally you can also wrap all credentials into a `local config
file <https://exasol.github.io/pyexasol/master/api.html>`__:

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
